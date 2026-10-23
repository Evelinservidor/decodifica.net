# Estado del relanzamiento de Decodifica

Última actualización: 23 de octubre de 2026 (agente de novedades).
Este archivo sirve para que cualquier sesión siguiente sepa qué está hecho, qué falta y qué ha decidido Jordi. Actualízalo al terminar cada bloque de trabajo.

Repositorios:
- Web: `Evelinservidor/decodifica.net` (Astro + Tailwind, GitHub Pages detrás de Cloudflare, Plausible, newsletter en Buttondown).
- Estrategia y operaciones (privado, foto del 15-07-2026, solo como referencia de criterio): `Evelinservidor/decodifica-ops` (`_strategy/`, `_web/SEO-RULES.md`, `_web/scripts/seo_preflight.py`).

Reglas de la casa: nada de relleno hecho con IA, toda afirmación con fuente original comprobada, nunca decir que se ha probado algo sin haberlo probado, nada de titulares sensacionalistas ni falsas prisas. El antiguo canal de YouTube de Decodifica ya no existe: no se enlaza ni se menciona.

## Plan aprobado por Jordi

1. **Fase 1 · Dejar la web impecable** — **publicada el 06-10-2026** (pull request #6 fusionado; comprobado en línea).
2. **Fase 2 · Elegir el nicho con datos** — **hecha (07-10-2026)**: Jordi elige seguir con **IA práctica**. Datos y comparación en `docs/fase-2-nichos.md`. Antes de usar Semrush/Ahrefs/OpenRush hay que preguntar a Jordi si gastan créditos o son de pago.
3. **Fase 3 · Agente semanal** — en marcha: instrucciones en `docs/AGENTE-SEMANAL.md`, revisión SEO en `scripts/seo_preflight.py`. (rutina en la nube, lunes por la mañana, hora de España) — pendiente. Al principio abre un pull request y Jordi aprueba; más adelante, publicación automática.

## Plan SEO (18-10-2026)

Jordi aprobó el plan de posicionamiento: **`docs/plan-seo.md`** es el mapa de temas (grupos A Claude en español, B IA en tu
ordenador, C prompts y generador, D IA en casa sin nube como puente; nada de energía solar ni vida sin red, que irá a otra
web más adelante). Los agentes eligen el trabajo con él (paso 3 de `docs/AGENTE-SEMANAL.md`).
- Hecho: #19 el mapa · #20 los agentes lo siguen · #21 el informe de Google guarda también 28 y 90 días y qué páginas
  están en Google (`data/gsc_weekly/latest_28d.json`, `latest_90d.json`, `latest_indexacion.md`), los lunes a las 04:17 UTC ·
  #22 enlaces internos de cada grupo (la guía de Claude es la guía principal del grupo A).
- Espera a Jordi: **#23 limpieza** (35 páginas finas con noindex y 3 fusionadas con redirección; lista en `src/data/poda-seo.json`).
- Los 4 artículos de octubre no salen en Google: **no hay nada técnico que lo impida** (se abren bien, `index, follow`,
  canónica correcta, están en el sitemap, robots.txt permite todo). Search Console (18-10): `lm-studio-que-es-como-usar` y
  `n8n-que-es-gratis` «descubierta: actualmente sin indexar» (Google sabe que existen y aún no las ha leído);
  `claude-ia-que-es-gratis` y `ollama-que-es-como-usar` «Google no reconoce esta URL»: Google leyó el sitemap por última vez
  el 09-10-2026, antes de publicarlas. Es prioridad baja de Google para la web (lo que ataca el plan). Desde el 19-10-2026
  el robot tiene «Acceso total» en Search Console y el sitemap se reenvía solo después de cada publicación
  (`deploy.yml`, trabajo `avisar-google`). «Solicitar indexación» no tiene API: solo se pide a mano si un artículo lleva
  más de 14 días fuera de Google.
- Primera comparación por grupos (28 días contra 28 días): hacia el 21-12-2026.

## Fase 1: hecho

- Vídeos privados del canal antiguo quitados de 13 artículos (incrustados, tarjetas «ver el vídeo», párrafos y citas en JSON-LD). Se mantienen los vídeos públicos de terceros que se citan como fuente (PewDiePie, canales «IA PRACTICA» e «Inteligencia Artificial»).
- Enlaces al canal antiguo eliminados: pie de página, contacto, `sameAs` del JSON-LD, `site-config.ts`, `llms.txt`. La página `/decodifica/` (canal de YouTube) redirige a `/sobre/`.
- Comunidad y registro (Supabase ya no existe): `/comunidad/`, `/comunidad/hilo/` y `/login/` redirigen a `/newsletter/`; fuera del menú, del pie y de las llamadas a la acción; borrado `public/auth/` (configuración del proyecto Supabase muerto); privacidad y cookies sin cuentas ni comunidad.
- Tres páginas «sobre nosotros» → una: `/sobre/` reúne quién está detrás + método editorial; `/quienes-somos/` y `/decodifica/` redirigen allí.
- Tildes restauradas en ~950 palabras de 48 archivos (textos visibles, sin tocar código ni URLs) y en encabezados («Qué cambia», «Por qué importa»…).
- Portada: el contador de workflows dice el número real (5).
- Sitemap: lleva `lastmod` en los artículos (fecha de `modifiedDate` o, si no hay, `pubDate`) y excluye las páginas que solo redirigen.
- Quitado el bloque genérico «TL;DR / Decisión rápida» que se repetía idéntico en 14 artículos.
- Generador de prompts: título orientado a la búsqueda («Generador de prompts gratis y sin registro»). Blog: título «Guías de IA práctica en español». Quitado `<main>` anidado en 5 páginas.
- Informe semanal de Search Console: el fallo era el token OAuth caducado (error 400 en `oauth2.googleapis.com/token`). El script ya acepta una **cuenta de servicio** (`GSC_SERVICE_ACCOUNT_JSON`), que no caduca. **Falta que Jordi cree la cuenta y guarde el secreto** (guía abajo).

## Fase 1: hecho (segunda parte)

- Fusiones con redirección (la página que se queda está reescrita con fuentes oficiales consultadas el 06-10-2026):
  - Claude Skills: `claude-skills-desde-cero` → `claude-skills-1000-gratis` («Claude Skills gratis: qué son, cómo instalarlas y crearlas»). Se quitó «+1.000» del título (no verificable).
  - NotebookLM: `notebooklm-google-openai` → `notebooklm-guia-2026`. **NotebookLM se llama «Gemini Notebook» desde el 16-07-2026** (notebooklm.google redirige a notebook.google); la guía usa ambos nombres.
  - IA gratis: `ia-gratis-silicon-valley` → `alternativas-gratis-chatgpt-2026` (7 asistentes; Le Chat ahora es «Mistral Vibe», chat de Qwen ahora es «Qwen Studio»). `5-atajos-ia-gratis` y `odysseus-pewdiepie-ia-gratis` se quedan (búsquedas distintas).
  - IA china: `glm-52-kimi-coinbase` y `prompts-chinos-abiertos` → `deepseek-app-oficial-espanol` («DeepSeek, Qwen y Kimi en español: cómo usarlos gratis»).
- «emergent ia»: `crear-app-web-ias-chinas-open-source` reescrito («Emergent IA: qué es, precios y cómo crear una app»); la URL se mantiene.
- Limpieza de texto de plantilla, primera persona sin respaldo y restos de guion de vídeo en 12 artículos; descripciones nuevas (ninguna termina en «...»); `modifiedDate` 2026-10-06 en todo lo reescrito.
- `alternativas-fable-5`: la suspensión de Fable 5 (12-06-2026, directiva de exportación de EE. UU.) y su vuelta (01-07-2026) están confirmadas en anthropic.com/news; el artículo lo cuenta con esas fuentes.
- Enlaces internos apuntan directamente a las guías fusionadas. Comprobado: 0 enlaces internos rotos en la web construida.
- Quitadas las últimas referencias a «vídeos» del canal antiguo en portada, recursos y newsletter.

## Portadas e imágenes (14-10-2026, rama `agente/portadas-ctr`)

- Investigación de qué imágenes traen clics y qué piden Google y las redes: `docs/portadas.md`. Clave: Google pide evitar imágenes con mucho texto en Discover/Imágenes, así que cada portada tiene una versión con gancho (redes y blog) y otra limpia (datos estructurados y cabecera del artículo).
- Sistema propio en `scripts/imagenes/` (Python + Pillow + Chromium sin pantalla, funciona en la nube): `portada.py` (3 plantillas: herramienta, lista, novedad), `logo.py` (logos de webs oficiales, fuentes en `logos/FUENTES.md`), `captura.py` (capturas de webs oficiales), `esquema.py` (pasos, comparativa, resumen). Fuentes Inter (OFL) en el repositorio. Datos de cada portada en `src/data/portadas.json`.
- 32 artículos con portada nueva; borradas las portadas negras antiguas (27 MB de PNG) y los scripts de Windows. `max-image-preview:large` en todas las páginas indexables.
- Imágenes dentro del texto en los 5 artículos con más impresiones: Claude Skills (3), DeepSeek/Qwen/Kimi (3), IA para Excel (2), organizar pendientes (2), Google Maps con Gemini (2).
- Velocidad (móvil, conexión lenta simulada): la cabecera de los artículos pasa de 0,9-1,7 MB (PNG) a 12-18 KB (WebP) y el LCP de 5-9 s a menos de 1 s en los artículos que la tenían.
- Pendiente: logos que las webs bloquean (chatgpt.com, Emergent, SlidesAI): ChatGPT usa el logo de OpenAI de su cuenta oficial de GitHub. Comparar plantillas cuando haya datos de Discover/Imágenes (repaso mensual).

## Rediseño de la web (14-10-2026, rama `agente/rediseno`, pull request #14)

- Jordi eligió entre 3 propuestas la **A, «Revista luminosa»**: fondo claro, las portadas ponen el color, con modo oscuro opcional. Maquetas, investigación, capturas y comprobaciones en `docs/rediseno/README.md`.
- Plantilla común de los artículos `src/components/Articulo.astro`: cabecera, «Respuesta rápida» (a partir del «En resumen:»), índice, boletín antes de las fuentes, recursos, autor y relacionados con portada. Cajas `Caja.astro` (consejo, ojo y nota). Cada artículo lleva `const tema` (`src/lib/temas.ts`). «Lo más leído» sale de Search Console (`src/lib/mas-leidos.ts`).
- Se cambió `docs/AGENTE-SEMANAL.md` («Cómo se escribe un artículo con el diseño nuevo») y `scripts/seo_preflight.py` da error si falta `<Articulo>` o `tema`.
- SEO idéntico (títulos, descripciones, datos estructurados, sitemap, `llms.txt` y robots); 0 problemas de accesibilidad; LCP en el móvil por debajo de 0,75 s.
- Pendiente: que Jordi lo apruebe y se fusione (con «Publicar sola: NO» no se fusiona solo). Faltan resúmenes en 4 artículos (`2026-07-17-hermes-agent-chino`, `2026-07-22-nano-banana-1000-prompts`, `5-atajos-ia-gratis` y `gpt-live-voz-chatgpt`); que los añada el agente semanal con fuentes.

## Imágenes en todos los artículos (14-10-2026, rama `agente/imagenes-todos`)

- Los 27 artículos que eran solo texto llevan ya 2-3 imágenes dentro (73 nuevas: capturas de webs oficiales y esquemas propios). Ya las tienen todos los artículos del blog.
- Velocidad igual (LCP medio en móvil de 780 a 784 ms con el diseño nuevo). Revisión SEO y build sin errores.
- Datos que ya no coincidían con las webs oficiales y lo que no se pudo capturar: `docs/informes/2026-10-14-imagenes.md`. Lo revisa el repaso mensual (`docs/AGENTE-SEMANAL.md`, que ya no pide añadir imágenes poco a poco, sino mantener las capturas al día).

## Pendiente

- [x] Jordi aprueba publicar la Fase 1 (06-10-2026); pull request #6 fusionado (https://github.com/Evelinservidor/decodifica.net/pull/6). Al fusionar a `main` se publica solo.
- [x] Informe de Search Console arreglado (06-10-2026). La organización de Google de Jordi bloquea crear claves (`iam.disableServiceAccountKeyCreation`), así que se usa **federación de identidades de GitHub sin claves**: proyecto `decodifica-informes-510822` (número 979898982695), pool `github`, proveedor `decodifica` (solo admite el repositorio Evelinservidor/decodifica.net), robot `informe-gsc@decodifica-informes-510822.iam.gserviceaccount.com` con permiso «Restringido» en Search Console. Probado: el informe de 28 días se generó y se subió a `data/gsc_weekly/`. Los 4 blogs de Blogspot que también lista `GSC_SITE_URLS` dan error porque el robot no tiene permiso en ellos (no hace falta para Decodifica).
- [ ] El informe solo guarda las 20 consultas principales; ampliarlo para la Fase 2 y el agente semanal.
- [ ] NotebookLM → «Gemini Notebook»: revisar la ficha `/herramientas/notebooklm/` (`src/data/tools.ts`) y la comparativa `/herramientas/notebooklm-vs-perplexity/` (nombre y límites).
- [ ] `chatgpt-work-archivos-a-entregables` y `gpt-live-voz-chatgpt`: las webs de OpenAI devolvieron 403 al consultarlas; la premisa de ChatGPT Work («presenta un plan antes de ejecutar») está sin verificar. Revisar cuando se pueda abrir la fuente.
- [ ] Aviso legal sin NIF ni domicilio: obligatorio (LSSI) antes de anuncios o afiliados. **Pedírselo a Jordi cuando toque monetizar; no inventarlo.**
- [ ] Revisión de fuentes del resto de artículos antiguos no reescritos (`ia-mejora-excel`, `ia-crea-presentaciones-completas`, `ia-organiza-pendientes`, `crear-agente-voz-ia-sin-programar`, `claude-emails-sonar-humanos`, `odysseus-pewdiepie-ia-gratis`, `qwen-code-agent-terminal`, `ia-resumir-reuniones-tareas-revisables`, `2026-07-28-higgsfield-davinci-plugin-ia`, `2026-08-01-qwen3-asr-transcribe-espanol`, `como-elegir-herramienta-ia`): tarea continua del agente semanal (Fase 3).
- [ ] Fase 2 (nicho con datos): antes de usar Semrush/Ahrefs/OpenRush, preguntar a Jordi si gastan créditos. Jordi confirma que sus cuentas de Semrush, Ahrefs y OpenRush son gratuitas, sin tarjeta: se pueden usar, aceptando los límites del plan gratis. Nota: Ahrefs respondió «Insufficient plan» a la consulta de uso; OpenRush no tiene Search Console conectado.

### Decisiones técnicas tomadas

- Las fechas del nombre de archivo de 10 artículos (p. ej. `2026-07-16-prompts-secretos-web`) no cuadran con `pubDate`. El `pubDate` es el correcto (coincide con el día en que se subió). **No se renombran las URLs** porque ya tienen impresiones; a partir de ahora los artículos nuevos no llevan fecha en el nombre del archivo.
- Redirecciones: GitHub Pages no tiene redirecciones de servidor. Se usa `return Astro.redirect('/destino/', 301)` en el `.astro`, que genera una página con `meta refresh`, `noindex` y `canonical` al destino (igual que `/recursos-ia/`). El sitemap excluye automáticamente cualquier artículo que sea una redirección.
- Para que el sitemap marque un artículo como actualizado, añade en su frontmatter `const modifiedDate = "AAAA-MM-DD";` y pásalo a `BaseLayout` (`modifiedDate={modifiedDate}`).

## Guía antigua (no aplicable: la organización bloquea las claves; ver arriba la solución aplicada)

1. Entra en Google Cloud con tu cuenta de Google y crea un proyecto (o usa el que ya tenías para la app OAuth): https://console.cloud.google.com/projectcreate — nombre, por ejemplo, «decodifica-informes».
2. Activa la API de Search Console en ese proyecto: https://console.cloud.google.com/apis/library/searchconsole.googleapis.com → botón **Habilitar**.
3. Crea una cuenta de servicio: https://console.cloud.google.com/iam-admin/serviceaccounts/create → nombre «informe-gsc» → **Crear y continuar** → no hace falta darle roles → **Listo**.
4. Abre la cuenta de servicio recién creada → pestaña **Claves** → **Agregar clave** → **Crear clave nueva** → **JSON** → se descarga un archivo `.json`. Guárdalo en lugar seguro y no lo compartas. Copia también el correo de la cuenta (termina en `@...iam.gserviceaccount.com`).
5. En Search Console, añade ese correo como usuario de la propiedad de decodifica.net: https://search.google.com/search-console/users → elige la propiedad `decodifica.net` → **Añadir usuario** → pega el correo → permiso **Restringido** (basta para leer datos).
6. En GitHub, guarda el contenido del archivo como secreto: https://github.com/Evelinservidor/decodifica.net/settings/secrets/actions/new → nombre `GSC_SERVICE_ACCOUNT_JSON` → pega el contenido completo del `.json` → **Add secret**.
7. Lanza el informe a mano para comprobarlo: https://github.com/Evelinservidor/decodifica.net/actions/workflows/weekly-gsc-report.yml → **Run workflow**. Si sale en verde, a partir de ahí se ejecuta solo cada lunes a las 9:00 (hora de España).

Si en el paso 4 Google dice que la creación de claves está bloqueada por una política de la organización, la alternativa es pasar la app OAuth a «producción» (https://console.cloud.google.com/auth/audience → **Publicar app**) y regenerar `GSC_REFRESH_TOKEN`.

## Decisiones de Jordi
- (14-10-2026) Cloudflare sigue bloqueando los robots de entrenamiento (GPTBot, ClaudeBot); los de búsqueda de IA pueden entrar. El correo hola@decodifica.net funciona.
- (07-10-2026) Nicho: **opción 2, solo IA práctica**. La «casa autosuficiente» (solar aislada, baterías, domótica, IA en casa) queda como propuesta para más adelante, posiblemente en una **web nueva aparte**. Datos en `docs/fase-2-nichos.md`.
- (06-10-2026) Publicar la Fase 1: sí.
- (06-10-2026) Apellido: **Castañeira** (con ñ). Corregido en toda la web.
- (06-10-2026) Redes activas: Facebook, Bluesky y Reddit (nadie publica en ellas). TikTok fuera de la web. Idea para la Fase 3: un agente programado que proponga publicaciones para esas redes a partir de los artículos (mismo esquema: propone, Jordi aprueba).
- (06-10-2026) PDF de Claude Skills: rehacerlo. Hecho: `public/lead-magnets/claude-skills-desde-cero.pdf` (5 páginas) generado con `lead-magnets/gen_claude_skills_pdf.py` a partir de la guía verificada; enlazado desde la guía y desde /recursos/.
- (06-10-2026) Semrush, Ahrefs y OpenRush: cuentas gratuitas, sin pago.

- (06-10-2026) Aprueba el plan de tres fases. El dinero, después: afiliados y producto propio antes que anuncios.

## Fase 2: notas

- (06-10-2026) Las cuentas gratuitas no dan datos de palabras clave por API:
  - Semrush: `no_api_units` (la cuenta no tiene unidades de API).
  - Ahrefs: «Insufficient plan».
  - OpenRush: «Insufficient credits» (402).
- Fuentes gratuitas que sí sirven:
  1. **Search Console de Decodifica** (en cuanto Jordi configure la cuenta de servicio): demanda real de lo que ya cubre la web.
  2. **Planificador de palabras clave de Google Ads** (gratis con una cuenta de Google Ads, sin campañas activas): volumen por rangos y puja (CPC) por país. Necesita que Jordi lo abra con su cuenta o comparta los resultados.
  3. **Autocompletado de Google** (funciona desde aquí, sin volumen): para listar qué se busca en cada nicho y país.
  4. Revisión manual de quién ocupa los primeros resultados (competencia) y de los programas de afiliados públicos (dinero por visita).

## Para que nos citen las IA (14-10-2026)

Rama `agente/para-las-ia`. Reglas nuevas para los agentes en `docs/AGENTE-SEMANAL.md` («Para que nos citen las IA»).

- `public/robots.txt`: permiso explícito a Googlebot, bingbot, Google-Extended, OAI-SearchBot, ChatGPT-User, Claude-SearchBot, Claude-User, PerplexityBot y Perplexity-User (nombres comprobados en las páginas oficiales de Google, OpenAI, Anthropic, Perplexity y Bing).
- **Cloudflare** devuelve 403 a GPTBot y ClaudeBot (robots que recogen textos para entrenar modelos); los robots de búsqueda de IA sí entran (comprobado con su identificador el 14-10-2026). Es un ajuste de Cloudflare, no del repositorio. Jordi decide dejarlo así (14-10-2026).
- `/llms.txt` se genera en cada build (`src/pages/llms.txt.ts`) con qué es Decodifica, para quién, cómo se hace y todos los artículos. Se borró el `public/llms.txt` antiguo (mencionaba el canal y los vídeos).
- Datos estructurados: un único `Article` por página, generado en `SEO.astro` (autor Jordi Castañeira con enlace a /sobre/, fechas de publicación y revisión, imagen, editor con logo, fuentes en `citation`). Se quitaron los bloques `Article` duplicados de 33 artículos y 5 páginas de herramientas/recursos. `Organization` y `WebSite` solo en la portada; `AboutPage` + `Person` en /sobre/. Componente `FaqSection` para preguntas frecuentes con `FAQPage` (añadido en 4 artículos). Validador de schema.org: 93 páginas, 0 errores, 0 avisos. La prueba de resultados enriquecidos de Google no se pudo pasar desde aquí.
- Cabecera de todos los artículos: «Publicado el …» y, si cambió, «Revisado el …».
- «En resumen:» añadido al principio de alternativas-fable-5, ia-resumir-reuniones, deepseek-app-oficial-espanol, kimi-k3, prompts-secretos-web y chatgpt-work; «TL;DR» → «En resumen» y «FAQ» → «Preguntas frecuentes».
- /sobre/: sección «Cómo se hace cada artículo» (fuentes oficiales, fecha de consulta, IA para borradores y Jordi aprueba, precios revisados cada mes).
- `scripts/seo_preflight.py` avisa si falta la respuesta corta, la fecha de revisión o `citations`, y da error si un artículo vuelve a meter su propio bloque `Article`.
- Pendiente: respuesta corta en `2026-07-17-hermes-agent-chino`, `2026-07-22-nano-banana-1000-prompts`, `5-atajos-ia-gratis` y `gpt-live-voz-chatgpt` (empiezan bien, pero sin «En resumen:»). `ia-organiza-pendientes` sigue con un «caso real» en primera persona sin prueba documentada (solo se quitaron las dos frases prohibidas): reescribirlo es el siguiente arreglo semanal. `2026-08-01-qwen3-asr-transcribe-espanol` dice «Probamos» en la descripción: revisar si hay prueba documentada.
- Respondido por Jordi (14-10-2026): el correo hola@decodifica.net funciona; el bloqueo de Cloudflare a GPTBot y ClaudeBot se queda como está.

## Agente semanal

- Rutina en la nube cada lunes (hora de España), después del informe de Search Console de las 9:00. Sigue `docs/AGENTE-SEMANAL.md`.
- Modo actual: **propone y Jordi aprueba** (pull request). Pasar a «Publicar sola: SÍ» cuando Jordi lo diga.
- Decisión de Jordi (07-10-2026): los arreglos pendientes de la web publicada los hace el agente, **uno por semana**.
- Cola de arreglos para el agente (el preflight los marca): ~~`claude-emails-sonar-humanos`~~ (hecho el 07-10-2026), ~~`crear-agente-voz-ia-sin-programar`~~ (hecho el 12-10-2026), `ia-organiza-pendientes` (las frases prohibidas se quitaron el 14-10-2026; falta reescribir el «caso real» en primera persona sin prueba documentada). Después: ficha `/herramientas/notebooklm/` y comparativa `/herramientas/notebooklm-vs-perplexity/` (nombre nuevo «Gemini Notebook» y límites), y la revisión de fuentes de los artículos antiguos no reescritos.

### Ejecuciones

- **07-10-2026 (prueba, miércoles):** rama `agente/2026-10-07`, pull request #10 aprobado y publicado por Jordi el 07-10-2026 (comprobado en línea). Artículos nuevos: `lm-studio-que-es-como-usar` y `n8n-que-es-gratis`. Arreglado `claude-emails-sonar-humanos`. Títulos nuevos en `/herramientas/notebooklm-vs-perplexity/` y `/herramientas/gamma-vs-canva-ai/`. Informe: `docs/informes/2026-10-07.md`; redes: `docs/redes/2026-10-07.md`.
  - Pendiente: precio mensual (no anual) de n8n sin confirmar; revisar dentro de unas semanas si «Emergent IA» y «DeepSeek, Qwen y Kimi» empiezan a recibir clics; idea para más adelante: mejorar el artículo de Nano Banana para «prompts para Gemini fotos» (mucha demanda en Latinoamérica).
- **12-10-2026:** rama `agente/2026-10-12`. Artículos nuevos: `claude-ia-que-es-gratis` y `ollama-que-es-como-usar`. Arreglado `crear-agente-voz-ia-sin-programar` (precios actualizados; título nuevo). Sin cambios de títulos por falta de datos nuevos. Informe: `docs/informes/2026-10-12.md`; redes: `docs/redes/2026-10-12.md`.
  - El informe de Search Console del lunes no se había generado a las 11:52 (retraso de las tareas programadas de GitHub). Si se repite, valorar mover la rutina del agente más tarde o lanzar el informe a mano.
  - Pendiente: precio de la API Realtime de OpenAI (openai.com da 403).
- **16-10-2026 (agente de novedades):** rama `agente/novedad-2026-10-16`. Novedad: GPT-Live-1.1 y voces en español de México en la voz de ChatGPT (15-10-2026), añadida como sección al artículo `gpt-live-voz-chatgpt` (título, descripción y portada `novedad` nuevos). Nota: `docs/novedades/2026-10-16.md`. Las páginas de ayuda de OpenAI se abren con el navegador sin pantalla (Chromium de Playwright) aunque con curl den 403. Ideas para el lunes: GPT-6 en ChatGPT gratis (07-10-2026) y Gemini 4 Argon (13-10-2026, solo Pro/Ultra).
- **19-10-2026 (semana 1 del plan SEO):** rama `agente/2026-10-19`, pull request #27 (espera a Jordi). Pilar A rehecho: `claude-ia-que-es-gratis` → «Claude en español: guía completa, gratis y planes» (países, límites, planes al día, Proyectos, memoria, conectores, cómo pedirle las cosas, FAQ; portada nueva). Mejora y artículo antiguo de la semana: `claude-emails-sonar-humanos` (resumen cortado arreglado, fuentes revisadas). Título nuevo de `/sobre/`. Informe: `docs/informes/2026-10-19.md`.
  - Pendiente: Emergent cayó de 153 apariciones a 0 en 28 días (decide Jordi). Semana que viene: pilar B (IA local en español) y guía del generador (pilar C). Sigue en la cola de arreglos `ia-organiza-pendientes`.
- **20-10-2026 (repaso mensual):** rama `agente/mensual-2026-10`. Excel rehecho sin `=COPILOT()` (retirada el 14-09-2026; ahora con el panel de Copilot); pasos de ChatGPT con Calendar y Notion en `ia-organiza-pendientes` corregidos a lo que confirma OpenAI (y quitado «mis pruebas»); precios de `ia-crea-presentaciones-completas` al día; 4 enlaces externos rotos arreglados. Informe: `docs/repaso-mensual/2026-10.md`.
  - Pendiente: tutorial de Gamma 5, resto de `ia-organiza-pendientes` (Manus, Gemini, Claude, Copilot), noindex de 3 páginas sin apariciones en 90 días (Emergent, Higgsfield, 5 atajos; aprobado por Jordi el 20-10-2026, rama `seo/noindex-sin-apariciones`).
- **22-10-2026 (agente de los jueves, primer repaso):** rama `agente/jueves-2026-10-22`, pull request #32 (espera a Jordi). Ningún artículo del blog se podía tocar (todos cambiaron título o descripción desde el 06-10; los del 06-10 se pueden tocar desde el 29-10). Títulos, descripciones, preguntas frecuentes y enlaces nuevos en tres páginas de herramientas: Manus vs ChatGPT, ficha de Kimi y ficha de Qwen Code (las plantillas de fichas y comparativas aceptan ahora título propio, preguntas, fuentes y «Sigue leyendo»). Repaso: `docs/repaso-jueves/2026-10-22.md`.
  - Medir hacia el 30-11-2026. Pendiente: ver si los títulos del 07-10 (Gamma vs Canva, NotebookLM vs Perplexity) funcionan cuando el informe de 28 días cubra solo el título nuevo.
- **23-10-2026 (agente de novedades):** rama `agente/novedad-2026-10-23`, pull request #33 (espera a Jordi). Novedad: Claude Duet (21-10-2026, solo EE. UU., Pro y Max con lista de espera), añadida como sección a la guía `claude-ia-que-es-gratis` (respuesta corta, captura, qué hace, precio, cómo probarlo, pregunta frecuente; `modifiedDate` 23-10) con enlace desde `ia-organiza-pendientes`. Nota: `docs/novedades/2026-10-23.md`. Para el lunes: dato de Agent Skills en la Agentic AI Foundation (22-10) para `claude-skills-1000-gratis`.
