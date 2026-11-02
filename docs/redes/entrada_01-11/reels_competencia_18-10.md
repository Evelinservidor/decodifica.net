---
tipo: investigación
creado: 2026-10-18
estado: borrador para Jordi (solo se ha mirado: no se ha publicado nada ni se ha tocado reel.py, visuales.py ni ninguna cuenta)
encargo: «investiga cómo hace la competencia los reels de IA práctica en español, para afinar los de Decodifica y subirlos también a TikTok»
---
# Reels de la competencia (IA práctica en español)

## Para Jordi, en corto
- **He mirado 13 cuentas de TikTok y 6 canales de YouTube Shorts** de IA en español (España y Latinoamérica): unos 450
  vídeos con sus cifras, y por dentro (fotogramas y lo que dicen) los ~20 que más se vieron.
- **Lo que más se ve, con diferencia, son los «códigos» y trucos de ChatGPT, las listas de webs o IAs útiles y los arreglos
  de fotos.** Los vídeos con más visitas: 2,8 millones («Códigos prohibidos de ChatGPT»), 1,9 millones («9 IAs que tienes
  que usar», ¡de solo 18 segundos!), 1,5 millones (una web-calculadora «para estudiantes»), 1,2 y 1,1 millones (códigos
  de ChatGPT y 3 webs con prompts).
- **Casi todos sacan la cara de una persona.** Eso no lo podemos copiar. Pero hay 3 cosas que hacen TODOS y que sí podemos
  hacer:
  1. **Un título fijo arriba que no se va en todo el vídeo** («10 CÓDIGOS SECRETOS DE ChatGPT», «3 sitios web con prompts
     infinitos»). Quien llega a mitad sabe enseguida de qué va. El nuestro solo dura los primeros 4 segundos.
  2. **Enseñan el RESULTADO pronto** (la foto ya arreglada, la web funcionando dentro del móvil) y **numeran** («1», «2», «3»
     enormes).
  3. **Terminan pidiendo algo concreto:** «guárdalo», «sígueme y aprende IA», «¿cuál vas a probar primero?».
- **Una buena noticia para nuestras reglas:** uno de los que más funciona (977.000 visitas) dice justo lo contrario del
  cebo: «Estos códigos NO son comandos oficiales de ChatGPT; funcionan porque…». **Ser honesto también engancha.**
- **Nuestro reel va bien encaminado** en ritmo (cortes cada ~1,5 s), subtítulos grandes palabra a palabra, voz y música.
  **Le falta:** el título fijo, el número de cada punto bien grande, una imagen del resultado en el primer segundo, y
  arreglar dos fallos que he visto (el «GUÁRDALO» final se sale de la pantalla por los lados, y el logo de remove.bg sale
  como un icono genérico).
- **TikTok:** la cuenta **@decodifica** que se ve desde fuera **parece de otra persona** (se llama «giusyderosa», con foto de
  una chica, 12 seguidores, 13 me gusta, sin descripción). **¿Es la suya? ¿O la suya tiene otro nombre?** Hace falta que me
  lo diga o que entre usted. El navegador compartido se colgó al abrir TikTok (ver el punto 5).
- **Ojo: la forma oficial de TikTok de subir vídeos (su «API») no es de pago.** Hay una opción que manda el vídeo a su
  bandeja de TikTok como borrador y usted lo publica con dos toques. Pide registrar una «app» de Decodifica en TikTok
  (gratis, la revisan ellos). Es más segura que manejar el navegador. Lo explico en el punto 5.

---

## 1. Las cuentas que he mirado y sus cifras

Cifras sacadas hoy (18-10, por la tarde) con `yt-dlp` sin bajar los vídeos: visitas, «me gusta», comentarios y compartidos
de los últimos 35 vídeos de cada cuenta (TikTok) o los últimos 60 Shorts (YouTube). La fecha de cada vídeo de TikTok sale
de su número.

### 1.1 TikTok

