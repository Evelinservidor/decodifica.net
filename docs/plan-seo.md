# Plan SEO de Decodifica: el mapa de temas

Aprobado por Jordi el 18-10-2026 («vamos a hacer todo lo que propones»). Lo siguen **todos los agentes** (lunes,
novedades, jueves y repaso mensual) antes de elegir qué escribir o qué mejorar. El estudio completo con los datos está en
la propuesta del 18-10-2026 (Search Console, planificador de Google Ads y 28 búsquedas reales en Google).

**Regla de oro: mejor una búsqueda pequeña que podemos ganar que una enorme que no.**

## Por qué este plan
- Google enseña poco la web (28 días hasta el 15-10-2026: 1.619 apariciones y 19 clics) y casi todo viene de tres
  páginas: Claude Skills, la portada y el generador de prompts.
- Lo que se escribió por volumen de búsqueda («claude ia», «ollama», «lm studio», «n8n») no ha entrado en Google: en
  esas búsquedas gana la web oficial.
- La mitad de la web son fichas cortas. Google valora la web entera: mejor pocos temas, a fondo y bien enlazados.

## Cómo se trabaja
- **Solo se escribe dentro de los grupos de abajo**, aunque fuera haya búsquedas con mucho más volumen.
- Cada grupo tiene una **guía principal** (la llamamos «pilar»: responde a lo general y enlaza a todos sus apoyos) y
  **artículos de apoyo** (cada uno responde a una pregunta concreta).
- Nunca una búsqueda de marca sola («claude ia», «ollama», «deepseek»): se eligen preguntas concretas («ollama o lm
  studio», «límites de claude gratis»).
- Antes de escribir, mirar los diez primeros de Google (España y México). Si solo salen la web oficial, medios grandes o
  quienes lo venden, y no hay nada concreto en que ganarles, pasar a la siguiente de la cola y decirlo en el informe.
- Las reglas de la casa de `docs/AGENTE-SEMANAL.md` siguen igual: fuentes originales comprobadas, nada de relleno, nunca
  «lo he probado» sin prueba de Jordi, sin sensacionalismo.

## Los enlaces entre páginas
- **Cada apoyo** enlaza a su pilar en el «En resumen» o en el primer párrafo, y otra vez en «Sigue leyendo»; y enlaza a
  1-2 apoyos hermanos del mismo grupo.
- **Cada pilar** tiene una lista «Guías de este tema» con todos sus apoyos. Al publicar un apoyo nuevo, se añade ahí.
- Portada y `/blog/`: un bloque «Empieza aquí» con los pilares. En el filtro de su tema, el pilar va el primero.
- Desde las páginas fuertes (Claude Skills, el generador) se enlaza a su pilar: así Google llega antes a lo nuevo.

## Grupo A · Claude en español (para quien no programa) — CRECER
- **Pilar:** `/blog/claude-ia-que-es-gratis/`, que se convertirá en «Claude en español: guía completa (gratis, planes y
  cómo usarlo)». Su dirección no cambia.
- **Apoyos que ya hay:** ✔ `/blog/claude-skills-1000-gratis/` (la página más fuerte de la web; su dirección no se toca) ·
  ✔ `/blog/claude-emails-sonar-humanos/` (revisado el 19-10-2026) · ✔ `/blog/alternativas-fable-5/` · ✔ `/herramientas/chatgpt-vs-claude/`
- **Cola de apoyos nuevos** (en este orden; antes de escribir, comprobar en la web oficial que la función existe hoy y
  cómo se llama):
  - [x] ✔ (19-10-2026) Pilar: rehacer `/blog/claude-ia-que-es-gratis/` como guía completa («Claude en español: guía completa, gratis y planes»)
  - [ ] Prompts para Claude con ejemplos (y cómo escribirlos según su guía oficial)
  - [ ] Claude Code sin saber programar: primeros pasos
  - [ ] Límites del plan gratis de Claude y cómo aprovecharlos
  - [ ] Proyectos de Claude: qué son y para qué sirven
  - [ ] Claude vs Gemini: cuál elegir según para qué
  - [ ] Conectores de Claude explicados sin jerga
  - [ ] Crear tu primera skill paso a paso (solo si no pisa a Claude Skills; si lo pisa, va como sección dentro)
  - [ ] Idea (19-10-2026): Memoria de Claude y chats de incógnito: qué recuerda y cómo borrarlo (el centro de ayuda lo explica con detalle; hoy es solo un apartado del pilar)

