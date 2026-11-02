# Redes de Decodifica — estrategia (14-10-2026; cambios del 18-10-2026 arriba)

## 18-10-2026: el plan nuevo (aprobado por Jordi; detalle y cifras en la bóveda:
## Jarvis/Movil/Borradores/2026-10-18 · Plan redes (propuesta).md)
- Por qué: desde mayo, los REELS de Facebook se vieron de media 76 veces; las fotos 5,5 y las publicaciones con enlace 6,4.
  Sin reels (desde septiembre) la página llega a ~18 personas al mes. Bluesky: 0 de todo en octubre.
- Facebook: lunes, miércoles y viernes a las 20:30 un REEL (reel.py) en lugar de la tarjeta: 15-30 s, gancho con el
  beneficio en los 2 primeros segundos, capturas reales de la web oficial y la tarjeta contada, sin imágenes de IA, voz de
  MiniMax = la de Tiempo de Aviso (Spanish_Debator, speech-2.8-hd), subtítulos grabados. Tope 600 puntos por reel.
  18-10 tarde (Jordi: el primero, «aburrido y lento»): ESTILO RÁPIDO: cortes cada ~1,5 s, capturas a pantalla completa con
  zoom a lo resaltado, subtítulos enormes palabra a palabra, efectos y música libre (sonidos/LICENCIAS.md), voz a 1,15.
  El lector escéptico lee también el guion del reel. Los 2 primeros (prueba del 20-10 al 01-11) esperan a Jordi.
- Facebook, 13:15: la portada como foto, el texto sin enlace y el enlace en el PRIMER COMENTARIO. Solo artículos NUEVOS
  (los viejos ya no se repiten, tampoco en Bluesky).
- Todos los enlaces a la web con ?utm_source=facebook|bluesky&utm_medium=social&utm_campaign=… (Plausible).
- Bluesky: lo de siempre (13:15 con tarjeta de enlace, 20:30 tarjeta) y la RONDA de las 12:00: Jarvis busca preguntas
  reales de IA en español y le prepara a Jordi hasta 3 respuestas; cada una sale SOLO con su sí (botón). Ojo: hay muy pocas
  preguntas de verdad (el 18-10, 48 publicaciones vistas en 2 días → 1 buena): muchos días no habrá ninguna.
- Revisión: 28-10 (a mitad) y 01-11 (final). Sale bien si los reels se ven 5 veces más que las tarjetas y aguantan ≥ 4 s.


Punto de partida (14-10): Bluesky jc-ia.bsky.social «Decodifica» 26 seguidores; página de Facebook «Decodifica» 7.
Lo de agosto (MiniMax): 5-6 consejos sueltos al día, sin enlace a la web → casi todo con 0 reacciones. No repetirlo.

## Qué se hace (automático, en el móvil viejo)
- Cada día a las 13:15 (mediodía en España, mañana en América): UNA publicación en Bluesky y en Facebook
  (`redes.py publicar`, desde herramientas/tareas_programadas.sh).
  - Prioridad: artículo NUEVO de la web (últimos 10 días). Si no hay, uno de siempre nunca publicado; luego, repetir
    los de hace más de 45 días. Así cada artículo que sacan las tareas de Decodifica sale solo en redes.
  - Siempre con la portada del artículo (la imagen og:image, 1200×630) y el enlace a la web.
  - Texto de Sonnet, solo con lo que dice el artículo: empieza por lo útil, datos concretos, sin exagerar; en Facebook
    acaba con una pregunta para que la gente comente.
- Cada día a las 20:30: UNA publicación de VALOR (Jordi, 14-10: «si solo hacemos publicidad de la web, no aportamos
  valor»). Útil por sí misma, sin necesidad de ir a la web: una tarjeta vertical 1080×1350 con el estilo de las portadas
  (imagen.py) + texto. Tema según el día: lunes prompt para copiar · martes truco paso a paso · miércoles ¿cuál uso? ·
  jueves error común · viernes lo de la semana (solo anuncios oficiales) · sábado herramienta gratis · domingo mito o
  realidad. Datos comprobados en internet (WebSearch/WebFetch) en fuentes oficiales; no repite temas (últimos 40).
  Enlace a la web solo si hay un artículo exactamente sobre lo mismo. (`redes.py valor`)
  Proporción: 1 de valor por cada 1 de artículo; si las cifras dicen que el valor funciona más, se sube el valor.
- Los domingos a las 21:30: cifras de la semana (`redes.py cifras`) → a Jarvis y a estado.json.

## Qué NO se hace, y por qué
- Reddit: publicar enlaces propios de forma automática es lo que más cuentas hace cerrar (normas contra la
  autopromoción). La cuenta guardada es la de Pergaminos Prohibidos. Si se hace, a mano y participando de verdad.
- Grupos de Facebook: la API ya no deja publicar en grupos; se comparte a mano.
- Seguir o contestar a gente de forma automática: parece spam y Bluesky lo castiga. (La ronda del 18-10 NO es
  automática: prepara las respuestas y cada una sale solo si Jordi dice que sí.)

## A revisar (el 28-10-2026, con dos semanas de cifras)
- Si Bluesky no sube: probar una segunda publicación por la tarde (20:30) con un truco corto y una imagen.
- Si una clase de artículo (gratis/precios, comparativas, novedades) va mejor, darle prioridad.
- Ideas que necesitan a Jordi: compartir a mano en 2-3 grupos de Facebook de IA en español; fijar un mensaje de
  presentación en Bluesky; poner en la web los botones de seguir en Bluesky y Facebook.

Claves: ~/.secretos/redes/ (copia de .minimax/credentials del disco del PC). Registro: registro.txt; estado.json.

## Reel de ejemplo oficial (Jordi, 21-10-2026)
/data/data/com.termux/files/home/decodifica-reels/_EJEMPLO_OFICIAL/ (la prueba 3D del 18-10, publicada el 21-10). Los reels tienen que salir como ese; si uno sale distinto, se compara con él.