| Cuenta | ¿Qué es? | ¿Sale una persona? | Vídeos por semana | Visitas (la mitad, más de) | El mejor | Duración típica |
|---|---|---|---|---|---|---|
| @mr.aifo | trucos de ChatGPT, listas de IAs | sí, hablando a cámara | 4,5 | 43.600 | **2,8 M** | 43 s |
| @achoesgratiss («Acho, es gratis») | trucos y webs útiles, ChatGPT | sí (una mujer) | 3,3 | **71.400** | **1,5 M** | 67 s |
| @ia_hipster | códigos de ChatGPT, webs de prompts, Gmail | sí | 3,9 | 53.700 | **1,2 M** | 73 s |
| @xabatzz (Xabi) | códigos de ChatGPT, novedades | sí | 7,7 | 32.200 | 977.000 | 81 s |
| @migue.baena (Migue Baena IA, España) | Claude Code, webs, herramientas | sí + B-roll | 7,2 | 33.500 | 531.800 | 45 s |
| @aprendeconvalerio | herramientas (muchos patrocinados: CapCut…) | sí | 1,1 | 237.300 | 563.000 | 67 s |
| @alejavirivera (Alejavi Rivera) | novedades de IA, IAs gratis | sí, en un círculo sobre la pantalla | 3,8 | 12.200 | 433.800 | 71 s |
| @johnrojas_ia | herramientas | sí | 6,0 | 3.077 | 475.100 | 56 s |
| @jonhernandezia (Jon Hernández, España, 103 mil seguidores) | noticias de IA | sí | **22** | 2.066 | 12.400 | 55 s |
| @webs.con.ia | «sitios web que deberían ser ilegales, parte 223» | **no: solo manos y pantalla** | 6,6 | 2.731 | 23.100 | **13 s** |
| @rmiaclub | prompts, herramientas | sí | 0,6 | 1.446 | 41.900 | 28 s |
| @eduardovazquez.ia | IA para empresas | sí | 6,3 | 3.854 | 4.677 | 83 s |
| (@iadesatada: humor hecho con IA, 2025; no es de lo nuestro y usa imágenes inventadas) | | | | | | |

**Lo que se aprende de TikTok:**
- **Publicar mucho no basta.** Jon Hernández sube 3 al día y la mitad de sus vídeos no llega a 2.100 visitas (son noticias
  leídas). Los que más se ven suben **3-5 por semana** de **trucos que se pueden usar hoy**.
- **Los temas que revientan:** «códigos/comandos de ChatGPT» (2,8 M, 1,2 M, 977 mil, 727 mil, 598 mil), **arreglar o
  editar fotos con ChatGPT** (823 mil, 555 mil, 648 mil), **listas de webs o IAs** (1,9 M, 1,1 M), **trucos de programas de
  siempre** (Gmail 546 mil, Word 532 mil), **estudiantes** (1,5 M). En cambio, las noticias («X lanza Y») y lo de empresas o
  programadores se ven mucho menos, salvo Migue Baena, que tiene público de programadores.
- **La duración no manda:** los más vistos van de **18 a 75 s**. El de 1,9 M dura 18 s y el de 1,5 M, 22 s. Lo que manda es
  que se entienda al momento y que se vea entero.
- **Los «me gusta» y los «guardados» son altísimos** en los que funcionan: un 5-8 % de las visitas da «me gusta» y un 1-2 %
  lo comparte. Es contenido «para guardar».
- **Música:** casi todos usan **«sonido original»**: su voz y, si acaso, una base suave. Solo 2 de los 16 más vistos llevan
  una canción de la biblioteca de TikTok.

### 1.2 YouTube Shorts

| Canal | Suscriptores | ¿Persona? | Short más visto (últimos 60) | Visitas |
|---|---|---|---|---|
| Alejavi Rivera | 590 mil | sí, en un círculo | «Google Antigravity en 1 minuto» (96 s) | 132.500 |
| Dot CSV (Carlos Santana, España) | — | sí | «¡Múdate a Gemini con su nueva funcionalidad!» (108 s) | 132.100 |
| Xavier Mitjana (España) | 384 mil | sí | «Cómo TRANSCRIBIR AUDIO y vídeos de YouTube… ¡GRATIS!» (32 s) | 83.400 |
| Migue Baena IA | 275 mil | sí + B-roll | «24 habilidades IA para programadores» (52 s) | 80.000 |
| Inteligencia Artificial | 818 mil | sí (cortes de entrevistas) | noticias con «Te dejo la guía en los comentarios» (50 s) | 15.750 |
| Adrián Sáenz | 4,1 M | sí | dinero; de IA: «Utilizo la IA para crear una canción de Quevedo» (2023) | 1,4 M |