## Grupo B · IA en tu ordenador (local y privada) — CRECER
- **Pilar (nuevo):** «IA local en español: cómo usar IA en tu ordenador sin internet» (qué programa elegir según tu
  ordenador, qué se puede hacer y qué no, privacidad).
- **Apoyos que ya hay:** ✔ `/blog/ollama-que-es-como-usar/` · ✔ `/blog/lm-studio-que-es-como-usar/` ·
  ✔ `/blog/2026-07-25-ia-local-oculta-datos/` · ✔ `/blog/2026-08-01-qwen3-asr-transcribe-espanol/` ·
  ✔ `/blog/odysseus-pewdiepie-ia-gratis/` · ✔ `/blog/2026-07-17-hermes-agent-chino/`
- **Cola:**
  - [ ] Pilar: «IA local en español» (nuevo)
  - [ ] Ollama o LM Studio: cuál elegir
  - [ ] Qué ordenador hace falta para la IA local (memoria y tarjeta gráfica, con las cifras oficiales de cada modelo)
  - [ ] Chatear con tus PDF sin subirlos a internet (AnythingLLM; aquí se fusiona la ficha `/herramientas/anythingllm/`)
  - [ ] Pasar audio a texto en tu ordenador (Whisper y similares)
  - [ ] Modelos que funcionan bien en español en local (con datos publicados; nunca «lo hemos probado» sin prueba de Jordi)

## Grupo C · Prompts y el generador — CUIDAR (mejorar lo que hay, poco nuevo)
- **Pilar:** `/herramientas/generador-prompts/` (sale en la posición 1-2 para «páginas para crear prompts»). Se mantiene
  la herramienta arriba y debajo se añade una guía corta (cómo hacer un buen prompt, 5 ejemplos, errores típicos; 600-900
  palabras con fuentes oficiales).
- **Apoyos que ya hay:** ✔ `/blog/2026-07-16-prompts-secretos-web/` · ✔ `/blog/2026-07-22-nano-banana-1000-prompts/` ·
  ✔ `/herramientas/evaluador/`
- **Cola:**
  - [ ] Pilar: la guía corta debajo del generador
  - [ ] Como mucho uno nuevo: «Cómo hacer un prompt: guía con ejemplos». Los «prompts para fotos», no (ganan las apps).

## Grupo D · IA en casa sin nube — PUENTE (después de A y B)
- Solo IA: asistente de voz, Home Assistant con IA local, avisos al móvil sin servicios de pago. **Nada de energía solar,
  baterías ni vida sin red**: eso irá, si acaso, a otra web más adelante (lo decidió Jordi el 18-10-2026).
- Solo con pruebas reales de Jordi (capturas y datos suyos): sin ellas no se escribe.
- **Cola:**
  - [ ] Pilar: «Asistente de voz con IA en casa, sin nube»
  - [ ] Home Assistant con IA local
  - [ ] Un asistente con un móvil viejo (contado con capturas y datos de Jordi)
  - [ ] Avisos de casa al móvil sin servicios de pago

## Fuera de los grupos (no se escribe nada nuevo)
- Oficina (Excel, presentaciones, reuniones, pendientes): ganan los que venden. Solo lo cuida el agente de los jueves.
- IA china, «IA gratis», crear apps, novedades sueltas: caducan en semanas. Se cuida lo que ya tiene apariciones.
- Emergent: no tocar hasta ver cómo sale en el informe del 19-10-2026.
- Las novedades (martes y viernes) solo si caen dentro de un grupo; si no, no se escriben.

