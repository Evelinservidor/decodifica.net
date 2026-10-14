"""Esquemas propios con los colores de Decodifica para meter dentro de un artículo.

Tres tipos, descritos en un JSON (archivo o texto):

  pasos        pasos en orden, numerados
  comparativa  dos o tres columnas (p. ej. gratis / de pago)
  resumen      cuadro resumen de filas «etiqueta: valor»

Ejemplos:
  python3 scripts/imagenes/esquema.py public/img/blog/n8n/pasos.webp --json '{
    "tipo": "pasos", "titulo": "Tu primer flujo en n8n",
    "pasos": ["Crea la cuenta o instala n8n", "Añade un disparador", "Conecta la app", "Prueba y activa"],
    "pie": "Según la documentación oficial de n8n (consultada en octubre de 2026)"}'

  python3 scripts/imagenes/esquema.py salida.webp --archivo esquema.json

Campos: «titulo» (opcional), «pie» (opcional, para la fuente), y según el tipo:
  pasos: "pasos": ["texto", ...]  (o [["título", "detalle"], ...])
  comparativa: "columnas": [{"nombre": "Gratis", "precio": "0 €", "puntos": ["...", ...], "destacar": false}, ...]
               marca un punto que NO incluye empezándolo por "✗ " y uno que sí por "✓ ".
  resumen: "filas": [["Qué es", "..."], ["Precio", "..."], ...]
Imprime ancho, alto y peso: copia ancho y alto en el <img>. Todo dato del
esquema debe estar también en el texto del artículo y salir de una fuente.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import COLORES, fuente, guardar  # noqa: E402

ANCHO = 1200
M = 56  # margen
C = COLORES


def partir(texto: str, f, ancho: int) -> list[str]:
    lineas: list[str] = []
    for parrafo in str(texto).split("\n"):
        actual = ""
        for palabra in parrafo.split():
            prueba = f"{actual} {palabra}".strip()
            if f.getlength(prueba) <= ancho or not actual:
                actual = prueba
            else:
                lineas.append(actual)
                actual = palabra
        lineas.append(actual)
    return lineas


class Lienzo:
    """Dibuja en un lienzo alto y al final recorta a la altura usada."""

    def __init__(self) -> None:
        self.img = Image.new("RGB", (ANCHO, 4000), C["fondo"])
        self.d = ImageDraw.Draw(self.img)
        self.y = M

    def texto(self, x, texto, f, color, ancho, interlineado=1.3) -> int:
        alto = round(f.size * interlineado)
        y0 = self.y
        for linea in partir(texto, f, ancho):
            self.d.text((x, self.y), linea, font=f, fill=color)
            self.y += alto
        return self.y - y0

    def cerrar(self, pie: str | None) -> Image.Image:
        if pie:
            self.y += 8
            self.texto(M, pie, fuente("medium", 20), C["gris"], ANCHO - 2 * M - 180)
        marca = "decodifica.net"
        f = fuente("bold", 20)
        self.d.text((ANCHO - M, self.y - 26 if pie else self.y + 4), marca, font=f, fill=C["brand_claro"], anchor="ra")
        self.y += 40 if not pie else 24
        alto = self.y + M // 2
        img = self.img.crop((0, 0, ANCHO, alto))
        ImageDraw.Draw(img).rounded_rectangle((0, 0, ANCHO - 1, alto - 1), 28, outline=C["linea"], width=2)
        return img


def titulo(l: Lienzo, t: str | None) -> None:
    if t:
        l.texto(M, t, fuente("black", 46), C["texto"], ANCHO - 2 * M, 1.15)
        l.y += 22


def pasos(spec: dict) -> Image.Image:
    l = Lienzo()
    titulo(l, spec.get("titulo"))
    items = spec["pasos"]
    for i, paso in enumerate(items, 1):
        cab, det = (paso if isinstance(paso, list) else [paso, None]) + [None] * 0
        r = 30
        cx, cy = M + r, l.y + r
        l.d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=C["brand"])
        l.d.text((cx, cy), str(i), font=fuente("black", 30), fill=C["texto"], anchor="mm")
        x = M + 2 * r + 24
        y0 = l.y
        l.y += 10
        l.texto(x, cab, fuente("bold", 32), C["texto"], ANCHO - x - M, 1.2)
        if det:
            l.y += 2
            l.texto(x, det, fuente("medium", 24), C["suave"], ANCHO - x - M, 1.35)
        l.y = max(l.y, y0 + 2 * r) + 18
        if i < len(items):
            l.d.line((cx, y0 + 2 * r + 4, cx, l.y - 4), fill=C["linea"], width=4)
    return l.cerrar(spec.get("pie"))


def comparativa(spec: dict) -> Image.Image:
    l = Lienzo()
    titulo(l, spec.get("titulo"))
    cols = spec["columnas"]
    hueco = 24
    w = (ANCHO - 2 * M - hueco * (len(cols) - 1)) // len(cols)
    y_ini = l.y
    alturas = []
    # Primera pasada: medir; segunda: dibujar con la misma altura
    for pasada in (0, 1):
        for n, col in enumerate(cols):
            x = M + n * (w + hueco)
            l.y = y_ini
            if pasada:
                destacar = col.get("destacar")
                l.d.rounded_rectangle(
                    (x, y_ini, x + w, y_ini + max(alturas)), 22,
                    fill=C["fondo2"], outline=C["naranja"] if destacar else C["linea"], width=3,
                )
            pad = 28
            l.y += pad
            dibujar = pasada == 1
            def t(texto, f, color, inter=1.3, x_off=0):
                if dibujar:
                    return l.texto(x + pad + x_off, texto, f, color, w - 2 * pad - x_off, inter)
                alto = len(partir(texto, f, w - 2 * pad - x_off)) * round(f.size * inter)
                l.y += alto
                return alto
            t(col["nombre"], fuente("black", 36), C["texto"], 1.15)
            if col.get("precio"):
                l.y += 4
                t(col["precio"], fuente("extrabold", 30), C["naranja"], 1.2)
            l.y += 14
            for punto in col.get("puntos", []):
                no = punto.startswith("✗")
                si = punto.startswith("✓")
                limpio = punto[1:].strip() if (si or no) else punto
                simbolo = "✗" if no else "✓"
                color = (248, 113, 113) if no else C["verde"]
                if dibujar:
                    l.d.text((x + pad, l.y), simbolo, font=fuente("bold", 26), fill=color)
                t(limpio, fuente("medium", 25), C["texto"] if not no else C["gris"], 1.3, x_off=34)
                l.y += 8
            l.y += pad - 8
            if not pasada:
                alturas.append(l.y - y_ini)
    l.y = y_ini + max(alturas) + 24
    return l.cerrar(spec.get("pie"))


def resumen(spec: dict) -> Image.Image:
    l = Lienzo()
    titulo(l, spec.get("titulo"))
    ancho_etq = spec.get("ancho_etiqueta", 300)
    for i, (etq, val) in enumerate(spec["filas"]):
        y0 = l.y
        l.y += 18
        f_etq = fuente("bold", 26)
        f_val = fuente("medium", 26)
        alto_val = len(partir(val, f_val, ANCHO - 2 * M - ancho_etq - 40)) * round(26 * 1.35)
        alto_etq = len(partir(etq, f_etq, ancho_etq - 20)) * round(26 * 1.3)
        alto = max(alto_val, alto_etq) + 36
        if i % 2 == 0:
            l.d.rounded_rectangle((M - 16, y0, ANCHO - M + 16, y0 + alto), 14, fill=C["fondo2"])
        yy = l.y
        l.texto(M, etq, f_etq, C["naranja"], ancho_etq - 20, 1.3)
        l.y = yy
        l.texto(M + ancho_etq + 20, val, f_val, C["texto"], ANCHO - 2 * M - ancho_etq - 40, 1.35)
        l.y = y0 + alto + 4
    l.y += 12
    return l.cerrar(spec.get("pie"))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("salida", help="ruta .webp de destino")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--json", help="descripción del esquema en JSON")
    g.add_argument("--archivo", help="archivo JSON con la descripción")
    ap.add_argument("--calidad", type=int, default=82)
    a = ap.parse_args()
    spec = json.loads(a.json) if a.json else json.loads(Path(a.archivo).read_text(encoding="utf-8"))
    tipos = {"pasos": pasos, "comparativa": comparativa, "resumen": resumen}
    if spec.get("tipo") not in tipos:
        print(f"✗ «tipo» debe ser uno de: {', '.join(tipos)}")
        return 1
    img = tipos[spec["tipo"]](spec)
    destino = Path(a.salida)
    peso = guardar(img, destino, a.calidad)
    print(f"✓ {destino} · {img.width}x{img.height} · {peso // 1024} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
