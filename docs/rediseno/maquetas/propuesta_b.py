"""Propuesta B · «Escaparate oscuro»: fondo oscuro como hoy, pero las portadas mandan, en filas que se deslizan."""
from base import (ART_SLUG, ICO_BUSCAR, ICO_MENU, PUNTOS, RESPUESTA, TEMAS, TOC, cookies, cuerpo_articulo, e,
                  fecha, img_tarjeta, pagina)

CSS = """
:root{--bg:#0a0c16;--sf:#141729;--sf2:#1b1f36;--ink:#f2f3fa;--ink2:#bcc1da;--ink3:#8e94b3;--line:#262a45;--brand:#a5b4fc;--acc:#ffb340;
--ok:#6ee7b7;--warn:#fcd34d}
body{background:var(--bg);color:var(--ink)}
.top{position:sticky;top:0;z-index:20;background:rgba(10,12,22,.9);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
.top .wrap{display:flex;align-items:center;gap:12px;height:58px}
.logo{display:flex;align-items:center;gap:8px;font-family:"ID";font-weight:900;font-size:21px;letter-spacing:-.02em;margin-right:auto}
.logo i{display:grid;place-items:center;width:28px;height:28px;border-radius:8px;background:#4f46e5;color:#fff;font-style:normal;font-size:15px}
.nav{display:none;gap:24px;font-weight:600;font-size:15px;color:var(--ink2);margin-right:16px}
.top button{width:44px;height:44px;display:grid;place-items:center;background:var(--sf);border:1px solid var(--line);color:var(--ink);border-radius:12px}
@media(min-width:900px){.nav{display:flex}.top .menu{display:none}}
.tag{display:inline-block;font-size:12px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;color:var(--acc)}
.meta{font-size:13px;color:var(--ink3);margin-top:6px}
/* portada destacada */
.dest{padding:18px 0 6px}.dest-in{display:grid;gap:16px}
.dest img{width:100%;aspect-ratio:16/9;object-fit:cover;border-radius:18px;box-shadow:0 20px 60px -20px rgba(79,70,229,.55)}
.dest h1{font-size:clamp(26px,6.6vw,44px);margin:8px 0 0}.dest p.d{color:var(--ink2);font-size:16px;line-height:1.5;margin:10px 0 0}
.dest .btn{margin-top:16px;background:#4f46e5;color:#fff}
@media(min-width:1000px){.dest-in{grid-template-columns:1.4fr 1fr;align-items:center;gap:40px}}
/* filas deslizables */
.fila{padding:22px 0 4px}.fila-h{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:12px}
.fila-h h2{font-size:21px}.fila-h a{font-size:14px;font-weight:700;color:var(--brand)}
.carril{display:grid;grid-auto-flow:column;grid-auto-columns:78%;gap:14px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-padding:0 16px;padding-bottom:10px;scrollbar-width:none;
margin:0 -16px;padding-left:16px;padding-right:16px}.carril::-webkit-scrollbar{display:none}
@media(min-width:640px){.carril{grid-auto-columns:42%}}@media(min-width:1000px){.carril{grid-auto-columns:calc((100% - 42px)/4);margin:0;padding-left:0;padding-right:0;scroll-padding:0}}
.c{scroll-snap-align:start}.c img{width:100%;aspect-ratio:16/9;object-fit:cover;border-radius:14px}
.c h3{font-size:17px;line-height:1.25;margin-top:10px}
.rank{position:relative}.rank b{position:absolute;left:-4px;bottom:46px;font-family:"ID";font-weight:900;font-size:76px;line-height:1;color:var(--bg);
-webkit-text-stroke:2px var(--acc);text-shadow:none}.rank img{margin-left:30px;width:calc(100% - 30px)}.rank h3{margin-left:30px}.rank .meta{margin-left:30px}
.temas{display:grid;grid-template-columns:1fr 1fr;gap:10px}.tile{border-radius:14px;padding:14px;min-height:84px;display:flex;flex-direction:column;justify-content:space-between;color:#fff}
.tile b{font-family:"ID";font-size:16px;line-height:1.15}.tile span{font-size:13px;opacity:.85}
@media(min-width:800px){.temas{grid-template-columns:repeat(5,1fr)}}
.g-indigo{background:linear-gradient(135deg,#1e1b4b,#4f46e5)}.g-verde{background:linear-gradient(135deg,#022c22,#059669)}
.g-rosa{background:linear-gradient(135deg,#500724,#db2777)}.g-azul{background:linear-gradient(135deg,#082f49,#0284c7)}
.g-naranja{background:linear-gradient(135deg,#7c2d12,#ea580c)}
.news{margin:30px 0;border:1px solid var(--line);background:var(--sf);border-radius:18px;padding:22px}
.news h2{font-size:22px}.news p{color:var(--ink2);margin:8px 0 14px;line-height:1.5}.news form{display:flex;flex-wrap:wrap;gap:8px}
.news input{flex:1 1 200px;min-height:48px;border-radius:12px;border:1px solid var(--line);background:var(--bg);color:var(--ink);padding:0 14px;font-size:16px}
.news .btn{background:var(--acc);color:#1a1200;min-height:48px}
footer{border-top:1px solid var(--line);margin-top:30px;padding:26px 0 120px;color:var(--ink3);font-size:14px}footer .cols{display:flex;flex-wrap:wrap;gap:12px 20px;margin-top:10px}
.ck{position:fixed;left:0;right:0;bottom:0;z-index:50;background:var(--sf2);border-top:1px solid var(--line);padding:12px 16px;display:flex;flex-wrap:wrap;gap:10px;align-items:center;justify-content:center}
.ck p{margin:0;font-size:14px;line-height:1.4;color:var(--ink2);flex:1 1 260px;max-width:560px}.ck a{color:var(--brand);text-decoration:underline}.ck b{color:var(--ink)}
.ck-b{display:flex;gap:8px;flex:1 1 200px;max-width:320px}.ck-btn{flex:1;background:transparent;border:1.5px solid var(--ink2);color:var(--ink);min-height:44px}
/* blog */
.bh{padding:24px 0 10px}.bh h1{font-size:clamp(30px,7vw,46px)}.bh p{color:var(--ink2);margin:8px 0 16px;line-height:1.5}
.buscar{display:flex;align-items:center;gap:10px;min-height:50px;border-radius:14px;background:var(--sf);border:1px solid var(--line);padding:0 14px;color:var(--ink3);font-size:16px}
.chip{background:var(--sf);border:1px solid var(--line);color:var(--ink2)}.chip.on{background:var(--ink);color:var(--bg)}
.grid{display:grid;gap:22px;margin-top:20px}@media(min-width:640px){.grid{grid-template-columns:1fr 1fr}}@media(min-width:1000px){.grid{grid-template-columns:repeat(3,1fr)}}
.grid .c h3{font-size:19px}
/* artículo: cabecera inmersiva */
.ah{background:radial-gradient(ellipse at 70% 0%,rgba(79,70,229,.35),transparent 60%);padding:20px 0 0}
.ah h1{font-size:clamp(30px,7.4vw,48px);margin:10px 0 0}.ah .dek{color:var(--ink2);font-size:19px;line-height:1.5;margin:12px 0}
.ah .meta{font-size:14px}.cab{width:100%;aspect-ratio:16/9;object-fit:cover;border-radius:18px;margin-top:18px}
.cuerpo{max-width:700px;margin:0 auto}
.rr{margin:24px 0;border-radius:16px;padding:18px;background:linear-gradient(135deg,rgba(79,70,229,.22),rgba(79,70,229,.06));border:1px solid rgba(165,180,252,.35)}
.rr-t{margin:0 0 6px;font-weight:800;font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--acc)}.rr p{margin:0;font-size:17px;line-height:1.6}
.rr ul{list-style:none;padding:0;margin:14px 0 0;display:flex;flex-wrap:wrap;gap:8px}.rr li{font-size:14px;background:var(--bg);border:1px solid var(--line);border-radius:999px;padding:6px 12px}
.rr li b{color:var(--acc)}
.toc{position:sticky;top:58px;z-index:10;background:rgba(10,12,22,.95);border-bottom:1px solid var(--line);margin:0 -16px;padding:0 16px}
.toc summary{min-height:46px;display:flex;align-items:center;gap:8px;font-weight:700;font-size:15px;cursor:pointer;color:var(--ink2)}
.toc ol{margin:0;padding:0 0 12px 22px;line-height:2}
.prosa{font-size:18px;line-height:1.75;color:#dfe2f1}.prosa p,.prosa ol,.prosa ul{margin:0 0 1.15em}
.prosa h2{font-family:"ID";font-weight:800;color:var(--ink);font-size:clamp(24px,5.6vw,30px);line-height:1.18;margin:1.9em 0 .6em;scroll-margin-top:110px}
.prosa a{color:var(--brand);text-decoration:underline}.prosa code{font-size:.86em;background:var(--sf2);padding:2px 5px;border-radius:5px}
.prosa figure{margin:1.6em 0}.prosa figure img{border-radius:12px}.prosa figcaption{font-size:14px;color:var(--ink3);margin-top:8px}
.tabla{overflow-x:auto;margin:1.4em 0;border-radius:14px;border:1px solid var(--line)}.tabla table{border-collapse:collapse;width:100%;min-width:520px;font-size:15px;line-height:1.45}
.tabla th,.tabla td{text-align:left;padding:12px 14px;border-bottom:1px solid var(--line);vertical-align:top}.tabla thead th{background:var(--sf2);color:var(--ink)}
.tabla tbody tr:nth-child(odd){background:var(--sf)}.tabla tbody th{color:var(--ink)}
.caja{border-radius:14px;padding:14px 16px;margin:1.4em 0;font-size:16.5px;line-height:1.6;background:var(--sf)}.caja p{margin:0}
.caja-t{font-weight:800;font-size:13px;letter-spacing:.05em;text-transform:uppercase;margin-bottom:4px!important}
.consejo{border:1px solid rgba(110,231,183,.35)}.consejo .caja-t{color:var(--ok)}.ojo{border:1px solid rgba(252,211,77,.35)}.ojo .caja-t{color:var(--warn)}
.bmed{border-radius:14px;background:var(--sf);padding:16px;margin:1.8em 0;display:flex;flex-wrap:wrap;gap:10px;align-items:center}
.bmed span{flex:1 1 240px;font-size:15px;color:var(--ink2);line-height:1.5}.bmed span b{color:var(--ink)}.bmed .btn{background:var(--acc);color:#1a1200}
.prosa details{border-top:1px solid var(--line);padding:12px 0}.prosa summary{font-weight:700;cursor:pointer;color:var(--ink)}
"""