## El ritmo
- **Semana 1** (desde el 19-10-2026): este mapa, el pilar A y la limpieza de páginas finas (un pull request aparte
  que aprueba Jordi).
- **Semana 2:** el pilar B y la guía del generador (pilar C).
- **Semanas 3-12:** **2 piezas por semana**, siempre dentro de los grupos: normalmente **1 apoyo nuevo y 1 mejora o
  fusión** de una página del mismo grupo, alternando A y B (D cuando A y B tengan su pilar).
- Al acabar cada pieza, marcarla aquí con ✔ (y la fecha). Las ideas nuevas van al final de su cola, sin escribirlas:
  Jordi las ve en el pull request.
- Avisar a Google: desde el 19-10-2026 el sitemap se reenvía solo a Search Console después de cada publicación
  (`deploy.yml` → `scripts/gsc_enviar_sitemap.py`; el robot tiene «Acceso total»). El botón «Solicitar indexación» no
  tiene API: no se le pide a Jordi cada semana. Solo si un artículo lleva más de 14 días fuera de Google (lo dice
  `latest_indexacion.md`), el informe lo apunta y Jordi (o Jarvis con el navegador compartido) lo pide a mano.

## Cómo se mide
Siempre **28 días contra 28 días**, **por grupos y por páginas** (no por búsquedas sueltas: Google esconde la mayoría).
El informe de los lunes guarda `data/gsc_weekly/latest_28d.json`, `latest_90d.json` y `latest_indexacion.json` (qué
páginas están en Google).

**Qué se mide de cada grupo:** apariciones, clics, posición media, cuántas de sus páginas tienen al menos una aparición y
cuántas están en Google. Y de toda la web: páginas en Google y páginas «rastreada: actualmente sin indexar».

**Punto de partida** (28 días del 18-09 al 15-10-2026; en Google, a 18-10-2026):

| Grupo | Apariciones | Clics | Posición | Páginas con apariciones | En Google |
|---|---|---|---|---|---|
| A · Claude | 393 | 8 | 7,7 | 4 de 6 | 4 de 6 |
| B · IA en tu ordenador | 29 | 0 | 8,1 | 5 de 9 | 5 de 9 |
| C · Prompts | 83 | 3 | 4,0 | 3 de 4 | 3 de 4 |
| Toda la web | 1.619 | 19 | — | — | 92 de 110 (6 «rastreada sin indexar») |

Para medir, cada grupo cuenta sus páginas de arriba (pilar y apoyos, ✔ o nuevos) y, mientras existan, sus fichas:
A `/herramientas/claude/`; B `/herramientas/ollama/`, `/herramientas/anythingllm/`, `/herramientas/casos/para-ia-local-abierta/`.

**Cuándo se compara:**
- Antes: 28-09 → 25-10-2026.
- **Primera comparación: hacia el 21-12-2026** (los 28 días que acaban 8 semanas después de empezar). Antes no se nota:
  las páginas nuevas tardan en entrar.
- Revisión grande: a las 12 semanas (~18-01-2027). Ojo con Navidad: esos días se busca menos.

**Objetivos a 12 semanas:**
- grupos A y B juntos: de ~420 a **más de 1.000 apariciones en 28 días**, y de ~8 a **25 clics o más**;
- todo artículo nuevo, en Google en **14 días como mucho**;
- menos de 5 páginas «rastreada: actualmente sin indexar».

**Cada cuánto se mira:**
- cada lunes, una línea por grupo en el informe del agente (sin sacar conclusiones con una semana);
- cada mes (día 20), la tabla por grupos en `docs/repaso-mensual/` y la lista de páginas sin apariciones en 3 meses;
- a las 12 semanas decide Jordi: el grupo que no haya doblado sus apariciones se cambia; si va bien, se sube el ritmo.

## Ideas para más adelante (no escribir sin que entren en un grupo)
- (vacío)
