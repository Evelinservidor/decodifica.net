"""Piezas comunes de las herramientas de imágenes de Decodifica.

Colores de la web (tailwind.config.mjs), fuentes libres guardadas en el
repositorio (Inter, licencia OFL) y utilidades para abrir Chromium sin
pantalla y guardar imágenes ligeras. Funciona en Linux, macOS y Windows.
"""
from __future__ import annotations

import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

RAIZ = Path(__file__).resolve().parents[2]
FUENTES = Path(__file__).resolve().parent / "fuentes"
LOGOS = Path(__file__).resolve().parent / "logos"

# Colores de la web (tailwind.config.mjs)
COLORES = {
    "fondo": (11, 13, 23),
    "fondo2": (22, 25, 45),
    "texto": (255, 255, 255),
    "suave": (199, 210, 254),  # brand-200
    "brand": (99, 102, 241),  # brand-500
    "brand_oscuro": (49, 46, 129),  # brand-900
    "brand_claro": (165, 180, 252),  # brand-300
    "naranja": (255, 149, 0),  # accent-orange
    "cta": (255, 107, 0),  # cta-500
    "verde": (0, 255, 136),  # accent-green
    "rosa": (236, 72, 153),  # accent-pink
    "gris": (148, 163, 184),
    "linea": (51, 58, 92),
}

# Fondos de portada: (color de arriba a la izquierda, color de abajo a la derecha)
FONDOS = {
    "indigo": ((30, 27, 75), (79, 70, 229)),
    "noche": ((8, 10, 20), (49, 46, 129)),
    "naranja": ((124, 45, 18), (234, 88, 12)),
    "verde": ((2, 44, 34), (5, 150, 105)),
    "rosa": ((80, 7, 36), (219, 39, 119)),
    "azul": ((8, 47, 73), (2, 132, 199)),
}


def fuente(peso: str, tam: int) -> ImageFont.FreeTypeFont:
    archivos = {
        "black": "InterDisplay-Black.otf",
        "extrabold": "InterDisplay-ExtraBold.otf",
        "bold": "InterDisplay-Bold.otf",
        "semibold": "Inter-SemiBold.otf",
        "medium": "Inter-Medium.otf",
    }
    return ImageFont.truetype(str(FUENTES / archivos[peso]), tam)


def degradado(w: int, h: int, c1, c2) -> Image.Image:
    """Degradado diagonal de c1 (arriba izquierda) a c2 (abajo derecha)."""
    from PIL import ImageChops

    base = Image.new("RGB", (w, h), c1)
    horiz = Image.linear_gradient("L").rotate(90).resize((w, h))
    vert = Image.linear_gradient("L").resize((w, h))
    mascara = ImageChops.add(ImageChops.invert(horiz), vert, scale=2)
    return Image.composite(Image.new("RGB", (w, h), c2), base, mascara)


def sombra(img: Image.Image, radio: int = 28, opacidad: int = 150, desplaz: int = 14):
    """Devuelve (capa_sombra, margen) para pegar debajo de una tarjeta."""
    from PIL import ImageFilter

    m = radio * 2
    capa = Image.new("RGBA", (img.width + m * 2, img.height + m * 2), (0, 0, 0, 0))
    forma = Image.new("L", img.size, 0)
    ImageDraw.Draw(forma).rounded_rectangle((0, 0, img.width - 1, img.height - 1), 24, fill=opacidad)
    capa.paste((0, 0, 0, 255), (m, m + desplaz), forma)
    return capa.filter(ImageFilter.GaussianBlur(radio)), m


def redondear(img: Image.Image, r: int) -> Image.Image:
    img = img.convert("RGBA")
    mascara = Image.new("L", img.size, 0)
    ImageDraw.Draw(mascara).rounded_rectangle((0, 0, img.width - 1, img.height - 1), r, fill=255)
    img.putalpha(Image.composite(img.getchannel("A"), mascara, mascara))
    return img


def guardar(img: Image.Image, destino: Path, calidad: int = 80) -> int:
    """Guarda en WebP, PNG (paleta optimizada) o JPEG según la extensión. Devuelve bytes."""
    destino.parent.mkdir(parents=True, exist_ok=True)
    ext = destino.suffix.lower()
    img = img.convert("RGB")
    if ext == ".webp":
        img.save(destino, "WEBP", quality=calidad, method=6)
    elif ext == ".png":
        img.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.FLOYDSTEINBERG).save(
            destino, "PNG", optimize=True
        )
    elif ext in (".jpg", ".jpeg"):
        img.save(destino, "JPEG", quality=calidad, optimize=True, progressive=True)
    else:
        raise ValueError(f"Formato no soportado: {ext}")
    return destino.stat().st_size


def abrir_navegador(p):
    """Lanza Chromium sin pantalla. Usa el navegador de Playwright o el de la nube."""
    ruta = os.environ.get("CHROMIUM_PATH")
    candidatos = [ruta] if ruta else []
    candidatos += [None, "/opt/pw-browsers/chromium"]
    ultimo = None
    for c in candidatos:
        try:
            if c is None:
                return p.chromium.launch()
            if Path(c).exists():
                return p.chromium.launch(executable_path=c)
        except Exception as e:  # noqa: BLE001
            ultimo = e
    raise RuntimeError(f"No se pudo abrir Chromium: {ultimo}")


AGENTE = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/140.0.0.0 Safari/537.36"
)
