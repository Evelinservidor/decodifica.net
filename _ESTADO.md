# Estado del relanzamiento de Decodifica

Última actualización: 7 de octubre de 2026.
Este archivo sirve para que cualquier sesión siguiente sepa qué está hecho, qué falta y qué ha decidido Jordi. Actualízalo al terminar cada bloque de trabajo.

Repositorios:
- Web: `Evelinservidor/decodifica.net` (Astro + Tailwind, GitHub Pages detrás de Cloudflare, Plausible, newsletter en Buttondown).
- Estrategia y operaciones (privado, foto del 15-07-2026, solo como referencia de criterio): `Evelinservidor/decodifica-ops` (`_strategy/`, `_web/SEO-RULES.md`, `_web/scripts/seo_preflight.py`).

Reglas de la casa: nada de relleno hecho con IA, toda afirmación con fuente original comprobada, nunca decir que se ha probado algo sin haberlo probado, nada de titulares sensacionalistas ni falsas prisas. El antiguo canal de YouTube de Decodifica ya no existe: no se enlaza ni se menciona.

## Plan aprobado por Jordi

1. **Fase 1 · Dejar la web impecable** — **publicada el 06-10-2026** (pull request #6 fusionado; comprobado en línea).
2. **Fase 2 · Elegir el nicho con datos** — **hecha (07-10-2026)**: Jordi elige seguir con **IA práctica**. Datos y comparación en `docs/fase-2-nichos.md`. Antes de usar Semrush/Ahrefs/OpenRush hay que preguntar a Jordi si gastan créditos o son de pago.
3. **Fase 3 · Agente semanal** — en marcha: instrucciones en `docs/AGENTE-SEMANAL.md`, revisión SEO en `scripts/seo_preflight.py`. (rutina en la nube, lunes por la mañana, hora de España) — pendiente. Al principio abre un pull request y Jordi aprueba; más adelante, publicación automática.

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

## Agente semanal

- Rutina en la nube cada lunes (hora de España), después del informe de Search Console de las 9:00. Sigue `docs/AGENTE-SEMANAL.md`.
- Modo actual: **propone y Jordi aprueba** (pull request). Pasar a «Publicar sola: SÍ» cuando Jordi lo diga.
- Decisión de Jordi (07-10-2026): los arreglos pendientes de la web publicada los hace el agente, **uno por semana**.
- Cola de arreglos para el agente (el preflight los marca): ~~`claude-emails-sonar-humanos`~~ (hecho el 07-10-2026), `crear-agente-voz-ia-sin-programar` («he probado», «increíble»), `ia-organiza-pendientes` («cambia las reglas del juego», «brutal»). Después: ficha `/herramientas/notebooklm/` y comparativa `/herramientas/notebooklm-vs-perplexity/` (nombre nuevo «Gemini Notebook» y límites), y la revisión de fuentes de los artículos antiguos no reescritos.

### Ejecuciones

- **07-10-2026 (prueba, miércoles):** rama `agente/2026-10-07`, pull request pendiente de aprobación de Jordi. Artículos nuevos: `lm-studio-que-es-como-usar` y `n8n-que-es-gratis`. Arreglado `claude-emails-sonar-humanos`. Títulos nuevos en `/herramientas/notebooklm-vs-perplexity/` y `/herramientas/gamma-vs-canva-ai/`. Informe: `docs/informes/2026-10-07.md`; redes: `docs/redes/2026-10-07.md`.
  - Pendiente: precio mensual (no anual) de n8n sin confirmar; revisar dentro de unas semanas si «Emergent IA» y «DeepSeek, Qwen y Kimi» empiezan a recibir clics; idea para más adelante: mejorar el artículo de Nano Banana para «prompts para Gemini fotos» (mucha demanda en Latinoamérica).
