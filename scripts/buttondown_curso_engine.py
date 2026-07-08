#!/usr/bin/env python3
"""
Engine del mini-curso Buttondown para Decodifica.

Responsabilidad única: enviar los emails del mini-curso (días 1-5) a cada
suscriptor activo que les toque. NO envía el welcome — Buttondown ya lo
hace automáticamente al confirmar suscripción (verificado 2026-07-02).

Estados (en metadata del suscriptor):
  welcome_sent_at       -> timestamp ISO del welcome (lo pone Buttondown,
                           no este script). Se usa como referencia para
                           saber cuándo empezar a contar los 24h del día 1.
  curso_dia_1_sent_at   -> timestamp ISO envío día 1
  curso_dia_2_sent_at   -> timestamp ISO envío día 2
  curso_dia_3_sent_at   -> timestamp ISO envío día 3
  curso_dia_4_sent_at   -> timestamp ISO envío día 4
  curso_dia_5_sent_at   -> timestamp ISO envío día 5
  curso_completed_at    -> timestamp ISO cuando se completó el curso

Reglas:
  - Si NO tiene welcome_sent_at todavía -> skip (esperando a Buttondown)
  - Para cada día N (1..5): si welcome_sent_at existe y han pasado >=24h,
    y no tiene dia_N_sent_at -> enviar día N
  - Después del día 5, marcar curso_completed_at (no hace nada más)
  - Días email ids: ver CURSO_EMAIL_IDS

Output (stdout JSON): { ok, processed, sent, skipped, errors, sent_log: [...] }
Reportado al root por el cron que invoca este script.
"""
import json
import os
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path
from urllib import request as urlrequest
from urllib.error import HTTPError, URLError

BASE_URL = "https://api.buttondown.email/v1"
CRED_PATH = Path(os.environ.get(
    "BUTTONDOWN_TOKEN_FILE",
    Path.home() / ".codex" / "decodifica" / "credentials" / "buttondown_token.json",
))
WELCOME_EMAIL_ID = "em_246penk44n9gcahbdtrtwshmz2"  # 3 PDFs
CURSO_EMAIL_IDS = {
    1: "em_2p4nm9th4s8fvbenmnhgwfn9h1",
    2: "em_083896cx5g9xbbs1w7kytejmva",
    3: "em_6mn51pashc8rxsm56dramsqd57",
    4: "em_2fsjs2q94y9g18ngefj1mathsf",
    5: "em_1mwqdy32y89y0bveqabyey97x8",
}
MIN_DELAY_BEFORE_WELCOME = timedelta(minutes=5)
DAY_DELAY = timedelta(hours=24)


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
    subs = []
    page = 1
    while True:
        r = api("GET", f"/subscribers?type=regular&page={page}&page_size=100", token)
        subs.extend(r.get("results", []))
        if not r.get("next"):
            break
        page += 1
    return subs


def send_email_to_subscriber(token: str, email_id: str, sub_id: str) -> None:
    # send-draft returns 200 OK with empty body — treat as fire-and-forget
    api("POST", f"/emails/{email_id}/send-draft", token,
        {"subscribers": [sub_id]}, expect_json=False)


def patch_metadata(token: str, sub_id: str, metadata: dict) -> None:
    api("PATCH", f"/subscribers/{sub_id}", token, {"metadata": metadata})


def parse_iso(s: str | None) -> datetime | None:
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except (ValueError, AttributeError):
        return None


