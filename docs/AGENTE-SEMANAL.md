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
   - Copiar la estructura técnica de un artículo reciente bueno (por ejemplo `crear-app-web-ias-chinas-open-source.astro` o `claude-skills-1000-gratis.astro`): `const title`, `description`, `pubDate` (hoy), `modifiedDate` (hoy), `readingTime`, `tags`, `pillar`, `pillarLabel`, `BaseLayout` con `modifiedDate`, cabecera, `ConversionBand`, newsletter, JSON-LD con `citation` igual a las fuentes.
   - Si no hay imagen OG propia, usar `ogImage="/og-default.png"` (no inventar rutas que no existen).
   - Título de 35 a 60 caracteres con la búsqueda al principio; descripción de 110 a 165 caracteres, concreta.
   - Al menos 3 secciones H2 útiles, al menos 2 fuentes externas originales y al menos 2 enlaces internos a páginas que existan.
   - Añadir enlaces desde 1-2 artículos existentes relacionados hacia el nuevo.
5. **Revisión SEO y editorial:** `python3 scripts/seo_preflight.py --changed`. Corregir todos los errores (✗). Revisar los avisos (·) y corregir los razonables.
6. **Mejorar títulos y descripciones** de hasta 3 páginas que salen en Google pero casi no reciben clics (paso 2). No cambiar URLs. Anotar en el informe el antes y el después y por qué.
7. **Un artículo antiguo por semana:** elegir uno que `python3 scripts/seo_preflight.py src/pages/blog/*.astro` marque con errores o que tenga datos desfasados, comprobar sus datos con fuentes oficiales y arreglarlo (con `modifiedDate` de hoy).
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

## Si Jordi contesta en la sesión

- «Sí»: fusionar el pull request (método merge) y comprobar que la publicación en GitHub Pages termina bien.
- Cambios: hacerlos en la misma rama, volver a pasar la revisión y el build, y avisar.

## Qué no hace el agente

- No toca `astro.config.mjs`, los workflows de GitHub, el aviso legal ni los datos personales de Jordi.
- No borra páginas con impresiones; si hay que fusionar, redirige con `return Astro.redirect('/destino/', 301);`.
- No añade enlaces de afiliado ni anuncios (eso lo decide Jordi más adelante y requiere NIF y domicilio en el aviso legal).
