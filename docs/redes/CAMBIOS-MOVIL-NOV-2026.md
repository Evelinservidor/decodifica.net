# Cambios en el móvil viejo · noviembre de 2026

**Para Jarvis.** Esta es la especificación de lo que hay que cambiar en `/root/tareas/redes/`
(`redes.py`, `reel.py`, `visuales.py`, `imagen.py`, `herramientas/tareas_programadas.sh`, `estado.json`) para aplicar el
plan de crecimiento que Jordi aprobó el 02-11-2026 (`docs/PLAN-CRECIMIENTO-NOV-2026.md`, apartados 4, 7 y 9).

**Cómo está escrito:** se ha hecho desde la nube, **sin ver el código del móvil**. Los nombres de funciones salen de los
planes del 18-10 y de la estrategia actual (`docs/redes/entrada_01-11/`); donde no coincidan, adapta el nombre y respeta
el comportamiento. Antes de cambiar nada, haz las copias de siempre (`redes.py.antes_nov2026`, etc.) y apúntalo en
`~/CAMBIOS-SIN-SUBIR.md`.

**Lo que no cambia:**
- las reglas de la casa (datos comprobados en la fuente oficial, nunca «lo hemos probado», sin cebo, sin imágenes
  inventadas por IA);
- el lector escéptico;
- la voz de MiniMax;
- el estilo rápido aprobado el 18-10 y el reel de ejemplo oficial (`~/decodifica-reels/_EJEMPLO_OFICIAL/`);
- nada se contesta ni se comparte sin el «sí» de Jordi.

**Por fases:** lo marcado **[F1]** se pone ya (fase 1, del 9 al 30 de noviembre). Lo marcado **[F2]** solo cuando la
revisión del 29-11 lo diga (ver el punto 9).

---

## 1. El calendario nuevo

| Hora (España) | Qué | Dónde | Fase |
|---|---|---|---|
| 12:00 lunes, miércoles y viernes | Ronda de Bluesky (antes, cada día) | Bluesky (solo con el sí de Jordi) | F1 |
| **13:15 cada día** | **Reel del día** (sale de la cola, punto 2) | Facebook reel + Instagram reel + Bluesky vídeo + TikTok (punto 4) | F1 |
| 17:30 si hay artículo nuevo | Artículo nuevo: la portada como foto, el texto sin URL y la URL en el primer comentario | Facebook, Instagram (sin enlace, «enlace en la bio»), Bluesky (con tarjeta de enlace) | F1 |
| 20:30 cada día | Tarjeta de valor | **Bluesky cada día**; Facebook e Instagram **solo lunes, miércoles y domingo** (punto 5) | F1 |
| 20:30 cada día | **Reel 2** (en lugar de la tarjeta en Facebook e Instagram) | como el de las 13:15 | **F2** |
| 21:00 cada día | Comentarios nuevos: prepara la respuesta y se la pasa a Jordi con botones | Facebook, Instagram, Bluesky y TikTok (cuando la API lo permita) | F1 |
| 22:00 cada día | **Fabricar reels** hasta que haya 5 en la cola (punto 2) | — | F1 |
| 21:30 domingo | Parte de la semana (cifras nuevas, punto 6) | `estado.json` | F1 |
| **12:30 lunes** | **Marcador** (punto 7), después del informe de Search Console | mensaje a Jordi + `docs/marcador/` | F1 |

- El artículo pasa de las 13:15 a las 17:30, para no coincidir con el reel. Sigue siendo **solo artículo nuevo** (de los
  últimos 10 días). Los días sin artículo no sale nada a esa hora.
- **Como mucho 3 publicaciones al día en Facebook** (reel + artículo + tarjeta o reel 2). Si un día coinciden más, se
  deja fuera la tarjeta.

---

## 2. La cola de reels (nueva) [F1]

**Por qué:** el 21-10 y el 30-10 se perdió el reel porque el lector escéptico dijo «rehacer» dos veces; el 20-10, por el
límite semanal de Claude; y el 18-10, por la red. Con 3-5 reels ya hechos y aprobados, nunca queda un día vacío.

