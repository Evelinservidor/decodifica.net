#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import date, datetime
from pathlib import Path


WEB_REPO = Path(__file__).resolve().parents[1]
DEFAULT_OPS_CONFIG = Path(os.environ.get("DECODIFICA_WEB_CONFIG", r"D:\gpt decodifica\_web\config\web-targets.json"))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

REQUIRED_PATHS = [
    "/",
    "/herramientas/",
    "/herramientas/para-estudiar/",
    "/herramientas/para-crear-contenido/",
    "/herramientas/para-programar/",
    "/herramientas/para-presentaciones/",
    "/recursos/mapa-herramientas-ia/",
    "/herramientas/alternativas-elevenlabs/",
    "/herramientas/chatgpt-vs-claude/",
    "/herramientas/gamma-vs-canva-ai/",
    "/herramientas/notebooklm-vs-perplexity/",
    "/herramientas/chatgpt/",
    "/herramientas/claude/",
    "/herramientas/notebooklm/",
    "/herramientas/perplexity/",
    "/herramientas/gamma/",
    "/herramientas/canva-ai/",
    "/herramientas/elevenlabs/",
    "/herramientas/qwen-code/",
    "/herramientas/deepseek/",
    "/recursos/",
    "/newsletter/",
    "/comunidad/",
    "/contacto/",
    "/quienes-somos/",
    "/privacidad/",
    "/cookies/",
    "/sitemap-index.xml",
    "/robots.txt",
]

INTERNAL_COPY_PATTERNS = [
    "como funciona el embudo",
    "youtube descubre",
    "la web ordena",
    "email retiene",
    "convertir visitas",
    "nota de produccion",
    "post corto",
    "comunidad esta preparada",
    "no depender solo del algoritmo",
    "cta unica",
]

REQUIRED_EMAILS = [
    "hola@decodifica.net",
    "colaboraciones@decodifica.net",
]

REQUIRED_SOCIALS = {
    "bluesky": "https://bsky.app/profile/jc-ia.bsky.social",
    "tiktok": "https://www.tiktok.com/@decodificalaia",
    "facebook": "https://www.facebook.com/JCAutomatizacionesIA",
    "youtube": "https://www.youtube.com/@decodificaia",
}


def now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")


def read_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value.rstrip() + "\n", encoding="utf-8")


def relative(path: Path, base: Path) -> str:
    try:
        return str(path.relative_to(base))
    except ValueError:
        return str(path)


def load_config(path: Path | None) -> dict:
    config_path = path or DEFAULT_OPS_CONFIG
    config = read_json(config_path)
    if config:
        config["_config_path"] = str(config_path)
        return config
    return {
        "_config_path": None,
        "repo_path": str(WEB_REPO),
        "site_url": "https://decodifica.net",
        "reports_root": str(WEB_REPO / "reports"),
    }


