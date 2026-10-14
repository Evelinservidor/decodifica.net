"""Propuesta C · «Guía de bolsillo»: buscador primero, listas compactas y un color por tema (el de las portadas)."""
from base import (ART_SLUG, ICO_BUSCAR, ICO_LUNA, ICO_MENU, PUNTOS, RESPUESTA, TEMAS, TOC, cookies, cuerpo_articulo, e,
                  fecha, img_tarjeta, pagina)

COL = {"indigo": "#4f46e5", "verde": "#059669", "rosa": "#db2777", "azul": "#0284c7", "naranja": "#ea580c"}
COL_T = {"indigo": "#4338ca", "verde": "#047857", "rosa": "#be185d", "azul": "#0369a1", "naranja": "#c2410c"}  # texto AA sobre claro

CSS = """
:root{--bg:#f5f3ee;--sf:#fff;--ink:#16182b;--ink2:#4d5168;--ink3:#6c7088;--line:#e3dfd6;--brand:#4f46e5}
body{background:var(--bg);color:var(--ink)}
.top{background:var(--ink);color:#fff}.top .wrap{display:flex;align-items:center;height:56px;gap:6px}
.logo{display:flex;align-items:center;gap:8px;font-family:"ID";font-weight:900;font-size:21px;margin-right:auto;letter-spacing:-.02em}
.logo i{display:grid;place-items:center;width:28px;height:28px;border-radius:8px;background:#ff9500;color:#16182b;font-style:normal;font-size:15px}
.top button{width:44px;height:44px;display:grid;place-items:center;background:none;border:0;color:#fff}
.nav{display:none;gap:24px;font-weight:600;font-size:15px;margin-right:12px}@media(min-width:900px){.nav{display:flex}.top .menu{display:none}}
.busca{background:var(--ink);color:#fff;padding:18px 0 22px}
.busca h1{font-size:clamp(24px,6vw,36px)}.busca p{margin:6px 0 14px;color:#c9cce0;font-size:15px}
.caja-b{display:flex;align-items:center;gap:10px;background:#fff;color:var(--ink3);border-radius:14px;min-height:54px;padding:0 16px;font-size:16px;max-width:680px}
.busca .chips{margin-top:12px}.busca .chip{background:rgba(255,255,255,.1);color:#fff;border:1px solid rgba(255,255,255,.2)}
.sec{padding:24px 0 6px}.sec-h{display:flex;justify-content:space-between;align-items:center;margin-bottom:6px}
.sec-h h2{font-size:21px;display:flex;align-items:center;gap:10px}.sec-h h2 i{width:12px;height:12px;border-radius:4px;display:inline-block}
.sec-h a{font-size:14px;font-weight:700;color:var(--brand)}
.it{display:grid;grid-template-columns:132px 1fr;gap:14px;align-items:center;padding:12px 0;border-bottom:1px solid var(--line)}
.it img{border-radius:10px;aspect-ratio:16/9;object-fit:cover}.it h3{font-size:16.5px;line-height:1.25}
.pill{display:inline-block;font-size:12px;font-weight:700;padding:2px 8px;border-radius:999px;margin-bottom:4px}
.meta{font-size:13px;color:var(--ink3);margin-top:4px}
.lista{background:var(--sf);border-radius:16px;padding:4px 16px;border:1px solid var(--line)}.lista .it:last-child{border-bottom:0}
.top5{list-style:none;margin:0;padding:0}.top5 li{display:flex;gap:12px;align-items:baseline;padding:12px 0;border-bottom:1px solid var(--line)}
.top5 li:last-child{border-bottom:0}.top5 b{font-family:"ID";font-weight:900;font-size:22px;color:#ea580c;width:22px;flex:none}.top5 span{font-weight:600;line-height:1.3}
.temas{display:grid;gap:10px}.tema{display:flex;align-items:center;gap:12px;background:var(--sf);border:1px solid var(--line);border-radius:14px;padding:10px;min-height:64px}
.tema i{width:44px;height:44px;border-radius:12px;flex:none}.tema b{display:block;font-size:16px}.tema span{font-size:13px;color:var(--ink3)}
@media(min-width:700px){.temas{grid-template-columns:repeat(auto-fill,minmax(220px,1fr))}}
@media(min-width:1000px){.dos{display:grid;grid-template-columns:1.6fr 1fr;gap:32px;align-items:start}}
.news{margin:26px 0;border-radius:16px;padding:20px;background:#ffedd5;border:1px solid #fed7aa}
.news h2{font-size:21px}.news p{margin:6px 0 12px;color:#5a3a1a;line-height:1.5}.news form{display:flex;flex-wrap:wrap;gap:8px}
.news input{flex:1 1 200px;min-height:48px;border-radius:12px;border:1px solid #fdba74;padding:0 14px;font-size:16px}.news .btn{background:var(--ink);color:#fff;min-height:48px}
footer{background:var(--ink);color:#b8bcd3;margin-top:30px;padding:26px 0 120px;font-size:14px}footer .cols{display:flex;flex-wrap:wrap;gap:12px 20px;margin-top:10px}
.ck{position:fixed;left:0;right:0;bottom:0;z-index:50;background:var(--sf);border-top:2px solid var(--ink);padding:12px 16px;display:flex;flex-wrap:wrap;gap:10px;align-items:center;justify-content:center}
.ck p{margin:0;font-size:14px;line-height:1.4;flex:1 1 260px;max-width:560px}.ck a{color:var(--brand);text-decoration:underline}
.ck-b{display:flex;gap:8px;flex:1 1 200px;max-width:320px}.ck-btn{flex:1;background:var(--sf);border:2px solid var(--ink);color:var(--ink);min-height:44px}
/* artículo */
.art{padding-top:16px}.miga{font-size:14px;color:var(--ink3)}
.art h1{font-size:clamp(28px,7vw,42px);margin:8px 0 0}.dek{font-size:18px;line-height:1.5;color:var(--ink2);margin:10px 0}
.by{font-size:14px;color:var(--ink3);display:flex;flex-wrap:wrap;gap:6px 14px;padding:10px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.by b{color:var(--ink)}
.cab{width:100%;aspect-ratio:16/9;object-fit:cover;border-radius:12px;margin:16px 0}
.rr{background:var(--sf);border:2px solid var(--ink);border-radius:14px;padding:16px;margin:0 0 20px;box-shadow:5px 5px 0 #ff9500;margin-right:5px}
.rr-t{margin:0 0 6px!important;font-family:"ID";font-weight:800;font-size:18px}.rr p{margin:0;font-size:17px;line-height:1.6}
.rr table{margin-top:12px;width:100%;border-collapse:collapse;font-size:15px}.rr td{padding:6px 0;border-top:1px solid var(--line);vertical-align:top}.rr td:first-child{font-weight:700;width:74px}
.toc{background:var(--sf);border:1px solid var(--line);border-radius:12px;margin-bottom:10px}.toc summary{min-height:48px;display:flex;align-items:center;padding:0 14px;font-weight:700;cursor:pointer}
.toc ol{margin:0;padding:0 14px 12px 34px;line-height:1.95;font-size:15px}.toc a{color:var(--ink2)}
.prosa{font-family:Charter,"Bitstream Charter","Iowan Old Style",Georgia,serif;font-size:19px;line-height:1.7}.prosa p,.prosa ol,.prosa ul{margin:0 0 1.1em}
.prosa h2{font-family:"ID";font-weight:800;font-size:clamp(23px,5.4vw,28px);line-height:1.2;margin:1.8em 0 .55em;scroll-margin-top:16px}
.prosa a{color:var(--brand)}.prosa code{font-family:ui-monospace,monospace;font-size:.8em;background:#ece9e1;padding:2px 5px;border-radius:5px}
.prosa figure{margin:1.5em 0}.prosa figure img{border-radius:10px}.prosa figcaption{font-family:Inter,system-ui;font-size:14px;color:var(--ink3);margin-top:6px}
.tabla{overflow-x:auto;margin:1.4em 0;font-family:Inter,system-ui}.tabla table{border-collapse:collapse;width:100%;min-width:500px;font-size:15px;line-height:1.45;background:var(--sf)}
.tabla th,.tabla td{text-align:left;padding:11px 12px;border:1px solid var(--line);vertical-align:top}.tabla thead th{background:var(--ink);color:#fff;border-color:var(--ink)}
.caja{font-family:Inter,system-ui;border-radius:12px;padding:14px 16px 14px 52px;margin:1.4em 0;font-size:16px;line-height:1.55;position:relative;background:var(--sf);border:1px solid var(--line)}
.caja p{margin:0}.caja::before{position:absolute;left:14px;top:12px;font-size:22px}.caja-t{font-weight:800;margin-bottom:2px!important}
.consejo::before{content:"💡"}.ojo::before{content:"⚠️"}
.bmed{font-family:Inter,system-ui;background:#ffedd5;border-radius:14px;padding:16px;margin:1.8em 0;display:grid;grid-template-columns:minmax(0,1fr);gap:8px}
.bmed form{display:flex;gap:8px}.bmed input{flex:1;min-width:0;min-height:44px;border:1px solid #fdba74;border-radius:10px;padding:0 12px;font-size:16px}
.bmed .btn{background:var(--ink);color:#fff}.bmed span{font-size:15px;color:#5a3a1a}
.prosa details{font-family:Inter,system-ui;border-top:1px solid var(--line);padding:12px 0;font-size:17px}.prosa summary{font-weight:700;cursor:pointer}
.lado{display:none}
@media(min-width:1100px){.lay{display:grid;grid-template-columns:minmax(0,720px) 300px;gap:56px;justify-content:center}
.lado{display:block;position:sticky;top:16px;align-self:start}.lado .toc{border:0;background:none}.lado .toc summary{padding:0;min-height:0;margin-bottom:6px;list-style:none}
.lado .toc ol{padding-left:20px}.toc-m{display:none}.lado .news{margin-top:16px}}
"""