**Lo que se aprende de Shorts:** en español, los Shorts de IA se ven **bastante menos que en TikTok** (10.000-130.000
visitas incluso con canales grandes). Lo que mejor funciona allí es lo mismo que en nuestro Facebook: **«gratis» + una tarea
concreta** (pasar audio a texto: 83 mil; nuestro mejor reel de verano también fue de voz a texto). En YouTube aguantan
vídeos más largos (hasta 3 minutos).

### 1.3 Facebook e Instagram
Con el navegador colgado no he podido mirar Reels por dentro. Pero estas mismas cuentas suben **el mismo vídeo** a
TikTok, Reels y Shorts. Se nota en los textos: achoesgratiss escribe «Guárdate este **Reel**» en TikTok, y aprendeconvalerio
sube a TikTok la captura de su Instagram. Es lo normal en este mundillo: **un vídeo, tres redes, sin cambiarlo apenas.**

---

## 2. Cómo están hechos por dentro (lo que se repite en los que mejor funcionan)

Lo he visto en fotogramas sueltos de 16 vídeos (sin bajarlos enteros) y en lo que dicen (subtítulos de YouTube y la
descripción de TikTok).

**Los 2 primeros segundos (el gancho):**
- **Texto grande arriba desde el fotograma 1**, que **se queda todo el vídeo** como un titular: «Códigos PROHIBIDOS en
  ChatGPT 🤯», «¿Esto es ilegal para los estudiantes?», «10 CÓDIGOS SECRETOS DE ChatGPT PARA IMÁGENES INCREÍBLES», «TU
  CHEAT CODE PARA EL BLACK FRIDAY», «3 sitios web con prompts infinitos», «SITIOS WEB QUE DEBERÍAN SER ILEGALES · PARTE 223».
- **La primera frase dice el número y la promesa:** «Aquí tienes 6 códigos prohibidos de ChatGPT», «¿Quieres una
  transcripción de cualquier vídeo de YouTube? Fácil, rápido y gratis», «¡Olvida PowerPoint! 3 herramientas para…».
  O una **pregunta con un dolor**: «¿Sigues haciendo tus presentaciones desde cero?», «¿Tus webs creadas con Claude siguen
  pareciendo genéricas?» (Migue Baena empieza casi todos así).
- **Muchos venden lo «prohibido», «secreto» o «ilegal».** Eso **no lo podemos hacer** (regla de no hacer cebo). Pero Xabi
  demuestra que hay otra forma: 977.000 visitas diciendo «no son comandos oficiales; te explico por qué funcionan».