ICO_LUZ = '<svg class="ico" viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>'


def cabecera():
    return f"""<header class="top"><div class="wrap"><a class="logo" href="inicio.html"><i>D</i>Decodifica</a>
<nav class="nav"><a href="#">Guías</a><a href="#">Temas</a><a href="#">Herramientas</a><a href="#">Boletín</a></nav>
<button aria-label="Buscar">{ICO_BUSCAR}</button><button aria-label="Modo claro">{ICO_LUZ}</button><button class="menu" aria-label="Menú">{ICO_MENU}</button></div></header>"""


def c(a, ancho="(min-width:1000px) 290px, 78vw"):
    return f'<a class="c" href="articulo.html">{img_tarjeta(a, ancho=ancho)}<h3 class="h">{e(a["titulo"])}</h3><p class="meta">{fecha(a["fecha"])} · {a["min"]}</p></a>'


def fila(titulo, arts, enlace="Ver todo →"):
    return f'<section class="fila"><div class="fila-h"><h2 class="h">{e(titulo)}</h2><a href="blog.html">{enlace}</a></div><div class="carril">{"".join(c(a) for a in arts)}</div></section>'


PIE = """<footer><div class="wrap"><b class="logo" style="font-size:18px"><i>D</i>Decodifica</b><p>Guías de IA práctica en español, con fuentes. Jordi revisa cada artículo antes de publicarlo.</p>
<div class="cols"><a href="#">Guías</a><a href="#">Herramientas</a><a href="#">Boletín</a><a href="#">Sobre</a><a href="#">Privacidad</a><a href="#">Cookies</a><a href="#">Aviso legal</a></div></div></footer>"""
NEWS = """<section class="news"><h2 class="h">Una guía útil cada sábado</h2><p>Qué probar, cómo usarlo y sus límites. Gratis y sin spam; te das de baja con un clic.</p>
<form><label class="sr" for="em">Tu email</label><input id="em" type="email" placeholder="tu@email.com"><button class="btn">Apuntarme gratis</button></form></section>"""