def process_subscriber(sub: dict, now: datetime, token: str) -> dict:
    """Devuelve {action, email_id, metadata_after} o {action: 'skip', reason}."""
    sub_id = sub["id"]
    metadata = sub.get("metadata") or {}
    creation = parse_iso(sub.get("creation_date"))

    # --- WELCOME (3 PDFs) — enviado por nosotros ---
    # Buttondown envía automáticamente un welcome genérico corto al confirmar,
    # pero NO envía el draft `em_246penk44n9gcahbdtrtwshmz2` con los 3 PDFs.
    # Somos nosotros quienes tenemos que enviar ese draft.
    # Si el suscriptor activo aún no tiene welcome_sent_at, le enviamos el draft
    # con los PDFs y marcamos timestamp.
    if "welcome_sent_at" not in metadata:
        if creation and (now - creation) < MIN_DELAY_BEFORE_WELCOME:
            return {"action": "skip", "reason": "too_new", "subscriber_id": sub_id}
        send_email_to_subscriber(token, WELCOME_EMAIL_ID, sub_id)
        new_metadata = {**metadata, "welcome_sent_at": now.isoformat()}
        patch_metadata(token, sub_id, new_metadata)
        return {
            "action": "sent_welcome",
            "subscriber_id": sub_id,
            "email_id": WELCOME_EMAIL_ID,
            "metadata": new_metadata,
        }

    welcome_sent = parse_iso(metadata.get("welcome_sent_at"))
    if not welcome_sent:
        # Metadata corrupta - la saltamos y reportamos
        return {"action": "skip", "reason": "bad_welcome_metadata", "subscriber_id": sub_id}

    # --- CURS0 DÍAS 1-5 ---
    if "curso_completed_at" in metadata:
        return {"action": "skip", "reason": "curso_completed", "subscriber_id": sub_id}

    last_sent = welcome_sent
    for day in range(1, 6):
        day_key = f"curso_dia_{day}_sent_at"
        if day_key in metadata:
            last_sent = parse_iso(metadata[day_key]) or last_sent
            continue
        # Este día no se ha enviado todavía
        if (now - last_sent) >= DAY_DELAY:
            email_id = CURSO_EMAIL_IDS[day]
            send_email_to_subscriber(token, email_id, sub_id)
            new_metadata = {**metadata, day_key: now.isoformat()}
            # Si es el último día, marcar completo también
            if day == 5:
                new_metadata["curso_completed_at"] = now.isoformat()
            patch_metadata(token, sub_id, new_metadata)
            return {
                "action": f"sent_dia_{day}",
                "subscriber_id": sub_id,
                "email_id": email_id,
                "metadata": new_metadata,
            }
        else:
            return {
                "action": "skip",
                "reason": f"waiting_for_dia_{day}",
                "subscriber_id": sub_id,
                "next_at": (last_sent + DAY_DELAY).isoformat(),
            }

    # Si llegamos aquí, todos los días están enviados pero no marcado como completed
    # (caso edge: metadata de alguien que completó antes de añadir el campo completed)
    new_metadata = {**metadata, "curso_completed_at": now.isoformat()}
    patch_metadata(token, sub_id, new_metadata)
    return {
        "action": "marked_completed",
        "subscriber_id": sub_id,
        "metadata": new_metadata,
    }


def main():
    execute = "--execute" in sys.argv
    if not execute:
        print(json.dumps({
            "ok": True,
            "dry_run": True,
            "message": "No se han consultado suscriptores ni enviado emails. Ejecuta con --execute solo tras aprobacion explicita.",
        }, ensure_ascii=False))
        return
    token = get_token()
    now = datetime.now(timezone.utc)
    sent_log = []
    skipped = 0
    errors = 0

    try:
        subs = list_active_subscribers(token)
    except (HTTPError, URLError) as e:
        print(json.dumps({"ok": False, "error": f"list_subscribers_failed: {e}"}))
        sys.exit(1)

    for sub in subs:
        try:
            result = process_subscriber(sub, now, token)
            # Append every result so skips carry their reason (waiting_for_dia_N,
            # stale_subscriber, too_new, etc.) — useful for diagnostics without
            # having to query Buttondown afterwards.
            sent_log.append(result)
            if not (result["action"].startswith("sent_") or result["action"] == "marked_completed"):
                skipped += 1
        except (HTTPError, URLError) as e:
            errors += 1
            sent_log.append({
                "action": "error",
                "subscriber_id": sub.get("id"),
                "error": str(e),
            })

    # Split into sends/marks vs skips vs errors for cleaner observability.
    actions = [r for r in sent_log if r["action"].startswith("sent_") or r["action"] == "marked_completed"]
    skips = [r for r in sent_log if r not in actions and r["action"] != "error"]
    error_log = [r for r in sent_log if r["action"] == "error"]

    print(json.dumps({
        "ok": True,
        "timestamp": now.isoformat(),
        "total_subscribers": len(subs),
        "sent": len([r for r in actions if r["action"].startswith("sent_")]),
        "marked_completed": len([r for r in actions if r["action"] == "marked_completed"]),
        "skipped": len(skips),
        "errors": len(error_log),
        "actions": actions,
        "skips": skips,
        "error_log": error_log,
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
