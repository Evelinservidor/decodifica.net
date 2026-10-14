"""Piezas comunes de las maquetas de las 3 propuestas de rediseño (fase 1).

Usa los artículos, portadas y datos de Search Console reales del repositorio.
No toca la web: escribe HTML en docs/rediseno/maquetas/<propuesta>/.

    python3 docs/rediseno/maquetas/generar.py
    python3 -m http.server 8765 --directory .     # desde la raíz del repositorio
    python3 scripts/capturas_rediseno.py http://localhost:8765 docs/rediseno/a \
        inicio=/docs/rediseno/maquetas/a/inicio.html ...
"""
import html
import json
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
SALIDA = Path(__file__).resolve().parent
BLOG = RAIZ / "src/pages/blog"
PORTADAS = json.loads((RAIZ / "src/data/portadas.json").read_text())

# Temas propuestos (hoy los artículos solo tienen «pilar», que no sirve para navegar).
TEMAS = {
    "chatbots": ("Chatbots y asistentes", "indigo"),
    "local": ("IA en tu ordenador", "verde"),
    "automatizar": ("Agentes y automatización", "rosa"),
    "oficina": ("Trabajo y día a día", "azul"),
    "crear": ("Imagen, vídeo y webs", "naranja"),
}
TEMA_DE = {
    "claude-ia-que-es-gratis": "chatbots", "alternativas-gratis-chatgpt-2026": "chatbots",
    "deepseek-app-oficial-espanol": "chatbots", "chatgpt-work-archivos-a-entregables": "chatbots",
    "gpt-live-voz-chatgpt": "chatbots", "2026-08-05-kimi-k3-investigacion-visual": "chatbots",
    "notebooklm-guia-2026": "chatbots", "alternativas-fable-5": "chatbots",
    "2026-07-26-arena-ai-modelos-gratis": "chatbots", "2026-07-27-tencent-hy3-modelo-abierto-agentes": "chatbots",
    "ollama-que-es-como-usar": "local", "lm-studio-que-es-como-usar": "local",
    "odysseus-pewdiepie-ia-gratis": "local", "2026-07-25-ia-local-oculta-datos": "local",
    "2026-08-01-qwen3-asr-transcribe-espanol": "local",
    "n8n-que-es-gratis": "automatizar", "2026-07-17-hermes-agent-chino": "automatizar",
    "crear-agente-voz-ia-sin-programar": "automatizar", "claude-skills-1000-gratis": "automatizar",
    "qwen-code-agent-terminal": "automatizar", "crear-app-web-ias-chinas-open-source": "automatizar",
    "ia-organiza-pendientes": "oficina", "ia-mejora-excel": "oficina",
    "ia-crea-presentaciones-completas": "oficina", "claude-emails-sonar-humanos": "oficina",
    "ia-resumir-reuniones-tareas-revisables": "oficina", "5-atajos-ia-gratis": "oficina",
    "2026-07-31-google-maps-gemini-paradas-ruta": "oficina", "como-elegir-herramienta-ia": "oficina",
    "2026-07-22-nano-banana-1000-prompts": "crear", "2026-07-28-higgsfield-davinci-plugin-ia": "crear",
    "2026-07-16-prompts-secretos-web": "crear",
}
MESES = "ene feb mar abr may jun jul ago sep oct nov dic".split()


def campo(src, nombre):
    m = re.search(rf'const\s+{nombre}\s*=\s*(["\'])(.*?)\1\s*;', src)
    return m.group(2).strip() if m else None


def articulos():
    lista = []
    for f in BLOG.glob("*.astro"):
        src = f.read_text()
        if f.stem == "index" or "Astro.redirect" in src:
            continue
        t, d, p = campo(src, "title"), campo(src, "description"), campo(src, "pubDate")
        if not (t and d and p) or f.stem not in PORTADAS:
            continue
        lista.append(dict(slug=f.stem, titulo=t, desc=d, fecha=p, mod=campo(src, "modifiedDate") or p,
                          min=(campo(src, "readingTime") or "5 min"), tema=TEMA_DE.get(f.stem, "oficina"),
                          etiqueta=PORTADAS[f.stem].get("etiqueta", "")))
    return sorted(lista, key=lambda a: a["fecha"], reverse=True)