def cabecera():
    return f"""<header class="top"><div class="wrap"><a class="logo" href="inicio.html"><i>D</i>Decodifica</a>
<nav class="nav"><a href="#">Guías</a><a href="#">Temas</a><a href="#">Herramientas</a><a href="#">Boletín</a></nav>
<button aria-label="Buscar">{ICO_BUSCAR}</button><button aria-label="Modo oscuro">{ICO_LUNA}</button><button class="menu" aria-label="Menú">{ICO_MENU}</button></div></header>"""


def pill(a):
    n, col = TEMAS[a["tema"]]
    return f'<span class="pill" style="background:{COL[col]}1a;color:{COL_T[col]}">{e(n)}</span>'


def it(a):
    return f'<a class="it" href="articulo.html">{img_tarjeta(a, ancho="132px")}<div>{pill(a)}<h3 class="h">{e(a["titulo"])}</h3><p class="meta">{fecha(a["fecha"])} · {a["min"]}</p></div></a>'


PIE = """<footer><div class="wrap"><b class="logo" style="font-size:18px;color:#fff"><i>D</i>Decodifica</b><p>Guías de IA práctica en español, con fuentes. Jordi revisa cada artículo antes de publicarlo.</p>
<div class="cols"><a href="#">Guías</a><a href="#">Herramientas</a><a href="#">Boletín</a><a href="#">Sobre</a><a href="#">Privacidad</a><a href="#">Cookies</a><a href="#">Aviso legal</a></div></div></footer>"""
NEWS = """<section class="news"><h2 class="h">📬 Una guía útil cada sábado</h2><p>Qué probar, cómo usarlo y sus límites. Gratis; te das de baja con un clic.</p>
<form><label class="sr" for="em">Tu email</label><input id="em" type="email" placeholder="tu@email.com"><button class="btn">Apuntarme</button></form></section>"""
TAREAS = ["IA gratis", "Sin internet", "Escribir emails", "Excel", "Presentaciones", "Automatizar"]


