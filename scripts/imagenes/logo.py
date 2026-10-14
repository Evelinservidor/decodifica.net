"""Descarga el logo (icono de la app) de una herramienta desde su web oficial.

Busca los iconos que la propia web declara (apple-touch-icon, icon, manifest),
se queda con el más grande y lo guarda en scripts/imagenes/logos/<nombre>.png.
Solo para identificar la herramienta de la que habla el artículo.

Uso:
  python3 scripts/imagenes/logo.py claude https://claude.com https://www.anthropic.com
  python3 scripts/imagenes/logo.py n8n https://n8n.io --selector "header a[href='/'] svg"

Si la primera URL falla (p. ej. protección antirobots), prueba las siguientes.
Con --selector hace una captura de ese elemento (útil para logos con nombre).
"""
from __future__ import annotations

import argparse
import base64
import io
import json
import sys
from pathlib import Path
from urllib.parse import urljoin

from PIL import Image
from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import AGENTE, LOGOS, abrir_navegador  # noqa: E402

JS_ICONOS = """
() => {
  const out = [];
  for (const l of document.querySelectorAll('link[rel]')) {
    const rel = (l.getAttribute('rel') || '').toLowerCase();
    if (rel.includes('icon')) out.push({href: l.href.baseVal || l.href, sizes: l.getAttribute('sizes') || '', rel, type: l.type || ''});
  }
  const m = document.querySelector('link[rel="manifest"]');
  return {iconos: out, manifest: m ? m.href : null};
}
"""


def tam_declarado(sizes: str) -> int:
    try:
        return max(int(s.lower().split("x")[0]) for s in sizes.split() if "x" in s.lower())
    except ValueError:
        return 0


def svg_a_png(pagina, datos: bytes, lado: int = 512) -> Image.Image:
    b64 = base64.b64encode(datos).decode()
    pagina.set_content(
        f'<html><body style="margin:0;background:transparent">'
        f'<img id="i" src="data:image/svg+xml;base64,{b64}" style="width:{lado}px;height:{lado}px;object-fit:contain"></body></html>'
    )
    pagina.wait_for_timeout(300)
    if not pagina.evaluate("document.getElementById('i').naturalWidth > 0"):
        raise ValueError("SVG no válido")
    return Image.open(io.BytesIO(pagina.locator("#i").screenshot(omit_background=True)))


def recortar(img: Image.Image, lado: int = 512) -> Image.Image:
    img = img.convert("RGBA")
    caja = img.getchannel("A").getbbox()
    if caja:
        img = img.crop(caja)
    img.thumbnail((lado, lado), Image.Resampling.LANCZOS)
    return img


JS_FETCH = """
async (u) => {
  try {
    const r = await fetch(u, {credentials: 'include'});
    if (!r.ok) return null;
    const b = new Uint8Array(await r.arrayBuffer());
    let s = ''; for (let i = 0; i < b.length; i++) s += String.fromCharCode(b[i]);
    return btoa(s);
  } catch (e) { return null; }
}
"""


def descargar(contexto, href: str, pagina=None) -> bytes | None:
    """Descarga un archivo: desde la propia página (mismas cookies), por petición directa o abriéndolo."""
    if pagina is not None:
        try:
            b64 = pagina.evaluate(JS_FETCH, href)
            if b64:
                datos = base64.b64decode(b64)
                if datos.lstrip()[:1] != b"<" or b"<svg" in datos[:3000].lower():
                    return datos
        except Exception:  # noqa: BLE001
            pass
    try:
        r = contexto.request.get(href, timeout=20000)
        if r.ok and r.body().lstrip()[:1] != b"<" or (r.ok and b"<svg" in r.body()[:3000].lower()):
            return r.body()
    except Exception:  # noqa: BLE001
        pass
    pg = contexto.new_page()
    try:
        resp = pg.goto(href, timeout=20000)
        return resp.body() if resp and resp.ok else None
    except Exception:  # noqa: BLE001
        return None
    finally:
        pg.close()


