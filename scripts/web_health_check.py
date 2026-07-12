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
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse


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
    "/lead-magnets/workflows-ia-dia-a-dia.pdf",
    "/newsletter/",
    "/comunidad/",
    "/contacto/",
    "/quienes-somos/",
    "/privacidad/",
    "/cookies/",
    "/sitemap-index.xml",
    "/robots.txt",
]

IGNORED_LINK_SCHEMES = {"data", "javascript", "mailto", "tel"}

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


def load_public_env(repo: Path) -> dict[str, str]:
    env_path = repo / ".env.local"
    if not env_path.exists():
        return {}

    values: dict[str, str] = {}
    for raw_line in env_path.read_text(encoding="utf-8-sig", errors="strict").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        if not key.startswith("PUBLIC_"):
            continue
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
            value = value[1:-1]
        values[key] = value
    return values


def run_build(repo: Path) -> dict:
    npm = shutil.which("npm") or shutil.which("npm.cmd")
    if not npm:
        return {
            "ok": False,
            "returncode": None,
            "stdout_tail": "",
            "stderr_tail": "npm executable not found in PATH",
        }
    build_env = os.environ.copy()
    build_env.update(load_public_env(repo))
    proc = subprocess.run(
        [npm, "run", "build"],
        cwd=str(repo),
        env=build_env,
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


class HrefParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.hrefs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "a":
            return
        for name, value in attrs:
            if name.lower() == "href" and value:
                self.hrefs.append(value)


class AssetParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.assets: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = {name.lower(): value for name, value in attrs}
        if tag.lower() == "img" and attributes.get("src"):
            self.assets.append(str(attributes["src"]))
        elif tag.lower() == "source" and attributes.get("srcset"):
            self.assets.extend(candidate.strip().split()[0] for candidate in str(attributes["srcset"]).split(",") if candidate.strip())
        elif tag.lower() == "meta":
            key = str(attributes.get("property") or attributes.get("name") or "").lower()
            if key in {"og:image", "twitter:image"} and attributes.get("content"):
                self.assets.append(str(attributes["content"]))


def normalize_internal_path(href: str, page_url: str, site_url: str) -> str | None:
    href = href.strip()
    if not href or href.startswith("#"):
        return None

    raw = urlparse(href)
    if raw.scheme.lower() in IGNORED_LINK_SCHEMES:
        return None

    resolved = urlparse(urljoin(page_url, href))
    site = urlparse(site_url)
    allowed_hosts = {site.netloc.lower()}
    if site.netloc.lower().startswith("www."):
        allowed_hosts.add(site.netloc.lower()[4:])
    else:
        allowed_hosts.add(f"www.{site.netloc.lower()}")

    if resolved.scheme not in {"http", "https"} or resolved.netloc.lower() not in allowed_hosts:
        return None

    return resolved.path or "/"


def built_page_route(path: Path, dist: Path) -> str:
    relative_path = path.relative_to(dist).as_posix()
    if relative_path == "index.html":
        return "/"
    if relative_path.endswith("/index.html"):
        return f"/{relative_path[:-len('index.html')]}"
    return f"/{relative_path}"


def collect_built_internal_paths(repo: Path, site_url: str) -> list[str]:
    dist = repo / "dist"
    if not dist.exists():
        return []

    discovered: set[str] = set()
    for path in dist.rglob("*.html"):
        page_route = built_page_route(path, dist)
        page_url = urljoin(f"{site_url.rstrip('/')}/", page_route.lstrip("/"))
        parser = HrefParser()
        parser.feed(path.read_text(encoding="utf-8-sig", errors="replace"))
        for href in parser.hrefs:
            internal_path = normalize_internal_path(href, page_url, site_url)
            if internal_path:
                discovered.add(internal_path)

    return sorted(discovered)


def collect_built_assets(repo: Path, site_url: str) -> list[dict]:
    dist = repo / "dist"
    if not dist.exists():
        return []

    discovered: dict[str, set[str]] = {}
    for path in dist.rglob("*.html"):
        page_route = built_page_route(path, dist)
        page_url = urljoin(f"{site_url.rstrip('/')}/", page_route.lstrip("/"))
        parser = AssetParser()
        parser.feed(path.read_text(encoding="utf-8-sig", errors="replace"))
        for asset in parser.assets:
            asset = asset.strip()
            if not asset or asset.startswith("#") or asset.startswith("data:"):
                continue
            resolved = urljoin(page_url, asset)
            if urlparse(resolved).scheme not in {"http", "https"}:
                continue
            discovered.setdefault(resolved, set()).add(page_route)

    return [{"url": url, "pages": sorted(pages)} for url, pages in sorted(discovered.items())]


def fetch_url(url: str, timeout: int = 15) -> dict:
    request = urllib.request.Request(url, headers={"User-Agent": "DecodificaWebHealth/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw_body = response.read(200000)
            content_type = response.headers.get_content_type()
            is_text = content_type.startswith("text/") or content_type in {
                "application/json",
                "application/javascript",
                "application/xml",
            }
            body_sample = raw_body.decode(response.headers.get_content_charset() or "utf-8", errors="replace")[:1000] if is_text else ""
            return {
                "url": url,
                "ok": 200 <= response.status < 400,
                "status": response.status,
                "length": len(raw_body),
                "content_type": content_type,
                "body_sample": body_sample,
            }
    except urllib.error.HTTPError as exc:
        return {"url": url, "ok": False, "status": exc.code, "error": str(exc)}
    except Exception as exc:
        return {"url": url, "ok": False, "status": None, "error": str(exc)}


def fetch_assets(built_assets: list[dict]) -> list[dict]:
    results: list[dict] = []
    for asset in built_assets:
        result = fetch_url(asset["url"])
        result["pages"] = asset["pages"]
        result["ok"] = bool(result.get("ok")) and str(result.get("content_type", "")).startswith("image/")
        results.append(result)
    return results


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
    failed_assets = [item for item in report["assets"] if not item["ok"]]
    copy_matches = report["internal_copy_matches"]
    missing_emails = [item for item in report["emails"] if not item["present"]]
    missing_socials = [item for item in report["socials"] if not item["present"]]
    recommendations = "\n".join(f"- {item}" for item in report["recommendations"]) or "- No immediate action."
    failed = "\n".join(f"- {item['url']}: {item.get('status') or item.get('error')}" for item in failed_urls) or "- none"
    failed_asset_lines = "\n".join(
        f"- {item['url']}: {item.get('status') or item.get('error')} ({item.get('content_type') or 'unknown type'})"
        for item in failed_assets
    ) or "- none"
    copy = "\n".join(f"- {item['path']}:{item['line']} -> {item['pattern']}" for item in copy_matches) or "- none"
    return f"""# Decodifica Web Health

Generated: {report['generated_at']}

## Status

- Overall ok: {report['ok']}
- Build ok: {report['build']['ok']}
- Production URLs checked: {len(production)}
- Internal paths discovered from build: {len(report['discovered_internal_paths'])}
- Production URL failures: {len(failed_urls)}
- Image/social assets checked: {len(report['assets'])}
- Image/social asset failures: {len(failed_assets)}
- Internal copy matches: {len(copy_matches)}
- Missing emails: {len(missing_emails)}
- Missing socials: {len(missing_socials)}

## Failed URLs

{failed}

## Failed Image and Social Assets

{failed_asset_lines}

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
    discovered_internal_paths = collect_built_internal_paths(repo, site_url)
    built_assets = collect_built_assets(repo, site_url)
    production_paths = sorted(set(REQUIRED_PATHS) | set(discovered_internal_paths))
    production = [] if args.skip_production else [fetch_url(f"{site_url}{path}") for path in production_paths]
    assets = [] if args.skip_production else fetch_assets(built_assets)
    copy_matches = scan_internal_copy(repo)
    emails = source_presence(repo, REQUIRED_EMAILS)
    socials = source_presence(repo, REQUIRED_SOCIALS)

    recommendations = []
    if not build.get("ok"):
        recommendations.append("Fix Astro build before shipping any web change.")
    if any(not item["ok"] for item in production):
        recommendations.append("Review failed production URLs before promoting new pages or CTAs.")
    if any(not item["ok"] for item in assets):
        recommendations.append("Restore broken image or social-preview assets before sharing affected pages.")
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
        and all(item["ok"] for item in assets)
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
        "discovered_internal_paths": discovered_internal_paths,
        "production": production,
        "assets": assets,
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