def temas_html(arts):
    cuenta = {k: sum(a["tema"] == k for a in arts) for k in TEMAS}
    return '<div class="temas">' + "".join(
        f'<a class="tema" href="blog.html"><i style="background:linear-gradient(135deg,#16182b,{COL[col]})"></i><div><b>{e(n)}</b><span>{cuenta[k]} guías</span></div></a>'
        for k, (n, col) in TEMAS.items()) + "</div>"


def inicio(arts, top):
    chips = '<div class="chips">' + "".join(f'<a class="chip" href="#">{t}</a>' for t in TAREAS) + "</div>"
    top5 = "".join(f'<li><b>{i}</b><a href="articulo.html"><span>{e(a["titulo"])}</span></a></li>' for i, a in enumerate(top, 1))
    cuerpo = f"""{cabecera()}<section class="busca"><div class="wrap"><h1 class="h">¿Qué quieres hacer con IA?</h1><p>{len(arts)} guías en español, con fuentes oficiales y pasos que puedes seguir.</p>
<label class="caja-b">{ICO_BUSCAR}<span>Ej.: transcribir audio, IA gratis…</span></label>{chips}</div></section>
<main class="wrap"><div class="dos"><section class="sec"><div class="sec-h"><h2 class="h">Lo último</h2><a href="blog.html">Ver todas →</a></div>
<div class="lista">{''.join(it(a) for a in arts[:6])}</div></section>
<section class="sec"><div class="sec-h"><h2 class="h">🔥 Lo más leído</h2></div><div class="lista"><ol class="top5">{top5}</ol></div>{NEWS}</section></div>
<section class="sec"><div class="sec-h"><h2 class="h">Por tema</h2></div>{temas_html(arts)}</section>
<section class="sec"><div class="sec-h"><h2 class="h"><i style="background:#059669"></i>IA en tu ordenador</h2><a href="blog.html">Ver las 5 →</a></div>
<div class="lista">{''.join(it(a) for a in arts if a['tema'] == 'local')}</div></section>
</main>{PIE}{cookies(None)}"""
    return pagina("Decodifica · IA práctica en español", CSS, cuerpo)


