#!/usr/bin/env python3
"""Publica un borrador semanal de Decodifica en Buttondown de forma idempotente.

El script está diseñado para ser llamado por la automatización semanal después
de crear el borrador. Sin ``--execute`` solo informa de lo que haría.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError

from buttondown_curso_engine import api, get_token, list_active_subscribers


ROOT = Path(__file__).resolve().parents[1]
DRAFTS = ROOT / "lead-magnets" / "newsletter-drafts"
SEND_LOG = DRAFTS / "registro-envios"
SOURCE = "decodifica_weekly_editorial"


def write_summary(
    path: Path | None,
    *,
    ok: bool,
    status: str,
    execute: bool,
    sent: bool,
    audience: int,
    failures: list[str],
) -> None:
    """Escribe evidencia sanitaria sin asunto, contenido ni datos personales."""
    if path is None:
        return
    payload = {
        "schema_version": "decodifica-newsletter-weekly-1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "ok": ok,
        "status": status,
        "execute": execute,
        "sent": sent,
        "audience_active": audience,
        "errors": len(failures),
        "failure_codes": failures,
        "contains_personal_data": False,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def latest_draft() -> Path:
    candidates = sorted(DRAFTS.glob("numero-*.md"), key=lambda path: path.stat().st_mtime, reverse=True)
    if not candidates:
        raise RuntimeError("weekly_draft_missing")
    return candidates[0]


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, flags=re.S)
    if not match:
        return {}, text
    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip()
    return values, text[match.end() :]


def extract_subject(text: str) -> str | None:
    match = re.search(r"^- \[[xX]\] Asunto (?:usado|sugerido):\s*(.+)$", text, flags=re.M)
    return match.group(1).strip() if match else None


def extract_preheader(text: str) -> str | None:
    match = re.search(r"^- \[[xX]\] Preheader (?:usado|sugerido):\s*(.+)$", text, flags=re.M)
    return match.group(1).strip() if match else None


def reader_body(text: str) -> str:
    return re.split(r"\n## (?:Fuentes revisadas|Checklist antes de enviar)\n", text, maxsplit=1)[0].strip()


def open_checklist_items(text: str) -> list[str]:
    return re.findall(r"^- \[ \]\s*(.+)$", text, flags=re.M)


def local_send_exists(draft_name: str) -> bool:
    if not SEND_LOG.exists():
        return False
    for path in SEND_LOG.glob("*.json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8-sig"))
        except json.JSONDecodeError:
            continue
        if data.get("draft") == draft_name and (data.get("buttondown") or {}).get("status") == "sent":
            return True
    return False


def remote_send_exists(token: str, draft_name: str, issue_date: str) -> bool:
    page = 1
    while True:
        result = api("GET", f"/emails?page={page}&page_size=100", token) or {}
        for email in result.get("results", []):
            metadata = email.get("metadata") or {}
            if (
                email.get("status") == "sent"
                and metadata.get("source") == SOURCE
                and (metadata.get("draft") == draft_name or metadata.get("issue_date") == issue_date)
            ):
                return True
        if not result.get("next"):
            return False
        page += 1


def write_send_log(draft: Path, issue_date: str, subject: str, response: dict, audience: int) -> Path:
    SEND_LOG.mkdir(parents=True, exist_ok=True)
    path = SEND_LOG / f"{issue_date}-weekly.json"
    payload = {
        "sent_at_utc": response.get("publish_date") or response.get("published_at"),
        "draft": draft.name,
        "subject": subject,
        "audience_active_at_send": audience,
        "buttondown": {
            "id": response.get("id"),
            "status": response.get("status"),
            "email_type": response.get("email_type"),
            "archival_mode": response.get("archival_mode"),
            "commenting_mode": response.get("commenting_mode"),
        },
        "follow_up": {"clicks": "pending", "responses": "pending", "unsubscribes": "pending"},
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description="Publica una newsletter semanal de Decodifica en Buttondown.")
    parser.add_argument("--draft", type=Path, help="Borrador numero-YYYY-MM-DD.md; por defecto, el más reciente.")
    parser.add_argument("--execute", action="store_true", help="Publica en Buttondown. Sin este flag, solo inspecciona.")
    parser.add_argument("--summary-output", type=Path, help="Evidencia sanitaria JSON sin datos personales.")
    args = parser.parse_args()

    draft = args.draft or latest_draft()
    if not draft.is_file():
        failures = ["draft_not_found"]
        write_summary(
            args.summary_output,
            ok=False,
            status="blocked",
            execute=args.execute,
            sent=False,
            audience=0,
            failures=failures,
        )
        print(json.dumps({"ok": False, "failures": failures}, ensure_ascii=False))
        return 1
    frontmatter, raw_body = parse_frontmatter(draft.read_text(encoding="utf-8"))
    issue_date = frontmatter.get("fecha")
    subject = extract_subject(raw_body)
    preheader = extract_preheader(raw_body)
    pending = open_checklist_items(raw_body)
    body = reader_body(raw_body)

    failures: list[str] = []
    if frontmatter.get("estado") == "enviado" or local_send_exists(draft.name):
        failures.append("already_sent_locally")
    if not issue_date:
        failures.append("issue_date_missing")
    if not subject:
        failures.append("approved_subject_missing")
    if not preheader:
        failures.append("approved_preheader_missing")
    if not body:
        failures.append("reader_body_missing")
    if "## Fuentes revisadas" not in raw_body or "## Checklist antes de enviar" not in raw_body:
        failures.append("review_sections_missing")
    if pending:
        failures.append("checklist_pending")

    try:
        token = get_token()
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        failures.append("buttondown_credentials_unavailable")
        audience = 0
        token = None
    try:
        if token and issue_date and remote_send_exists(token, draft.name, issue_date):
            failures.append("already_sent_remotely")
        if token:
            audience = len(list_active_subscribers(token))
    except (HTTPError, URLError) as exc:
        failures.append(f"buttondown_read_failed:{type(exc).__name__}")
        audience = 0
    if audience < 1:
        failures.append("no_active_subscribers")

    summary = {
        "ok": not failures,
        "execute": args.execute,
        "draft": draft.name,
        "issue_date": issue_date,
        "subject": subject,
        "reader_body_chars": len(body),
        "audience_active": audience,
        "failures": failures,
    }
    if not args.execute or failures:
        write_summary(
            args.summary_output,
            ok=not failures,
            status="ready" if not failures else "blocked",
            execute=args.execute,
            sent=False,
            audience=audience,
            failures=failures,
        )
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return 0 if not failures else 1

    payload = {
        "subject": subject,
        "description": preheader,
        "body": body,
        "email_type": "public",
        "archival_mode": "enabled",
        "commenting_mode": "disabled",
        "metadata": {"source": SOURCE, "draft": draft.name, "issue_date": issue_date},
    }
    try:
        created = api("POST", "/emails", token, {**payload, "status": "draft"}) or {}
        email_id = created.get("id")
        if not email_id:
            raise RuntimeError("buttondown_email_id_missing")
        sent = api("POST", f"/emails/{email_id}/publish", token, payload) or {}
        if sent.get("status") != "sent":
            raise RuntimeError("buttondown_publish_not_sent")
        log_path = write_send_log(draft, issue_date, subject, sent, audience)
        write_summary(
            args.summary_output,
            ok=True,
            status="sent",
            execute=True,
            sent=True,
            audience=audience,
            failures=[],
        )
        print(json.dumps({**summary, "ok": True, "sent": True, "send_log": str(log_path)}, ensure_ascii=False, indent=2))
        return 0
    except (HTTPError, URLError, RuntimeError) as exc:
        failure_codes = [type(exc).__name__]
        write_summary(
            args.summary_output,
            ok=False,
            status="blocked",
            execute=True,
            sent=False,
            audience=audience,
            failures=failure_codes,
        )
        print(json.dumps({**summary, "ok": False, "sent": False, "error": type(exc).__name__}, ensure_ascii=False, indent=2))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