def inicio(arts, top):
    d = arts[0]
    cuenta = {k: sum(a["tema"] == k for a in arts) for k in TEMAS}
    tiles = "".join(f'<a class="tile g-{col}" href="blog.html"><b>{e(n)}</b><span>{cuenta[k]} guías</span></a>' for k, (n, col) in TEMAS.items())
    ranking = "".join(f'<a class="c rank" href="articulo.html"><b>{i}</b>{img_tarjeta(a, ancho="78vw")}<h3 class="h">{e(a["titulo"])}</h3><p class="meta">{e(TEMAS[a["tema"]][0])}</p></a>' for i, a in enumerate(top, 1))
    por_tema = lambda k: [a for a in arts if a["tema"] == k][:8]  # noqa: E731
    cuerpo = f"""{cabecera()}<main class="wrap"><section class="dest"><div class="dest-in"><a href="articulo.html">{img_tarjeta(d, ancho="(min-width:1000px) 680px, 100vw", lazy=False)}</a>
<div><span class="tag">Nueva guía · {e(TEMAS[d['tema']][0])}</span><h1 class="h">{e(d['titulo'])}</h1><p class="d">{e(d['desc'])}</p>
<a class="btn" href="articulo.html">Leer la guía · {d['min']}</a></div></div></section>
{fila("Lo último", arts[1:9])}
<section class="fila"><div class="fila-h"><h2 class="h">Lo más leído</h2></div><div class="carril">{ranking}</div></section>
<section class="fila"><div class="fila-h"><h2 class="h">Elige un tema</h2></div><div class="temas">{tiles}</div></section>
{fila("IA en tu ordenador", por_tema("local"))}
{NEWS}
{fila("Chatbots y asistentes", por_tema("chatbots"))}
</main>{PIE}{cookies(None)}"""
    return pagina("Decodifica · IA práctica en español", CSS, cuerpo, tema_oscuro=True)