def buscar_icono(contexto, url: str) -> Image.Image | None:
    pagina = contexto.new_page()
    lienzo = contexto.new_page()  # para pasar SVG a PNG sin salir de la web
    try:
        pagina.goto(url, timeout=45000, wait_until="domcontentloaded")
        pagina.wait_for_timeout(2000)
        if "just a moment" in pagina.title().lower():
            print(f"  {url}: protección antirobots, se prueba la siguiente")
            return None
        datos = pagina.evaluate(JS_ICONOS)
        candidatos = [(i["href"], tam_declarado(i["sizes"]), i["type"]) for i in datos["iconos"]]
        if datos["manifest"]:
            try:
                r = contexto.request.get(datos["manifest"], timeout=20000)
                man = json.loads(r.body())
                for i in man.get("icons", []):
                    candidatos.append((urljoin(datos["manifest"], i["src"]), tam_declarado(i.get("sizes", "")), i.get("type", "")))
            except Exception:  # noqa: BLE001
                pass
        for extra in ("/apple-touch-icon.png", "/favicon.svg"):
            candidatos.append((urljoin(url, extra), 180 if extra.endswith("png") else 0, ""))
        mejor, mejor_lado = None, 0
        for href, _, tipo in candidatos:
            try:
                cuerpo = descargar(contexto, href, pagina)
                if not cuerpo:
                    continue
                es_svg = b"<svg" in cuerpo[:3000].lower()
                if not es_svg and cuerpo.lstrip()[:1] == b"<":
                    continue  # página HTML (error o antirobots), no una imagen
                img = svg_a_png(lienzo, cuerpo) if es_svg else Image.open(io.BytesIO(cuerpo))
                if getattr(img, "n_frames", 1) > 1:
                    img.seek(img.n_frames - 1)  # .ico: el tamaño más grande
                lado = 1024 if es_svg else min(img.size)
                if lado > mejor_lado:
                    mejor, mejor_lado = img.copy(), lado
            except Exception:  # noqa: BLE001
                continue
        if mejor is not None:
            print(f"  {url}: icono de {mejor_lado}px")
        return mejor
    except Exception as e:  # noqa: BLE001
        print(f"  {url}: error {e}")
        return None
    finally:
        pagina.close()
        lienzo.close()


def capturar_elemento(contexto, url: str, selector: str) -> Image.Image | None:
    pagina = contexto.new_page(device_scale_factor=4)
    try:
        pagina.goto(url, timeout=45000, wait_until="domcontentloaded")
        pagina.wait_for_timeout(2500)
        return Image.open(io.BytesIO(pagina.locator(selector).first.screenshot(omit_background=True)))
    except Exception as e:  # noqa: BLE001
        print(f"  {url}: no se pudo capturar {selector}: {e}")
        return None
    finally:
        pagina.close()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("nombre", help="nombre corto del archivo, p. ej. claude")
    ap.add_argument("urls", nargs="+", help="web(s) oficial(es) de la herramienta")
    ap.add_argument("--selector", help="captura este elemento de la página en vez del icono")
    ap.add_argument("--min", type=int, default=120, help="tamaño mínimo aceptable en px (por defecto 120)")
    a = ap.parse_args()

    with sync_playwright() as p:
        nav = abrir_navegador(p)
        ctx = nav.new_context(user_agent=AGENTE, locale="es-ES")
        img, usada = None, a.urls[0]
        for url in a.urls:
            usada = url
            img = capturar_elemento(ctx, url, a.selector) if a.selector else buscar_icono(ctx, url)
            if img is not None and min(img.size) >= a.min:
                break
            img = None
        nav.close()
    if img is None:
        print(f"✗ No se encontró un logo de al menos {a.min}px para {a.nombre}.")
        return 1
    LOGOS.mkdir(parents=True, exist_ok=True)
    destino = LOGOS / f"{a.nombre}.png"
    recortar(img).save(destino, optimize=True)
    fuentes = LOGOS / "FUENTES.md"
    linea = f"- `{a.nombre}.png`: {usada}" + (f" (elemento `{a.selector}`)" if a.selector else "") + "\n"
    texto = fuentes.read_text(encoding="utf-8") if fuentes.exists() else (
        "# De dónde sale cada logo\n\nIconos descargados de la web oficial de cada herramienta con "
        "`scripts/imagenes/logo.py`. Se usan solo para identificar la herramienta de la que habla el artículo.\n\n"
    )
    texto = "".join(l for l in texto.splitlines(True) if not l.startswith(f"- `{a.nombre}.png`")) + linea
    fuentes.write_text(texto, encoding="utf-8")
    print(f"✓ {destino.relative_to(Path.cwd()) if destino.is_relative_to(Path.cwd()) else destino} ({img.width}x{img.height})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
