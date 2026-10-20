#!/usr/bin/env python3
"""
Vuelve a enviar el sitemap de decodifica.net a Search Console.

Lo ejecuta deploy.yml después de cada publicación, para que Google sepa que hay
páginas nuevas o cambiadas sin que Jordi tenga que entrar en Search Console.
No es lo mismo que «Solicitar indexación» (ese botón no tiene API): Google decide
cuándo lee cada página, pero se entera antes de que el sitemap ha cambiado.

Necesita que el robot tenga permiso «Acceso total» en Search Console (con
«Restringido» Google no deja enviar sitemaps) y el permiso de escritura
`webmasters` (no `webmasters.readonly`). Usa la misma autenticación que
scripts/weekly_gsc_report.py.
Variables opcionales:
  GSC_SITE     - propiedad de Search Console (por defecto sc-domain:decodifica.net)
  SITEMAP_URL  - por defecto https://decodifica.net/sitemap-index.xml
"""
from __future__ import annotations

import os
import sys
from pathlib import Path
from urllib.parse import quote

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
from weekly_gsc_report import get_access_token  # noqa: E402

SCOPE_ESCRITURA = "https://www.googleapis.com/auth/webmasters"


def main() -> int:
    site = os.environ.get("GSC_SITE", "sc-domain:decodifica.net")
    sitemap = os.environ.get("SITEMAP_URL", "https://decodifica.net/sitemap-index.xml")
    token = get_access_token(SCOPE_ESCRITURA)
    base = f"https://www.googleapis.com/webmasters/v3/sites/{quote(site, safe='')}/sitemaps"

    r = requests.put(f"{base}/{quote(sitemap, safe='')}",
                     headers={"Authorization": f"Bearer {token}"}, timeout=30)
    if r.status_code not in (200, 204):
        print(f"✗ Google no aceptó el sitemap: HTTP {r.status_code}: {r.text[:300]}", file=sys.stderr)
        if r.status_code == 403:
            print("  ¿Tiene el robot «Acceso total» en Search Console?", file=sys.stderr)
        return 1

    r = requests.get(f"{base}/{quote(sitemap, safe='')}",
                     headers={"Authorization": f"Bearer {token}"}, timeout=30)
    info = r.json() if r.ok else {}
    print(f"✓ Sitemap enviado: {sitemap} (enviado {info.get('lastSubmitted', '?')}, "
          f"leído por Google {info.get('lastDownloaded', '?')})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
