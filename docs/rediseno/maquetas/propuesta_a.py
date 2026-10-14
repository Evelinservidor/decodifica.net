"""Propuesta A · «Revista luminosa»: fondo claro, las portadas ponen el color, portada de revista."""
from base import (ART_SLUG, ICO_BUSCAR, ICO_LUNA, ICO_MENU, PUNTOS, RESPUESTA, TEMAS, TOC, cookies,
                  cuerpo_articulo, e, fecha, img_tarjeta, pagina)

CSS = """
:root{--bg:#fbfaf7;--sf:#fff;--ink:#12142a;--ink2:#4b5066;--ink3:#6b7086;--line:#e6e3dc;--brand:#4f46e5;--brand-s:#eef2ff;--acc:#c2410c;
--ok:#047857;--ok-s:#ecfdf5;--warn:#b45309;--warn-s:#fffbeb}
.oscuro{--bg:#0d0f1c;--sf:#151829;--ink:#eef0f8;--ink2:#b7bcd3;--ink3:#9096b0;--line:#272b44;--brand:#a5b4fc;--brand-s:#1c1f3d;--acc:#fdba74;
--ok:#6ee7b7;--ok-s:#0f2a24;--warn:#fcd34d;--warn-s:#2b230f}
body{background:var(--bg);color:var(--ink)}
.top{position:sticky;top:0;z-index:20;background:color-mix(in srgb,var(--bg) 92%,transparent);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.top .wrap{display:flex;align-items:center;justify-content:space-between;height:56px}
.logo{display:flex;align-items:center;gap:8px;font-family:"ID";font-weight:900;font-size:21px;letter-spacing:-.02em}
.logo i{display:grid;place-items:center;width:28px;height:28px;border-radius:8px;background:linear-gradient(135deg,#1e1b4b,#4f46e5);color:#fff;font-style:normal;font-size:15px}
.nav{display:none;gap:26px;font-weight:600;font-size:15px}.nav a:hover{color:var(--brand)}
.acc{display:flex;gap:4px}.acc button{width:44px;height:44px;display:grid;place-items:center;background:none;border:0;color:var(--ink);border-radius:10px}
@media(min-width:900px){.nav{display:flex}.acc .menu{display:none}}
.temas{border-bottom:1px solid var(--line);background:var(--bg)}.temas .chips{padding:10px 0}
.chip{background:var(--sf);border:1px solid var(--line);color:var(--ink2)}.chip.on{background:var(--ink);color:var(--bg);border-color:var(--ink)}
.tag{font-size:12px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:var(--acc)}
.meta{font-size:13px;color:var(--ink3);margin-top:8px}
.sec{padding:28px 0}.sec-h{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:16px;border-top:3px solid var(--ink);padding-top:12px}
.sec-h h2{font-size:22px}.sec-h a{font-size:14px;font-weight:700;color:var(--brand)}
.lead img{border-radius:14px;aspect-ratio:16/9;object-fit:cover;width:100%}
.lead h3{font-size:clamp(25px,6.5vw,38px);margin-top:12px}.lead p.d{color:var(--ink2);font-size:16px;line-height:1.5;margin:8px 0 0}
.row{display:grid;grid-template-columns:124px 1fr;gap:14px;align-items:start;padding:14px 0;border-top:1px solid var(--line)}
.row img{border-radius:10px;aspect-ratio:16/9;object-fit:cover}.row h3{font-size:17px;line-height:1.25}
.top5{counter-reset:n;list-style:none;margin:0;padding:0}.top5 li{display:grid;grid-template-columns:44px 1fr;gap:6px;padding:12px 0;border-top:1px solid var(--line)}
.top5 li::before{counter-increment:n;content:counter(n);font-family:"ID";font-weight:900;font-size:34px;line-height:1;color:var(--acc)}
.top5 h3{font-size:17px;line-height:1.25}
.tiles{display:grid;grid-template-columns:1fr 1fr;gap:10px}.tile{border-radius:14px;padding:16px;min-height:96px;color:#fff;display:flex;flex-direction:column;justify-content:space-between}
.tile b{font-family:"ID";font-size:17px;line-height:1.15}.tile span{font-size:13px;opacity:.85}
.g-indigo{background:linear-gradient(135deg,#1e1b4b,#4f46e5)}.g-verde{background:linear-gradient(135deg,#022c22,#059669)}
.g-rosa{background:linear-gradient(135deg,#500724,#db2777)}.g-azul{background:linear-gradient(135deg,#082f49,#0284c7)}
.g-naranja{background:linear-gradient(135deg,#7c2d12,#ea580c)}.g-noche{background:linear-gradient(135deg,#080a14,#312e81)}
.grid{display:grid;gap:22px}.card img{border-radius:12px;aspect-ratio:16/9;object-fit:cover;width:100%}.card h3{font-size:19px;margin-top:10px;line-height:1.22}
.card .tag{display:block;margin-top:12px}
@media(min-width:640px){.grid{grid-template-columns:1fr 1fr}.tiles{grid-template-columns:repeat(3,1fr)}}
@media(min-width:1000px){.grid{grid-template-columns:repeat(3,1fr)}.tiles{grid-template-columns:repeat(5,1fr)}
.hero{display:grid;grid-template-columns:1.55fr 1fr;gap:36px}.hero .row:first-child{border-top:0;padding-top:0}
.duo{display:grid;grid-template-columns:2fr 1fr;gap:40px}}
.news{border-radius:18px;padding:24px;color:#fff;background:linear-gradient(135deg,#1e1b4b,#4f46e5)}
.news h2{font-size:24px}.news p{color:#dfe3ff;margin:8px 0 16px;line-height:1.5}
.news form{display:flex;flex-wrap:wrap;gap:8px}.news input{flex:1 1 200px;min-height:48px;border-radius:10px;border:0;padding:0 14px;font-size:16px}
.news .btn{background:#ff9500;color:#1a1200;min-height:48px}.news small{display:block;margin-top:10px;color:#c7d2fe}
.utils{display:grid;gap:10px}.util{display:flex;gap:12px;align-items:center;padding:14px;border:1px solid var(--line);border-radius:12px;background:var(--sf)}
.util b{display:block}.util span{font-size:14px;color:var(--ink2)}
@media(min-width:800px){.utils{grid-template-columns:repeat(3,1fr)}}
footer{margin-top:40px;border-top:1px solid var(--line);padding:28px 0 120px;color:var(--ink3);font-size:14px}
footer .cols{display:flex;flex-wrap:wrap;gap:12px 22px}
.ck{position:fixed;left:12px;right:12px;bottom:12px;z-index:50;background:var(--sf);color:var(--ink);border:1px solid var(--line);border-radius:14px;
box-shadow:0 10px 30px rgba(0,0,0,.15);padding:12px 14px;display:flex;flex-wrap:wrap;gap:10px;align-items:center;max-width:720px;margin:0 auto}
.ck p{margin:0;font-size:14px;line-height:1.4;flex:1 1 260px}.ck a{color:var(--brand);text-decoration:underline}
.ck-b{display:flex;gap:8px;flex:1 1 200px}.ck-btn{flex:1;background:var(--ink);color:var(--bg);min-height:44px}
/* lista del blog */
.bh{padding:26px 0 8px}.bh h1{font-size:clamp(30px,7vw,46px)}.bh p{color:var(--ink2);margin:8px 0 16px;font-size:16px;line-height:1.5}
.buscar{display:flex;align-items:center;gap:8px;border:1px solid var(--line);background:var(--sf);border-radius:12px;padding:0 12px;min-height:48px;color:var(--ink3)}
.buscar span{font-size:16px}
.mas{display:flex;justify-content:center;margin-top:24px}.mas .btn{background:var(--sf);border:1px solid var(--line);color:var(--ink)}
/* artículo */
.art{padding-top:18px}.miga{font-size:14px;color:var(--ink3)}.miga a{color:var(--brand);font-weight:600}
.art h1{font-size:clamp(30px,7.4vw,46px);margin-top:10px}.dek{font-size:19px;line-height:1.5;color:var(--ink2);margin:12px 0 0}
.by{display:flex;align-items:center;gap:10px;margin:16px 0 18px;font-size:14px;color:var(--ink3)}
.by i{width:36px;height:36px;border-radius:50%;display:grid;place-items:center;background:var(--brand-s);color:var(--brand);font-style:normal;font-weight:800}
.by b{color:var(--ink);display:block}
.cab{border-radius:14px;aspect-ratio:16/9;object-fit:cover;width:100%}
.rr{margin:22px 0;background:var(--brand-s);border-radius:14px;padding:18px;border-left:5px solid var(--brand)}
.rr-t{margin:0 0 6px;font-weight:800;font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--brand)}
.rr p{margin:0;font-size:17px;line-height:1.6}.rr dl{display:grid;gap:8px;margin:14px 0 0}.rr dl div{display:grid;grid-template-columns:70px 1fr;gap:8px;font-size:15px}
.rr dt{font-weight:800}.rr dd{margin:0;color:var(--ink2)}
.toc{border:1px solid var(--line);border-radius:12px;background:var(--sf);margin:0 0 8px}.toc summary{min-height:48px;display:flex;align-items:center;padding:0 16px;font-weight:700;cursor:pointer}
.toc ol{margin:0;padding:0 16px 14px 36px;line-height:1.9}.toc a{color:var(--ink2)}.toc a:hover{color:var(--brand)}
.prosa{font-size:18px;line-height:1.72;color:var(--ink)}.prosa p,.prosa ol,.prosa ul{margin:0 0 1.15em}
.prosa h2{font-family:"ID";font-weight:800;font-size:clamp(24px,5.6vw,30px);line-height:1.18;letter-spacing:-.015em;margin:1.9em 0 .6em;scroll-margin-top:72px}
.prosa a{color:var(--brand);text-decoration:underline;text-underline-offset:3px}.prosa code{font-size:.86em;background:var(--brand-s);padding:2px 5px;border-radius:5px}
.prosa figure{margin:1.6em 0}.prosa figure img{border-radius:10px;border:1px solid var(--line)}.prosa figcaption{font-size:14px;color:var(--ink3);margin-top:8px}
.tabla{overflow-x:auto;margin:1.4em 0;border:1px solid var(--line);border-radius:12px;background:var(--sf)}
.tabla table{border-collapse:collapse;width:100%;min-width:520px;font-size:15px;line-height:1.45}
.tabla th,.tabla td{text-align:left;padding:12px 14px;border-bottom:1px solid var(--line);vertical-align:top}
.tabla thead th{background:var(--bg);font-size:13px;text-transform:uppercase;letter-spacing:.04em;color:var(--ink3)}
.tabla tbody th{position:sticky;left:0;background:var(--sf)}.tabla tr:last-child>*{border-bottom:0}
.caja{border-radius:12px;padding:14px 16px;margin:1.4em 0;font-size:16.5px;line-height:1.6}.caja p{margin:0}
.caja-t{font-weight:800;font-size:13px;letter-spacing:.05em;text-transform:uppercase;margin-bottom:4px!important}
.consejo{background:var(--ok-s);border-left:4px solid var(--ok)}.consejo .caja-t{color:var(--ok)}
.ojo{background:var(--warn-s);border-left:4px solid var(--warn)}.ojo .caja-t{color:var(--warn)}
.bmed{border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:16px 0;margin:1.8em 0;display:grid;gap:10px}
.bmed b{font-size:16px}.bmed span{font-size:15px;color:var(--ink2);line-height:1.5}.bmed form{display:flex;gap:8px}
.bmed input{flex:1;min-width:0;min-height:44px;border:1px solid var(--line);border-radius:10px;padding:0 12px;font-size:16px;background:var(--sf);color:var(--ink)}
.bmed .btn{background:var(--brand);color:#fff}.oscuro .bmed .btn{color:#12142a}
.prosa details{border-top:1px solid var(--line);padding:12px 0}.prosa summary{font-weight:700;cursor:pointer;min-height:32px}
.fuentes{font-size:16px}
.autor{display:flex;gap:14px;border:1px solid var(--line);border-radius:14px;padding:16px;margin:28px 0;background:var(--sf);font-size:15px;line-height:1.5;color:var(--ink2)}
.autor i{flex:none;width:48px;height:48px;border-radius:50%;display:grid;place-items:center;background:var(--brand-s);color:var(--brand);font-style:normal;font-weight:800;font-size:20px}
.autor b{color:var(--ink)}
.cuerpo{max-width:700px;margin:0 auto}
@media(min-width:1100px){.lay{display:grid;grid-template-columns:230px minmax(0,700px) 1fr;gap:48px}.lay .cuerpo{margin:0}
.lado{position:sticky;top:76px;align-self:start;font-size:14px}.lado .toc{border:0;background:none}.lado .toc summary{padding:0;min-height:0;margin-bottom:8px;pointer-events:none;list-style:none}
.lado .toc summary::-webkit-details-marker{display:none}.lado .toc ol{padding:0 0 0 18px}.toc-m{display:none}}
@media(max-width:1099px){.lado{display:none}}
"""


