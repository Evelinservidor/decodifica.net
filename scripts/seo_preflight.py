#!/usr/bin/env python3
"""Revisión SEO y editorial de artículos de Decodifica antes de publicarlos.

Adaptado de decodifica-ops/_web/scripts/seo_preflight.py y _web/SEO-RULES.md.

Uso:
  python scripts/seo_preflight.py src/pages/blog/mi-articulo.astro [...]
  python scripts/seo_preflight.py --changed      # artículos cambiados frente a origin/main

Sale con código 1 si algún artículo tiene errores (los avisos no bloquean).
"""
from __future__ import annotations

import json
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
PORTADAS = ROOT / "src" / "data" / "portadas.json"
VARIANTES = [".jpg", "-tarjeta.webp", "-tarjeta-960.webp", "-16x9.webp", "-16x9-800.webp", "-4x3.webp", "-1x1.webp"]
MIN_FIGURAS = 2
MAX_KB_FIGURA = 200
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
    h1 = len(re.findall(r"<h1\b", body)) + len(re.findall(r"<Articulo\b", body))  # <Articulo> pinta el H1
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

    audit_images(path.stem, text, body, errors, warnings)
    usa_articulo = f'<Articulo slug="{path.stem}"' in body
    if not usa_articulo:
        errors.append(f'sin la plantilla común: envuelve el texto en <Articulo slug="{path.stem}"> (docs/AGENTE-SEMANAL.md)')
    if not re.search(r'^const\s+tema\s*=\s*["\'](chatbots|local|automatizar|oficina|crear)["\']', text, flags=re.M):
        errors.append('falta const tema = "…" (chatbots, local, automatizar, oficina o crear: src/lib/temas.ts)')
    if not usa_articulo and "ConversionBand" not in text and "embed-subscribe" not in text:
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
    # Para que nos citen las IA (docs/AGENTE-SEMANAL.md)
    if re.search(r'["\']@type["\']\s*:\s*["\']Article["\']', body):
        errors.append("bloque JSON-LD Article propio: usa citations={[...]} en BaseLayout")
    if "citations=" not in text:
        warnings.append("sin citations={[...]} en BaseLayout (fuentes en los datos estructurados)")
    if not usa_articulo and "datetime={modifiedDate}" not in body:
        warnings.append("la cabecera no muestra la fecha de revisión")
    if not re.search(r'<p>\s*<strong>En resumen:</strong>|class="respuesta-rapida"', body):
        warnings.append("no empieza con una respuesta corta («<p><strong>En resumen:</strong> …», sale en el recuadro «Respuesta rápida»)")
    if re.search(r"\b(TL;DR)\b", body) and "Qué mirar:</strong> si la herramienta" in body:
        errors.append("bloque TL;DR genérico de plantilla")
    return errors, warnings


def audit_images(slug: str, text: str, body: str, errors: list[str], warnings: list[str]) -> None:
    """Portada propia (docs/portadas.md) e imágenes dentro del texto."""
    portadas = json.loads(PORTADAS.read_text(encoding="utf-8")) if PORTADAS.exists() else {}
    og = re.search(r'ogImage="([^"]*)"', text)
    if not og or og.group(1) != f"/og/blog/{slug}.jpg":
        errors.append(f'sin portada propia: ogImage debe ser "/og/blog/{slug}.jpg" (docs/portadas.md)')
    if slug not in portadas:
        errors.append("falta la entrada del artículo en src/data/portadas.json")
    else:
        faltan = [v for v in VARIANTES if not (ROOT / "public" / "og" / "blog" / f"{slug}{v}").exists()]
        if faltan:
            errors.append(f"faltan archivos de portada ({', '.join(faltan)}): python3 scripts/imagenes/portada.py {slug}")
        if f'<Articulo slug="{slug}"' not in body and f'<PortadaArticulo slug="{slug}"' not in body:
            warnings.append("sin portada en la cabecera (la pone <Articulo slug=…>)")
    for tag in re.findall(r"<img\b[^>]*>", body, flags=re.S):
        src = re.search(r'src="([^"]+)"', tag)
        if not re.search(r'\balt="[^"]{10,}"', tag) and "alt={" not in tag:
            errors.append(f"imagen sin texto alternativo útil: {src.group(1) if src else tag[:60]}")
        if "width=" not in tag or "height=" not in tag:
            warnings.append(f"imagen sin width/height (la página salta al cargar): {src.group(1) if src else ''}")
        if 'loading="lazy"' not in tag:
            warnings.append(f"imagen sin loading=\"lazy\": {src.group(1) if src else ''}")
    figuras = re.findall(r"<FiguraArticulo\b(.*?)/>", body, flags=re.S)
    for f in figuras:
        src = re.search(r'src="([^"]+)"', f)
        alt = re.search(r'alt="([^"]*)"', f)
        if not src or not (ROOT / "public" / src.group(1).lstrip("/")).exists():
            errors.append(f"FiguraArticulo con imagen que no existe: {src.group(1) if src else '?'}")
            continue
        if not alt or len(alt.group(1)) < 30:
            errors.append(f"FiguraArticulo sin alt descriptivo (30+ caracteres): {src.group(1)}")
        kb = (ROOT / "public" / src.group(1).lstrip("/")).stat().st_size // 1024
        if kb > MAX_KB_FIGURA:
            warnings.append(f"imagen de {kb} KB (máximo {MAX_KB_FIGURA}): {src.group(1)}")
    total = len(figuras) + len(re.findall(r"<img\b", body))
    if total < MIN_FIGURAS:
        warnings.append(f"{total} imágenes dentro del texto (lo normal son 2-3: capturas o esquemas, docs/portadas.md)")


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