def blog(arts, top):
    chips = '<div class="chips">' + "".join(f'<a class="chip" href="#">{e(n)}</a>' for n, _ in TEMAS.values()) + "</div>"
    cuerpo = f"""{cabecera()}<section class="busca"><div class="wrap"><h1 class="h">Todas las guías</h1><p>{len(arts)} guías de IA práctica, de la más nueva a la más antigua.</p>
<label class="caja-b">{ICO_BUSCAR}<span>Busca una herramienta o una tarea…</span></label>{chips}</div></section>
<main class="wrap"><section class="sec"><div class="lista">{''.join(it(a) for a in arts[:16])}</div>
<div style="display:flex;justify-content:center;margin-top:18px"><button class="btn" style="background:var(--sf);border:1px solid var(--line);color:var(--ink)">Ver {len(arts) - 16} guías más</button></div></section>
{NEWS}</main>{PIE}"""
    return pagina("Guías de IA práctica · Decodifica", CSS, cuerpo)


def articulo(arts, top):
    a = next(x for x in arts if x["slug"] == ART_SLUG)
    rel = [x for x in arts if x["tema"] == a["tema"] and x["slug"] != ART_SLUG][:4]
    toc = "".join(f'<li><a href="#{i}">{e(t)}</a></li>' for i, t in TOC)
    bmed = """<div class="bmed"><b>📬 ¿Te sirve? Recibe una guía así cada sábado.</b><form><label class="sr" for="e2">Tu email</label><input id="e2" type="email" placeholder="tu@email.com"><button class="btn">Apuntarme</button></form><span>Gratis. Te das de baja con un clic.</span></div>"""
    filas = "".join(f"<tr><td>{e(k)}</td><td>{e(v)}</td></tr>" for k, v in PUNTOS)
    n, col = TEMAS[a["tema"]]
    cuerpo = f"""{cabecera()}<main class="wrap art"><div class="lay"><article><p class="miga"><a href="blog.html">Guías</a> › {pill(a)}</p>
<h1 class="h">{e(a['titulo'])}</h1><p class="dek">{e(a['desc'])}</p>
<div class="by"><span>Por <b>Jordi Castañeira</b></span><span>Revisado el 6 oct 2026</span><span>⏱ {a['min']}</span></div>
<img class="cab" src="/public/og/blog/{ART_SLUG}-16x9-800.webp" width="800" height="450" alt="Logo de Claude" fetchpriority="high">
<section class="rr"><p class="rr-t">⚡ Respuesta rápida</p><p>{RESPUESTA}</p><table>{filas}</table></section>
<details class="toc toc-m"><summary>📑 En esta guía ({len(TOC)})</summary><ol>{toc}</ol></details>
<div class="prosa">{cuerpo_articulo({'boletin_medio': bmed})}</div>
<section class="sec"><div class="sec-h"><h2 class="h"><i style="background:{COL[col]}"></i>Más de {e(n.lower())}</h2></div><div class="lista">{''.join(it(x) for x in rel)}</div></section></article>
<aside class="lado"><details class="toc" open><summary>En esta guía</summary><ol>{toc}</ol></details>{NEWS}</aside></div></main>{PIE}"""
    return pagina(a["titulo"], CSS, cuerpo)


def paginas(arts, top):
    return {"inicio": inicio(arts, top), "blog": blog(arts, top), "articulo": articulo(arts, top)}