def cabecera(activo=""):
    nav = "".join(f'<a href="#"{" style=color:var(--brand)" if t == activo else ""}>{t}</a>' for t in ("Guías", "Temas", "Herramientas", "Boletín"))
    return f"""<header class="top"><div class="wrap"><a class="logo" href="inicio.html"><i>D</i>Decodifica</a>
<nav class="nav">{nav}</nav><div class="acc"><button aria-label="Buscar">{ICO_BUSCAR}</button><button aria-label="Modo oscuro">{ICO_LUNA}</button>
<button class="menu" aria-label="Menú">{ICO_MENU}</button></div></div></header>"""


def chips_temas(on="Todas"):
    items = ["Todas"] + [n for n, _ in TEMAS.values()]
    return '<div class="chips">' + "".join(f'<a class="chip{" on" if i == on else ""}" href="#">{e(i)}</a>' for i in items) + "</div>"


def tema(a):
    return TEMAS[a["tema"]][0]


def card(a):
    return f'<a class="card" href="articulo.html">{img_tarjeta(a, ancho="(min-width:1000px) 380px, (min-width:640px) 50vw, 100vw")}<span class="tag">{e(tema(a))}</span><h3 class="h">{e(a["titulo"])}</h3><p class="meta">{fecha(a["fecha"])} · {a["min"]}</p></a>'