- **Carpeta:** `~/decodifica-reels/cola/<AAAA-MM-DD_HHMM>_<slug>/`. En cada una:
  - `reel.mp4` (1080×1920, H.264 + AAC, 30 fps, 18-30 s);
  - `portada.jpg`;
  - `guion.json` (punto 3);
  - `veredicto.json` (lo que dijo el lector escéptico).
- **Fabricar (22:00, y otra vez a las 10:00 si hay menos de 3):** mientras haya menos de 5 en la cola, escribir el guion,
  pasar el lector escéptico (con una segunda vuelta si dice «rehacer»; si vuelve a decirlo, se descarta y se pasa al
  siguiente tema) y hacer el reel con `reel.py`. Como mucho 3 reels nuevos por noche, por el gasto de CPU y de MiniMax.
- **Publicar (13:15 y, en F2, 20:30):** se coge el **más antiguo** de la cola. Si está vacía, ese día no sale reel y se
  avisa a Jarvis. No se hace uno deprisa.
- **Caducidad:** los reels de la serie «Lo de la semana» caducan a los 7 días; los demás, a los 30 (hay que volver a
  comprobar precios y límites). Al caducar se borran de la cola, sin publicar.
- **Temas:** no repetir el tema de ningún reel de los últimos 40 ni el de una tarjeta de los últimos 7 días (mirar en
  `estado.json`).
- **Del repositorio:** si `docs/redes/<AAAA-MM-DD>.md` trae un «Guion de reel» (los deja el agente de los lunes para
  cada artículo nuevo, y el de novedades para «Lo de la semana»), ese guion tiene prioridad sobre un tema inventado.

---

## 3. El guion del reel [F1]

`guion.json`:

```json
{
  "serie": "gratis-y-util | cual-uso | truco-del-dia | mito-o-realidad | lo-de-la-semana",
  "numero_serie": 7,
  "tema": "Quitar el fondo de una foto gratis",
  "gancho": "Quita fondos GRATIS: 3 formas",
  "gancho_b": "¿Pagas por quitar fondos? Hay 3 gratis",
  "gancho_visual": "antes/después de la foto de ejemplo de la ayuda oficial",
  "aportacion": "qué hace cada una con la foto en el móvil y cuál pide cuenta",
  "puntos": [{"texto": "...", "capturas": ["https://url-oficial"], "dato_y_fuente": "..."}],
  "cierre": "Guárdalo y síguenos. ¿Cuál te queda más a mano?",
  "fuentes": ["https://...", "https://..."],
  "texto_facebook": "...", "texto_instagram": "...", "texto_tiktok": "...", "texto_bluesky": "...",
  "grabacion_jordi": null
}
```

**Lo que se le pide al guion** (añadir al prompt del reel; viene del estudio de la competencia del 18-10 y de lo que ha
marcado el lector escéptico):

1. **El resultado en el segundo 0** (`gancho_visual`): el antes y después, o la herramienta funcionando (capturas de la
   web o de la ayuda oficial). Nada de iconos quietos al principio.
2. **Título fijo arriba durante todo el vídeo**, números grandes en cada punto y subtítulos cortados por trozos con
   sentido.
3. **Una aportación nuestra** (`aportacion`): una comparación, el límite del plan gratis, el paso que nadie explica, si
   sirve en España y Latinoamérica. **Si el guion solo lee lo que sale en pantalla, se rehace.** Meta saca de las
   recomendaciones el contenido que «narra lo que sale en pantalla sin añadir nada» (Meta, 13-03-2026).
4. **Nunca 💳 junto a «gratis».** El lector escéptico lo ha marcado 4 veces. Si algo tiene parte de pago, se dice con
   palabras.
5. **Series fijas** con número («Gratis y útil nº 7»). Hay que repartirlas en la semana. Por lo que funcionó en verano y
   en la competencia, más de «gratis y útil», «truco del día» (Gmail, WhatsApp, Word, Excel, el móvil) y «cuál uso»; menos
   de novedades.
6. **Cierre:** «Guárdalo» y una pregunta de verdad. **Nunca** «comenta SÍ», «comparte si…» ni «etiqueta a un amigo»: Meta
   enseña menos ese cebo.
