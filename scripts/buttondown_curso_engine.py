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
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib import request as urlrequest
from urllib.error import HTTPError, URLError


BASE_URL = "https://api.buttondown.com/v1"
ROOT = Path(__file__).resolve().parents[1]
CRED_PATH = Path(os.environ.get(
    "BUTTONDOWN_TOKEN_FILE",
    Path.home() / ".codex" / "decodifica" / "credentials" / "buttondown_token.json",
))
COURSE_FILES = {
    1: ("dia-1-setup.md", "Día 1 de 5: el setup que cambia cómo ChatGPT te responde"),
    2: ("dia-2-estructura-prompts.md", "Día 2 de 5: el framework RTF para escribir prompts que funcionan siempre"),
    3: ("dia-3-contexto-archivos.md", "Día 3 de 5: cómo hacer que ChatGPT lea TUS documentos"),
    4: ("dia-4-iteracion.md", "Día 4 de 5: el truco del segundo turno"),
    5: ("dia-5-agentes.md", "Día 5 de 5: tu primer Custom GPT en 10 minutos"),
}
COURSE_DIR = ROOT / "lead-magnets" / "mini-curso"
DAY_DELAY = timedelta(hours=24)
SEND_TOLERANCE = timedelta(hours=6)
COURSE_VERSION = "decodifica_codex_v2"
SEND_TAG_NAME = "curso-envio-activo"


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


def parse_course_email(day: int) -> tuple[str, str]:
    filename, fallback_subject = COURSE_FILES[day]
    path = COURSE_DIR / filename
    text = path.read_text(encoding="utf-8")
    subject_match = re.search(r"\*\*Asunto:\*\*\s*(.+)", text)
    subject = subject_match.group(1).strip() if subject_match else fallback_subject
    parts = text.split("\n---\n", 1)
    body = parts[1].strip() if len(parts) == 2 else text.strip()
    return subject, body


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


def list_tags(token: str) -> list[dict]:
    tags = []
    page = 1
    while True:
        result = api("GET", f"/tags?page={page}&page_size=100", token)
        tags.extend(result.get("results", []))
        if not result.get("next"):
            break
        page += 1
    return tags


def get_tag_id(token: str, name: str) -> str:
    for tag in list_tags(token):
        if tag.get("name") == name:
            return tag["id"]
    raise RuntimeError(f"required_tag_missing:{name}")


def ensure_subscriber_tag(token: str, subscriber: dict, tag_id: str) -> list:
    tags = subscriber.get("tags") or []
    if tag_id in tags:
        return tags
    api("PATCH", f"/subscribers/{subscriber['id']}", token, {"tags": [*tags, tag_id]})
    return tags


def restore_subscriber_tags(token: str, subscriber_id: str, tags: list) -> None:
    api("PATCH", f"/subscribers/{subscriber_id}", token, {"tags": tags})


def clear_send_tag(token: str, tag_id: str, keep_subscriber_id: str) -> None:
    for subscriber in list_active_subscribers(token):
        subscriber_id = subscriber["id"]
        tags = subscriber.get("tags") or []
        if subscriber_id != keep_subscriber_id and tag_id in tags:
            restore_subscriber_tags(
                token,
                subscriber_id,
                [tag for tag in tags if tag != tag_id],
            )


def recipient_filter(tag_id: str) -> dict:
    return {
        "filters": [
            {
                "field": "subscriber.tags",
                "operator": "contains",
                "value": tag_id,
            }
        ],
        "groups": [],
        "predicate": "and",
    }


def send_course_email(token: str, day: int, subscriber: dict) -> str:
    subscriber_id = subscriber["id"]
    tag_id = get_tag_id(token, SEND_TAG_NAME)
    clear_send_tag(token, tag_id, subscriber_id)
    original_tags = ensure_subscriber_tag(token, subscriber, tag_id)
    subject, body = parse_course_email(day)
    payload = {
        "subject": subject,
        "body": body,
        "email_type": "private",
        "archival_mode": "disabled",
        "commenting_mode": "disabled",
        "filters": recipient_filter(tag_id),
        "metadata": {
            "source": "decodifica_codex_course",
            "course_version": COURSE_VERSION,
            "course_day": day,
        },
    }
    created = api("POST", "/emails", token, {**payload, "status": "draft"})
    email_id = created["id"]
    try:
        api("POST", f"/emails/{email_id}/publish", token, payload)
    except (HTTPError, URLError):
        try:
            api("DELETE", f"/emails/{email_id}", token, expect_json=False)
        except (HTTPError, URLError):
            pass
        raise
    finally:
        try:
            restore_subscriber_tags(token, subscriber_id, original_tags)
        except (HTTPError, URLError):
            pass
    return email_id


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
        day_key = f"curso_dia_{force_day}_sent_at"
        email_id = None
        if execute:
            email_id = send_course_email(token, force_day, subscriber)
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
            "email_id": email_id or "fresh_private_email",
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

        if (now - last_sent) >= (DAY_DELAY - SEND_TOLERANCE):
            email_id = None
            if execute:
                new_metadata = {**metadata, day_key: now.isoformat()}
                if day == 5:
                    new_metadata["curso_completed_at"] = now.isoformat()
                email_id = send_course_email(token, day, subscriber)
                patch_metadata(token, subscriber_id, new_metadata)
            return {
                "action": f"{'sent' if execute else 'would_send'}_dia_{day}",
                "subscriber_id": subscriber_id,
                "email_id": email_id or "fresh_private_email",
            }

        return {
            "action": "skip",
            "reason": f"waiting_for_dia_{day}",
            "subscriber_id": subscriber_id,
            "next_at": (last_sent + DAY_DELAY - SEND_TOLERANCE).isoformat(),
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
    parser.add_argument("--summary-output", help="Guarda un resumen operativo agregado sin datos personales.")
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
        except (HTTPError, URLError, RuntimeError) as exc:
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

    report = {
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
    }
    if args.summary_output:
        action_counts = {}
        for item in action_rows:
            action = item.get("action", "unknown")
            action_counts[action] = action_counts.get(action, 0) + 1
        summary = {
            "schema_version": "decodifica-newsletter-minicurso-1.0",
            "generated_at": report["timestamp"],
            "ok": report["ok"],
            "phase": "execute" if report["execute"] else "inspect",
            "total_subscribers": report["total_subscribers"],
            "sent": report["sent"],
            "would_send": report["would_send"],
            "initialized": report["initialized"],
            "skipped": report["skipped"],
            "errors": report["errors"],
            "action_counts": action_counts,
        }
        summary_path = Path(args.summary_output)
        summary_path.parent.mkdir(parents=True, exist_ok=True)
        summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 1 if error_rows else 0


if __name__ == "__main__":
    raise SystemExit(main())
