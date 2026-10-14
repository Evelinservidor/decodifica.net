# Portadas e imágenes de los artículos

Qué hemos aprendido sobre las imágenes que consiguen clics, cómo es el sistema de portadas de Decodifica y cómo se añaden imágenes dentro de los artículos. Lo siguen todos los agentes (lunes, novedades y repaso mensual).

Investigación hecha el 14 de octubre de 2026. Las fuentes están al final; las citas son de la documentación oficial.

## 1. Dónde influye de verdad la imagen

| Dónde | Qué imagen usa | Qué importa |
|---|---|---|
| **Google Discover** | `og:image` o la imagen de los datos estructurados | Imagen grande (1200 px de ancho o más, más de 300.000 píxeles, 16:9) y `max-image-preview:large`. Sin ella, Discover muestra una miniatura pequeña y se pierden clics. |
| **Google Imágenes** | Las imágenes de la página | Texto alternativo (lo más importante), nombre de archivo descriptivo, imagen cerca del texto que la explica, formatos modernos (WebP). |
| **Miniatura en los resultados normales** | Google elige «la imagen más relevante de la página» para cada búsqueda | Se puede influir con `og:image` y los datos estructurados, pero Google no lo garantiza. Sale más en búsquedas de cosas visuales. |
| **Redes al compartir** (Facebook, WhatsApp, Bluesky, Reddit, LinkedIn, X) | `og:image` | 1200x630 (1,91:1). Peso: menos de 300 KB para que WhatsApp la enseñe; Bluesky corta en 1 MB. |
| **La portada del blog** (`/blog/`) | La tarjeta de cada artículo | Aquí sí manda el texto corto: la gente elige entre muchas tarjetas en la misma pantalla. |

## 2. Lo que piden Google y las redes

- **Discover:** al menos 1200 px de ancho, más de 300.000 píxeles, 16:9, `max-image-preview:large`. Indicar la imagen con `og:image` o con schema.org. No usar el logo de la web ni imágenes genéricas. Google recorta solo: lo importante, en el centro.
- **Ojo con el texto en la imagen.** Discover: *«avoid using text-heavy images in the schema.org markup or og:image meta tag»*. Google Imágenes: *«avoid using a generic image (for example, your site logo) or an image with text»*. Por eso cada portada tiene dos versiones (ver §4).
- **Nada de gancho engañoso.** Discover castiga los *«misleading or exaggerated details in preview content (title, snippets, or images)»* y el sensacionalismo; si se incumple, puede haber acciones manuales en Search Console.
- **Datos estructurados (Article):** varias imágenes de alta resolución (al menos 50.000 píxeles) en 16:9, 4:3 y 1:1, relacionadas con el artículo, no logos.
- **Facebook:** 1200x630 recomendado; mínimo 600x315 para la vista grande; máximo 8 MB; declarar `og:image:width` y `og:image:height`.
- **X:** `summary_large_image`, 2:1, menos de 5 MB, JPG/PNG/WEBP. **LinkedIn:** 1200x627 o más, 1,91:1, 5 MB. **Bluesky:** usa `og:image`, máximo 1 MB. **WhatsApp:** sin documentación oficial; en la práctica, por debajo de ~300 KB.
- **Velocidad:** la imagen de cabecera se carga enseguida (`fetchpriority="high"`) y el resto con `loading="lazy"`. Todas con `width` y `height` para que la página no salte.

## 3. Patrones de las portadas que funcionan

Mirado en medios de tecnología en español (Xataka, Genbeta, Applesfera, Computer Hoy) y en miniaturas de YouTube de IA con muchas visitas. Solo patrones: no se copia ningún diseño ni se usan imágenes de otros.

- **Un protagonista claro** que se reconozca de un vistazo: el logo o la interfaz real de la herramienta, un producto o una cara. En temas de IA, reconocer la herramienta (ChatGPT, Claude, Gemini…) es el gancho principal.
- **Contraste alto** figura/fondo y **un color de marca constante**, para que la serie se reconozca en Discover y en el blog.
- **Los medios en español no ponen texto en su `og:image`**: el titular va en el HTML. Usan 840x560 o 1920x1080 y WebP muy ligeros (30-110 KB).
- **YouTube sí usa texto**: en un estudio de vidIQ (julio de 2026, 500 vídeos que despegaron) el 69 % lleva una cara, el 56 % contraste alto y la mediana es de **5 palabras**; solo 1 de cada 20 exagera la expresión. La prueba A/B de YouTube elige la ganadora por tiempo de visionado, no por clics: gana la miniatura que cumple lo que promete.
- **Un número grande** funciona en listas y comparativas («5», «7»): se entiende sin leer.
- **Una etiqueta corta** (NUEVO, GRATIS, COMPARATIVA) solo si es verdad.

