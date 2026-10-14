# Agente semanal de Decodifica

Instrucciones para la rutina que se ejecuta cada lunes por la mañana (hora de España). Si cambian las reglas, se cambian aquí: la rutina lee este archivo en cada ejecución.

## Configuración

- **Publicar sola: NO.** Mientras diga NO, el agente abre un pull request y Jordi lo aprueba. Cuando Jordi diga que la calidad es buena, se cambia a SÍ y el agente fusiona su propio pull request si la revisión SEO y el build pasan sin errores.
- Nicho: **IA práctica en español** (herramientas, prompts, comparativas, guías de uso). Decidido por Jordi el 07-10-2026. La «casa autosuficiente» queda como idea para otra web: no escribir de eso aquí.
- Público: España y toda Latinoamérica (México, Perú, Colombia, Argentina, Chile, EE. UU. hispano). Español neutro.
- Artículos por semana: 2 (máximo 3 si hay demanda clara y fuentes sólidas). Mejor 2 buenos que 3 flojos.

## Reglas de la casa (no se rompen nunca)

1. Nada de relleno hecho con IA: cada párrafo aporta un dato, un paso o una decisión. Nada de frases vacías, listas de tres por costumbre ni conclusiones que repiten lo dicho.
2. Toda afirmación factual (precios, límites, funciones, fechas, cifras, licencias) sale de una fuente original abierta en esa misma ejecución (documentación oficial, página de precios, blog oficial, repositorio oficial). Se enlaza en «Fuentes». Si no se puede comprobar, no va, o se dice claramente que no está confirmado.
3. Nunca decir ni insinuar que Decodifica o Jordi lo ha probado si no hay una prueba documentada por Jordi. Prohibido «he probado», «lo uso a diario», «en mis pruebas». Las pruebas se proponen como pasos que hace quien lee.
4. Nada de titulares sensacionalistas ni falsas prisas.
5. Contenido que no caduque en semanas: guías, cómo se usa, cuándo conviene, alternativas. Las novedades solo si cambian cómo se usa algo, y escritas para que sigan sirviendo meses después. Precios y límites con «consultado en <mes> de <año>».
6. El antiguo canal de YouTube de Decodifica no existe: ni se enlaza ni se menciona. Tampoco `/comunidad/` ni `/login/`.
7. Ortografía y tildes correctas.

## Para que nos citen las IA

Reglas para que ChatGPT, Claude, Gemini, Perplexity y Copilot entiendan la web y la citen. Las siguen todos los agentes (lunes, jueves, novedades y repaso mensual) en cada artículo nuevo o revisado:

1. **Respuesta corta al principio.** El primer párrafo del artículo es `<p><strong>En resumen:</strong> …</p>` y responde en 2-4 frases a lo que busca la gente (qué es, cuánto cuesta, cómo se hace, cuál elegir). Con datos concretos, no con una introducción. La plantilla `<Articulo>` lo convierte sola en el recuadro «Respuesta rápida»: no hay que darle formato.
2. **Fecha visible.** La cabecera muestra «Publicado el …» y, si `modifiedDate` es distinta, «Revisado el …». Se cambia `modifiedDate` solo cuando se han vuelto a comprobar los datos, nunca para aparentar frescura.
3. **Datos estructurados.** No escribir bloques JSON-LD `Article` dentro del artículo: los genera `SEO.astro` a partir de `BaseLayout` (`type="article"`, `pubDate`, `modifiedDate`, `keywords`) y las fuentes se pasan en `citations={[...]}` con las mismas URLs de la sección «Fuentes». Si el artículo tiene preguntas frecuentes, usar el componente `FaqSection` (pinta las preguntas y su `FAQPage` con el mismo texto).
4. **llms.txt.** `/llms.txt` se genera solo en cada build con todos los artículos (`src/pages/llms.txt.ts`). Si se añade una sección nueva importante de la web (no un artículo), añadirla a mano en ese archivo.
5. **Robots.** No tocar `public/robots.txt` para bloquear robots de buscadores de IA (OAI-SearchBot, ChatGPT-User, Claude-SearchBot, Claude-User, PerplexityBot, Perplexity-User, Google-Extended, bingbot) sin que lo decida Jordi.
6. **/sobre/ dice la verdad.** La página explica que Jordi aprueba cada artículo antes de publicarlo. Si «Publicar sola» pasa a SÍ, cambiar esa frase en `src/pages/sobre.astro` en el mismo pull request.