def mas_leidos(arts, n=5):
    """Ranking por clics y luego impresiones en Search Console (último informe)."""
    datos = json.loads((RAIZ / "data/gsc_weekly/latest.json").read_text())
    sitio = next(v for k, v in datos["per_site"].items() if "decodifica" in k)
    por_slug = {a["slug"]: a for a in arts}
    filas = sorted(sitio["pages"]["current"], key=lambda r: (-r["clicks"], -r["impressions"]))
    out = []
    for r in filas:
        m = re.search(r"/blog/([^/]+)/", r["page"])
        if m and m.group(1) in por_slug and por_slug[m.group(1)] not in out:
            out.append(por_slug[m.group(1)])
    return out[:n]


def fecha(iso):
    a, m, d = iso.split("-")
    return f"{int(d)} {MESES[int(m) - 1]} {a}"


def e(t):
    return html.escape(t, quote=True)


def img_tarjeta(a, cls="", ancho="(min-width: 1024px) 400px, 100vw", lazy=True):
    b = f"/public/og/blog/{a['slug']}"
    return (f'<img class="{cls}" src="{b}-tarjeta.webp" srcset="{b}-tarjeta.webp 640w, {b}-tarjeta-960.webp 960w" '
            f'sizes="{ancho}" width="640" height="360" alt="" {"loading=lazy" if lazy else "fetchpriority=high"} decoding="async">')


FUENTES_CSS = """
@font-face{font-family:"ID";src:url(/scripts/imagenes/fuentes/InterDisplay-ExtraBold.otf);font-weight:800;font-display:swap}
@font-face{font-family:"ID";src:url(/scripts/imagenes/fuentes/InterDisplay-Black.otf);font-weight:900;font-display:swap}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}body{margin:0;font-family:Inter,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
a{color:inherit;text-decoration:none}img{display:block;max-width:100%;height:auto}
.wrap{max-width:1200px;margin:0 auto;padding:0 16px}@media(min-width:768px){.wrap{padding:0 32px}}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
.h{font-family:"ID",Inter,system-ui,sans-serif;font-weight:800;letter-spacing:-.02em;line-height:1.12;margin:0}
.chips{display:flex;gap:8px;overflow-x:auto;scrollbar-width:none;padding:2px 0}.chips::-webkit-scrollbar{display:none}
.chip{flex:none;display:inline-flex;align-items:center;min-height:36px;padding:0 14px;border-radius:999px;font-size:14px;font-weight:600;white-space:nowrap}
.ico{width:22px;height:22px;stroke:currentColor;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.desliza{font-size:13px;margin:1.2em 0 -.9em;opacity:.7}@media(min-width:700px){.desliza{display:none}}
.btn{display:inline-flex;align-items:center;justify-content:center;min-height:44px;padding:0 18px;border-radius:10px;font-weight:700;font-size:15px;border:0;cursor:pointer;font-family:inherit}
"""
ICO_BUSCAR = '<svg class="ico" viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>'
ICO_MENU = '<svg class="ico" viewBox="0 0 24 24"><path d="M4 7h16M4 12h16M4 17h16"/></svg>'
ICO_LUNA = '<svg class="ico" viewBox="0 0 24 24"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>'

# ---------------------------------------------------------------- artículo de ejemplo
# Texto real (resumido) de /blog/claude-skills-1000-gratis/ para ver cómo queda la lectura.
ART_SLUG = "claude-skills-1000-gratis"
TOC = [("que-es", "Qué es una Skill de Claude"), ("planes", "Dónde funcionan y qué plan necesitas"),
       ("gratis", "Dónde conseguir Skills gratis"), ("instalar", "Cómo instalar una Skill"),
       ("crear", "Cómo crear tu propia Skill"), ("seguridad", "Seguridad: qué revisar antes"),
       ("faq", "Preguntas frecuentes")]
RESPUESTA = ("<strong>En resumen:</strong> una Skill es una carpeta con un archivo <code>SKILL.md</code> que Claude carga "
             "solo cuando tu petición encaja con su descripción. Anthropic incluye cuatro gratis (Word, Excel, PowerPoint "
             "y PDF), publica más en el repositorio <code>anthropics/skills</code> y te deja subir las tuyas en Claude.ai, "
             "Claude Code y la API.")
PUNTOS = [("Planes", "Free, Pro, Max, Team y Enterprise, con ejecución de código"), ("Dónde", "Claude.ai, Claude Code y la API"),
          ("Ojo", "Una Skill puede ejecutar código: revisa las de terceros")]