def fila(a):
    return f'<a class="row" href="articulo.html">{img_tarjeta(a, ancho="124px")}<div><span class="tag">{e(tema(a))}</span><h3 class="h">{e(a["titulo"])}</h3><p class="meta">{fecha(a["fecha"])} · {a["min"]}</p></div></a>'


PIE = """<footer><div class="wrap"><p class="logo" style="font-size:18px"><i>D</i>Decodifica</p><p>Guías de IA práctica en español, con fuentes. Cada artículo lo revisa Jordi antes de publicarse.</p>
<div class="cols"><a href="#">Guías</a><a href="#">Herramientas</a><a href="#">Boletín</a><a href="#">Sobre Decodifica</a><a href="#">Privacidad</a><a href="#">Cookies</a><a href="#">Aviso legal</a></div></div></footer>"""

NEWS = """<section class="news"><h2 class="h">Una guía útil cada sábado</h2><p>Qué herramienta probar, cómo usarla y qué límites tiene. Gratis, sin spam.</p>
<form><label class="sr" for="em">Tu email</label><input id="em" type="email" placeholder="tu@email.com"><button class="btn">Apuntarme gratis</button></form>
<small>Te das de baja con un clic.</small></section>"""


def inicio(arts, top):
    lead, resto = arts[0], arts[1:]
    cuenta = {k: sum(a["tema"] == k for a in arts) for k in TEMAS}
    tiles = "".join(f'<a class="tile g-{c}" href="blog.html"><b>{e(n)}</b><span>{cuenta[k]} guías</span></a>' for k, (n, c) in TEMAS.items())
    cuerpo = f"""{cabecera()}<div class="temas"><div class="wrap">{chips_temas()}</div></div>
<main class="wrap"><section class="sec"><div class="sec-h"><h2 class="h">Lo último</h2><a href="blog.html">Todas las guías →</a></div>
<div class="hero"><a class="lead" href="articulo.html">{img_tarjeta(lead, ancho="(min-width:1000px) 700px, 100vw", lazy=False)}<span class="tag" style="display:block;margin-top:14px">{e(tema(lead))}</span>
<h3 class="h">{e(lead['titulo'])}</h3><p class="d">{e(lead['desc'])}</p><p class="meta">{fecha(lead['fecha'])} · {lead['min']} de lectura</p></a>
<div>{''.join(fila(a) for a in resto[:4])}</div></div></section>
<div class="duo"><section class="sec"><div class="sec-h"><h2 class="h">Más guías</h2></div><div class="grid" style="grid-template-columns:repeat(auto-fill,minmax(260px,1fr))">{''.join(card(a) for a in resto[4:8])}</div></section>
<section class="sec"><div class="sec-h"><h2 class="h">Lo más leído</h2></div><ol class="top5">{''.join(f'<li><a href="articulo.html"><h3 class="h">{e(a["titulo"])}</h3><p class="meta" style="margin-top:4px">{e(tema(a))}</p></a></li>' for a in top)}</ol></section></div>
<section class="sec"><div class="sec-h"><h2 class="h">Explora por tema</h2></div><div class="tiles">{tiles}</div></section>
<section class="sec">{NEWS}</section>
<section class="sec"><div class="sec-h"><h2 class="h">Herramientas gratis</h2><a href="#">Ver todas →</a></div><div class="utils">
<a class="util" href="#"><div><b>Generador de prompts</b><span>Ordena tu petición en 4 pasos</span></div></a>
<a class="util" href="#"><div><b>Comparador de IA</b><span>Pon dos herramientas frente a frente</span></div></a>
<a class="util" href="#"><div><b>¿Puedo subir estos datos?</b><span>Revisa el riesgo antes de usar una IA</span></div></a></div></section>
</main>{PIE}{cookies(None)}"""
    return pagina("Decodifica · IA práctica en español", CSS, cuerpo)


