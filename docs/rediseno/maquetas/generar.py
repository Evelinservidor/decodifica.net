"""Maquetas estáticas de las 3 propuestas de rediseño (fase 1).

Usa los artículos, portadas y datos de Search Console reales del repositorio.
No toca la web: escribe HTML en docs/rediseno/maquetas/<propuesta>/.

    python3 docs/rediseno/maquetas/generar.py
    python3 -m http.server 8765        # desde la raíz del repositorio
    python3 scripts/capturas_rediseno.py http://localhost:8765 docs/rediseno/a inicio=/docs/rediseno/maquetas/a/inicio.html
"""
import base
import propuesta_a
import propuesta_b
import propuesta_c

arts = base.articulos()
top = base.mas_leidos(arts)
for mod, nombre in ((propuesta_a, "a"), (propuesta_b, "b"), (propuesta_c, "c")):
    d = base.SALIDA / nombre
    d.mkdir(exist_ok=True)
    for pag, contenido in mod.paginas(arts, top).items():
        (d / f"{pag}.html").write_text(contenido)
    print(nombre, "ok")