7. **Texto de cada red:**
   - TikTok: la primera línea con las palabras que busca la gente («Quitar el fondo de una foto gratis: 3 formas»), la
     lista de herramientas, una pregunta y 4-5 etiquetas (#inteligenciaartificial #ia #trucos + 1-2 del tema). Sin
     enlace.
   - Instagram: igual, y al final «Fuentes: enlace en la bio».
   - Facebook: igual, sin etiquetas largas.
   - Bluesky: hasta 300 caracteres.
   - El crédito de la música CC BY va en todas.
8. **`grabacion_jordi`:** si Jordi ha mandado esa semana una grabación de pantalla de esa herramienta, va en el primer
   plano (después del título), recortada a 3-6 s y sin datos personales. Solo en ese caso se puede escribir «funciona»
   como prueba suya.
9. **El lector escéptico lee también `aportacion`** y responde una pregunta más: «¿aporta algo que no diga ya la web de
   la herramienta?». Si contesta que no, es «rehacer».

---

## 4. Publicar el mismo vídeo en cuatro redes [F1]

Se sube **el mismo `reel.mp4` original** a cada red, nunca uno descargado de otra (las marcas de agua bajan el alcance).
Si una red falla, se reintenta 2 veces con 5 minutos de espera y se apunta en el registro; las demás salen igual.

### 4.1 Facebook (como ahora)
- `video_reels` en 3 pasos (start → subida → finish), con `texto_facebook`.
- **Etiqueta de IA:** mira en la documentación de Reels Publishing API si hay un campo para declarar el audio hecho con
  IA. Si lo hay, actívalo. Si no lo hay, no se inventa: apúntalo en el registro y avisa a Jarvis una vez.

### 4.2 Instagram (nuevo)
Necesita que Jordi haya hecho el paso 2 de `docs/PARA-JORDI-PASOS.md`. Permisos del token de la página:
`instagram_basic`, `instagram_content_publish`, `instagram_manage_insights` (además de los de Facebook que ya hay).

1. Una vez: `GET /{page-id}?fields=instagram_business_account` → guarda el `ig-user-id` en `~/.secretos/redes/`.
2. Crea el contenedor: `POST graph.facebook.com/{versión}/{ig-user-id}/media` con `media_type=REELS`,
   `upload_type=resumable`, `caption=<texto_instagram>` y `share_to_feed=true`.
3. Sube el archivo: `POST rupload.facebook.com/ig-api-upload/{versión}/{id-del-contenedor}`, con la cabecera
   `Authorization: OAuth <token>`, `offset: 0` y `file_size`.
4. Espera a que `GET /{id-del-contenedor}?fields=status_code` diga `FINISHED`. Pregunta cada 10 s, durante 5 minutos como
   mucho.
5. Publica: `POST /{ig-user-id}/media_publish` con `creation_id=<id-del-contenedor>`.
6. Antes de publicar, mira `GET /{ig-user-id}/content_publishing_limit`. La documentación da 50 o 100 publicaciones al
   día según la página; nosotros publicamos 2-4.
7. **Trial reels [F2, y solo con 200 seguidores o más]:** el mismo vídeo con `gancho_b`, como «trial reel»
   (`trial_params` con `graduation_strategy: MANUAL`). Jarvis compara a las 48 h las vistas de los dos ganchos y lo
   apunta en `estado.json`.

### 4.3 TikTok
- **F1 (a mano):** copia `reel.mp4` en **Descargas** del móvil de Jordi (como ya se hace) y mándale el `texto_tiktok`
  para pegar. Jordi lo sube (`docs/PARA-JORDI-PASOS.md`, Parte 2).
- **F2 (API oficial, modo «Upload», cuando TikTok apruebe la app):**
  1. `POST https://open.tiktokapis.com/v2/post/publish/inbox/video/init/` con
     `{"source_info": {"source": "FILE_UPLOAD", "video_size": <bytes>, "chunk_size": <bytes>, "total_chunk_count": 1}}`.
     Hace falta el permiso `video.upload`.
  2. `PUT` del archivo a la `upload_url` que devuelve, con `Content-Range`. La URL caduca en 1 hora.
  3. El vídeo llega a la bandeja de Jordi como borrador. Jordi lo abre, activa «Contenido generado por IA» y publica.
  4. **Límites oficiales:** 6 peticiones por minuto por token y **como mucho 5 borradores pendientes en 24 h**. Con 1-2
     vídeos al día sobra, siempre que Jordi los vaya publicando. Si hay 4 pendientes, no se manda más y se avisa.
- **Nunca** con el navegador automático: TikTok lo detecta y puede limitar la cuenta.

### 4.4 Bluesky
- El vídeo con el servicio de vídeo de Bluesky (`app.bsky.video.uploadVideo`) y `texto_bluesky`. Si falla, sale la
  `portada.jpg` como imagen, con el mismo texto.

### 4.5 La página «Lo que sale en los vídeos» (`decodifica.net/redes/`)
Después de publicar cada reel, añade una entrada al principio de `src/data/videos-redes.json` en el repositorio
`Evelinservidor/decodifica.net` (rama `main`). Usa la API de GitHub (`PUT /repos/.../contents/...`) con el token que ya
usa Jarvis, como hace el informe de Search Console con `data/gsc_weekly/`. Así la web se vuelve a publicar sola.

```json
{"fecha": "2026-11-09", "titulo": "Quita fondos GRATIS: 3 formas", "serie": "gratis-y-util", "numero_serie": 7,
 "resumen": "Tres webs gratis para quitar el fondo de una foto desde el móvil y qué pide cada una.",
 "fuentes": [{"nombre": "remove.bg: Pricing", "url": "https://..."}],
 "guia": "/blog/slug-si-hay-una-guia-de-lo-mismo/",
 "enlaces": {"facebook": "https://...", "instagram": "https://...", "tiktok": null, "bluesky": "https://..."}}
```

- Como mucho 60 entradas; la más antigua se borra.
- Mensaje del commit: `redes: vídeo del <fecha> en /redes/`.
- **Solo datos de vídeos ya publicados.** Nunca toques otro archivo del repositorio.

La página la crea el pull request de la web del 02-11-2026; hasta que se fusione, este paso no se hace.

---

## 5. Qué publicaciones de imagen se quitan [F1]

| Publicación de hoy | Qué pasa |
|---|---|
| Facebook 13:15 «no hay nada que publicar» (14 de cada 19 días) | Pasa a ser el **reel del día** |
| Facebook 13:15 artículo nuevo | Pasa a las **17:30**; sigue igual (portada como foto, enlace en el primer comentario) |
| Facebook 20:30 tarjeta de valor **martes** (truco), **jueves** (error común), **viernes** (lo de la semana) y **sábado** (herramienta gratis) | **Se quita en Facebook.** Esos temas pasan a los reels (series «truco del día», «gratis y útil», «lo de la semana»). En Bluesky siguen. |
| Facebook 20:30 tarjeta **lunes** (prompt para copiar), **miércoles** (¿cuál uso?) y **domingo** (mito o realidad) | **Se queda en F1**, también como **carrusel** de 3-5 imágenes en Instagram (una imagen por punto, con `imagen.py`). En F2 se quita en Facebook si entra el reel 2. |
| Bluesky: artículo, tarjeta de cada día | **Se queda todo** (casi no cuesta nada) |
| Reels 3 días por semana (lunes, miércoles y viernes) | **Cada día** (punto 1) |

**Motivo:** desde mayo, las fotos y tarjetas de Facebook se vieron 5,5 veces de media y los reels 76. Con 7 seguidores,
cada publicación de más reparte el poco alcance y la página parece spam.

---

## 6. El parte del domingo (cifras de verdad) [F1]

Hoy `redes.py cifras` solo cuenta seguidores y reacciones. A partir de ahora guarda en `estado.json` (`"cifras"`), por
publicación y por semana, todo lo de esta tabla.

| Red | Qué | Cómo |
|---|---|---|
| Facebook, página | Seguidores | `GET /{page-id}?fields=followers_count` |
| Facebook, página | Personas alcanzadas en la semana | métrica `page_total_media_view_unique` (sustituye a `page_impressions_unique`, que Meta retiró el 15-06-2026) |
| Facebook, reel | Reproducciones y segundos vistos de media | las métricas que funcionaron el 18-10 (`fb_reels_total_plays`, `post_video_avg_time_watched`) |
| Facebook, publicación | Personas alcanzadas | `post_total_media_view_unique` |
| Instagram, cuenta | Seguidores | `GET /{ig-user-id}?fields=followers_count` |
| Instagram, reel | Vistas, alcance, guardados y segundos vistos de media | `GET /{ig-media-id}/insights?metric=views,reach,saved,ig_reels_avg_watch_time` (el tiempo puede venir en milisegundos: compruébalo con una respuesta real) |
| TikTok | Seguidores y vistas | F1: a mano (Jordi manda una captura de su perfil el domingo, solo si quiere); F2: Display API con los permisos `user.info.stats` (`follower_count`) y `video.list` (`view_count`), pedidos en la misma app (comprobar los nombres al registrarla) |
| Bluesky | Seguidores, me gusta y respuestas | `public.api.bsky.app/xrpc/app.bsky.actor.getProfile?actor=jc-ia.bsky.social` → `followersCount` (y lo de hoy) |
| Web | Visitas desde cada red | Plausible Stats API v2: `POST https://plausible.io/api/v2/query` con `{"site_id":"decodifica.net","metrics":["visitors"],"date_range":"7d","dimensions":["visit:utm_source"]}` (clave del paso 4 de Jordi) |
| Newsletter | Suscriptores | Buttondown: `GET https://api.buttondown.com/v1/subscribers?type=regular` → `count` (la clave de Buttondown es la que ya usan los scripts de `scripts/`; si Jarvis no la tiene, pedírsela a Jordi) |

- **Si una métrica de Meta da «invalid metric»:** Meta cambia los nombres a menudo. No se para el parte: se apunta la
  métrica que falló y se busca la nueva en la referencia de Insights de su versión. Esa semana sale sin ese dato.
- **Se agrupa** por red, por serie y por formato (reel, tarjeta, artículo). Se apuntan **la mejor y la peor** de la
  semana, con su gancho.
- Las cifras de cada reel se vuelven a pedir a los 7 días de publicarlo, porque los reels siguen sumando vistas, y se
  guardan las dos (a 48 h y a 7 días).

---

## 7. El marcador de los lunes [F1]

**Cuándo:** lunes a las 12:30. Antes, comprueba que `data/gsc_weekly/latest_28d.json` es de ese lunes
(`fetched_at`). GitHub lo genera tarde a menudo (el 26-10 salió a las 10:19 UTC). Si no es de hoy, espera a las 15:00 y,
si sigue sin estar, usa el último y dilo.

**Los 3 números y de dónde sale cada uno:**

| Número | De dónde sale |
|---|---|
| **1. Seguidores sumando todo** (el número grande) | Facebook `followers_count` + Instagram `followers_count` + TikTok `follower_count` (o el último dato a mano) + Bluesky `followersCount` + suscriptores de la newsletter (`count`). Se compara con el lunes anterior: «52 (+14)». |
| **2. Vistas de los vídeos de la semana** | Suma de las vistas, a día de hoy, de los reels publicados de lunes a domingo de la semana pasada: Facebook `fb_reels_total_plays` + Instagram `views` + TikTok `view_count`. Bluesky no da vistas: no cuenta. Se compara con la semana anterior. |
| **3. Clics desde Google en 28 días** | `data/gsc_weekly/latest_28d.json` → `per_site["sc-domain:decodifica.net"].totals.current.clicks`. En 28 días porque con 7 hay tan pocos que suben y bajan por azar. Se compara con el lunes anterior. |

**El mensaje a Jordi** (corto, con flechas, sin jerga):

```
📈 Decodifica, semana del 9 al 15 de noviembre
Seguidores (todas las redes + newsletter): 52 (+14)
Vistas de los vídeos esta semana:      2.300 (+900)
Clics desde Google (últimos 28 días):    21 (+2)
Lo mejor: «Quita el fondo GRATIS» · 1.100 vistas en TikTok · 6,1 s de media
Lo peor:  «Lo de la semana» · 40 vistas
Meta de noviembre: 40 seguidores en Facebook (vamos por 23)
```

- La última línea compara con la meta del mes (abajo) **solo de un número**: el que vaya peor respecto a su meta. Sin
  dramas: si va por detrás, se dice y ya.
- **Se guarda** en `estado.json` (`"marcador"`) y en el repositorio, en `docs/marcador/<AAAA-MM-DD>.md` (mismo método
  que el punto 4.5; solo ese archivo).

**Las metas** (copiadas del apartado 7.2 del plan; guárdalas en `~/tareas/redes/metas_nov2026.json`):

```json
{
  "2026-11": {"fb_seguidores": 40,  "fb_alcance_mes": 1000,  "fb_segundos_reel": 3.5, "ig_seguidores": 30,  "tt_seguidores_ganados": 30,   "tt_vistas_medianas": 200,  "bsky_seguidores": 35, "google_clics_28d": 25,  "newsletter_ganados": 10},
  "2026-12": {"fb_seguidores": 80,  "fb_alcance_mes": 3000,  "fb_segundos_reel": 4.0, "ig_seguidores": 100, "tt_seguidores_ganados": 120,  "tt_vistas_medianas": 350,  "bsky_seguidores": 40, "google_clics_28d": 30,  "newsletter_ganados": 25},
  "2027-01": {"fb_seguidores": 150, "fb_alcance_mes": 6000,  "fb_segundos_reel": 4.5, "ig_seguidores": 200, "tt_seguidores_ganados": 300,  "tt_vistas_medianas": 500,  "bsky_seguidores": 45, "google_clics_28d": 45,  "newsletter_ganados": 45},
  "2027-02": {"fb_seguidores": 250, "fb_alcance_mes": 10000, "fb_segundos_reel": 5.0, "ig_seguidores": 350, "tt_seguidores_ganados": 600,  "tt_vistas_medianas": 600,  "bsky_seguidores": 50, "google_clics_28d": 70,  "newsletter_ganados": 65},
  "2027-03": {"fb_seguidores": 350, "fb_alcance_mes": 15000, "fb_segundos_reel": 5.0, "ig_seguidores": 550, "tt_seguidores_ganados": 1000, "tt_vistas_medianas": 800,  "bsky_seguidores": 55, "google_clics_28d": 100, "newsletter_ganados": 85},
  "2027-04": {"fb_seguidores": 450, "fb_alcance_mes": 20000, "fb_segundos_reel": 5.0, "ig_seguidores": 800, "tt_seguidores_ganados": 1500, "tt_vistas_medianas": 1000, "bsky_seguidores": 60, "google_clics_28d": 130, "newsletter_ganados": 100}
}
```

El punto de partida de TikTok y de la newsletter se apunta el primer lunes (09-11-2026). Las metas de ganados se cuentan
desde ahí.

---

## 8. Otros cambios pequeños [F1]

1. **Comentarios (21:00):** mira lo nuevo desde la última vez:
   - Facebook: `/{post-id}/comments` de las publicaciones de los últimos 14 días;
   - Instagram: `/{ig-media-id}/comments`, con el permiso `instagram_manage_comments`;
   - Bluesky: las notificaciones.
   Prepara una respuesta corta, de tú, con el dato que piden y su fuente. Si no se sabe: «No lo sé seguro; lo miro y te
   digo». Se la pasa a Jordi con botones [Responder] [Cambiar] [No]. **Nunca se responde sin su sí.** No se contesta a
   provocaciones ni a quien vende algo.
2. **Ronda de Bluesky:** solo lunes, miércoles y viernes.
3. **Límite de Claude:** si la respuesta contiene «hit your weekly limit» o «usage limit», **no se reintenta** (el 20-10
   se reintentó 12 veces). Ese turno usa la cola y se avisa a Jarvis una vez. Para repartir el gasto: Sonnet para los
   guiones, los textos y el lector escéptico; Opus solo si Jarvis lo decide para algo difícil.
4. **Enlaces con marca `utm`:** todos los enlaces a la web llevan `?utm_source=<red>&utm_medium=social&utm_campaign=<reel|articulo|valor|bio>`.
   La bio de las cuatro redes apunta a `https://decodifica.net/redes/?utm_source=<red>&utm_medium=social&utm_campaign=bio`
   (o a `https://decodifica.net/` hasta que exista `/redes/`).
5. **Bios:** cuando Jordi diga «sí» (paso 5 de su guía), cámbialas con los textos de allí. Quita el YouTube viejo de
   Facebook y de Bluesky.
6. **Grupos de Facebook (domingo):** con el parte, prepara a Jordi el texto para compartir el mejor reel en su perfil y,
   como mucho, en 1 de sus grupos (mira antes las normas del grupo, si las tiene guardadas). Lo publica él.
7. **Ronda de foros (sábado, nueva):** busca en Reddit en español (r/InteligenciArtificial, r/espanol y foros de
   ordenadores) 1-3 preguntas recientes que responda de verdad una guía de la web. Prepara la respuesta: útil por sí
   sola, con el enlace solo si la guía responde exactamente a eso, y respetando las normas del subreddit sobre
   autopromoción. Jordi la publica a mano, si quiere. **Nunca** se publica de forma automática.
8. **`ESTRATEGIA.md`:** reescríbela con este documento (qué se hace, qué no y las fechas de revisión).

---

## 9. Cuándo se pasa a la fase 2

El domingo 29-11, con el parte, Jarvis comprueba:

| Condición | Si se cumple |
|---|---|
| Segundos vistos de media de los reels en Facebook ≥ 4 s **o** vistas medianas en TikTok ≥ 300 | Se activa el **reel 2** de las 20:30 (y fuera la tarjeta de Facebook e Instagram) |
| TikTok aprobó la app | La subida a TikTok pasa a la API (punto 4.3) |
| Instagram ≥ 200 seguidores | Se activan los trial reels (punto 4.2.7) |
| Ninguna de las dos primeras se cumple | Se sigue con 1 reel al día y se cambian las 2 series que peor fueron; se avisa a Jordi |

**Fase 3 (desde el 29-12):** hasta 3 reels al día **solo en TikTok** (el tercero, solo a TikTok, desde la cola), si la
retención aguanta y el lector escéptico no ha empezado a pedir «rehacer» más de 1 de cada 4 veces.

---

## 10. Cómo comprobar que funciona (antes de dejarlo solo)

1. `redes.py reel --prueba` hace un reel con un guion de la cola, **sin publicar**, y lo copia a Descargas para que
   Jordi lo vea.
2. Publicar el primer reel de Instagram a mano con el programa y comprobar que sale en el perfil (los reels por API no
   salen como «REELS» en `media_type`: hay que mirar `media_product_type`).
3. `redes.py cifras --prueba` y `redes.py marcador --prueba`: imprimen sin guardar ni mandar nada. Jarvis comprueba que
   cada número es razonable (por ejemplo, que los seguidores de Facebook son 7 y no 0).
4. Una semana con todo en marcha y Jarvis mirando el registro cada día. Después, solo.

## Fuentes técnicas (consultadas el 02-11-2026)
- Instagram, publicar reels (subida reanudable): https://developers.facebook.com/docs/instagram-platform/content-publishing/resumable-uploads/
  y https://developers.facebook.com/docs/instagram-platform/content-publishing/
- Instagram, métricas de cada publicación: https://developers.facebook.com/docs/instagram-platform/reference/instagram-media/insights/
- Facebook, métricas de página retiradas el 15-06-2026 y sus sustitutas: https://developers.facebook.com/docs/graph-api/reference/insights
- TikTok, subir a la bandeja: https://developers.tiktok.com/doc/content-posting-api-reference-upload-video y
  https://developers.tiktok.com/doc/content-posting-api-get-started-upload-content/
- Meta, contenido original (13-03-2026): https://about.fb.com/news/2026/03/rewarding-original-creators-on-facebook/