**El ritmo:**
- Un cambio de imagen cada **1-2 s** al principio y cada **2-3 s** después. Lo mismo que hacemos nosotros.
- **Los números de cada punto, enormes** («#1», «1» en amarillo con borde, «3» gigante).
- La voz va **rápida y sin pausas**, sin saludo ni «hola, hoy vamos a ver».

**Las imágenes:**
- **La persona hablando** ocupa la mitad del tiempo (no lo podemos copiar ni lo necesitamos).
- **La pantalla grabada DE VERDAD**: el móvil con ChatGPT escribiendo el código y saliendo la foto, la web abierta, el dedo
  pulsando. Es lo segundo que más sale. En casi todos, **lo que se enseña es el RESULTADO** (la foto arreglada, la
  calculadora con los juegos), no un texto que haya que leer.
- **Logos y capturas de la web oficial** (GitHub, Google, Antigravity) y **B-roll**. Ojo: Migue Baena y Alejavi usan
  imágenes **hechas con IA** (una mano con un rayo, una oficina). Eso nosotros no lo hacemos.
- **Webs.con.ia, la única cuenta sin cara**, graba con el móvil la pantalla del ordenador y unas manos tecleando: vídeos
  de 13-16 s, una web por vídeo y una serie numerada. Tiene muchas menos visitas (2.700 de media). **Sin cara se puede, pero
  hay que compensarlo con un resultado muy visual.**

**Los subtítulos:** 1-3 palabras, blancas y gruesas con borde negro o fondo oscuro, a media altura o algo más abajo, y la
palabra clave en otro color (amarillo, morado). **Igual que los nuestros.**

**El sonido:** su voz casi siempre, música muy baja o ninguna. Algún «whoosh» o «pop». Nada de canciones de moda.

**El final (la llamada a la acción):**
- «**Guárdalo** / Guárdate este reel, que luego no te vas a acordar de cómo se llamaba» (achoesgratiss, ia_hipster).
- «**Sígueme** y aprende IA» con el texto en pantalla (mr.aifo).
- «**¿Cuál vas a probar primero?**» (pregunta para que comenten).
- «Comenta "CREAR" y te lo mando» o «link en mi bio» (sirve para cobrar comisiones o hacer listas; **no lo recomiendo**:
  obliga a contestar mensajes a mano y huele a venta).

**La descripción (TikTok):** larga, con la lista de lo que sale en el vídeo (nombre de cada web o herramienta) y 3-6
etiquetas: #inteligenciaartificial #ia #chatgpt #trucos #tecnologia #herramientasia. TikTok funciona mucho como buscador:
lo que pone en la descripción y en el texto de la pantalla ayuda a que lo encuentren.

---

## 3. Nuestro reel de prueba comparado (la 3.ª versión, 28 s)

He mirado un fotograma por segundo de `~/decodifica-reels/prueba_visual/reel.mp4` («Quita fondos GRATIS: 3 formas»).

**Lo que ya hacemos bien (igual que los que funcionan):**
- Cortes cada ~1,5 s, cada uno con una idea visual distinta.
- Subtítulos enormes, palabra a palabra, con la palabra que suena en naranja.
- Gancho con número + beneficio («3 formas», «GRATIS») y sin saludo.
- Voz rápida (1,15) sin pausas, música y efectos.
- Antes y después (el perro con fondo → sin fondo): es justo el tipo de «resultado» que enseñan ellos.
- La duración (28 s) está en la zona buena para Facebook.
- Contenido original, sin imágenes inventadas por IA y con todo comprobado (en eso vamos por delante de varios de ellos).

**Lo que nos falta:**
1. **Un título fijo arriba durante todo el reel.** El nuestro dura 4 s y luego desaparece. Quien llega a la mitad (en Reels
   pasa mucho) no sabe de qué va.
2. **El gancho dura 4 s con unas tijeras quietas.** Es el momento en que se va la gente (en verano, a los 2-3 s). Los buenos
   enseñan algo que se mueve y el resultado en el primer segundo.
3. **El número de cada punto es pequeño** (un circulito de esquina). Ellos ponen «1», «2», «3» enormes al empezar cada uno.
4. **Los subtítulos se cortan en sitios raros:** «DE REMOVE.BG TE», «EL SUJETO Y». Mejor cortar por trozos con sentido
   («EN REMOVE.BG», «TE QUITA EL FONDO»).
5. **Un fallo:** al final, «GUÁRDALO» es más ancho que la pantalla y se corta por los dos lados.
6. **Otro fallo:** el logo de remove.bg no existe en Simple Icons y sale un icono genérico de capas que no dice nada. Mejor
   el nombre escrito en grande dentro de una «pastilla».
7. **El cierre solo pide guardar.** Le falta «Síguenos» y una pregunta para comentar.
8. **Los iconos 3D seguidos cansan un poco** (tarjeta, pincel, ratón, flechas…). Los buenos mezclan más **pantalla
   real** (la web oficial funcionando) con el resultado.

**Lo que NO podemos hacer (y cómo lo suplimos):**
- **Cara de una persona:** no sale nadie. Lo suplimos con el título fijo, los números grandes y el resultado visual.
- **Imágenes inventadas por IA** (B-roll de IA, «influencers» de IA): no. Fotos CC0, iconos y capturas de verdad.
- **Grabar la pantalla usando la herramienta** («mira, la pruebo»): sin que usted la pruebe no podemos decir que funciona
  (regla 3). Podemos enseñar la web oficial y las imágenes de ejemplo de su propia ayuda. **Si algún día usted graba 10 s de
  la pantalla de su móvil usándola**, eso sería lo mejor de todo: es lo que más se ve, es original y además cuenta como
  su prueba.
- **Cebo** («prohibido», «ilegal», «secreto»): no. Mejor la honestidad de Xabi: «No es un truco secreto: es esto, y
  funciona por esto».
- **Voz:** MiniMax está bien. Lo único que nos distingue es que no hay una cara detrás.

---

## 4. Cambios que propongo (NO aplicados)

### 4.1 En `reel.py` y `visuales.py`
1. **Título fijo arriba durante todo el reel** (`Reel.titulo_fijo()`, llamado en `pintar()` salvo en el cierre). Es el
   gancho resumido en 2 líneas (máx. ~28 letras por línea), blanco con la palabra clave en naranja y con una franja
   oscura semitransparente detrás. Iría entre y=200 y y=420: por encima no estorba la barra de «Para ti/Siguiendo» de TikTok
   ni el nombre de la página de Facebook. La barra de progreso se queda.
2. **Gancho más corto y con movimiento:** la pantalla del gancho como mucho **1,5 s**, y en el segundo 0 ya **el resultado**
   (el antes/después o el logo girando). El texto del gancho sigue en la voz y pasa a ser el título fijo. En el guion
   (`redes.py`, prompt del reel): pedir `gancho_visual` (el visual del primer segundo) además de `gancho_icono`.
3. **Número grande al empezar cada punto:** un plano de 0,5 s con «1», «2», «3» gigante (amarillo con borde, que entra
   botando y hace «pop»), o el número enorme en una esquina durante todo el punto.
4. **Subtítulos por trozos con sentido** (`grupos_sub`): no cortar entre preposición o artículo y nombre («DE | REMOVE.BG»),
   y preferir cortar en comas y puntos. Si un nombre propio es largo (remove.bg, Windows 11), que vaya solo.
5. **Arreglar el «GUÁRDALO»** (`plano_cierre`): medir el ancho y bajar el tamaño hasta que quepa en 1.000 px (ahora entra a
   180 de tamaño y con el «rebote» se pasa).
6. **Logos que no existen** (`visuales.logo_img`): si Simple Icons no tiene la marca, no poner un icono cualquiera: el nombre
   en grande dentro de una pastilla blanca con sombra (es lo que hacen ellos con las webs pequeñas).
7. **Más pantalla de verdad y menos iconos sueltos:** en cada punto, 1 plano del móvil 3D con la web oficial (o la imagen
   de ejemplo de su página de ayuda) + 1-2 visuales. Los iconos 3D, para las ideas abstractas (gratis, un clic, privado).
8. **Cierre en 2 tiempos (2,5 s):** «GUÁRDALO» (con 🔖) y debajo «Síguenos: IA útil cada semana», y en el texto del reel una
   pregunta («¿Cuál te queda más a mano?»). En la voz basta «Guárdalo y síguenos para más.» (unos 30 puntos de MiniMax).
9. **Música más baja** cuando habla la voz (que la voz se entienda con el móvil a medio volumen). Los que funcionan casi
   no llevan música.
10. **Opcional, más adelante:** el formato «serie numerada» que usan varios («Gratis y útil · nº 7»). Crea costumbre y
    deja claro que hay más.

### 4.2 En los temas y los guiones
- **Más de lo que funciona y encaja con nuestras reglas:**
  - **«Comandos/prompts de ChatGPT que sí funcionan, y por qué»** (el tema número 1 en TikTok), contado con honestidad y con
    el resultado de ejemplo de la ayuda oficial.
  - **Arreglar o editar fotos gratis** (quitar fondos, restaurar fotos viejas, mejorar la calidad).
  - **«X webs/IAs gratis para…»** una tarea concreta: estudiar, el trabajo, el correo, un viaje.
  - **Trucos de lo que todo el mundo ya usa:** Gmail, Word, Excel, el móvil (546 y 532 mil visitas). Es justo lo nuestro de
    «tareas de cada día».
  - **Voz a texto y audio** (nuestro mejor reel de verano y el mejor Short de Xavier Mitjana).
- **Menos de:** novedades («X lanza Y»), cosas de programadores y de empresas.
- **Primera frase del guion:** número + promesa («3 formas gratis de quitar el fondo a una foto») o pregunta con dolor
  («¿Pagas por quitar fondos? Hay 3 formas gratis»). Nunca «hoy os traigo».
- **Cada punto, una sola idea en ~4-6 s:** nombre → qué hace → el detalle que importa (gratis o de pago, qué hace falta).

### 4.3 El mismo reel en TikTok
- **El mismo vídeo** (9:16, 1080×1920, H.264 + AAC; TikTok lo acepta igual que Facebook). **No hace falta alargarlo a 1
  minuto:** el programa de pagos de TikTok (para vídeos de más de 1 minuto) no está abierto en España, y los cortos también
  triunfan (18-22 s con 1,5-1,9 M).
- **Subir el archivo original** (`reel.mp4`), nunca uno bajado de Facebook con marca de agua: TikTok baja el alcance a lo
  que lleva marcas de otras redes.
- **Zona segura de TikTok:** nada importante en la columna derecha (botones, unos 140 px), ni en los 350-400 px de abajo
  (nombre y texto), ni en los ~150 px de arriba. Con el título fijo en y=200-420 y los subtítulos en y≈1270, vale.
- **Descripción:** la primera línea es el gancho con la palabra que la gente busca («Quitar el fondo de una foto gratis: 3
  formas»), luego la lista con los nombres y una pregunta. 4-5 etiquetas: #inteligenciaartificial #ia #trucos
  #herramientasia y una del tema (#chatgpt, #fotos…). Sin enlace (en TikTok no se puede pulsar; la web, en la bio).
- **Portada:** el fotograma con el título fijo y el resultado. TikTok deja elegir el fotograma o subir una imagen: la
  `portada.jpg` que ya sale.
- **El crédito de la música** CC BY (Kevin MacLeod) va en la descripción, igual que en Facebook.
- **La etiqueta «Contenido generado por IA»:** no hace falta. Es para imágenes o vídeos realistas hechos con IA, y los
  nuestros no lo son. La voz de MiniMax es sintética: si se quiere ir con todo el cuidado, se puede activar, pero no es lo
  que pide la norma.
- **Hora:** la misma que Facebook (20:30) o un poco antes. Ritmo: **los mismos 3 por semana** que en Facebook.
- **La bio de TikTok:** «IA práctica en español, sin humo · Guías en decodifica.net».

---

## 5. TikTok: la cuenta y cómo se subiría

### 5.1 La cuenta «decodifica»
- **No he podido verla desde dentro.** El navegador compartido (el Firefox, que hoy estaba funcionando en su Nothing) **se
  quedó colgado al abrir tiktok.com** y no volvió a contestar. Lo he **apagado** con su orden normal (`navegador apagar`),
  así que la próxima vez arrancará limpio. Ojo: puede que al encenderse vuelva a abrir la pestaña de TikTok y se cuelgue
  otra vez. Si pasa, basta con cerrar esa pestaña desde la app (🌐).
- **Desde fuera (con el Chrome del móvil viejo, sin su sesión):** la cuenta **tiktok.com/@decodifica** existe con el nombre
  **«giusyderosa»**, una foto de una chica, **12 seguidores, 27 seguidos, 13 me gusta** y sin descripción. Los vídeos no se
  ven sin entrar. **No parece la suya.** Otros nombres parecidos (@decodificaia, @decodifica.ia, @decodificaai) son de
  cuentas de Brasil o Italia sin nada. @decodifica.net y @decodifica_ia no existen.
- **Lo que necesito de usted:** decirme el nombre exacto de su cuenta de TikTok, o entrar en ella en el navegador compartido
  (botón 🌐 → tiktok.com → Iniciar sesión). Con la sesión abierta, miro las cifras (seguidores, vídeos y visitas de los
  últimos) y la página de subir.

### 5.2 La página de subir vídeo (tiktok.com/tiktokstudio/upload)
**Esto no lo he visto con mis ojos** (hace falta su sesión). Lo cuento por la ayuda de TikTok y lo compruebo cuando entre:
1. «Seleccionar vídeo» (o arrastrarlo) → sube y se procesa.
2. Pantalla de edición: **Descripción** (hasta unos 4.000 caracteres, con # y @), **Portada** (elegir fotograma o subir
   imagen), ubicación, etiquetar personas.
3. **Configuración:** quién puede verlo (Todo el mundo / Amigos / **Solo yo**), permitir comentarios, dúos y pegar,
   «Divulgación de contenido» (si es publicidad) y «Contenido generado por IA».
4. **Programar** (para que salga solo a una hora, hasta unos 10 días antes) o **Publicar**. También hay **Descartar** y,
   según la ayuda, **guardar como borrador** (esto lo confirmo cuando lo vea).
- **Para la prueba se puede subir como «Solo yo»**: queda en su perfil, oculto, y usted lo pasa a público con un toque.
  Sirve como borrador seguro.

### 5.3 Riesgos de hacerlo con el navegador (automático)
- **TikTok es de las webs que más vigilan a los robots.** Mira cómo se mueve el ratón, la velocidad y si el navegador está
  manejado por un programa. El nuestro lo está (Marionette). El riesgo va de **un «demuestra que eres humano»** (lo resuelve
  usted con el dedo) a **que limiten la cuenta** o le quiten alcance a lo que sube, si lo hace un robot muchas veces o
  muy deprisa.
- **La web de TikTok es pesada:** hoy ha colgado el Firefox. En el móvil viejo iría peor.
- **TikTok cambia la página a menudo:** lo que hoy es un botón, mañana se mueve, y la subida automática se rompe sin
  avisar.
- **Mi consejo, de más seguro a menos:**
  1. **La forma oficial de TikTok, gratis** («Content Posting API», modo «Upload»): el programa manda el `reel.mp4` a **su
     bandeja de TikTok como borrador**. Le llega un aviso, abre TikTok, revisa y pulsa Publicar (2 toques). No hay robot
     en ningún navegador, ni riesgo de bloqueo. Pide registrar una «app» de Decodifica en developers.tiktok.com, con la web
     y una página de privacidad (decodifica.net ya las tiene), y que TikTok apruebe el permiso `video.upload` (unos días).
     **No es de pago.** Lo que pide una revisión más larga es publicar directamente sin pasar por usted: hasta que se aprueba,
     los vídeos solo pueden salir como «Solo yo».
  2. **Medio automático con el navegador compartido:** Jarvis sube el vídeo, rellena la descripción y lo deja en «Solo yo»
     o como borrador; usted lo mira y pulsa Publicar. Despacio y una vez al día como mucho.
  3. **Totalmente automático con el navegador:** no lo recomiendo (es lo más frágil y lo que más riesgo tiene).
- **Programas de otros que lo hacen** (Postiz, Blotato, Buffer…): suelen ser de pago, o hay que montarlos y registrar
  igualmente la app de TikTok.

---

## 6. Lo que tiene que decidir usted
1. **¿Aplico los cambios del punto 4.1** (título fijo, gancho de 1,5 s con el resultado, números grandes, subtítulos con
   sentido, los dos fallos y el cierre «Guárdalo y síguenos»)? Primero haría un reel de prueba para que lo vea.
2. **¿Cuál es su cuenta de TikTok?** (la @decodifica parece de otra persona). Si es suya, entre en el navegador compartido
   para que mire sus cifras y la página de subir.
3. **¿Cómo subimos a TikTok?** a) la forma oficial gratis (borrador en su bandeja; hay que registrar la app, lo preparo
   yo y usted solo acepta), b) navegador medio automático, o c) a mano de momento.
