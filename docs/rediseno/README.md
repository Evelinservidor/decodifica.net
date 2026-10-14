# Rediseño de Decodifica · Fase 1: propuestas

Octubre de 2026. Tres propuestas para la página principal, la lista del blog y la página de artículo, pensadas para lucir las portadas nuevas (pull request #13, `docs/portadas.md`). **Todavía no cambia nada de la web publicada**: son maquetas con los artículos, portadas y datos de Search Console reales.

## Qué falla hoy (móvil)

![Primera pantalla del móvil: hoy y las tres propuestas](comparativa-inicio-movil.webp)

- Arriba sale un texto abstracto («Convierte una tarea repetitiva en un workflow de IA…») y un botón: ningún artículo ni ninguna portada en la primera pantalla. El primer enlace a un artículo aparece a 4.340 px de altura (unas cinco pantallas más abajo) y la portada no tiene ni una imagen.
- Muchas cajas oscuras iguales con letra pequeña: parece una aplicación, no una revista.
- El aviso de cookies mide 207 px de alto: una cuarta parte de la pantalla, justo encima del botón principal.
- En el artículo, la portada queda tapada por el aviso, y el «En resumen» se pierde como un párrafo más.

## Las tres propuestas

Las tres comparten lo importante: **un artículo con su portada en la primera pantalla**, temas para navegar, «Lo más leído» (con los datos de Search Console), buscador, y en el artículo un recuadro de **respuesta rápida**, índice, tablas que se deslizan, cajas de consejo y «ojo», boletín a mitad del texto sin ventanas que molesten y artículos relacionados con portada. Y un **aviso de cookies pequeño** con «Rechazar» y «Aceptar» del mismo tamaño y estilo.

| | A · Revista luminosa | B · Escaparate oscuro | C · Guía de bolsillo |
|---|---|---|---|
| Fondo | Claro (con modo oscuro opcional) | Oscuro, como ahora | Claro, color papel |
| Primera pantalla del móvil | El último artículo con su portada grande | El último artículo con su portada grande y un botón «Leer la guía» | Un buscador «¿Qué quieres hacer con IA?» y atajos por tarea |
| Lista de artículos | Tarjetas grandes con portada | Filas que se deslizan con el dedo (como Netflix o YouTube) | Lista compacta: portada pequeña a la izquierda y título |
| Lectura | Letra sin serifa, 18 px, 700 px de ancho máximo, índice a la izquierda en ordenador | Letra clara sobre fondo oscuro, 18 px, índice que se queda fijo arriba al bajar | Letra con serifa (tipo libro), 19 px, índice y boletín a la derecha en ordenador |
| Parecido a | Xataka, The Verge, revistas | Plataformas de vídeo | Zapier, How-To Geek, manuales |

### A · Revista luminosa (recomendada)

| Inicio | Blog | Artículo |
|---|---|---|
| ![](propuesta-a/inicio-movil-pantalla.webp) | ![](propuesta-a/blog-movil-pantalla.webp) | ![](propuesta-a/articulo-movil-pantalla.webp) |

Ordenador: [inicio](propuesta-a/inicio-ordenador.jpg) · [blog](propuesta-a/blog-ordenador.jpg) · [artículo](propuesta-a/articulo-ordenador.jpg) · [artículo en modo oscuro](propuesta-a/articulo-oscuro-ordenador.jpg). Móvil completo: [inicio](propuesta-a/inicio-movil.jpg) · [blog](propuesta-a/blog-movil.jpg) · [artículo](propuesta-a/articulo-movil.jpg) · [artículo en modo oscuro](propuesta-a/articulo-oscuro-movil.jpg).

### B · Escaparate oscuro

| Inicio | Blog | Artículo |
|---|---|---|
| ![](propuesta-b/inicio-movil-pantalla.webp) | ![](propuesta-b/blog-movil-pantalla.webp) | ![](propuesta-b/articulo-movil-pantalla.webp) |

Ordenador: [inicio](propuesta-b/inicio-ordenador.jpg) · [blog](propuesta-b/blog-ordenador.jpg) · [artículo](propuesta-b/articulo-ordenador.jpg). Móvil completo: [inicio](propuesta-b/inicio-movil.jpg) · [blog](propuesta-b/blog-movil.jpg) · [artículo](propuesta-b/articulo-movil.jpg).

### C · Guía de bolsillo

| Inicio | Blog | Artículo |
|---|---|---|
| ![](propuesta-c/inicio-movil-pantalla.webp) | ![](propuesta-c/blog-movil-pantalla.webp) | ![](propuesta-c/articulo-movil-pantalla.webp) |

Ordenador: [inicio](propuesta-c/inicio-ordenador.jpg) · [blog](propuesta-c/blog-ordenador.jpg) · [artículo](propuesta-c/articulo-ordenador.jpg). Móvil completo: [inicio](propuesta-c/inicio-movil.jpg) · [blog](propuesta-c/blog-movil.jpg) · [artículo](propuesta-c/articulo-movil.jpg).

Hoy: [inicio](antes/inicio-movil.jpg) · [blog](antes/blog-movil.jpg) · [artículo](antes/articulo-movil.jpg) (móvil, página completa).

Comparativas de la primera pantalla en el móvil: [inicio](comparativa-inicio-movil.webp) · [blog](comparativa-blog-movil.webp) · [artículo](comparativa-articulo-movil.webp).

## Por qué recomendamos la A

INVESTIGACION_RECOMENDACION

## Lo que se ha aprendido de otras webs

INVESTIGACION_PATRONES

## Qué se haría en la fase 2 (con la propuesta elegida)

- Mismas direcciones de todas las páginas; títulos, descripciones, datos estructurados, `llms.txt`, robots, sitemap y enlaces internos sin tocar.
- Componentes nuevos para los artículos: `RespuestaRapida` (el recuadro, que mantiene el párrafo «**En resumen:**» que piden las reglas para las IA), `Indice`, `Caja` (consejo / ojo / nota), `Tabla` (se desliza en el móvil) y `BoletinEnTexto`. Se aplican a los 32 artículos y se explican en `docs/AGENTE-SEMANAL.md`.
- Temas: un campo `tema` en cada artículo (5 temas: Chatbots y asistentes, IA en tu ordenador, Agentes y automatización, Trabajo y día a día, Imagen, vídeo y webs). Se filtran en `/blog/` sin crear páginas nuevas.
- «Lo más leído» se calcula solo en cada build con el último informe de Search Console (`data/gsc_weekly/latest.json`).
- Buscador: un índice pequeño (título, descripción y temas de cada guía) que se busca en el propio navegador; sin servicios externos.
- Velocidad: la letra de los titulares (Inter Display, la de las portadas) se sirve desde la propia web y solo en el peso que se usa; el texto, con la letra del sistema. La portada del primer artículo se carga la primera; el resto, al bajar.
- Aviso de cookies: se mantiene el mismo funcionamiento (Plausible solo si se acepta, «Configurar» para elegir), solo cambia el aspecto y el tamaño.
- Accesibilidad: contraste AA en textos, botones y zonas de toque de 44 px o más, foco visible, modo claro/oscuro.

## Cómo se hicieron las maquetas y capturas

```bash
python3 docs/rediseno/maquetas/generar.py                 # crea docs/rediseno/maquetas/{a,b,c}/*.html
python3 -m http.server 8765 &                              # desde la raíz del repositorio
python3 scripts/capturas_rediseno.py http://localhost:8765 docs/rediseno/propuesta-a \
    inicio=/docs/rediseno/maquetas/a/inicio.html blog=/docs/rediseno/maquetas/a/blog.html articulo=/docs/rediseno/maquetas/a/articulo.html
```

`capturas_rediseno.py` sirve también para la web de verdad (`npm run build && npx astro preview` y `http://localhost:4321`): guarda la primera pantalla (`-pantalla.webp`) y la página entera (`.jpg`) a 390 px y 1280 px.

El texto del artículo de ejemplo es un resumen del artículo real de Claude Skills; los temas de cada artículo son una propuesta.