def blog(arts, top):
    chips = '<div class="chips" style="margin:14px 0 4px">' + "".join(
        f'<a class="chip{" on" if i == 0 else ""}" href="#">{e(n)}</a>' for i, n in enumerate(["Todas"] + [n for n, _ in TEMAS.values()])) + "</div>"
    cuerpo = f"""{cabecera()}<main class="wrap"><header class="bh"><h1 class="h">Todas las guías</h1><p>{len(arts)} guías de IA práctica en español, con fuentes oficiales.</p>
<label class="buscar">{ICO_BUSCAR}<span>¿Qué quieres hacer con IA?</span></label>{chips}</header>
<div class="grid">{''.join(c(a, ancho="(min-width:1000px) 380px, (min-width:640px) 50vw, 100vw") for a in arts[:12])}</div>
<div style="display:flex;justify-content:center;margin-top:22px"><button class="btn" style="background:var(--sf);color:var(--ink);border:1px solid var(--line)">Ver {len(arts) - 12} guías más</button></div>
{NEWS}</main>{PIE}"""
    return pagina("Guías de IA práctica · Decodifica", CSS, cuerpo, tema_oscuro=True)


def articulo(arts, top):
    a = next(x for x in arts if x["slug"] == ART_SLUG)
    rel = [x for x in arts if x["tema"] == a["tema"] and x["slug"] != ART_SLUG][:6]
    toc = "".join(f'<li><a href="#{i}">{e(t)}</a></li>' for i, t in TOC)
    bmed = """<div class="bmed"><span><b>¿Te sirve esta guía?</b> Recibe una así cada sábado, gratis.</span><a class="btn" href="#">Apuntarme</a></div>"""
    puntos = "".join(f"<li><b>{e(k)}:</b> {e(v)}</li>" for k, v in PUNTOS)
    cuerpo = f"""{cabecera()}<div class="ah"><div class="wrap"><div class="cuerpo"><span class="tag">{e(TEMAS[a['tema']][0])}</span><h1 class="h">{e(a['titulo'])}</h1>
<p class="dek">{e(a['desc'])}</p><p class="meta">Por <b style="color:var(--ink)">Jordi Castañeira</b> · Revisado el 6 oct 2026 · {a['min']}</p>
<img class="cab" src="/public/og/blog/{ART_SLUG}-16x9-800.webp" width="800" height="450" alt="Logo de Claude" fetchpriority="high"></div></div></div>
<main class="wrap"><div class="cuerpo"><section class="rr"><p class="rr-t">Respuesta rápida</p><p>{RESPUESTA}</p><ul>{puntos}</ul></section>
<details class="toc"><summary>☰ En esta guía · {len(TOC)} apartados</summary><ol>{toc}</ol></details>
<div class="prosa">{cuerpo_articulo({'boletin_medio': bmed})}</div></div>
{fila("Sigue con esto", rel, "Más del tema →")}</main>{PIE}"""
    return pagina(a["titulo"], CSS, cuerpo, tema_oscuro=True)


def paginas(arts, top):
    return {"inicio": inicio(arts, top), "blog": blog(arts, top), "articulo": articulo(arts, top)}