## Pasos de cada lunes

1. **Ponerse al día.** Leer `_ESTADO.md`, este archivo y el último informe de `docs/informes/` (si existe).
2. **Leer Search Console.** El informe automático se genera los lunes a las 9:00 en `data/gsc_weekly/latest.json` (y `latest.md`). Si es de hoy, usarlo; si no, usar el último disponible y decirlo en el informe. Mirar:
   - búsquedas con impresiones y posición 4-20 (casi en primera página);
   - páginas con impresiones y CTR por debajo del 2 %;
   - búsquedas que no tienen una página que las responda (`query_pages` dice qué página sale).
3. **Elegir 2-3 temas** con demanda dentro del nicho:
   - Fuentes de demanda, por este orden: Search Console; `data/keyword-planner/` (datos del planificador de Google Ads); sugerencias de Google (`https://suggestqueries.google.com/complete/search?client=firefox&hl=es&gl=es&q=...`, también `gl=mx`, `gl=co`, `gl=ar`).
   - Antes de elegir, comprobar que no existe ya un artículo parecido en `src/pages/blog/` (títulos y slugs). Si existe, mejorarlo en vez de duplicarlo.
   - Preferir búsquedas con intención clara («cómo…», «qué es…», «mejor … para …», «alternativas a…», «… vs …») frente a búsquedas de marca sola.
4. **Escribir los artículos** como archivos `src/pages/blog/<slug>.astro`:
   - Slug corto, sin fecha, en minúsculas con guiones, con la búsqueda principal.
   - Copiar la estructura técnica de un artículo reciente bueno (por ejemplo `ollama-que-es-como-usar.astro` o `claude-skills-1000-gratis.astro`): `const title`, `description`, `pubDate` (hoy), `modifiedDate` (hoy), `readingTime`, `tema`, `tags`, `pillar`, `pillarLabel`, y `BaseLayout` con `modifiedDate` y `citations` (las URLs de «Fuentes»). Sin bloque JSON-LD `Article` propio (ver «Para que nos citen las IA»).
   - **Diseño (plantilla `<Articulo>`, ver «Cómo se escribe un artículo con el diseño nuevo» más abajo).** Todo el texto va dentro de `<Articulo slug="<slug>"> … </Articulo>`. La plantilla pinta sola el título, la entradilla, las fechas, la portada, el recuadro «Respuesta rápida», el índice, el boletín, los recursos y los artículos relacionados: **no** escribir `<header>`, `<h1>`, `<PortadaArticulo>`, `<ConversionBand>` ni formularios de newsletter dentro del artículo.
   - **Portada propia, siempre** (nunca `/og-default.png`). Seguir `docs/portadas.md`: añadir la entrada a `src/data/portadas.json` eligiendo la plantilla (`herramienta`, `lista` o `novedad`) y un gancho de 3-6 palabras pensado para el clic, distinto del título y que el artículo cumpla; descargar el logo de la web oficial si falta (`scripts/imagenes/logo.py`); generar con `python3 scripts/imagenes/portada.py <slug>`; mirar el resultado (`--muestra`) antes de seguir. En el artículo basta con `ogImage="/og/blog/<slug>.jpg"` en `BaseLayout`: `<Articulo>` pone la portada en la cabecera.
   - **2-3 imágenes útiles dentro del texto**, cada una junto al párrafo que explica: capturas de la web oficial (`scripts/imagenes/captura.py`: la página, el botón de descarga, los planes de precios) o esquemas propios (`scripts/imagenes/esquema.py`: pasos, gratis/de pago, cuadro resumen). Con `FiguraArticulo`, texto alternativo descriptivo y menos de 150 KB. Ningún dato en un esquema que no esté en el artículo con su fuente. Nada de imágenes generadas con IA ni de bancos de fotos.
   - Título de 35 a 60 caracteres con la búsqueda al principio; descripción de 110 a 165 caracteres, concreta.
   - Al menos 3 secciones H2 útiles, al menos 2 fuentes externas originales y al menos 2 enlaces internos a páginas que existan.
   - Añadir enlaces desde 1-2 artículos existentes relacionados hacia el nuevo.
