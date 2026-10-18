#!/usr/bin/env python3
"""
Qué páginas de decodifica.net tiene Google (inspección de URLs de Search Console).

Lee todas las direcciones del sitemap publicado y pregunta a Search Console por
cada una (API «URL Inspection», solo lectura). Guarda:
  data/gsc_weekly/latest_indexacion.json  (una entrada por página)
  data/gsc_weekly/latest_indexacion.md    (resumen: cuántas en Google y cuáles no)

Sirve para medir el plan de docs/plan-seo.md («cuántas páginas de cada grupo
están en Google») y para ver si un artículo nuevo ha entrado ya.

Usa la misma autenticación que scripts/weekly_gsc_report.py.
Variables opcionales:
  GSC_SITE        - propiedad de Search Console (por defecto sc-domain:decodifica.net)
  SITEMAP_URL     - por defecto https://decodifica.net/sitemap-0.xml
  OUTPUT_DIR      - por defecto ./data/gsc_weekly
Límite de Google: 2.000 inspecciones al día por propiedad (la web tiene ~110 páginas).
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
from collections import Counter
from datetime import date
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
from weekly_gsc_report import get_access_token  # noqa: E402

INSPECT_URL = "https://searchconsole.googleapis.com/v1/urlInspection/index:inspect"


def leer_sitemap(url: str) -> list[str]:
    r = requests.get(url, timeout=30, headers={"User-Agent": "decodifica-informe/1.0"})
    r.raise_for_status()
    return re.findall(r"<loc>([^<]+)</loc>", r.text)


def inspeccionar(token: str, site: str, page: str) -> dict:
    r = requests.post(
        INSPECT_URL,
        headers={"Authorization": f"Bearer {token}"},
        json={"inspectionUrl": page, "siteUrl": site, "languageCode": "es"},
        timeout=60,
    )
    if r.status_code != 200:
        return {"page": page, "error": f"HTTP {r.status_code}: {r.text[:200]}"}
    res = r.json().get("inspectionResult", {}).get("indexStatusResult", {})
    return {
        "page": page,
        "verdict": res.get("verdict"),
        "coverageState": res.get("coverageState"),
        "indexingState": res.get("indexingState"),
        "robotsTxtState": res.get("robotsTxtState"),
        "pageFetchState": res.get("pageFetchState"),
        "lastCrawlTime": res.get("lastCrawlTime"),
        "googleCanonical": res.get("googleCanonical"),
        "userCanonical": res.get("userCanonical"),
    }


def sitemaps_enviados(token: str, site: str) -> list[dict]:
    """Los sitemaps que tiene Search Console y cuándo los leyó Google por última vez."""
    from urllib.parse import quote

    r = requests.get(
        f"https://www.googleapis.com/webmasters/v3/sites/{quote(site, safe='')}/sitemaps",
        headers={"Authorization": f"Bearer {token}"},
        timeout=30,
    )
    if r.status_code != 200:
        return [{"error": f"HTTP {r.status_code}: {r.text[:200]}"}]
    return [
        {
            "path": m.get("path"),
            "lastSubmitted": m.get("lastSubmitted"),
            "lastDownloaded": m.get("lastDownloaded"),
            "isPending": m.get("isPending"),
            "errors": m.get("errors"),
            "warnings": m.get("warnings"),
            "contents": m.get("contents"),
        }
        for m in r.json().get("sitemap", [])
    ]


def main() -> int:
    site = os.environ.get("GSC_SITE", "sc-domain:decodifica.net")
    sitemap = os.environ.get("SITEMAP_URL", "https://decodifica.net/sitemap-0.xml")
    out = Path(os.environ.get("OUTPUT_DIR", "./data/gsc_weekly"))
    out.mkdir(parents=True, exist_ok=True)

    pages = leer_sitemap(sitemap)
    print(f"{len(pages)} páginas en el sitemap", file=sys.stderr)
    token = get_access_token()

    mapas = sitemaps_enviados(token, site)
    filas = []
    for i, page in enumerate(pages, 1):
        filas.append(inspeccionar(token, site, page))
        if i % 50 == 0:
            print(f"  {i}/{len(pages)}", file=sys.stderr)
        time.sleep(0.2)  # muy por debajo del límite de 600 por minuto

    hoy = date.today().isoformat()
    (out / "latest_indexacion.json").write_text(
        json.dumps({"fetched_at": hoy, "site": site, "sitemap": sitemap,
                    "sitemaps_en_search_console": mapas, "pages": filas},
                   indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    estados = Counter(f.get("coverageState") or f.get("error", "?")[:40] for f in filas)
    en_google = sum(1 for f in filas if f.get("verdict") == "PASS")
    md = [
        f"# Páginas en Google — {hoy}",
        "",
        f"Del sitemap: {len(filas)} páginas. En Google (verdict PASS): {en_google}.",
        "",
        "| Estado en Search Console | Páginas |",
        "|---|---|",
    ]
    md += [f"| {k} | {v} |" for k, v in estados.most_common()]
    md += ["", "## Sitemaps enviados a Search Console", ""]
    if mapas:
        md += [
            f"- {m.get('path') or m.get('error')}: enviado {m.get('lastSubmitted') or '—'}, "
            f"leído por Google {m.get('lastDownloaded') or '—'}, errores {m.get('errors', '—')}"
            for m in mapas
        ]
    else:
        md += ["- Ninguno: hay que enviar https://decodifica.net/sitemap-index.xml en Search Console."]
    fuera = [f for f in filas if f.get("verdict") != "PASS"]
    if fuera:
        md += ["", "## Las que no están en Google", "", "| Página | Estado | Último rastreo |", "|---|---|---|"]
        md += [
            f"| {f['page']} | {f.get('coverageState') or f.get('error', '?')} | {f.get('lastCrawlTime') or '—'} |"
            for f in fuera
        ]
    (out / "latest_indexacion.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"En Google: {en_google} de {len(filas)}", file=sys.stderr)
    errores = sum(1 for f in filas if "error" in f)
    # Si TODAS fallan (p. ej. sin permiso), que se vea en GitHub como fallo.
    return 1 if filas and errores == len(filas) else 0


if __name__ == "__main__":
    sys.exit(main())