4. **¿Le apetece grabar alguna vez 10 s de la pantalla de su móvil usando una herramienta?** No hace falta que salga usted.
   Es lo que más se ve y cuenta como su prueba.

---

## Fuentes y cómo se ha mirado
- Cifras de TikTok y YouTube: `yt-dlp` sin bajar vídeos (listas de cada cuenta, 18-10-2026, ~15:00). Fotogramas: trozos de
  1-3 s de 16 vídeos (borrados después); subtítulos automáticos de 7 Shorts. Datos en bruto (se borran al reiniciar):
  `/tmp/compet/tt/v_*.txt`, `/tmp/compet/sh_*.txt`, hojas de fotogramas en `/tmp/compet/ttf/` y `/tmp/compet/fot/`.
- Perfiles públicos de TikTok vistos con `chrome-movil` (sin sesión): @decodifica, @jonhernandezia y búsquedas de cuentas.
- TikTok for Developers, Content Posting API: https://developers.tiktok.com/docs/en/content-posting-api-get-started y
  https://developers.tiktok.com/doc/content-posting-api-get-started-upload-content («All content posted by unaudited
  clients will be restricted to private viewing mode»; el modo «Upload» manda el vídeo a la bandeja para que el creador
  lo termine).
- Listas de creadores consultadas (poco fiables, con intereses comerciales; solo para encontrar nombres):
  https://www.upliora.es/comparativas/mejores-tiktokers-ia-espana-2026 · https://www.heepsy.com/es/top-tiktok/artificial-intelligence/spain
- Etiqueta de IA en TikTok (blogs, sin confirmar en la ayuda oficial): https://www.cinerads.com/blog/tiktok-ai-content-policy
- Programa de pagos de TikTok (blogs: vídeos de más de 1 minuto, países sin España): https://www.toptal.com/creator/post/how-to-join-the-tiktok-creator-rewards-program
- Duración ideal: no hay ningún estudio serio. Los blogs se contradicen (de 7 a 90 s). Mandan nuestras propias cifras y lo que
  se ve arriba.
