# Encargo del especialista de la web para el repaso mensual del 20-11-2026

Lo deja el 🌐 especialista el 19-11-2026, con el informe de Google del lunes 16-11 (`data/gsc_weekly/latest_28d.json`,
28 días del 17-10 al 13-11-2026, y `latest_indexacion.md`). Es una lista de partida: las normas de siempre mandan
(como máximo 5 artículos, solo datos comprobados en fuentes oficiales). Si al mirar ves que una no tiene nada
desfasado, no la toques y dilo.

## 1. NO tocar este mes (pruebas abiertas: cualquier cambio las estropea o las retrasa)

| Página | Por qué |
|---|---|
| `/blog/ia-local-sin-internet/` (408 apariciones, 4 clics) | Es la página que más clics puede dar. Cambiada el 09-11: el jueves 03-12 es su primer turno para el título. Cualquier cambio de hoy lo retrasaría al 17-12. Solo si encuentras un dato FALSO, corrígelo y explícalo en el repaso. |
| `/blog/n8n-que-es-gratis/` | Título y preguntas nuevos el 19-11 (jueves). Precios ya comprobados ese día. |
| `/herramientas/qwen-code/` | Prueba de título del 22-10 que Google vio por primera vez el 06-11. Se mide el 30-11 y el 07-12. Su revisión del ledger (le toca el 21-11) puede esperar al jueves 26-11 o hacerse sin tocar título ni descripción. |
| `/blog/claude-skills-1000-gratis/` | Prueba de descripción hasta el 07-12. |
| Título y descripción de `/blog/ia-crea-presentaciones-completas/` y de la ficha de Mistral Vibe | Pruebas de título del 12-11. Los DATOS sí se pueden poner al día (abajo). |
| `/blog/deepseek-app-oficial-espanol/` y `/blog/alternativas-gratis-chatgpt-2026/` | Datos puestos al día el 12-11 (jueves). |

## 2. Por dónde empezar (las 4 primeras salen en Google y tienen datos que cambian)

| # | Página | Apariciones / clics / posición (28 d) | Último rastreo de Google | Qué mirar |
|---|---|---|---|---|
| 1 | `/blog/ia-organiza-pendientes/` | 68 / 0 / 12,2 | 03-10 | Lo que quedó sin revisar en octubre (ver `2026-10.md`): Manus (precio «unos 39 $», «ahora parte de Meta»), Gemini, Claude con MCP y Copilot; y el cuadro `que-conecta-cada-ia.webp`, que se queda corto con ChatGPT. |
| 2 | `/blog/ia-crea-presentaciones-completas/` | 52 / 0 / 11,0 | **31-07** | Pendiente de octubre: el tutorial de 7 pasos de Gamma y su esquema pueden estar desfasados (Gamma 5 funciona hablando con un agente). Sin tocar título ni descripción (prueba del 12-11). Google no la lee desde julio: poner los datos al día y la fecha de revisión le da un motivo para volver. |
| 3 | `/herramientas/notebooklm-vs-perplexity/` | 23 / 0 / 6,5 | 14-10 | NotebookLM y Perplexity llevan en el ledger desde el 14-07 (cada 14 días). `_ESTADO.md` tiene pendiente que NotebookLM se llama ahora «Gemini Notebook»: comprobarlo en la fuente oficial. Título del 29-10: no tocarlo. |
| 4 | `/herramientas/comparativas/manus-vs-chatgpt-apps/` | 16 / 0 / 5,8 | 14-09, **rastreada sin indexar** | Manus en el ledger desde el 14-07. Fuera de Google, así que tocarla no estropea ninguna prueba. |
| 5 | A tu elección | | | Por ejemplo `/blog/2026-07-31-google-maps-gemini-paradas-ruta/` (20 apariciones, cambiada el 29-10) o una ficha muy atrasada del ledger. |

## 3. El ledger de fichas está casi entero atrasado

`src/data/tool-review-ledger.json`: **29 de 31 herramientas** pasan de su fecha de revisión (25 siguen con la del
14-07-2026; Kimi tocaba el 05-11; Granola y Fathom, hoy). La ficha de ChatGPT, por ejemplo, dice a Google
`dateModified 2026-07-14`. Ojo: el ledger no siempre se actualiza cuando se comprueban datos (Gamma y Canva se
comprobaron el 05-11 en «Gamma vs Canva» y siguen con el 14-07).

- Cuando compruebes una herramienta (también dentro de un artículo), pon al día su `verifiedAt`.
- En `docs/repaso-mensual/2026-11.md`, deja la lista de las que siguen atrasadas, ordenadas por apariciones en 28 días.
  Las de más apariciones son NotebookLM y Perplexity (comparativa con 23), Manus (16), Granola (13), Kimi (11) y
  HuggingChat (10). Las demás tienen menos de 10.
  Así decidimos si hace falta un turno solo para fichas (eso lo pide el especialista a Jordi, no lo cambies tú).

## Qué mido yo
- Los informes del 30-11 y del 07-12, en las páginas que toques, frente a las cifras de la tabla de arriba.
- La fecha de último rastreo de Google de `ia-crea-presentaciones-completas` y de `manus-vs-chatgpt-apps`: ¿vuelve
  Google después de la revisión?