def run_build(repo: Path) -> dict:
    npm = shutil.which("npm") or shutil.which("npm.cmd")
    if not npm:
        return {
            "ok": False,
            "returncode": None,
            "stdout_tail": "",
            "stderr_tail": "npm executable not found in PATH",
        }
    proc = subprocess.run(
        [npm, "run", "build"],
        cwd=str(repo),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    return {
        "ok": proc.returncode == 0,
        "returncode": proc.returncode,
        "stdout_tail": proc.stdout[-5000:],
        "stderr_tail": proc.stderr[-5000:],
    }


def fetch_url(url: str, timeout: int = 15) -> dict:
    request = urllib.request.Request(url, headers={"User-Agent": "DecodificaWebHealth/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read(200000).decode("utf-8", errors="replace")
            return {
                "url": url,
                "ok": 200 <= response.status < 400,
                "status": response.status,
                "length": len(body),
                "body_sample": body[:1000],
            }
    except urllib.error.HTTPError as exc:
        return {"url": url, "ok": False, "status": exc.code, "error": str(exc)}
    except Exception as exc:
        return {"url": url, "ok": False, "status": None, "error": str(exc)}


def iter_source_files(repo: Path):
    roots = [repo / "src" / "pages", repo / "src" / "components", repo / "src" / "data", repo / "src" / "lib"]
    for root in roots:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if path.suffix.lower() in {".astro", ".ts", ".tsx", ".js", ".jsx", ".md", ".mdx"}:
                yield path


def scan_internal_copy(repo: Path) -> list[dict]:
    matches: list[dict] = []
    for path in iter_source_files(repo):
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        lower = text.lower()
        for pattern in INTERNAL_COPY_PATTERNS:
            if pattern in lower:
                line_no = lower[: lower.index(pattern)].count("\n") + 1
                matches.append({"path": relative(path, repo), "line": line_no, "pattern": pattern})
    return matches


def source_presence(repo: Path, values: list[str] | dict[str, str]) -> list[dict]:
    text = "\n".join(path.read_text(encoding="utf-8-sig", errors="replace") for path in iter_source_files(repo))
    items = values.items() if isinstance(values, dict) else [(value, value) for value in values]
    return [{"name": name, "value": value, "present": value in text} for name, value in items]


def markdown(report: dict) -> str:
    production = report["production"]
    failed_urls = [item for item in production if not item["ok"]]
    copy_matches = report["internal_copy_matches"]
    missing_emails = [item for item in report["emails"] if not item["present"]]
    missing_socials = [item for item in report["socials"] if not item["present"]]
    recommendations = "\n".join(f"- {item}" for item in report["recommendations"]) or "- No immediate action."
    failed = "\n".join(f"- {item['url']}: {item.get('status') or item.get('error')}" for item in failed_urls) or "- none"
    copy = "\n".join(f"- {item['path']}:{item['line']} -> {item['pattern']}" for item in copy_matches) or "- none"
    return f"""# Decodifica Web Health

Generated: {report['generated_at']}

## Status

- Overall ok: {report['ok']}
- Build ok: {report['build']['ok']}
- Production URL failures: {len(failed_urls)}
- Internal copy matches: {len(copy_matches)}
- Missing emails: {len(missing_emails)}
- Missing socials: {len(missing_socials)}

## Failed URLs

{failed}

## Internal Copy Matches

{copy}

## Recommendations

{recommendations}
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Dry-run Decodifica web health check. Never publishes.")
    parser.add_argument("--config", type=Path, help="Optional web-targets.json path.")
    parser.add_argument("--skip-build", action="store_true")
    parser.add_argument("--skip-production", action="store_true")
    args = parser.parse_args()

    config = load_config(args.config)
    repo = Path(config.get("repo_path", WEB_REPO))
    reports_root = Path(config.get("reports_root", str(WEB_REPO / "reports")))
    site_url = str(config.get("site_url", "https://decodifica.net")).rstrip("/")

    build = {"ok": True, "skipped": True} if args.skip_build else run_build(repo)
    production = [] if args.skip_production else [fetch_url(f"{site_url}{path}") for path in REQUIRED_PATHS]
    copy_matches = scan_internal_copy(repo)
    emails = source_presence(repo, REQUIRED_EMAILS)
    socials = source_presence(repo, REQUIRED_SOCIALS)

    recommendations = []
    if not build.get("ok"):
        recommendations.append("Fix Astro build before shipping any web change.")
    if any(not item["ok"] for item in production):
        recommendations.append("Review failed production URLs before promoting new pages or CTAs.")
    if copy_matches:
        recommendations.append("Rewrite internal-production copy matches into reader-facing public copy.")
    if any(not item["present"] for item in emails):
        recommendations.append("Add the missing public contact emails to the relevant web surfaces.")
    if any(not item["present"] for item in socials):
        recommendations.append("Restore missing real social links in site configuration/navigation.")
    if not recommendations:
        recommendations.append("Keep current conversion surfaces stable and use weekly GSC data for the next changes.")

    ok = (
        bool(build.get("ok"))
        and all(item["ok"] for item in production)
        and not copy_matches
        and all(item["present"] for item in emails)
        and all(item["present"] for item in socials)
    )
    report = {
        "generated_at": now_iso(),
        "job": "daily-health",
        "auto_publish": False,
        "ok": ok,
        "config_path": config.get("_config_path"),
        "repo_path": str(repo),
        "build": build,
        "production": production,
        "internal_copy_matches": copy_matches,
        "emails": emails,
        "socials": socials,
        "recommendations": recommendations,
    }
    out_dir = reports_root / "health" / date.today().isoformat()
    write_json(out_dir / "web-health.json", report)
    write_text(out_dir / "web-health.md", markdown(report))
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
