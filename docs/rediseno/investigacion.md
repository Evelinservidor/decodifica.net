# Investigación: patrones de diseño en publicaciones tech/IA (foco móvil 390px)

Fecha: 14-oct-2026. Método: Chromium headless (Playwright) a 390x844 con UA de iPhone, capturas del primer pantallazo y de los primeros ~2400px, más medición por JS del cuerpo de artículo (font-size, line-height, familia, ancho y caracteres por línea reales) a 390px y 1280px.
Aviso: la salida a Internet pasa por un proxy que probablemente no está en la UE, así que los banners de cookies vistos pueden ser la variante "no UE" (p. ej. Ars Technica no mostró banner y Xataka mostró el aviso de "si sigues navegando").
Hipertextual devolvió una verificación anti-bot ("Checking your browser") y no se pudo analizar.

Sitios analizados (11): Xataka, Genbeta, Computer Hoy, Wwwhat's new, The Verge, Ars Technica, Zapier blog, The Rundown AI, Smashing Magazine, Android Authority, How-To Geek, Tom's Guide.

---

## 1. Fichas por sitio

### Xataka — https://www.xataka.com
- **Primer pantallazo (móvil):** cabecera oscura (menú / logo / "Nuevo"), una fila de categorías con scroll horizontal y un CTA "Suscríbete a XTRA" fijo a la derecha, un hueco de publicidad de ~120px y después la **historia principal: imagen a sangre con el titular superpuesto** (blanco, 24/32px). Aviso de cookies en una barra inferior con X.
- **Tarjetas:** las 3 primeras son a sangre con el titular sobre degradado. Luego "Lo último": **titular a la izquierda (17-18px, negrita) y miniatura cuadrada ~120px a la derecha**, con meta debajo (nº de comentarios + "hace 5 horas"). La etiqueta de categoría solo aparece cuando la pieza viene de otro sitio de la red ("Xataka Hogar").
- **Tendencias:** franja de chips "🔥 AEMET — China — Nintendo Switch 2…" tras el bloque principal (sirve de "lo más buscado").
- **Artículo** (https://www.xataka.com/robotica-e-ia/gemini-4-argon-nueva-bestia-google-para-trabajo-pesado-codigo-ciencia-finanzas-ciberseguridad): H1 24/32 sans (Tofino), imagen 16:9 a sangre y luego **una lista de viñetas a modo de resumen** (los ladillos del artículo). Cuerpo **serif (IBM Plex Serif) 18/28px, ~37 car./línea en móvil**; en escritorio 21/32px, 736px, ~67 car./línea. Sin índice ni tablas. Enlaces internos "desvío" a mitad del texto (cajas "EN XATAKA HOGAR…"). Bloque de newsletter hacia el 86% de la página.

### Genbeta — https://www.genbeta.com (misma red Webedia que Xataka)
- **Cookies:** **muro de pago** a pantalla completa: "Accede por 2€ sin cookies publicitarias" o "Aceptar y leer GRATIS". El botón de aceptar es azul y llamativo y el de rechazar es gris. Es el patrón que hay que evitar en un sitio pequeño, porque destroza la primera impresión.
- **Home:** listado de tarjetas con H2 18/22.8 en fuente del sistema e imagen al lado.
- **Artículo:** cuerpo **sans del sistema 17/26px, ~38 car./línea** en móvil y 19/30 en escritorio (~72 car./línea). Varios H2 descriptivos, sin índice. Newsletter cerca del final (87%).

### Computer Hoy — https://computerhoy.20minutos.es
- **Cookies:** modal centrado "Acepta para leer gratis y sin límites" con **"Aceptar y cerrar" en negro sólido y "Rechazar y pagar" con contorno** (pay-or-ok). Otro antiejemplo.
- **Home:** lista compacta de miniatura a la izquierda (~110px, 4:3) con titular 18/20 Montserrat y autor en versalitas grises. Después un bloque "Hoy destacamos" con imagen grande y H2 25px. Hay huecos grandes en blanco reservados para anuncios.
- **Artículo:** H1 24/26.4 Montserrat y cuerpo **Open Sans 18/29, ~36 car./línea** (370px de ancho, casi sin margen). H2 de tipo "Para qué se puede usar X / Cómo probar X", una buena estructura de guía.

### Wwwhat's new — https://wwwhatsnew.com
- **Home:** fondo azul con **tarjetas blancas apiladas: imagen ilustrada ~16:10 arriba, titular en MAYÚSCULAS azul (20/30 Lato), extracto de 4-5 líneas, avatar + "Publicado el… por…"**. Después titulares en Oswald 24px en mayúsculas.
- **Lección:** con titulares largos, las mayúsculas cuestan de leer: 6 líneas en mayúsculas por tarjeta. El extracto y el avatar del autor sí dan confianza y contexto.
- **Artículo:** Lato 18/27, ~39 car./línea en móvil, pero **86 car./línea en escritorio (832px)**, demasiado ancho. El texto es gris (#4A5568), con menos contraste. Dos H2 en forma de pregunta ("¿Cómo se consigue…?", "¿Es replicable…?"), que encajan con búsquedas.

### The Verge — https://www.theverge.com
- **Primer pantallazo:** logo enorme, pestañas en forma de píldora ("TOP STORIES / LATEST / FOLLOWING") y después la historia principal con imagen grande, una etiqueta de categoría en una caja de color ("HANDS-ON") y un titular condensado gigante. Botón "Subscribe" pequeño en la cabecera.
- **Tarjetas secundarias:** miniatura cuadrada pequeña a la izquierda, titular en negrita 15-17px, **autor en color de acento y en mayúsculas + icono de comentarios**.
- **Bloques:** "Most Popular" y "Most Discussed" como listas numeradas, y "Latest from AI/Tech…" por sección.
- **Artículo:** H1 sans (polySans) y cuerpo **serif (fkRoman) 18/28.8, ~36 car./línea** en móvil y 600px (~70 car./línea) en escritorio. "Most Popular" y "More in AI" al final.
- **Cookies (variante no UE):** caja oscura de texto largo con X, que tapa ~30% de la pantalla.

### Ars Technica — https://arstechnica.com
- **Home:** selector "GRID" (cambia entre rejilla y lista) y después **tarjetas de imagen 16:9 a sangre + franja de acento verde, titular serif (Faustina) 24-30px, entradilla de 1-2 líneas, AUTOR – fecha + comentarios**. La destacada lleva la insignia "★ FEATURED" y un "kicker" de serie ("I, ROBOT WORKER").
- **Artículo:** H1 serif 30px y cuerpo **sans (Source Sans 3) 18/25.2**, ~46 car./línea en móvil y **675px (~68 car./línea)** en escritorio. H2 cortos ("The future of work"). Sin índice.
- Interfaz con conmutador claro/oscuro ("THEME") en la cabecera.

### Zapier blog — https://zapier.com/blog/ ⭐ (el más parecido a decodifica)
- **Portadas:** ilustraciones planas con **logos de apps sobre fondos de color o patrón** (oscuro, morado, gris). Es casi el mismo lenguaje que las portadas de decodifica.
- **Home del blog:** subnav "Blog | Categories ▾" fija. **Artículo destacado:** imagen 16:9 con la insignia "Featured article", categoría subrayada en azul, H2 ~22px, extracto, avatar + autor + "16 min read". Después una **lista compacta sin imagen** (categoría / título centrado / "fecha | X min read") y después un **bloque de newsletter a todo el ancho con fondo crema** ("Get productivity tips…", email + Subscribe). Luego vuelven las tarjetas grandes.
- **Artículo** (https://zapier.com/blog/zapier-ai-guide/): categoría + "5 min read" encima del H1 centrado (26/32), "By autor · fecha", iconos de compartir y portada. Cuerpo **Inter 16/24 en móvil (~40 car./línea)** y 18/31 a 700px (~81 car./línea) en escritorio. H2 orientados a tareas. Al final, "Related articles". Newsletter fuera del cuerpo. Usa "Note:" como recurso.

### The Rundown AI — https://www.therundown.ai
- **Primer pantallazo dedicado a la newsletter:** "Learn AI in 5 minutes a day.", campo de email + botón en una sola fila, prueba social ("2,000,000+ readers", logos de Google, OpenAI…). Es su producto, así que tiene sentido, pero en un blog sería excesivo.
- **Tarjetas:** imagen ~16:9 con esquinas redondeadas y una **etiqueta de categoría en píldora blanca sobre la imagen** ("AI", "Robotics"), título 17px seminegrita, "Autor • 7 minutes". Botón "View all newsletters →".

### Smashing Magazine — https://www.smashingmagazine.com/articles/
- **Buscador grande justo bajo el logo** y **chips de categorías** (Accessibility, UX, CSS…), más "Hidden gems" en chips verdes. La búsqueda es protagonista.
- **Listado:** sin imagen. Avatar del autor + "wrote", título 22px, "7 min read · comentarios", fecha en versalitas + extracto serif y "Read more…".
- **Artículo** (https://www.smashingmagazine.com/2026/10/how-name-things/): autor/fecha, H1 32px, caja gris de meta (min de lectura, etiquetas, compartir) y después **"QUICK SUMMARY ↬" en versalitas de color + resumen en cursiva**. Cuerpo **serif (Elena) 18/27.8, ~39 car./línea** en móvil y 596px (~68 car./línea) en escritorio. 11 H2 con ancla "#" y un "Jump to" (índice). 10 figuras y 2 citas destacadas.
- **Cookies:** barra inferior corta ("We use cookies for login, checkout and stats") con **dos botones del mismo tamaño**: "No, thanks." (contorno) y "It's okay." (verde). Es el patrón más limpio de los vistos.

### Android Authority — https://www.androidauthority.com
- **Home:** franja de oferta afiliada arriba y después **tarjetas redondeadas: imagen 16:9 + categoría en verde ("News", "Features") + titular 22px + avatar/autor + comentarios**. La primera tarjeta es oscura para destacar.
- **"Top stories":** lista con categoría pequeña en verde, titular 15px y miniatura cuadrada a la derecha.

### How-To Geek — https://www.howtogeek.com
- **Home:** historia principal con imagen 16:9, **etiqueta de categoría en naranja superpuesta en la esquina inferior izquierda de la imagen** ("VPN", "USB"), titular 24px y "By autor | 💬 10". Después una **rejilla de 2 columnas** (imagen + titular 16px) y luego tarjetas grandes otra vez. "LATEST" con "3 HOURS AGO" en naranja.
- **Artículo:** H1 33.6/40, imagen a sangre, barra Like/Follow/Thread y **"Add How-To Geek on Google"** (fuente preferida en Google). Cuerpo **Roboto 19/30.4, ~41 car./línea** en móvil, pero **850px (~98 car./línea) en escritorio**, demasiado ancho. Resumen automático ("fact-based summary") arriba y un mini-quiz incrustado. Newsletter al final (94%).

### Tom's Guide — https://www.tomsguide.com
- **Home:** píldora "↗ Trending" + temas con scroll horizontal. Historia principal con imagen redondeada, titular 26px y entradilla. Tarjetas con imagen grande y titular 14-15px en negrita, alguna **tarjeta de fondo azul noche con el titular en blanco grande**. Un bloque de confianza ("Lab tested / 100% independent / Peer reviewed").
- **Artículo** (guía de ChatGPT): migas de pan "AI > ChatGPT", H1 Inter 30/36, **chip azul "How To"** + autor + "Published fecha", subtítulo y aviso de afiliación. Cuerpo **Inter 18/26, ~37 car./línea**. Remata con un H2 **"The takeaway"**. Muchos `aside` (12) de anuncios y enlaces relacionados.

---

## 2. Tabla resumen del cuerpo de artículo (medido)

| Sitio | Familia cuerpo | Móvil fs/lh | Car./línea móvil | Ancho escritorio | Car./línea escritorio |
|---|---|---|---|---|---|
| Xataka | Serif (Plex Serif) | 18/28 | 37 | 736px (21px) | 67 |
| Genbeta | Sans sistema | 17/26 | 38 | 736px (19px) | 72 |
| Computer Hoy | Open Sans | 18/29 | 36 | 720px | 71 |
| Wwwhat's new | Lato (gris) | 18/27 | 39 | 832px | **86** ✗ |
| The Verge | Serif | 18/28.8 | 36 | 600px | 70 |
| Ars Technica | Source Sans 3 | 18/25.2 | 46 | 675px | 68 |
| Zapier | Inter | 16/24 | 40 | 700px (18/31) | 81 |
| Smashing | Serif (Elena) | 18/27.8 | 39 | 596px (19.8) | 68 |
| How-To Geek | Roboto | 19/30.4 | 41 | 850px | **98** ✗ |
| Tom's Guide | Inter | 18/26 | 37 | 602px (16px) | 74 |

**Conclusión:** el consenso en móvil es **17-19px con un interlineado de 1.45-1.6** (casi todos usan 18px), lo que da 36-46 caracteres por línea en 390px. En escritorio, los que mejor se leen se quedan en **600-700px y unos 65-72 caracteres por línea**. Serif y sans están igualados, porque lo que importa es el tamaño y el contraste (#111-#333 sobre blanco).

---

## 3. Referencias de legibilidad y cookies

- **Longitud de línea:** 50-75 caracteres por línea con espacios (Ruder, 50-60). Hay que mantenerse por debajo de 80 según WCAG 1.4.8, y se puede aplicar con `max-width: ~70ch` o `34em`. En móvil vertical el ancho ya limita la línea, así que el problema es el escritorio o el móvil en horizontal. Baymard, "Readability: The Optimal Line Length" (2022): https://baymard.com/blog/line-length-readability
- **Tamaño mínimo:** Lighthouse marcaba como ilegible el texto de menos de 12px si superaba el 40% de la página. Es un mínimo absoluto: el cuerpo debe ir a 16px o más (los sitios medidos usan 18px). https://developer.chrome.com/docs/lighthouse/seo/font-size
- **NN/g, "Cookie Permissions 101"** (Tankala, nov-2023): overlays pequeños que no oculten el sitio, opciones claras desde el principio (Aceptar todo / Rechazar todo / Gestionar), no esconder el rechazo detrás de "Más información", no resaltar solo "Aceptar", que la X equivalga a "solo necesarias" y **no mostrar a la vez la newsletter y el banner de cookies**. https://www.nngroup.com/articles/cookie-permissions/
- **AEPD, "Guía sobre el uso de las cookies"** (actualizada en mayo de 2024): https://www.aepd.es/guias/guia-cookies.pdf
  - Primera capa, apartado 3.1.2.2, punto b: *"Un botón o mecanismo equivalente, similar al anterior (si se utiliza un botón para aceptar, deberá utilizarse un botón para rechazar), con las palabras 'Rechazar cookies', 'Rechazar' o textos similares"*. Punto c: un botón para el panel de configuración granular.
  - Apartado 3.2.3: *"la opción de rechazar las cookies deberá ofrecerse al usuario al mismo tiempo, al mismo nivel y con la misma visibilidad que la de aceptarlas, sin remitirle a otra capa o lugar diferente para realizar esa acción."*
  - Contraste: *"No será válido, por ejemplo, que la opción para rechazar las cookies sea un botón con un texto que no contrasta lo suficiente con el color del botón"*.
  - "Seguir navegando" no es aceptación válida. En pantallas pequeñas se puede adaptar el tamaño de la primera capa.
  - Apartado 3.2.10: no se permiten "muros de cookies" sin una alternativa equivalente. El pay-or-ok de Genbeta y Computer Hoy es la excepción con alternativa de pago, que no tiene sentido para un sitio pequeño.
  - **Lo más sencillo para decodifica:** si no usa cookies no exentas (analítica sin cookies o solo técnicas), puede prescindir del banner.

---

## 4. Síntesis: 14 patrones aplicables a decodifica.net (~35 guías, portadas 16:9 de colores)

1. **Un solo destacado arriba, sin carrusel.** Todos los sitios abren con una historia principal: imagen 16:9 a sangre o con esquinas redondeadas y el titular debajo (Ars, Zapier, HTG, Tom's Guide). En decodifica, la portada ya lleva su propio gancho en Inter, así que **no hay que superponer el titular a la imagen** (Xataka lo hace porque sus fotos no tienen texto). Imagen 16:9 + categoría + H2 de 22-24px + entradilla de una línea + "X min".
2. **Encima del destacado, solo marca y una frase de propuesta.** Rundown y Zapier dejan claro "qué es esto" en una línea. Bastan un logo y una frase como "Guías prácticas de IA para gente no técnica" (1-2 líneas). Nada de un hero de 600px ni de publicidad, para que la primera portada se vea en el primer pantallazo.
3. **Chips de categoría con scroll horizontal bajo la cabecera** (Xataka, Tom's Guide "Trending", Smashing). Con unas 35 guías bastan 5-7 categorías por herramienta o tarea (ChatGPT, Imágenes, Productividad…). Si no hay buscador, sirven de navegación principal.
4. **Combinar dos densidades de tarjeta.** Tarjeta grande (imagen 16:9 arriba) para 1-3 destacados y **fila compacta** (miniatura a la derecha, ~96-120px de ancho, título 16-17px en negrita) para el resto (Xataka "Lo último", Android Authority "Top stories", Verge). Ojo: un 16:9 recortado a cuadrado pierde el gancho de texto de la portada, así que **en filas compactas hay que mantener la miniatura en 16:9** (~120x68) o usar solo el color de la portada como borde o acento.
5. **Anatomía de tarjeta mínima y constante:** categoría (texto pequeño de color o píldora, como Rundown y Android Authority) → título → meta en una línea "fecha · X min de lectura". El "min de lectura" es el dato más útil para guías (Zapier, Smashing, Rundown). El autor es opcional si todo lo escribe la misma persona.
6. **Sacar partido al color de las portadas.** Zapier demuestra que las portadas planas con logos sobre fondo de color quedan bien a pantalla completa. Se puede **teñir el chip de categoría o la franja de acento con el color dominante de la portada** (como la franja verde de Ars), o darle a una tarjeta especial fondo azul noche con el título en blanco (Tom's Guide). No hay que añadir sombras ni degradados encima.
7. **Bloque "Lo más leído" o "Empieza por aquí"** como lista numerada de 3-5 títulos sin imagen, tras el destacado (Verge "Most Popular", HTG "Popular News"). Para gente no técnica, "Empieza por aquí" (guías básicas) vale más que "Lo último".
8. **Listado del blog:** una columna en móvil y 2-3 en escritorio. Filtro por chips arriba y orden por fecha. Con 35 artículos no hace falta paginar, basta "Ver más" o cargar todo con imágenes en lazy loading. Smashing muestra que un extracto de 2 líneas ayuda a elegir. **Que no haya mayúsculas en los títulos** (el contraejemplo es Wwwhat's new).
9. **Cuerpo de artículo:** 18px y line-height 1.6 en móvil (17-19px es el consenso), **`max-width` de unos 66-70ch (~640-680px)** en escritorio y texto #1a1a1a-#333 sobre blanco. Hay que evitar el gris claro (Wwwhat's new) y los anchos de 830px o más (HTG, Wwwhat's new). Inter para todo es válido (Zapier, Tom's Guide).
10. **Cabecera del artículo, en este orden:** migas o categoría → H1 26-30px → subtítulo de una frase → "fecha · actualizado · X min" → portada 16:9. Tom's Guide y Zapier lo hacen así y el primer párrafo asoma en el primer pantallazo. Hay que poner la fecha de actualización, porque las herramientas de IA cambian rápido.
11. **Caja de resumen al principio** ("En resumen" o "Lo que vas a conseguir", 3-4 viñetas): Smashing "Quick summary", las viñetas iniciales de Xataka, el resumen de HTG. Y un **cierre "En pocas palabras / Siguiente paso"** como el "The takeaway" de Tom's Guide. Es la pieza que más valor aporta a un lector no técnico.
12. **Índice plegable ("Contenido") solo en guías largas** (5 H2 o más), con anclas en los H2 (el "Jump to" y los "#" de Smashing). En móvil, mejor un `<details>` cerrado bajo el resumen que una barra pegajosa. Los H2 deben describir tareas o preguntas ("Cómo…", "¿Para qué sirve…?"), como Computer Hoy, Zapier y Wwwhat's new.
13. **Cajas de consejo o aviso** ("Consejo", "Ojo", "Nota:" como en Zapier) con fondo suave y borde izquierdo de color, sin iconos grandes. Las tablas comparativas deben llevar scroll horizontal dentro de su contenedor y la primera columna fija. Ninguno de los sitios medidos usaba tablas en estas piezas, lo que deja un hueco para decodifica (comparar planes, precios o herramientas).
14. **Newsletter y artículos relacionados al final, nunca encima del contenido.** Todos los sitios ponen la newsletter tras el cuerpo (al 86-94% de la página) o como banda entre tarjetas en la home (Zapier). Hay que **poner 3 relacionados de la misma categoría** con la misma tarjeta compacta, luego una banda de newsletter de una línea (email + botón) y no usar pop-ups ni nada fijo en pantalla (NN/g: no acumular overlays).
15. **Cookies (si hacen falta):** barra inferior pequeña (máximo ~25% del alto en 390px) con **"Rechazar" y "Aceptar" del mismo tamaño, peso y contraste** y un enlace "Configurar" (AEPD 3.2.3 y NN/g). Smashing es el modelo a seguir. Lo que no hay que copiar: "si sigues navegando aceptas" (Xataka, variante no UE), los muros de pago (Genbeta y Computer Hoy) y el texto largo con solo una X (The Verge). Lo mejor es no necesitar el banner, con analítica sin cookies.

**Extras de bajo coste:** "Añadir a Google como fuente preferida" (HTG, Tom's Guide), conmutador claro/oscuro (Ars) y migas de pan con schema (Tom's Guide).
