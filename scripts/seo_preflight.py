#!/usr/bin/env python3
"""Revisión SEO y editorial de artículos de Decodifica antes de publicarlos.

Adaptado de decodifica-ops/_web/scripts/seo_preflight.py y _web/SEO-RULES.md.

Uso:
  python scripts/seo_preflight.py src/pages/blog/mi-articulo.astro [...]
  python scripts/seo_preflight.py --changed      # artículos cambiados frente a origin/main

Sale con código 1 si algún artículo tiene errores (los avisos no bloquean).
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "src" / "pages" / "blog"
PAGES = ROOT / "src" / "pages"

TITLE_MIN, TITLE_MAX = 35, 60          # el sitio añade " | Decodifica"
DESC_MIN, DESC_MAX = 110, 165
MIN_H2, MIN_INTERNAL, MIN_EXTERNAL = 3, 2, 2

# Frases de relleno y de plantilla que no deben aparecer (reglas de la casa).
BANNED = [
    "en el mundo actual", "revolucionari", "cambia las reglas del juego", "cambiar las reglas del juego",
    "no es solo", "sin precedentes", "en la era de", "hay herramientas de ia que llaman la atención",
    "para mi, una herramienta empieza", "la prueba buena no es abrir", "próximo vídeo", "cuéntame en comentarios",
    "en el vídeo", "he probado", "lo uso a diario", "en mis pruebas", "corre a", "antes de que lo quiten",
    "no te lo vas a creer", "increíble", "brutal",
]
FORBIDDEN_LINKS = ["youtube.com/@decodifica", "/comunidad/", "/login/"]
MOJIBAKE = ["Ã©", "Ã³", "Ã¡", "Ã±", "Ã‚", "Ãƒ", "â€"]


def const(text: str, name: str) -> str | None:
    m = re.search(rf"const\s+{name}\s*=\s*([\"'])(.*?)\1\s*;", text, flags=re.S)
    return m.group(2).strip() if m else None


def internal_target_exists(href: str) -> bool:
    path = href.split("#")[0].split("?")[0].strip("/")
    if not path:
        return True
    if path.startswith(("lead-magnets/", "og/", "downloads/")):
        return (ROOT / "public" / path).exists()
    candidates = [PAGES / f"{path}.astro", PAGES / path / "index.astro"]
    parent = (PAGES / path).parent
    # Rutas dinámicas ([slug].astro): se aceptan si existe la plantilla.
    candidates.append(parent / "[slug].astro")
    return any(c.exists() for c in candidates)


def audit(path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    text = path.read_text(encoding="utf-8")
    if "Astro.redirect(" in text:
        return errors, warnings

    title = const(text, "title")
    desc = const(text, "description")
    pub = const(text, "pubDate")
    mod = const(text, "modifiedDate")

    if not title:
        errors.append("falta const title")
    elif not TITLE_MIN <= len(title) <= TITLE_MAX:
        warnings.append(f"título de {len(title)} caracteres (ideal {TITLE_MIN}-{TITLE_MAX})")
    if not desc:
        errors.append("falta const description")
    else:
        if not DESC_MIN <= len(desc) <= DESC_MAX:
            warnings.append(f"descripción de {len(desc)} caracteres (ideal {DESC_MIN}-{DESC_MAX})")
        if desc.endswith("..."):
            errors.append("la descripción termina en «...»")
    for name, value in (("pubDate", pub), ("modifiedDate", mod)):
        if value and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
            errors.append(f"{name} no tiene formato AAAA-MM-DD")
    if not pub:
        errors.append("falta const pubDate")

    body = text.split("---", 2)[-1]
    h1 = len(re.findall(r"<h1\b", body))
    if h1 != 1:
        errors.append(f"{h1} H1 (debe haber 1)")
    h2 = len(re.findall(r"<h2\b", body))
    if h2 < MIN_H2:
        warnings.append(f"solo {h2} secciones H2 (mínimo {MIN_H2})")

    internal = re.findall(r'href="(/[^"#][^"]*)"', body)
    external = {h for h in re.findall(r'href="(https?://[^"]+)"', body) if "decodifica.net" not in h}
    if len(set(internal)) < MIN_INTERNAL:
        warnings.append(f"{len(set(internal))} enlaces internos (mínimo {MIN_INTERNAL})")
    if len(external) < MIN_EXTERNAL:
        errors.append(f"{len(external)} fuentes externas (mínimo {MIN_EXTERNAL})")
    for href in sorted(set(internal)):
        if not internal_target_exists(href):
            errors.append(f"enlace interno roto: {href}")

    if "ogImage" not in text:
        warnings.append("sin ogImage")
    if "ConversionBand" not in text and "embed-subscribe" not in text:
        warnings.append("sin llamada a la newsletter")

    lower = re.sub(r"<[^>]+>", " ", body).lower()
    for phrase in BANNED:
        if phrase in lower:
            errors.append(f"frase prohibida: «{phrase}»")
    for link in FORBIDDEN_LINKS:
        if link in text:
            errors.append(f"enlace prohibido: {link}")
    for mark in MOJIBAKE:
        if mark in text:
            errors.append(f"texto con caracteres rotos ({mark})")
    if re.search(r"\b(TL;DR)\b", body) and "Qué mirar:</strong> si la herramienta" in body:
        errors.append("bloque TL;DR genérico de plantilla")
    return errors, warnings


def changed_articles() -> list[Path]:
    out = subprocess.run(
        ["git", "diff", "--name-only", "origin/main...HEAD", "--", "src/pages/blog/"],
        cwd=ROOT, capture_output=True, text=True, check=False,
    ).stdout.split()
    return [ROOT / p for p in out if p.endswith(".astro") and (ROOT / p).exists() and not p.endswith("index.astro")]


def main(argv: list[str]) -> int:
    files = changed_articles() if argv[:1] == ["--changed"] else [Path(a).resolve() for a in argv]
    files = [f for f in files if f.name != "index.astro"]
    if not files:
        print("No hay artículos que revisar.")
        return 0
    failed = False
    for f in files:
        errors, warnings = audit(f)
        status = "ERROR" if errors else ("AVISOS" if warnings else "OK")
        print(f"[{status}] {f.relative_to(ROOT)}")
        for e in errors:
            print(f"   ✗ {e}")
        for w in warnings:
            print(f"   · {w}")
        failed |= bool(errors)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
