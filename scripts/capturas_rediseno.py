"""Capturas de páginas a 390 px (móvil) y 1280 px (ordenador).

Uso: python3 scripts/capturas_rediseno.py <url_base> <carpeta_salida> nombre=/ruta/ [nombre=/ruta/ ...]
Guarda <nombre>-<tamaño>-pantalla.webp (lo que se ve al entrar) y <nombre>-<tamaño>.jpg (página entera).
     [--oscuro]    fuerza prefers-color-scheme: dark
"""
import io
import sys
from pathlib import Path
from PIL import Image
from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).parent / "imagenes"))
from comun import abrir_navegador  # noqa: E402

args = [a for a in sys.argv[1:] if not a.startswith("--")]
opts = {a for a in sys.argv[1:] if a.startswith("--")}
base, salida, paginas = args[0].rstrip("/"), Path(args[1]), args[2:]
salida.mkdir(parents=True, exist_ok=True)
TAMANOS = {"movil": (390, 844), "ordenador": (1280, 800)}

with sync_playwright() as p:
    nav = abrir_navegador(p)
    for nombre_tam, (ancho, alto) in TAMANOS.items():
        ctx = nav.new_context(viewport={"width": ancho, "height": alto}, device_scale_factor=1,
                              color_scheme="dark" if "--oscuro" in opts else "light",
                              is_mobile=nombre_tam == "movil", has_touch=nombre_tam == "movil")
        for item in paginas:
            nombre, ruta = item.split("=", 1)
            pag = ctx.new_page()
            pag.goto(base + ruta, wait_until="networkidle")
            pag.wait_for_timeout(400)
            # Primera pantalla (lo que se ve al entrar) y página completa.
            Image.open(io.BytesIO(pag.screenshot())).convert("RGB").save(
                salida / f"{nombre}-{nombre_tam}-pantalla.webp", quality=85, method=6)
            # JPEG para la completa: WebP no admite más de 16.383 px de alto.
            Image.open(io.BytesIO(pag.screenshot(full_page=True))).convert("RGB").save(
                salida / f"{nombre}-{nombre_tam}.jpg", quality=78, optimize=True, progressive=True)
            pag.close()
        ctx.close()
    nav.close()