5. **Revisión SEO y editorial:** `python3 scripts/seo_preflight.py --changed`. Corregir todos los errores (✗). Revisar los avisos (·) y corregir los razonables.
6. **Mejorar títulos y descripciones** de hasta 3 páginas que salen en Google pero casi no reciben clics (paso 2). No cambiar URLs. Anotar en el informe el antes y el después y por qué.
7. **Un artículo antiguo por semana:** elegir uno que `python3 scripts/seo_preflight.py src/pages/blog/*.astro` marque con errores o que tenga datos desfasados, comprobar sus datos con fuentes oficiales y arreglarlo (con `modifiedDate` de hoy). Si el artículo no empieza con un «En resumen:», añadírselo (ver «Para que nos citen las IA»). Si tiene menos de 2 imágenes dentro del texto, añadirle 2-3 (ver paso 4).
8. **Construir:** `npm ci` (si hace falta), `npm run type-check` y `npm run build`. Todo sin errores. Si falla, arreglarlo antes de seguir.
9. **Borradores para redes** en `docs/redes/<AAAA-MM-DD>.md`, uno por artículo nuevo:
   - Facebook: 2-4 frases y el enlace.
   - Bluesky: máximo 300 caracteres con el enlace.
   - Reddit: subreddit sugerido y un texto que aporte por sí mismo (no solo el enlace); avisar de que cada subreddit tiene sus normas sobre autopromoción.
   Jordi los publica a mano; el agente no publica en redes.
10. **Informe** en `docs/informes/<AAAA-MM-DD>.md`, en español sencillo, sin jerga:
    - cómo fue la semana en Google (impresiones, clics, posición; comparado con la semana anterior);
    - qué artículos nuevos y por qué esos temas (con el dato de demanda);
    - qué títulos se cambiaron;
    - fuentes usadas;
    - lo que no se pudo comprobar;
    - si hay algo que tenga que decidir Jordi.
11. **Entregar:**
    - Rama `agente/<AAAA-MM-DD>`, commits pequeños y claros, push.
    - Abrir un pull request (no borrador) hacia `main` con el resumen del informe en el cuerpo.
    - Si «Publicar sola» es NO: no fusionar.
    - Si es SÍ y preflight y build están en verde: fusionar.
    - Actualizar `_ESTADO.md` (sección «Agente semanal») con la fecha, el pull request y lo pendiente.
    - El último mensaje de la sesión es el resumen para Jordi, corto y sencillo, con el enlace al pull request y qué tiene que hacer: «Si te parece bien, pulsa Merge pull request en GitHub o contesta "sí" en esta conversación».

## Cómo se escribe un artículo con el diseño nuevo

Diseño «Revista luminosa», elegido por Jordi en octubre de 2026 (maquetas y capturas en `docs/rediseno/`). Esqueleto mínimo:

```astro
---
import BaseLayout from '../../layouts/BaseLayout.astro';
import Articulo from '../../components/Articulo.astro';
import FiguraArticulo from '../../components/FiguraArticulo.astro';
import Caja from '../../components/Caja.astro';

const title = "…";
const description = "…";
const pubDate = "AAAA-MM-DD";
const modifiedDate = "AAAA-MM-DD";
const readingTime = "8 min";
const tema = "local";   // chatbots | local | automatizar | oficina | crear (src/lib/temas.ts)
const tags = ["…"];
const pillar = "tips-productividad";
const pillarLabel = "Pilar 2: Tips productividad";
---

<BaseLayout title={title} description={description} ogImage="/og/blog/<slug>.jpg" type="article"
  pubDate={pubDate} modifiedDate={modifiedDate} section={pillarLabel} keywords={tags} citations={[ "…" ]}>
  <Articulo slug="<slug>">
    <p><strong>En resumen:</strong> …</p>
    <h2>Primer apartado</h2>
    …
    <h2 id="fuentes">Fuentes</h2>
    <ul>…</ul>
    <h2>Sigue leyendo</h2>
    <ul>…enlaces internos…</ul>
  </Articulo>
</BaseLayout>
```

