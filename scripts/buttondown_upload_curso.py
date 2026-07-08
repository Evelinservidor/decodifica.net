#!/usr/bin/env python3
"""
Sube los 5 emails del mini-curso a Buttondown como DRAFTS.
Extrae subject y body de cada archivo .md.

Output: data/buttondown_emails.json con mapeo dia-N -> email_id.
"""
import json
import os
import re
import sys
from pathlib import Path
from urllib import request as urlrequest
from urllib.error import HTTPError, URLError

BASE_URL = "https://api.buttondown.email/v1"
ROOT = Path(__file__).resolve().parents[1]
CRED_PATH = Path(os.environ.get(
    "BUTTONDOWN_TOKEN_FILE",
    Path.home() / ".codex" / "decodifica" / "credentials" / "buttondown_token.json",
))
CURSO_DIR = ROOT / "lead-magnets" / "mini-curso"
OUTPUT_PATH = ROOT / "data" / "buttondown_emails.json"

DAYS = [
    ("dia-1-setup.md", "Día 1 de 5: el setup que cambia cómo ChatGPT te responde"),
    ("dia-2-estructura-prompts.md", "Día 2 de 5: el framework RTF para escribir prompts que funcionan siempre"),
    ("dia-3-contexto-archivos.md", "Día 3 de 5: cómo hacer que ChatGPT lea TUS documentos (no los de internet)"),
    ("dia-4-iteracion.md", "Día 4 de 5: el truco del segundo turno (el 90% no lo hace)"),
    ("dia-5-agentes.md", "Día 5 de 5: tu primer Custom GPT en 10 minutos (sin programar)"),
]


def get_token() -> str:
    env_token = os.environ.get("BUTTONDOWN_API_TOKEN")
    if env_token:
        return env_token
    cred = json.loads(CRED_PATH.read_text(encoding="utf-8-sig"))
    return cred["api_token"]


def post_email(token: str, subject: str, body: str) -> dict:
    payload = {"subject": subject, "body": body, "status": "draft"}
    data = json.dumps(payload).encode("utf-8")
    req = urlrequest.Request(
        f"{BASE_URL}/emails",
        data=data,
        method="POST",
        headers={
            "Authorization": f"Token {token}",
            "Content-Type": "application/json",
        },
    )
    with urlrequest.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def parse_md(path: Path, fallback_subject: str) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8")
    # Subject: try to extract from "**Asunto:** ..." line, else fallback
    m = re.search(r"\*\*Asunto:\*\*\s*(.+)", text)
    subject = m.group(1).strip() if m else fallback_subject
    # Body: from the first "---" separator onward (skip frontmatter-like top)
    parts = text.split("\n---\n", 1)
    body = parts[1].strip() if len(parts) == 2 else text
    return subject, body


def main():
    execute = "--execute" in sys.argv
    token = get_token() if execute else ""
    existing = {}
    if execute and OUTPUT_PATH.exists():
        try:
            existing = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            existing = {}

    results = dict(existing)
    for filename, fallback_subject in DAYS:
        slug = filename.replace(".md", "")
        if execute and slug in results and results[slug].get("email_id"):
            print(f"[skip] {slug} ya tiene email_id {results[slug]['email_id']}", flush=True)
            continue
        path = CURSO_DIR / filename
        if not path.exists():
            print(f"[error] no existe {path}", file=sys.stderr, flush=True)
            continue
        subject, body = parse_md(path, fallback_subject)
        if not execute:
            results[slug] = {
                "subject": subject,
                "filename": filename,
                "status": "dry_run",
                "body_chars": len(body),
            }
            print(f"[dry-run] {slug}: {subject}", flush=True)
            continue
        try:
            resp = post_email(token, subject, body)
            email_id = resp.get("id")
            results[slug] = {
                "email_id": email_id,
                "subject": subject,
                "filename": filename,
                "status": resp.get("status", "draft"),
            }
            print(f"[ok] {slug} -> {email_id}", flush=True)
        except HTTPError as e:
            err = e.read().decode("utf-8", errors="replace")
            print(f"[http {e.code}] {slug}: {err[:300]}", file=sys.stderr, flush=True)
            results[slug] = {"error": err[:500], "filename": filename}
        except URLError as e:
            print(f"[url] {slug}: {e.reason}", file=sys.stderr, flush=True)

    if execute:
        OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT_PATH.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"\nMapeo guardado en {OUTPUT_PATH}")
    else:
        print("\nDry-run: no se han creado drafts ni escrito estado.")


if __name__ == "__main__":
    main()