def blog(arts, top):
    cuerpo = f"""{cabecera("Guías")}<main class="wrap"><header class="bh"><h1 class="h">Guías de IA práctica</h1>
<p>{len(arts)} guías en español con fuentes oficiales: qué es cada herramienta, cuánto cuesta y cómo se usa.</p>
<label class="buscar">{ICO_BUSCAR}<span>Busca una herramienta o una tarea…</span></label></header>
<div style="margin:14px 0 22px">{chips_temas()}</div>
<div class="grid">{''.join(card(a) for a in arts[:12])}</div>
<div class="mas"><button class="btn">Ver {len(arts) - 12} guías más</button></div>
<section class="sec">{NEWS}</section></main>{PIE}"""
    return pagina("Guías de IA práctica · Decodifica", CSS, cuerpo)


def articulo(arts, top, oscuro=False):
    a = next(x for x in arts if x["slug"] == ART_SLUG)
    rel = [x for x in arts if x["tema"] == a["tema"] and x["slug"] != ART_SLUG][:3]
    toc = "".join(f'<li><a href="#{i}">{e(t)}</a></li>' for i, t in TOC)
    bmed = """<div class="bmed"><b>¿Te está sirviendo?</b><span>Cada sábado mandamos una guía como esta. Gratis y sin spam.</span>
<form><label class="sr" for="e2">Tu email</label><input id="e2" type="email" placeholder="tu@email.com"><button class="btn">Apuntarme</button></form></div>"""
    puntos = "".join(f"<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>" for k, v in PUNTOS)
    cuerpo = f"""{cabecera("Guías")}<main class="wrap art"><div class="lay"><aside class="lado"><details class="toc" open><summary>En esta guía</summary><ol>{toc}</ol></details></aside>
<article class="cuerpo"><p class="miga"><a href="blog.html">Guías</a> › <a href="#">{e(tema(a))}</a></p>
<h1 class="h">{e(a['titulo'])}</h1><p class="dek">{e(a['desc'])}</p>
<div class="by"><i>J</i><div><b>Jordi Castañeira</b>Revisado el 6 oct 2026 · {a['min']} de lectura</div></div>
<img class="cab" src="/public/og/blog/{ART_SLUG}-16x9-800.webp" width="800" height="450" alt="Logo de Claude" fetchpriority="high">
<section class="rr" aria-label="Respuesta rápida"><p class="rr-t">⚡ Respuesta rápida</p><p>{RESPUESTA}</p><dl>{puntos}</dl></section>
<details class="toc toc-m"><summary>En esta guía · {len(TOC)} apartados</summary><ol>{toc}</ol></details>
<div class="prosa">{cuerpo_articulo({'boletin_medio': bmed})}</div>
<div class="autor"><i>J</i><div><b>Jordi Castañeira</b><br>Escribe Decodifica. Cada dato sale de la documentación oficial enlazada en «Fuentes».</div></div>
</article></div>
<section class="sec"><div class="sec-h"><h2 class="h">Sigue leyendo</h2></div><div class="grid">{''.join(card(x) for x in rel)}</div></section></main>{PIE}"""
    return pagina(a["titulo"], CSS, cuerpo, tema_oscuro=oscuro)


def paginas(arts, top):
    return {"inicio": inicio(arts, top), "blog": blog(arts, top), "articulo": articulo(arts, top),
            "articulo-oscuro": articulo(arts, top, oscuro=True)}
