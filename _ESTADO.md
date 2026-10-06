# Estado del relanzamiento de Decodifica

Última actualización: 6 de octubre de 2026.
Este archivo sirve para que cualquier sesión siguiente sepa qué está hecho, qué falta y qué ha decidido Jordi. Actualízalo al terminar cada bloque de trabajo.

Repositorios:
- Web: `Evelinservidor/decodifica.net` (Astro + Tailwind, GitHub Pages detrás de Cloudflare, Plausible, newsletter en Buttondown).
- Estrategia y operaciones (privado, foto del 15-07-2026, solo como referencia de criterio): `Evelinservidor/decodifica-ops` (`_strategy/`, `_web/SEO-RULES.md`, `_web/scripts/seo_preflight.py`).

Reglas de la casa: nada de relleno hecho con IA, toda afirmación con fuente original comprobada, nunca decir que se ha probado algo sin haberlo probado, nada de titulares sensacionalistas ni falsas prisas. El antiguo canal de YouTube de Decodifica ya no existe: no se enlaza ni se menciona.

## Plan aprobado por Jordi

1. **Fase 1 · Dejar la web impecable** — en curso (rama `fase-1-arreglos`).
2. **Fase 2 · Elegir el nicho con datos** — pendiente. Antes de usar Semrush/Ahrefs/OpenRush hay que preguntar a Jordi si gastan créditos o son de pago.
3. **Fase 3 · Agente semanal** (rutina en la nube, lunes por la mañana, hora de España) — pendiente. Al principio abre un pull request y Jordi aprueba; más adelante, publicación automática.

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

## Fase 1: en curso / pendiente

- [ ] Fusiones con redirección (en revisión):
  - Claude Skills: `claude-skills-desde-cero` → `claude-skills-1000-gratis` (guía única reescrita).
  - NotebookLM: `notebooklm-google-openai` → `notebooklm-guia-2026`. La comparativa `/herramientas/notebooklm-vs-perplexity/` se queda (otra búsqueda).
  - IA gratis: `ia-gratis-silicon-valley` → `alternativas-gratis-chatgpt-2026` (actualizada a octubre de 2026). `5-atajos-ia-gratis` y `odysseus-pewdiepie-ia-gratis` se quedan: responden a búsquedas distintas.
  - IA china: `glm-52-kimi-coinbase` y `prompts-chinos-abiertos` → `deepseek-app-oficial-espanol` (guía DeepSeek/Qwen/Kimi en español).
- [ ] «emergent ia»: reescribir `crear-app-web-ias-chinas-open-source` (la URL se mantiene porque ya tiene impresiones) para responder qué es Emergent, precios y cómo usarlo.
- [ ] Limpiar texto de plantilla y descripciones cortadas con «...» en 12 artículos más.
- [ ] Actualizar enlaces internos que apunten a URLs redirigidas.
- [ ] `claude-skills-desde-cero.pdf` (da 404): **no se ha publicado a propósito**. Contiene afirmaciones en primera persona que no podemos comprobar («he creado 8 skills», «lo uso 5-8 veces al día»), un dato técnico dudoso y el usuario del canal antiguo. Ninguna página de la web lo enlaza. Opciones: rehacerlo a partir de la guía nueva de Claude Skills, o dejarlo sin publicar. Pendiente de Jordi.
- [ ] Aviso legal sin NIF ni domicilio: obligatorio (LSSI) antes de poner anuncios o afiliados. **Pedírselo a Jordi cuando toque monetizar; no inventarlo.**
- [ ] Nombre del autor: en unas páginas «Jordi Castaneira» y en el JSON-LD de un artículo «Jordi Castañeira». Confirmar con Jordi cuál es el correcto.
- [ ] Redes sociales de `site-config.ts` (Facebook, Bluesky, TikTok, Reddit): confirmar con Jordi que siguen activas y son suyas.
- [ ] Revisión de datos (fuentes) del resto de artículos antiguos que no se han reescrito: queda como tarea continua del agente semanal.

### Decisiones técnicas tomadas

- Las fechas del nombre de archivo de 10 artículos (p. ej. `2026-07-16-prompts-secretos-web`) no cuadran con `pubDate`. El `pubDate` es el correcto (coincide con el día en que se subió). **No se renombran las URLs** porque ya tienen impresiones; a partir de ahora los artículos nuevos no llevan fecha en el nombre del archivo.
- Redirecciones: GitHub Pages no tiene redirecciones de servidor. Se usa `return Astro.redirect('/destino/', 301)` en el `.astro`, que genera una página con `meta refresh`, `noindex` y `canonical` al destino (igual que `/recursos-ia/`). El sitemap excluye automáticamente cualquier artículo que sea una redirección.
- Para que el sitemap marque un artículo como actualizado, añade en su frontmatter `const modifiedDate = "AAAA-MM-DD";` y pásalo a `BaseLayout` (`modifiedDate={modifiedDate}`).

## Guía para Jordi: arreglar el informe de Search Console (una sola vez, ~15 minutos)

1. Entra en Google Cloud con tu cuenta de Google y crea un proyecto (o usa el que ya tenías para la app OAuth): https://console.cloud.google.com/projectcreate — nombre, por ejemplo, «decodifica-informes».
2. Activa la API de Search Console en ese proyecto: https://console.cloud.google.com/apis/library/searchconsole.googleapis.com → botón **Habilitar**.
3. Crea una cuenta de servicio: https://console.cloud.google.com/iam-admin/serviceaccounts/create → nombre «informe-gsc» → **Crear y continuar** → no hace falta darle roles → **Listo**.
4. Abre la cuenta de servicio recién creada → pestaña **Claves** → **Agregar clave** → **Crear clave nueva** → **JSON** → se descarga un archivo `.json`. Guárdalo en lugar seguro y no lo compartas. Copia también el correo de la cuenta (termina en `@...iam.gserviceaccount.com`).
5. En Search Console, añade ese correo como usuario de la propiedad de decodifica.net: https://search.google.com/search-console/users → elige la propiedad `decodifica.net` → **Añadir usuario** → pega el correo → permiso **Restringido** (basta para leer datos).
6. En GitHub, guarda el contenido del archivo como secreto: https://github.com/Evelinservidor/decodifica.net/settings/secrets/actions/new → nombre `GSC_SERVICE_ACCOUNT_JSON` → pega el contenido completo del `.json` → **Add secret**.
7. Lanza el informe a mano para comprobarlo: https://github.com/Evelinservidor/decodifica.net/actions/workflows/weekly-gsc-report.yml → **Run workflow**. Si sale en verde, a partir de ahí se ejecuta solo cada lunes a las 9:00 (hora de España).

Si en el paso 4 Google dice que la creación de claves está bloqueada por una política de la organización, la alternativa es pasar la app OAuth a «producción» (https://console.cloud.google.com/auth/audience → **Publicar app**) y regenerar `GSC_REFRESH_TOKEN`.

## Decisiones de Jordi

- (06-10-2026) Aprueba el plan de tres fases. El dinero, después: afiliados y producto propio antes que anuncios.
