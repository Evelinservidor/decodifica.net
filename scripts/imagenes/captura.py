"""Captura de pantalla de la web oficial de una herramienta, lista para un artículo.

Abre la página con Chromium sin pantalla, quita avisos de cookies y barras
fijas, recorta lo importante (un elemento, una zona o la primera pantalla) y la
guarda en WebP ligero dentro de un marco de navegador con el dominio visible
(para que se vea de dónde sale).

Uso:
  # Primera pantalla de la web
  python3 scripts/imagenes/captura.py https://n8n.io public/img/blog/n8n-que-es-gratis/web-n8n.webp

  # Solo un elemento (planes de precios, botón de descarga...)
  python3 scripts/imagenes/captura.py https://n8n.io/pricing/ public/img/blog/n8n/precios.webp \\
      --selector "section:has(h2)" --desplazar "text=Starter"

  # Una zona concreta de la página (x,y,ancho,alto en píxeles CSS)
  python3 scripts/imagenes/captura.py https://lmstudio.ai salida.webp --zona 0,0,1280,720

Opciones útiles: --ancho/--alto (ventana, por defecto 1280x800), --movil,
--esperar (ms), --sin-marco, --clic "texto o selector" (p. ej. aceptar algo).
Imprime ancho, alto y peso: copia ancho y alto en el <img>.
"""
from __future__ import annotations

import argparse
import io
import sys
from pathlib import Path
from urllib.parse import urlparse

from PIL import Image, ImageDraw
from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import AGENTE, COLORES, abrir_navegador, fuente, guardar  # noqa: E402

# Botones habituales de los avisos de cookies (se pulsan si aparecen)
COOKIES = [
    "#onetrust-accept-btn-handler", "#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll",
    "button:has-text('Aceptar todo')", "button:has-text('Aceptar todas')", "button:has-text('Aceptar')",
    "button:has-text('Accept all')", "button:has-text('Accept All')", "button:has-text('Accept')",
    "button:has-text('Rechazar todo')", "button:has-text('Reject all')", "button:has-text('Got it')",
    "button:has-text('Entendido')", "button:has-text('I agree')", "button:has-text('Allow all')",
]

# Quita lo que tapa la página: banners de cookies, chats flotantes y cabeceras fijas
JS_LIMPIAR = """
(quitarFijos) => {
  const patron = /(cookie|consent|gdpr|onetrust|cookiebot|intercom|drift|crisp|hubspot-messages|chat-widget|banner-promo)/i;
  for (const el of document.querySelectorAll('body *')) {
    const id = (el.id || '') + ' ' + (typeof el.className === 'string' ? el.className : '');
    const cs = getComputedStyle(el);
    if (patron.test(id) && (cs.position === 'fixed' || cs.position === 'sticky')) { el.remove(); continue; }
    if (quitarFijos && cs.position === 'fixed' && el.getBoundingClientRect().top > 40) el.remove();
  }
  document.documentElement.style.scrollBehavior = 'auto';
}
"""


def marco(img: Image.Image, dominio: str) -> Image.Image:
    """Marco de navegador sencillo con la dirección de la web."""
    barra = 44
    ancho = img.width
    lienzo = Image.new("RGB", (ancho, img.height + barra), (30, 33, 52))
    d = ImageDraw.Draw(lienzo)
    for i, c in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]):
        d.ellipse((16 + i * 22, 15, 30 + i * 22, 29), fill=c)
    x0 = 96
    d.rounded_rectangle((x0, 8, min(ancho - 16, x0 + 520), barra - 8), 8, fill=(15, 17, 30))
    d.text((x0 + 14, barra // 2), dominio, font=fuente("medium", 17), fill=COLORES["suave"], anchor="lm")
    lienzo.paste(img.convert("RGB"), (0, barra))
    return lienzo


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("url")
    ap.add_argument("salida", help="ruta .webp (o .png) de destino, p. ej. public/img/blog/<slug>/<nombre>.webp")
    ap.add_argument("--selector", help="captura solo este elemento (selector CSS o de Playwright)")
    ap.add_argument("--zona", help="x,y,ancho,alto en píxeles CSS")
    ap.add_argument("--desplazar", help="hace scroll hasta este selector antes de capturar la primera pantalla")
    ap.add_argument("--clic", action="append", default=[], help="pulsa este selector antes de capturar (se puede repetir)")
    ap.add_argument("--ancho", type=int, default=1280)
    ap.add_argument("--alto", type=int, default=800)
    ap.add_argument("--movil", action="store_true", help="ventana de móvil (390x844)")
    ap.add_argument("--esperar", type=int, default=2500, help="ms de espera tras cargar")
    ap.add_argument("--max-ancho", type=int, default=1200, help="ancho máximo del archivo final")
    ap.add_argument("--sin-marco", action="store_true")
    ap.add_argument("--dejar-fijos", action="store_true", help="no quitar elementos fijos (menús flotantes)")
    ap.add_argument("--calidad", type=int, default=78)
    a = ap.parse_args()

    vp = {"width": 390, "height": 844} if a.movil else {"width": a.ancho, "height": a.alto}
    with sync_playwright() as p:
        nav = abrir_navegador(p)
        ctx = nav.new_context(viewport=vp, user_agent=AGENTE, locale="es-ES", device_scale_factor=1 if not a.movil else 2)
        pg = ctx.new_page()
        pg.goto(a.url, timeout=60000, wait_until="domcontentloaded")
        try:
            pg.wait_for_load_state("networkidle", timeout=15000)
        except Exception:  # noqa: BLE001
            pass
        pg.wait_for_timeout(a.esperar)
        if "just a moment" in pg.title().lower():
            print("✗ La web muestra una protección antirobots; prueba otra URL oficial (docs, blog, GitHub).")
            nav.close()
            return 1
        for sel in COOKIES:
            try:
                b = pg.locator(sel).first
                if b.is_visible(timeout=300):
                    b.click(timeout=1500)
                    pg.wait_for_timeout(500)
                    break
            except Exception:  # noqa: BLE001
                continue
        for sel in a.clic:
            pg.locator(sel).first.click(timeout=5000)
            pg.wait_for_timeout(1200)
        pg.evaluate(JS_LIMPIAR, not a.dejar_fijos)
        if a.desplazar:
            pg.locator(a.desplazar).first.scroll_into_view_if_needed(timeout=8000)
            pg.wait_for_timeout(800)
        if a.selector:
            png = pg.locator(a.selector).first.screenshot(timeout=15000)
        elif a.zona:
            x, y, w, h = (int(v) for v in a.zona.split(","))
            png = pg.screenshot(clip={"x": x, "y": y, "width": w, "height": h}, full_page=True)
        else:
            png = pg.screenshot()
        nav.close()

    img = Image.open(io.BytesIO(png))
    if not a.sin_marco:
        img = marco(img, urlparse(a.url).netloc.removeprefix("www."))
    if img.width > a.max_ancho:
        img = img.resize((a.max_ancho, round(img.height * a.max_ancho / img.width)), Image.Resampling.LANCZOS)
    destino = Path(a.salida)
    peso = guardar(img, destino, a.calidad)
    print(f"✓ {destino} · {img.width}x{img.height} · {peso // 1024} KB")
    if peso > 150 * 1024:
        print("  · Pesa más de 150 KB: recorta con --selector/--zona o baja --calidad.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