def cuerpo_articulo(c):
    """c: dict con clases/estilos de la propuesta para los componentes."""
    tabla = """<p class="desliza">Desliza la tabla para ver todas las columnas →</p><div class="tabla" role="region" aria-label="Tabla: dónde funcionan las Skills" tabindex="0"><table>
<thead><tr><th>Dónde</th><th>Skills de Anthropic</th><th>Skills propias</th></tr></thead><tbody>
<tr><th>Claude.ai</th><td>Sí, se usan solas al crear documentos</td><td>Sí, subiendo un ZIP</td></tr>
<tr><th>Claude Code</th><td>No vienen incluidas; se instalan del repositorio</td><td>Sí, como carpetas o plugins</td></tr>
<tr><th>API</th><td>Sí: <code>pptx</code>, <code>xlsx</code>, <code>docx</code>, <code>pdf</code></td><td>Sí, con <code>/v1/skills</code></td></tr>
</tbody></table></div>"""
    return f"""
<h2 id="que-es">Qué es una Skill de Claude</h2>
<p>Anthropic las llama <strong>Agent Skills</strong> y las define como «carpetas organizadas de instrucciones, scripts y recursos que los agentes pueden descubrir y cargar de forma dinámica» para hacer mejor una tarea concreta.</p>
<p>Lo que las distingue de un prompt largo es cómo se cargan. La documentación lo llama <em>carga progresiva</em> y lo divide en tres niveles: los metadatos (siempre), las instrucciones (al activarse) y los archivos y scripts (solo cuando hacen falta).</p>
<figure><img src="/public/img/blog/{ART_SLUG}/tres-niveles-de-carga.webp" width="1200" height="489" loading="lazy" alt="Esquema de los tres niveles de carga de una Skill"><figcaption>Los tres niveles de carga de una Skill. Fuente: documentación de Anthropic.</figcaption></figure>
<aside class="caja consejo"><p class="caja-t">Consejo</p><p>Puedes tener muchas Skills instaladas: hasta que se activan, cada una solo ocupa unos 100 tokens (su nombre y su descripción).</p></aside>
<h2 id="planes">Dónde funcionan y qué plan necesitas</h2>
<p>El centro de ayuda indica que las Skills están disponibles en los planes Free, Pro, Max, Team y Enterprise, siempre que esté activada la ejecución de código.</p>
{tabla}
<aside class="caja ojo"><p class="caja-t">Ojo</p><p>No se sincronizan: una Skill subida a Claude.ai no aparece en la API ni en Claude Code. Hay que instalarla en cada sitio.</p></aside>
{c['boletin_medio']}
<h2 id="gratis">Dónde conseguir Skills gratis</h2>
<p>El punto de partida más seguro es el repositorio oficial <code>anthropics/skills</code>, porque lo mantiene Anthropic. A 6 de octubre de 2026 contiene 19 Skills, entre ellas <code>skill-creator</code>, que ayuda a crear Skills nuevas.</p>
<ol><li>Abre el repositorio y entra en la carpeta <code>skills/</code>.</li><li>Elige una Skill y descarga su carpeta.</li><li>Comprímela en ZIP y súbela en Ajustes → Capacidades.</li></ol>
<h2 id="faq">Preguntas frecuentes</h2>
<details open><summary>¿Las Skills de Claude son gratis?</summary><p>Sí: las cuatro de Anthropic vienen incluidas y las del repositorio oficial son gratuitas. Necesitas tener activada la ejecución de código.</p></details>
<details><summary>¿Una Skill es lo mismo que un proyecto?</summary><p>No. Un proyecto da conocimiento de fondo siempre cargado; una Skill aporta un procedimiento que se activa solo cuando hace falta.</p></details>
<h2 id="fuentes">Fuentes</h2>
<ul class="fuentes"><li><a href="#">Agent Skills · documentación de Anthropic</a></li><li><a href="#">Using Skills in Claude · centro de ayuda</a></li><li><a href="#">anthropics/skills · GitHub</a></li></ul>
"""


def cookies(c):
    """Aviso discreto. Rechazar y Aceptar en la primera capa, mismo tamaño y mismo peso visual."""
    return f"""<div class="ck" role="dialog" aria-label="Privacidad" aria-live="polite">
<p>Solo usamos analítica sin publicidad <b>si aceptas</b>. <a href="#">Configurar</a> · <a href="#">Más información</a></p>
<div class="ck-b"><button class="btn ck-btn">Rechazar</button><button class="btn ck-btn">Aceptar</button></div></div>"""


def pagina(titulo, css, cuerpo, tema_oscuro=False):
    return f"""<!doctype html><html lang="es"{' class="oscuro"' if tema_oscuro else ''}><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(titulo)}</title>
<style>{FUENTES_CSS}{css}</style></head><body>{cuerpo}</body></html>"""