- **Tema** (`const tema`): obligatorio. Decide en qué filtro de `/blog/` y en qué bloque de la portada sale, y qué artículos relacionados se muestran. Si ninguno encaja, `oficina`. Un tema nuevo se añade en `src/lib/temas.ts` (con uno de los colores de las portadas) solo si lo decide Jordi.
- **Títulos de apartado:** `<h2>` sencillos, escritos como tarea o pregunta («Cómo instalarlo», «¿Es gratis?»). La plantilla les pone el id y, si hay 5 o más, crea el índice («En esta guía»). El apartado de fuentes, con `id="fuentes"`: el boletín se coloca justo antes.
- **Cajas:** `<Caja tipo="consejo">…</Caja>` (verde), `<Caja tipo="ojo">…</Caja>` (ámbar, para límites, riesgos o cosas que cuestan dinero) y `<Caja tipo="nota">…</Caja>` (azul). Una o dos por artículo, cuando de verdad ayuden; no para repetir el texto.
- **Tablas:** `<div><table>…</table></div>` normal, con `<thead>`. En el móvil se deslizan solas y avisan de que hay más columnas.
- **Imágenes dentro del texto:** `FiguraArticulo` (ver `docs/portadas.md` §5).
- **Lo que ya no se escribe a mano:** cabecera con fechas, `<h1>`, `<PortadaArticulo>`, `<ConversionBand>`, el formulario de newsletter y el bloque «artículos anteriores y siguientes». Todo eso lo pone `<Articulo>`.
- «Lo más leído» de la portada se calcula solo con el último informe de Search Console (`src/lib/mas-leidos.ts`).
- `python3 scripts/seo_preflight.py` da error si falta `<Articulo slug=…>` o `const tema`.

## Repaso mensual (primer lunes de cada mes)

Además de los pasos de cada lunes:

1. **Imágenes en artículos antiguos, poco a poco:** añadir 2-3 imágenes dentro del texto (capturas oficiales o esquemas, ver `docs/portadas.md`) a 3-4 artículos que aún no las tengan (`python3 scripts/seo_preflight.py src/pages/blog/*.astro` los marca con el aviso «imágenes dentro del texto»), empezando por los que más impresiones tienen en Search Console.
2. **Portadas caducadas:** si un artículo usa la plantilla `novedad` y la función salió hace más de 30 días, cambiarla a `herramienta` y regenerar. Si cambió el logo o la web de una herramienta, volver a descargarlo y regenerar sus portadas.
3. **Comparar plantillas:** cuando Search Console tenga datos de Discover o de Imágenes (Rendimiento → Discover; tipo de búsqueda «Imagen»), comparar el CTR por plantilla y por tipo de imagen (logo, captura, número) y apuntar el resultado y la decisión en la tabla de `docs/portadas.md` §6. Con pocos datos, decirlo y no sacar conclusiones.

## Si Jordi contesta en la sesión

- «Sí»: fusionar el pull request (método merge) y comprobar que la publicación en GitHub Pages termina bien.
- Cambios: hacerlos en la misma rama, volver a pasar la revisión y el build, y avisar.

## Qué no hace el agente

- No toca `astro.config.mjs`, los workflows de GitHub, el aviso legal ni los datos personales de Jordi.
- No borra páginas con impresiones; si hay que fusionar, redirige con `return Astro.redirect('/destino/', 301);`.
- No añade enlaces de afiliado ni anuncios (eso lo decide Jordi más adelante y requiere NIF y domicilio en el aviso legal).