## 4. El sistema de portadas de Decodifica

Cada artículo tiene una entrada en `src/data/portadas.json` y se genera con:

```bash
python3 scripts/imagenes/portada.py <slug>          # o sin slug para todas
python3 scripts/imagenes/portada.py <slug> --muestra /tmp/muestra.png   # hoja para revisarlas a ojo
```

Funciona en Linux (Python + Pillow) con las fuentes Inter guardadas en `scripts/imagenes/fuentes/` (licencia OFL). Crea en `public/og/blog/`:

| Archivo | Tamaño | Versión | Para qué |
|---|---|---|---|
| `<slug>.jpg` | 1200x630 | con gancho | `og:image`: redes al compartir (~80-110 KB) |
| `<slug>-tarjeta.webp` / `-tarjeta-960.webp` | 640x360 / 960x540 | con gancho | Tarjeta en `/blog/` |
| `<slug>-16x9.webp` / `-16x9-800.webp` | 1600x900 / 800x450 | limpia | Cabecera del artículo y datos estructurados (Discover, Imágenes) |
| `<slug>-4x3.webp`, `<slug>-1x1.webp` | 1200x900, 1200x1200 | limpia | Datos estructurados |

- **Con gancho:** imagen a la derecha y 3-6 palabras muy grandes a la izquierda. Es lo que se ve al compartir y en el blog.
- **Limpia:** solo la imagen (logo, captura o número) sin el gancho, para lo que lee Google. Así cumplimos la recomendación de no usar imágenes cargadas de texto sin renunciar al gancho en redes.
- `SEO.astro` lo conecta solo cuando el artículo usa `ogImage="/og/blog/<slug>.jpg"`: `og:image:width/height/alt`, `twitter:image:alt`, las tres imágenes limpias en el JSON-LD y `max-image-preview:large` en todas las páginas indexables.
- En el artículo no hay que poner nada más: la plantilla `<Articulo slug="<slug>">` muestra la versión limpia en la cabecera. En `/blog/`, en la portada de la web y en «Sigue con esto» se usa la versión con gancho (`-tarjeta`).

### Plantillas

| Plantilla | Cuándo | Qué lleva |
|---|---|---|
| `herramienta` | Guías de una herramienta o de varias concretas | Logo(s) de la web oficial (`logos`) o captura de la web oficial con el logo encima (`captura`). Para guías de método sin herramienta: `casillas` (3 frases cortas que salgan del artículo). |
| `lista` | Comparativas y «N cosas» | Número grande (`numero`) con una palabra debajo (`rotulo`) y los logos de lo que se compara. El número tiene que ser el del artículo. |
| `novedad` | Una función que salió hace menos de 30 días | Etiqueta verde «NUEVO» (también en la versión limpia). Pasado ese tiempo, el repaso mensual la cambia a `herramienta`. |

### Cómo elegir el gancho (pensando en el CTR)

1. **3-6 palabras**, distintas del título (el título ya sale al lado en Google y en redes; el gancho suma, no repite).
2. **La promesa que el artículo cumple**, con el beneficio o la duda de quien busca: «¿n8n es *gratis*?», «IA *sin internet* en tu PC», «Emails que *no suenan* a robot».
3. **Una palabra resaltada** (entre asteriscos en el JSON) en la idea clave: *gratis*, *en español*, *sin programar*.
4. **Nada que el artículo no sostenga**: si dice «gratis», el artículo explica qué es gratis y con qué límites. Sin «increíble», «brutal», «secreto», ni falsas prisas.
5. **Etiqueta** de 1-3 palabras que aporte un dato: «Precios 2026», «Comparativa», «Plantillas», «Guía paso a paso».
6. **Fondo**: alterna colores (`indigo`, `noche`, `naranja`, `verde`, `rosa`, `azul`) para que el blog no quede monótono; el mismo color para la misma herramienta ayuda a reconocerla.
7. **Texto alternativo (`alt`)**: describe lo que se ve en la versión limpia (el gancho se añade solo en la versión con texto). Al menos 40 caracteres.

### Logos y capturas: solo oficiales

- Logos: `python3 scripts/imagenes/logo.py <nombre> <web oficial> [otra web oficial]`. Toma el icono que declara la propia web, lo guarda en `scripts/imagenes/logos/` y apunta la fuente en `logos/FUENTES.md`. Solo para identificar la herramienta de la que habla el artículo. Si la web lo bloquea, probar otra página oficial (docs, blog, la cuenta oficial en GitHub) y anotarlo.
- Capturas para la portada: `python3 scripts/imagenes/captura.py <web oficial> scripts/imagenes/capturas/<nombre>.webp --calidad 85 --max-ancho 1280`.
- **Revisar siempre a ojo** el resultado (logo correcto, captura sin errores ni banners). Algunas webs (chatgpt.com, openai.com, gamma.app) tienen protección antirobots; el script lo avisa.
- Nada de imágenes generadas con IA ni de bancos de fotos de terceros.

