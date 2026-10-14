"""Genera las portadas de los artículos de Decodifica.

Lee src/data/portadas.json (una entrada por artículo) y crea en public/og/blog/:

  <slug>.jpg             1200x630  con gancho  -> og:image (redes al compartir)
  <slug>-tarjeta.webp     640x360  con gancho  -> portada del blog (lista de artículos)
  <slug>-tarjeta-960.webp 960x540  con gancho  -> la misma para pantallas grandes
  <slug>-16x9.webp       1600x900  limpia      -> datos estructurados (Google, Discover) y cabecera del artículo
  <slug>-16x9-800.webp    800x450  limpia      -> cabecera del artículo en móvil
  <slug>-4x3.webp        1200x900  limpia      -> datos estructurados
  <slug>-1x1.webp       1200x1200  limpia      -> datos estructurados

«Con gancho» lleva el texto corto (3-6 palabras); «limpia» solo la imagen y,
como mucho, una etiqueta corta (el número o NUEVO), porque Google pide evitar
imágenes con mucho texto en Discover y en Imágenes (ver docs/portadas.md).

Plantillas:
  herramienta  logo(s) o captura de la web oficial de la herramienta
  lista        número grande (comparativas, «5 IAs para…», «7 alternativas…»)
  novedad      etiqueta NUEVO; solo si la función salió hace menos de 30 días

Uso:
  python3 scripts/imagenes/portada.py                 # todas
  python3 scripts/imagenes/portada.py n8n-que-es-gratis ollama-que-es-como-usar
  python3 scripts/imagenes/portada.py --muestra salida.png slug1 slug2   # hoja de comprobación
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import COLORES, FONDOS, LOGOS, RAIZ, degradado, fuente, guardar, redondear  # noqa: E402

DATOS = RAIZ / "src" / "data" / "portadas.json"
SALIDA = RAIZ / "public" / "og" / "blog"
CAPTURAS = Path(__file__).resolve().parent / "capturas"

AMARILLO = (255, 214, 10)
PLANTILLAS = ("herramienta", "lista", "novedad")


# ---------- utilidades de dibujo ----------

def resaltado(fondo: str):
    return AMARILLO if fondo in ("naranja", "rosa") else COLORES["naranja"]


def fondo_base(w: int, h: int, nombre: str) -> Image.Image:
    c1, c2 = FONDOS[nombre]
    img = degradado(w, h, c1, c2).convert("RGBA")
    # brillo suave detrás de la imagen principal
    brillo = Image.new("L", (w, h), 0)
    r = int(min(w, h) * 0.55)
    cx, cy = int(w * 0.72), int(h * 0.5)
    ImageDraw.Draw(brillo).ellipse((cx - r, cy - r, cx + r, cy + r), fill=90)
    brillo = brillo.filter(ImageFilter.GaussianBlur(r // 2))
    img.paste((255, 255, 255, 255), (0, 0), brillo.point(lambda v: v // 3))
    # retícula de puntos discreta
    d = ImageDraw.Draw(img)
    paso = max(24, int(min(w, h) * 0.045))
    for y in range(paso // 2, h, paso):
        for x in range(paso // 2, w, paso):
            d.ellipse((x - 1, y - 1, x + 1, y + 1), fill=(255, 255, 255, 28))
    return img


def con_sombra(lienzo: Image.Image, capa: Image.Image, pos, radio=None, opacidad=0.45):
    """Pega `capa` (RGBA) con una sombra suave sacada de su propia forma."""
    radio = radio or max(8, int(min(capa.size) * 0.06))
    alfa = capa.getchannel("A").point(lambda v: int(v * opacidad))
    marco = radio * 3
    sombra = Image.new("L", (capa.width + 2 * marco, capa.height + 2 * marco), 0)
    sombra.paste(alfa, (marco, marco))
    sombra = sombra.filter(ImageFilter.GaussianBlur(radio))
    x, y = pos
    lienzo.paste((0, 0, 0, 255), (x - marco, y - marco + radio // 2), sombra)
    lienzo.alpha_composite(capa, (x, y))


def cargar_logo(nombre: str) -> Image.Image:
    ruta = LOGOS / f"{nombre}.png"
    if not ruta.exists():
        raise SystemExit(f"✗ Falta el logo {ruta}. Descárgalo con scripts/imagenes/logo.py {nombre} <web oficial>")
    return Image.open(ruta).convert("RGBA")


def opaco_en_esquinas(img: Image.Image) -> bool:
    a = img.getchannel("A")
    w, h = img.size
    pts = [(2, 2), (w - 3, 2), (2, h - 3), (w - 3, h - 3)]
    return all(a.getpixel(p) > 200 for p in pts)


def ficha_logo(nombre: str, lado: int) -> Image.Image:
    """Logo dentro de una ficha redondeada (blanca si el logo es transparente)."""
    logo = cargar_logo(nombre)
    r = int(lado * 0.22)
    if opaco_en_esquinas(logo) and abs(logo.width - logo.height) < 4:
        return redondear(logo.resize((lado, lado), Image.Resampling.LANCZOS), r)
    ficha = Image.new("RGBA", (lado, lado), (0, 0, 0, 0))
    ImageDraw.Draw(ficha).rounded_rectangle((0, 0, lado - 1, lado - 1), r, fill=(255, 255, 255, 255))
    interior = int(lado * 0.68)
    logo.thumbnail((interior, interior), Image.Resampling.LANCZOS)
    if logo.width < interior and logo.height < interior:
        f = interior / max(logo.size)
        logo = logo.resize((round(logo.width * f), round(logo.height * f)), Image.Resampling.LANCZOS)
    ficha.alpha_composite(logo, ((lado - logo.width) // 2, (lado - logo.height) // 2))
    return ficha


# ---------- piezas visuales (devuelven una capa RGBA del tamaño de la caja) ----------

def visual_logos(logos: list[str], bw: int, bh: int) -> Image.Image:
    capa = Image.new("RGBA", (bw, bh), (0, 0, 0, 0))
    n = len(logos)
    if n == 1:
        lado = int(min(bw, bh) * 0.78)
        con_sombra(capa, ficha_logo(logos[0], lado), ((bw - lado) // 2, (bh - lado) // 2))
        return capa
    if n == 2:
        lado = int(min(bw * 0.58, bh * 0.66))
        con_sombra(capa, ficha_logo(logos[0], lado), (int(bw * 0.04), int(bh * 0.06)))
        con_sombra(capa, ficha_logo(logos[1], lado), (bw - lado - int(bw * 0.04), bh - lado - int(bh * 0.06)))
        return capa
    if n == 3:
        lado = int(min(bw * 0.46, bh * 0.5))
        pos = [((bw - lado) // 2, int(bh * 0.04)), (int(bw * 0.04), bh - lado - int(bh * 0.06)),
               (bw - lado - int(bw * 0.04), bh - lado - int(bh * 0.06))]
        for nombre, p in zip(logos, pos):
            con_sombra(capa, ficha_logo(nombre, lado), p)
        return capa
    filas = [logos[: (n + 1) // 2], logos[(n + 1) // 2:]]
    hueco = int(min(bw, bh) * 0.05)
    por_fila = max(len(f) for f in filas)
    lado = int(min((bw - hueco * (por_fila - 1)) / por_fila, (bh - hueco) / 2))
    y = (bh - (2 * lado + hueco)) // 2
    for fila in filas:
        x = (bw - (len(fila) * lado + (len(fila) - 1) * hueco)) // 2
        for nombre in fila:
            con_sombra(capa, ficha_logo(nombre, lado), (x, y))
            x += lado + hueco
        y += lado + hueco
    return capa


def visual_captura(captura: str, logos: list[str], bw: int, bh: int, sangrar: bool) -> Image.Image:
    capa = Image.new("RGBA", (bw, bh), (0, 0, 0, 0))
    img = Image.open(CAPTURAS / captura).convert("RGB")
    # nos quedamos con la parte de arriba (lo que se ve al entrar en la web)
    img = img.crop((0, 0, img.width, min(img.height, int(img.width * 0.66))))
    ancho = int(bw * (1.12 if sangrar else 0.92))
    alto = round(img.height * ancho / img.width)
    if alto > bh * 0.86:
        alto = int(bh * 0.86)
        ancho = round(img.width * alto / img.height)
    img = redondear(img.resize((ancho, alto), Image.Resampling.LANCZOS), max(10, ancho // 60))
    x = int(bw * 0.1) if sangrar else (bw - ancho) // 2
    y = (bh - alto) // 2 - (int(bh * 0.04) if logos else 0)
    con_sombra(capa, img, (x, y))
    if logos:
        lado = int(min(bw, bh) * 0.32)
        con_sombra(capa, ficha_logo(logos[0], lado), (max(0, x - lado // 4), min(bh - lado, y + alto - lado * 2 // 3)))
    return capa


def visual_numero(numero: str, rotulo: str | None, logos: list[str], bw: int, bh: int, color) -> Image.Image:
    capa = Image.new("RGBA", (bw, bh), (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    alto_logos = int(bh * 0.24) if logos else 0
    zona = bh - alto_logos - (int(bh * 0.05) if logos else 0)
    tam = int(zona * (0.95 if not rotulo else 0.8))
    f = fuente("black", tam)
    caja = d.textbbox((0, 0), numero, font=f, anchor="ls")
    an_num = caja[2] - caja[0]
    alto_num = -caja[1]
    f_rot = fuente("black", max(20, int(tam * 0.2))) if rotulo else None
    alto_rot = int(f_rot.size * 1.05) if rotulo else 0
    total = alto_num + alto_rot
    y_base = (zona - total) // 2 + alto_num
    sombra = Image.new("RGBA", capa.size, (0, 0, 0, 0))
    ImageDraw.Draw(sombra).text(((bw - an_num) // 2, y_base + tam // 40), numero, font=f, fill=(0, 0, 0, 120), anchor="ls")
    capa.alpha_composite(sombra.filter(ImageFilter.GaussianBlur(tam // 30)))
    d.text(((bw - an_num) // 2, y_base), numero, font=f, fill=color, anchor="ls")
    if rotulo:
        d.text((bw // 2, y_base + int(f_rot.size * 0.25)), rotulo, font=f_rot, fill=(255, 255, 255), anchor="mt")
    if logos:
        hueco = int(alto_logos * 0.18)
        lado = min(alto_logos, int((bw - hueco * (len(logos) - 1)) / len(logos)))
        x = (bw - (len(logos) * lado + (len(logos) - 1) * hueco)) // 2
        for nombre in logos:
            con_sombra(capa, ficha_logo(nombre, lado), (x, bh - lado))
            x += lado + hueco
    return capa


def visual_lista_control(puntos: list[str], bw: int, bh: int) -> Image.Image:
    """Tarjeta con casillas marcadas (para guías de método, sin herramienta concreta)."""
    capa = Image.new("RGBA", (bw, bh), (0, 0, 0, 0))
    ancho, alto = int(bw * 0.94), int(bh * 0.86)
    tarjeta = Image.new("RGBA", (ancho, alto), (0, 0, 0, 0))
    d = ImageDraw.Draw(tarjeta)
    d.rounded_rectangle((0, 0, ancho - 1, alto - 1), int(alto * 0.07), fill=(255, 255, 255, 255))
    fila = alto / (len(puntos) + 0.6)
    tam = int(fila * 0.34)
    disponible = ancho * 0.93 - int(fila * 0.48) - int(ancho * 0.11)
    while tam > 12 and max(fuente("bold", tam).getlength(p) for p in puntos) > disponible:
        tam -= 1
    f = fuente("bold", tam)
    for i, p in enumerate(puntos):
        cy = int(fila * (i + 0.8))
        c = int(fila * 0.24)
        x0 = int(ancho * 0.07)
        d.rounded_rectangle((x0, cy - c, x0 + 2 * c, cy + c), c // 3, fill=COLORES["brand"])
        d.line((x0 + c * 0.45, cy, x0 + c * 0.9, cy + c * 0.5, x0 + c * 1.6, cy - c * 0.5), fill="white", width=max(3, c // 4), joint="curve")
        d.text((x0 + 2 * c + int(ancho * 0.04), cy), p, font=f, fill=(17, 24, 39), anchor="lm")
    con_sombra(capa, tarjeta, ((bw - ancho) // 2, (bh - alto) // 2))
    return capa


def visual(spec: dict, bw: int, bh: int, sangrar: bool) -> Image.Image:
    logos = spec.get("logos", [])
    if spec["plantilla"] == "lista" and spec.get("numero"):
        return visual_numero(spec["numero"], spec.get("rotulo"), logos, bw, bh, resaltado(spec.get("fondo", "indigo")))
    if spec.get("captura"):
        return visual_captura(spec["captura"], logos, bw, bh, sangrar)
    if spec.get("casillas"):
        return visual_lista_control(spec["casillas"], bw, bh)
    if logos:
        return visual_logos(logos, bw, bh)
    raise SystemExit(f"✗ {spec['slug']}: la portada necesita logos, captura, número o casillas")


# ---------- textos ----------

def trozos(gancho: str):
    """'¿Claude es *gratis*?' -> [[('¿Claude', False)], [('es', False)], [('gratis', True), ('?', False)]]

    Cada palabra es una lista de tramos (texto, resaltado) para que la
    puntuación pegada a una palabra resaltada no se separe.
    """
    palabras, marcado = [], False
    for token in gancho.split():
        tramos = []
        for i, parte in enumerate(token.split("*")):
            if i > 0:
                marcado = not marcado
            if parte:
                tramos.append((parte, marcado))
        if tramos:
            palabras.append(tramos)
    return palabras


def colocar_gancho(d: ImageDraw.ImageDraw, gancho: str, x: int, y: int, ancho: int, alto: int, color_hl, s: float):
    palabras = trozos(gancho)
    for tam in range(int(118 * s), int(50 * s), -2):
        f = fuente("black", tam)
        esp = f.getlength(" ")
        lineas, actual, an = [], [], 0.0
        for tramos in palabras:
            w = sum(f.getlength(t) for t, _ in tramos)
            if actual and an + esp + w > ancho:
                lineas.append(actual)
                actual, an = [], 0.0
            actual.append((tramos, w))
            an += (esp if len(actual) > 1 else 0) + w
        if actual:
            lineas.append(actual)
        inter = int(tam * 1.04)
        if len(lineas) <= 3 and len(lineas) * inter <= alto and all(w <= ancho for l in lineas for _, w in l):
            yy = y + (alto - len(lineas) * inter) // 2 + int(tam * 0.86)  # línea base
            som = max(2, tam // 40)
            for linea in lineas:
                xx = x
                for tramos, w in linea:
                    for t, m in tramos:
                        d.text((xx + som, yy + som), t, font=f, fill=(0, 0, 0, 90), anchor="ls")
                        d.text((xx, yy), t, font=f, fill=color_hl if m else (255, 255, 255), anchor="ls")
                        xx += f.getlength(t)
                    xx += esp
                yy += inter
            return tam
    raise SystemExit(f"✗ El gancho «{gancho}» no cabe: acórtalo (3-6 palabras).")


def etiqueta(d: ImageDraw.ImageDraw, texto: str, x: int, y: int, tam: int, fondo, color) -> tuple[int, int]:
    f = fuente("black", tam)
    pad_x, pad_y = int(tam * 0.55), int(tam * 0.32)
    w = int(f.getlength(texto.upper()))
    caja = (x, y, x + w + 2 * pad_x, y + tam + 2 * pad_y)
    d.rounded_rectangle(caja, int(tam * 0.4), fill=fondo)
    d.text((x + pad_x, y + pad_y + tam // 2), texto.upper(), font=f, fill=color, anchor="lm")
    return caja[2] - caja[0], caja[3] - caja[1]


def marca(d: ImageDraw.ImageDraw, x: int, y: int, s: float, alinear="izq", w_total=None):
    lado = int(34 * s)
    f = fuente("black", int(24 * s))
    texto = "decodifica.net"
    ancho = lado + int(10 * s) + int(f.getlength(texto))
    if alinear == "der":
        x = w_total - x - ancho
    d.rounded_rectangle((x, y, x + lado, y + lado), int(8 * s), fill=(255, 255, 255))
    d.text((x + lado // 2, y + lado // 2), "D", font=fuente("black", int(24 * s)), fill=COLORES["brand_oscuro"], anchor="mm")
    d.text((x + lado + int(10 * s), y + lado // 2), texto, font=f, fill=(255, 255, 255), anchor="lm")


# ---------- composiciones ----------

def con_gancho(spec: dict, w: int, h: int) -> Image.Image:
    s = h / 630
    fondo = spec.get("fondo", "indigo")
    img = fondo_base(w, h, fondo)
    m = int(60 * s)
    col = int(w * 0.53)
    # imagen principal a la derecha
    vx, vy = col + int(20 * s), int(44 * s)
    vw, vh = w - vx - int(36 * s), h - 2 * vy
    capa = visual(spec, vw, vh, sangrar=True)
    img.alpha_composite(capa, (vx, vy))
    d = ImageDraw.Draw(img)
    # etiqueta
    y = m
    if spec["plantilla"] == "novedad":
        _, alto_et = etiqueta(d, spec.get("etiqueta", "NUEVO"), m, y, int(34 * s), COLORES["verde"], (6, 30, 20))
    elif spec.get("etiqueta"):
        _, alto_et = etiqueta(d, spec["etiqueta"], m, y, int(26 * s), resaltado(fondo), (20, 16, 40))
    else:
        alto_et = 0
    # gancho
    arriba = y + alto_et + int(18 * s)
    abajo = h - m - int(34 * s) - int(18 * s)
    colocar_gancho(d, spec["gancho"], m, arriba, col - m - int(24 * s), abajo - arriba, resaltado(fondo), s)
    marca(d, m, h - m - int(34 * s), s)
    return img.convert("RGB")


def limpia(spec: dict, w: int, h: int) -> Image.Image:
    s = min(w, h) / 900
    fondo = spec.get("fondo", "indigo")
    img = fondo_base(w, h, fondo)
    # imagen centrada y grande; en 16:9 lo principal queda en el centro (recortes de Discover)
    lado = min(w, h)
    caja_w = int(min(w * 0.82, lado * 1.3))
    caja_h = int(lado * 0.78)
    x0, y0 = (w - caja_w) // 2, (h - caja_h) // 2 + int(lado * 0.03)
    img2 = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    img2.paste(img)
    img = img2
    # en la limpia el brillo va centrado
    capa = visual(spec, caja_w, caja_h, sangrar=False)
    img.alpha_composite(capa, (x0, y0))
    d = ImageDraw.Draw(img)
    if spec["plantilla"] == "novedad":
        tam = int(54 * s)
        f = fuente("black", tam)
        ancho_et = int(f.getlength(spec.get("etiqueta", "NUEVO").upper())) + int(tam * 1.1)
        etiqueta(d, spec.get("etiqueta", "NUEVO"), (w - ancho_et) // 2, int(y0 - tam * 1.9), tam, COLORES["verde"], (6, 30, 20))
    marca(d, int(36 * s), h - int(36 * s) - int(34 * s), s * 1.1, alinear="der", w_total=w)
    return img.convert("RGB")


def generar(spec: dict) -> list[tuple[Path, int, tuple[int, int]]]:
    slug = spec["slug"]
    hechos = []
    og = con_gancho(spec, 1200, 630)
    tarjeta = con_gancho(spec, 1280, 720)
    limpia_16x9 = limpia(spec, 1600, 900)
    salidas = [
        (og, f"{slug}.jpg", 86),
        (tarjeta.resize((640, 360), Image.Resampling.LANCZOS), f"{slug}-tarjeta.webp", 80),
        (tarjeta.resize((960, 540), Image.Resampling.LANCZOS), f"{slug}-tarjeta-960.webp", 80),
        (limpia_16x9, f"{slug}-16x9.webp", 82),
        (limpia_16x9.resize((800, 450), Image.Resampling.LANCZOS), f"{slug}-16x9-800.webp", 80),
        (limpia(spec, 1200, 900), f"{slug}-4x3.webp", 82),
        (limpia(spec, 1200, 1200), f"{slug}-1x1.webp", 82),
    ]
    for img, nombre, calidad in salidas:
        destino = SALIDA / nombre
        peso = guardar(img, destino, calidad)
        hechos.append((destino, peso, img.size))
    return hechos


def validar(slug: str, spec: dict) -> list[str]:
    errores = []
    if spec.get("plantilla") not in PLANTILLAS:
        errores.append(f"plantilla debe ser una de {PLANTILLAS}")
    n = len(trozos(spec.get("gancho", "")))
    if not 2 <= n <= 6:
        errores.append(f"el gancho tiene {n} palabras (de 3 a 6)")
    alt = spec.get("alt", "")
    if len(alt) < 40:
        errores.append("falta un texto alternativo (alt) descriptivo de al menos 40 caracteres")
    if spec.get("fondo", "indigo") not in FONDOS:
        errores.append(f"fondo debe ser uno de {list(FONDOS)}")
    if not (RAIZ / "src" / "pages" / "blog" / f"{slug}.astro").exists():
        errores.append("no existe src/pages/blog/<slug>.astro")
    return errores


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slugs", nargs="*", help="artículos (por defecto, todos los de portadas.json)")
    ap.add_argument("--muestra", help="guarda también una hoja con las portadas generadas (PNG)")
    a = ap.parse_args()
    datos = json.loads(DATOS.read_text(encoding="utf-8"))
    slugs = a.slugs or [k for k in datos if not k.startswith("_")]
    fallos = 0
    tarjetas = []
    for slug in slugs:
        if slug not in datos:
            print(f"✗ {slug}: no está en {DATOS.relative_to(RAIZ)}")
            fallos += 1
            continue
        spec = {**datos[slug], "slug": slug}
        errores = validar(slug, spec)
        if errores:
            print(f"✗ {slug}: " + "; ".join(errores))
            fallos += 1
            continue
        hechos = generar(spec)
        total = sum(p for _, p, _ in hechos)
        og_kb = hechos[0][1] // 1024
        aviso = "  · og:image > 300 KB (WhatsApp puede no mostrarla)" if og_kb > 300 else ""
        print(f"✓ {slug} · {spec['plantilla']} · og {og_kb} KB · total {total // 1024} KB{aviso}")
        tarjetas.append(hechos[0][0])
    if a.muestra and tarjetas:
        cols = 2
        miniaturas = [Image.open(p).resize((600, 315)) for p in tarjetas]
        filas = (len(miniaturas) + cols - 1) // cols
        hoja = Image.new("RGB", (cols * 610 + 10, filas * 325 + 10), (255, 255, 255))
        for i, m in enumerate(miniaturas):
            hoja.paste(m, (10 + (i % cols) * 610, 10 + (i // cols) * 325))
        hoja.save(a.muestra)
        print(f"Hoja de muestra: {a.muestra}")
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
