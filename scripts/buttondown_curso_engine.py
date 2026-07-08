#!/usr/bin/env python3
"""
Engine del mini-curso Buttondown para Decodifica.

Buttondown Free no incluye Automations nativas. Este script hace el drip
controlado desde Codex usando drafts ya creados en Buttondown y metadata de
suscriptor.

Importante:
- No envia el welcome. Buttondown ya envia el email de bienvenida configurado.
- Sin --execute no envia emails ni actualiza metadata.
- --force-day requiere --test-email para evitar envios masivos accidentales.

Metadata usada:
- curso_started_at
- curso_dia_1_sent_at ... curso_dia_5_sent_at
- curso_completed_at
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib import request as urlrequest
from urllib.error import HTTPError, URLError


BASE_URL = "https://api.buttondown.com/v1"
CRED_PATH = Path(os.environ.get(
    "BUTTONDOWN_TOKEN_FILE",
    Path.home() / ".codex" / "decodifica" / "credentials" / "buttondown_token.json",
))
CURSO_EMAIL_IDS = {
    1: "em_2p4nm9th4s8fvbenmnhgwfn9h1",
    2: "em_083896cx5g9xbbs1w7kytejmva",
    3: "em_6mn51pashc8rxsm56dramsqd57",
    4: "em_2fsjs2q94y9g18ngefj1mathsf",
    5: "em_1mwqdy32y89y0bveqabyey97x8",
}
DAY_DELAY = timedelta(hours=24)
COURSE_VERSION = "decodifica_codex_v2"


def get_token() -> str:
    env_token = os.environ.get("BUTTONDOWN_API_TOKEN")
    if env_token:
        return env_token
    cred = json.loads(CRED_PATH.read_text(encoding="utf-8-sig"))
    return cred["api_token"]


def api(method: str, path: str, token: str, body: dict | None = None, expect_json: bool = True) -> dict | None:
    data = json.dumps(body).encode("utf-8") if body else None
    req = urlrequest.Request(
        f"{BASE_URL}{path}",
        data=data,
        method=method,
        headers={
            "Authorization": f"Token {token}",
            "Content-Type": "application/json",
        },
    )
    with urlrequest.urlopen(req) as resp:
        raw = resp.read().decode("utf-8").strip()
        if not expect_json or not raw:
            return None
        return json.loads(raw)


def list_active_subscribers(token: str) -> list[dict]:
    subscribers = []
    page = 1
    while True:
        result = api("GET", f"/subscribers?type=regular&page={page}&page_size=100", token)
        subscribers.extend(result.get("results", []))
        if not result.get("next"):
            break
        page += 1
    return subscribers


def send_email_to_subscriber(token: str, email_id: str, subscriber_id: str) -> None:
    api(
        "POST",
        f"/emails/{email_id}/send-draft",
        token,
        {"subscribers": [subscriber_id]},
        expect_json=False,
    )


def patch_metadata(token: str, subscriber_id: str, metadata: dict) -> None:
    api("PATCH", f"/subscribers/{subscriber_id}", token, {"metadata": metadata})


def parse_iso(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (ValueError, AttributeError):
        return None
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def redacted(result: dict) -> dict:
    cleaned = dict(result)
    cleaned.pop("metadata", None)
    return cleaned


def without_old_course_metadata(metadata: dict) -> dict:
    return {key: value for key, value in metadata.items() if not key.startswith("curso_")}


def process_subscriber(
    subscriber: dict,
    now: datetime,
    token: str,
    *,
    execute: bool,
    force_day: int | None = None,
) -> dict:
    subscriber_id = subscriber["id"]
    metadata = subscriber.get("metadata") or {}
    if metadata.get("curso_version") != COURSE_VERSION:
        new_metadata = {
            **without_old_course_metadata(metadata),
            "curso_version": COURSE_VERSION,
            "curso_started_at": now.isoformat(),
        }
        if execute:
            patch_metadata(token, subscriber_id, new_metadata)
        return {
            "action": "initialized_curso" if execute else "would_initialize_curso",
            "subscriber_id": subscriber_id,
            "next_at": (now + DAY_DELAY).isoformat(),
        }

    if "curso_completed_at" in metadata:
        return {"action": "skip", "reason": "curso_completed", "subscriber_id": subscriber_id}

    if force_day is not None:
        email_id = CURSO_EMAIL_IDS[force_day]
        day_key = f"curso_dia_{force_day}_sent_at"
        if execute:
            send_email_to_subscriber(token, email_id, subscriber_id)
            new_metadata = {
                **metadata,
                "curso_version": COURSE_VERSION,
                "curso_started_at": metadata.get("curso_started_at") or now.isoformat(),
                day_key: now.isoformat(),
            }
            if force_day == 5:
                new_metadata["curso_completed_at"] = now.isoformat()
            patch_metadata(token, subscriber_id, new_metadata)
        return {
            "action": f"{'sent' if execute else 'would_send'}_dia_{force_day}",
            "subscriber_id": subscriber_id,
            "email_id": email_id,
        }

    started = parse_iso(metadata.get("curso_started_at"))
    if not started:
        return {"action": "skip", "reason": "missing_creation_date", "subscriber_id": subscriber_id}

    if "curso_started_at" not in metadata:
        if execute:
            patch_metadata(token, subscriber_id, {**metadata, "curso_started_at": started.isoformat()})
        return {
            "action": "initialized_curso" if execute else "would_initialize_curso",
            "subscriber_id": subscriber_id,
            "next_at": (started + DAY_DELAY).isoformat(),
        }

    last_sent = started
    for day in range(1, 6):
        day_key = f"curso_dia_{day}_sent_at"
        if day_key in metadata:
            last_sent = parse_iso(metadata[day_key]) or last_sent
            continue

        if (now - last_sent) >= DAY_DELAY:
            email_id = CURSO_EMAIL_IDS[day]
            if execute:
                new_metadata = {**metadata, day_key: now.isoformat()}
                if day == 5:
                    new_metadata["curso_completed_at"] = now.isoformat()
                send_email_to_subscriber(token, email_id, subscriber_id)
                patch_metadata(token, subscriber_id, new_metadata)
            return {
                "action": f"{'sent' if execute else 'would_send'}_dia_{day}",
                "subscriber_id": subscriber_id,
                "email_id": email_id,
            }

        return {
            "action": "skip",
            "reason": f"waiting_for_dia_{day}",
            "subscriber_id": subscriber_id,
            "next_at": (last_sent + DAY_DELAY).isoformat(),
        }

    if execute:
        patch_metadata(token, subscriber_id, {**metadata, "curso_completed_at": now.isoformat()})
    return {
        "action": "marked_completed" if execute else "would_mark_completed",
        "subscriber_id": subscriber_id,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Drip del mini-curso Buttondown de Decodifica.")
    parser.add_argument("--execute", action="store_true", help="Envia emails y actualiza metadata.")
    parser.add_argument("--inspect", action="store_true", help="Consulta suscriptores y muestra que haria, sin enviar.")
    parser.add_argument("--test-email", help="Limita la corrida a un unico email de prueba.")
    parser.add_argument("--force-day", type=int, choices=range(1, 6), help="Fuerza un dia concreto. Requiere --test-email.")
    args = parser.parse_args()

    if args.force_day and not args.test_email:
        print(json.dumps({"ok": False, "error": "--force-day requiere --test-email"}, ensure_ascii=False))
        return 2

    if not args.execute and not args.inspect:
        print(json.dumps({
            "ok": True,
            "dry_run": True,
            "message": "No se han consultado suscriptores ni enviado emails. Usa --inspect o --execute.",
        }, ensure_ascii=False))
        return 0

    token = get_token()
    now = datetime.now(timezone.utc)
    try:
        subscribers = list_active_subscribers(token)
    except (HTTPError, URLError) as exc:
        print(json.dumps({"ok": False, "error": f"list_subscribers_failed: {exc}"}, ensure_ascii=False))
        return 1

    if args.test_email:
        target = args.test_email.strip().lower()
        subscribers = [
            sub for sub in subscribers
            if str(sub.get("email_address", "")).strip().lower() == target
        ]
        if not subscribers:
            print(json.dumps({"ok": False, "error": "test_subscriber_not_found"}, ensure_ascii=False))
            return 1

    results = []
    for subscriber in subscribers:
        try:
            result = process_subscriber(
                subscriber,
                now,
                token,
                execute=args.execute,
                force_day=args.force_day,
            )
            results.append(redacted(result))
        except (HTTPError, URLError) as exc:
            results.append({
                "action": "error",
                "subscriber_id": subscriber.get("id"),
                "error": str(exc),
            })

    action_rows = [
        item for item in results
        if item["action"].startswith(("sent_", "would_send_"))
        or item["action"] in {"initialized_curso", "would_initialize_curso", "marked_completed", "would_mark_completed"}
    ]
    error_rows = [item for item in results if item["action"] == "error"]
    skip_rows = [item for item in results if item not in action_rows and item not in error_rows]

    print(json.dumps({
        "ok": not error_rows,
        "timestamp": now.isoformat(),
        "execute": args.execute,
        "inspect": args.inspect,
        "test_mode": bool(args.test_email),
        "total_subscribers": len(subscribers),
        "sent": len([item for item in action_rows if item["action"].startswith("sent_")]),
        "would_send": len([item for item in action_rows if item["action"].startswith("would_send_")]),
        "initialized": len([item for item in action_rows if item["action"] in {"initialized_curso", "would_initialize_curso"}]),
        "skipped": len(skip_rows),
        "errors": len(error_rows),
        "actions": action_rows,
        "skips": skip_rows,
        "error_log": error_rows,
    }, indent=2, ensure_ascii=False))
    return 1 if error_rows else 0


if __name__ == "__main__":
    raise SystemExit(main())