## 5. Imágenes dentro del artículo (2-3 por artículo)

Dos herramientas, ambas en `scripts/imagenes/`:

**Capturas de la web oficial** (la página, el botón de descarga, los planes de precios):

```bash
python3 scripts/imagenes/captura.py https://n8n.io/pricing/ public/img/blog/<slug>/precios-n8n.webp \
    --selector "css del bloque de precios"      # o --zona x,y,ancho,alto, o la primera pantalla sin opciones
```

Quita los avisos de cookies, pone un marco de navegador con el dominio (se ve de dónde sale) y guarda WebP de 1200 px. Si la página sale en blanco o con error, lo avisa: mírala antes de usarla. `--idioma en-US` si la versión en español falla.

**Esquemas propios** con los colores de la web:

```bash
python3 scripts/imagenes/esquema.py public/img/blog/<slug>/<nombre>.webp --json '{
  "tipo": "pasos" | "comparativa" | "resumen", "titulo": "...", ..., "pie": "Fuente: ..."}'
```

- `pasos`: pasos en orden (instalar, configurar, comprobar).
- `comparativa`: columnas tipo gratis / de pago (puntos con «✓ » o «✗ »).
- `resumen`: cuadro de «etiqueta: valor» (qué es, precio, dónde se guardan los datos…).

En el artículo:

```astro
import FiguraArticulo from '../../components/FiguraArticulo.astro';

<FiguraArticulo src="/img/blog/<slug>/<nombre>.webp" alt="Qué muestra la imagen, con los datos clave" width={1200} height={600} caption="Opcional: fuente o fecha de la captura" />
```

Reglas:
- Cada imagen **explica algo del texto que tiene al lado** (Google Imágenes la relaciona con ese texto). Ningún dato del esquema que no esté en el artículo y en su fuente.
- Texto alternativo que diga lo que se ve y los datos clave (30+ caracteres). Nombre de archivo descriptivo en minúsculas con guiones.
- `width` y `height` reales (los imprime el script). Carga diferida (lo hace el componente). Menos de 150 KB cada una.
- La revisión SEO (`scripts/seo_preflight.py`) da error si falta la portada o alguna imagen no existe o no tiene alt, y avisa si hay menos de 2 imágenes dentro del texto.

## 6. Medir qué plantilla funciona

Cuando Search Console tenga datos de **Discover** o de **Imágenes** (pestañas «Discover» y tipo de búsqueda «Imagen» en Rendimiento), el repaso mensual compara el CTR por plantilla (`herramienta`, `lista`, `novedad`) y por tipo de imagen (logo, captura, número) y apunta aquí el resultado:

| Fecha | Datos | Plantilla con mejor CTR | Decisión |
|---|---|---|---|
| — | Aún sin datos de Discover (sitio pequeño, octubre de 2026) | — | — |

## Fuentes (consultadas en octubre de 2026)

- Google Discover: https://developers.google.com/search/docs/appearance/google-discover
- Políticas de contenido de Discover: https://support.google.com/websearch/answer/9982767
- Google Imágenes: https://developers.google.com/search/docs/appearance/google-images
- Datos estructurados Article: https://developers.google.com/search/docs/appearance/structured-data/article
- Meta robots (`max-image-preview`): https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag
- Galería de elementos visuales: https://developers.google.com/search/docs/appearance/visual-elements-gallery
- Carga diferida: https://developers.google.com/search/docs/crawling-indexing/javascript/lazy-loading y https://web.dev/articles/browser-level-image-lazy-loading
- Facebook: https://developers.facebook.com/docs/sharing/webmasters/images/
- X (documentación antigua; la actual no abrió): https://dev.twitter.com/cards/types/summary-large-image
- LinkedIn: https://www.linkedin.com/help/linkedin/answer/46687
- Bluesky: https://github.com/bluesky-social/atproto/blob/main/lexicons/app/bsky/embed/external.json
- YouTube (miniaturas y prueba A/B): https://support.google.com/youtube/answer/72431 y https://support.google.com/youtube/answer/13861714
- Estudio de miniaturas de vidIQ (julio de 2026, fuente de terceros): https://vidiq.com/blog/post/youtube-thumbnail-design-tips/
- WhatsApp (no oficial): https://support.wix.com/en/article/wix-editor-recommended-ogimage-size
