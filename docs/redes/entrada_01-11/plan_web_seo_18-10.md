---
tipo: propuesta
creado: 2026-10-18
estado: borrador para Jordi (solo investigado: no se ha cambiado nada en el repositorio, en las rutinas ni en la web)
parte de: «2026-10-18 · Tres planes de crecimiento (encargo)», punto 3
---
# Plan de posicionamiento de decodifica.net (Google)

**Para Jordi, en corto.**
- Hoy Google casi no enseña la web: **unas 400 apariciones a la semana y 4-6 clics** (3 meses: 3.220 apariciones, 27 clics).
  De los 19 clics del último mes, **14 vienen de tres páginas**: Claude Skills, la portada y el generador de prompts.
- El agente de los lunes elige temas por volumen («claude ia», «ollama», «lm studio», «n8n»). Los cuatro artículos
  de octubre **aún no están ni en Google** (0 apariciones; uno lleva 11 días publicado). En esas búsquedas sale primero la
  web oficial, con la respuesta de la IA de Google encima.
- La web está repartida en 7 temas y **casi la mitad de sus páginas son fichas cortas** (de 100 a 400 palabras). Google
  ha dejado 46 páginas fuera (9 las ha leído y ha decidido no enseñarlas).
- Propuesta: **pocos temas, a fondo y enlazados**. Dos grupos para crecer (**Claude en español** e **IA en tu ordenador**),
  uno para cuidar (**prompts y el generador**) y uno opcional que hace de puente con tu casa (**IA en casa sin nube**).
  Cada grupo tiene una página principal (la llamo «pilar») y artículos de apoyo que la enlazan. Se recogen las fichas
  cortas. El agente de los lunes deja de elegir por volumen y sigue un mapa (`docs/plan-seo.md`).
- **El tema de la casa sin red:** es el mejor candidato a largo plazo: cada visita vale más, lo escrito no caduca y nadie
  tiene datos reales de una casa como la tuya. Pero lo recomiendo **en una web aparte, empezando en enero**, no dentro de
  Decodifica. Lo decides tú (apartado 2.3).
- No se ha gastado nada: ni Semrush ni Ahrefs (tampoco hacen falta). Se ha usado Search Console, el planificador de Google
  Ads de octubre y 28 búsquedas reales en Google con el Chrome del móvil viejo.

---

## 1. Diagnóstico con datos

### 1.1 Las cifras
Fuentes: el informe automático del repositorio (`data/gsc_weekly/`, el último es del 12-10 con datos hasta el 09-10) y
Search Console abierto hoy con tu sesión en el Chrome del móvil viejo (datos hasta el 15-10-2026).

| Periodo | Apariciones | Clics | % que pulsa (CTR) | Posición media |
|---|---|---|---|---|
| 3 meses (16-07 → 15-10) | 3.220 | 27 | 0,8 % | 8,3 |
| 28 días (18-09 → 15-10) | 1.620 | 19 | 1,2 % | — |
| 7 días (09-10 → 15-10) | 407 | 4 | 1,0 % | 7,8 |
| 7 días (03-10 → 09-10) | 417 | 6 | 1,4 % | 7,5 |

Por países (28 días hasta el 03-10): España 293, México 269, Perú 168, Colombia 148, Argentina 99, Chile 69, Venezuela 67.
Por aparatos: ordenador 906 y móvil 595.

### 1.2 Lo que dicen
1. **Google esconde casi todas las búsquedas.** En 3 meses solo enseña 49 búsquedas distintas. La de la semana del 03-10
   enseña 7, que suman 99 de 417 apariciones (**el 76 % queda oculto**, porque cada una la buscan muy pocas personas). En
   Claude Skills, que es la mejor página (647 apariciones y 10 clics en 3 meses), **no se ve ni una búsqueda**. Por eso el
   agente, con el informe de 7 días, no ve qué se busca y se va al planificador: ahí ganan las búsquedas enormes. **Hay
   que planificar por páginas y por temas, no por búsquedas sueltas.**
2. **«decodifica» no es tu marca para Google.** Es la búsqueda que más sale (527 apariciones y 4 clics en 3 meses), en
   posición 7: es una palabra corriente («decodificar»). No merece trabajo.
3. **Pocas páginas traen algo.** En 28 días: Claude Skills 382 apariciones y 7 clics; portada 160 y 4; generador de
   prompts 72 y 3. Con apariciones pero 0 clics: `deepseek-app-oficial-espanol` (91), `ia-organiza-pendientes` e
   `ia-mejora-excel` (14-18 a la semana).
4. **Lo que se hizo por volumen no ha entrado.** `lm-studio-que-es-como-usar` y `n8n-que-es-gratis` (del 07-10) y
   `claude-ia-que-es-gratis` y `ollama-que-es-como-usar` (del 12-10): **0 apariciones** y, buscándolas con «site:»,
   **Google no las tiene todavía**.
5. **Emergent se ha caído.** «emergent ia» dio 150 apariciones en septiembre (posición 9,7). Desde el 03-10 no aparece y
   hoy no está en la primera página. El artículo se rehízo el 06-10. No se puede saber si fue por el cambio o por Google:
   el informe de mañana lo dirá. Que el agente de los jueves no lo toque más hasta verlo.
6. **Google valora la web entera, y la mitad es fina** (contado hoy en la web publicada):

| Tipo de página | Cuántas | Palabras | Apariciones en 28 días |
|---|---|---|---|
| Fichas «X: guía práctica y cuándo usarla» | ~36 | 250-400 | casi todas < 10 |
| Comparativas (`/herramientas/comparativas/`) | 8 | 220-240 | `manus-vs-chatgpt-apps` 38; `chatgpt-vs-gemini` en la posición 78 |
| Casos («Herramientas IA para…») | 8 | ~200 | 1-2 |
| Workflows | 5 | 160-190 | 1-3 |
| Herramientas (generador, evaluador, preflight) | 3 | 96-129 | el generador 72 |
| Artículos del blog | 33 | 650-4.500 | casi todo lo que hay |

   Informe «Indexación de páginas» (12-10): **95 páginas en Google y 46 fuera**: 9 «rastreada: actualmente sin
   indexar» (Google las leyó y no las quiso), 10 «descubierta: sin indexar» (ni las ha leído), 12 redirecciones, 12
   canónicas y 3 con noindex (las tres últimas cosas son normales). Que los artículos nuevos tarden más de 10 días en
   entrar es otra señal de que Google le da poca prioridad a la web.
7. **Por temas** (páginas agrupadas a mano, 28 días hasta el 03-10):

| Tema | Apariciones | Clics | Posición |
|---|---|---|---|
| Oficina (Excel, presentaciones, reuniones, pendientes) | 317 | 4 | 7,1 |
| **Claude** | 310 | **7** | 7,4 |
| Crear apps y agentes (sobre todo Emergent) | 221 | 1 | 9,1 |
| IA china y gratis | 210 | 1 | 7,3 |
| **Prompts** | 69 | 1 | **4,9** |
| IA local y privada | 28 | 0 | 8,4 |
| (Páginas fijas y «decodifica») | 394 | 3 | 8,2 |

   Claude es lo único que da clics de forma constante. Los prompts salen más arriba que nada (el generador está en la
   posición 1-2 para «páginas para crear prompts» y parecidas). La IA local casi no sale todavía, pero sus artículos
   nuevos aún no están en Google.

---

## 2. Dónde se puede ganar

### 2.1 Quién sale en Google
28 búsquedas hechas hoy en google.com (España; dos con México), con el Chrome del móvil viejo. Ojo: es una muestra
y los resultados están personalizados (tu sesión, Sabadell). Volúmenes del planificador de Google Ads (07-10-2026),
por tramos (50 / 500 / 5.000…), **España / Latinoamérica**.

| Búsqueda | Volumen ES / LatAm | Quién sale arriba | ¿Se le puede ganar? |
|---|---|---|---|
| claude en español | 500 / 5.000 («claude ai español») | docs oficiales, claude.ai y después **blogs pequeños** (aicad.es, uxdivi, mentoraia) | **sí** |
| prompts para claude | 500 / 500 | blogs pequeños (luzzidigital, donweb, berzerk), ayuda oficial | **sí** |
| claude vs chatgpt | 500 / 500 | luzzidigital, gurusup, ionos, zapier, datacamp | medio |
| claude code para principiantes | (sin dato) | docs oficiales, un libro de Amazon, nxcode, datos.ninja | **sí** |
| claude skills | 5.000 / 5.000 (+9.900 % en un año) | ayuda y docs oficiales, tododeia, listas en inglés | ya estamos (pos. ~7,6) |
| ia local | 500 / 500 | manz.dev, ialocal.org, levanteapp, Xataka, coolmod, sedic | **sí** |
| ollama en español | (marca: 50.000) | ollama.com, iacedemy, lenguajejs, Univ. de Granada | **sí** |
| lm studio como usar | (marca: 50.000) | apidog, datacamp, onlyoffice, academias | medio |
| asistente de voz local | (sin dato) | tiendas de domótica, noticias.ai, promptquorum, wiki de Seeed | **sí** |
| ia en casa sin nube | 50 / 50 («ia en casa») | yaps.ai, javadex, pochocosta, okdiario | **sí** |
| generador de prompts | 500 / 5.000 | webs que son herramientas (jotform, generateprompt, promptsera) | ya estamos (pos. ~4) |
| prompts para gemini fotos (MX) | 500 / 5.000 | webs de apps de fotos (openart, hitpaw, seaart) | difícil y de poco valor |
| ia para excel (ES y MX) | 500 / 5.000 | Microsoft, iaexcel, Kimi, Julius (los que venden) | **no** |
| mejor ia para hacer presentaciones | 500 / 500 | Gamma, Genially, Slidesgo (los que venden) | **no** |
| ia para resumir reuniones | — | read.ai, tldv, notta (los que venden) | **no** |
| deepseek en español | 500 / 5.000 | webs copia de DeepSeek, la oficial, El Mundo | **no** |
| alternativas a chatgpt gratis | 500 / 500 | Xataka, datacamp, manus.im | **no** |

**La respuesta de la IA de Google sale arriba en las 19 búsquedas de IA** (en las de la casa, en 6 de 9). Eso quita
clics en «qué es X»: gana quien responde algo concreto que el resumen no da (pasos, «cuál elijo si…», límites del plan
gratis en tu país, problemas típicos).

### 2.2 Los grupos (dificultad y valor)

| Grupo | Lo que ya hay | Dificultad | Valor | Propuesta |
|---|---|---|---|---|
| **A. Claude en español** (para quien no programa) | Claude Skills (la mejor página), guía de Claude (nueva), emails con Claude, alternativas a Fable 5, `chatgpt-vs-claude` (844 palabras), ficha de Claude | media: primero la web oficial; después, blogs pequeños | medio (puja 0,25-2 €); interés creciendo mucho (+900 % «claude ia», +9.900 % «claude skills») | **crecer** |
| **B. IA en tu ordenador** (local y privada) | Ollama, LM Studio, Presidio, Qwen3-ASR, Odysseus, Hermes, fichas de Ollama y AnythingLLM, caso «IA local» | baja (anunciantes casi nulos: índice 2-12 de 100) | medio; caduca poco | **crecer** |
| **C. Prompts y el generador** | generador (pos. 1-2), prompts para webs, Nano Banana, evaluador | baja en lo largo («páginas para crear prompts») | bajo-medio | **cuidar** (mejorar lo que hay, poco nuevo) |
| **D. IA en casa sin nube** (puente con la casa) | nada | baja: blogs pequeños | medio; **tu experiencia real** (Jarvis en un móvil viejo, voz, la casa) | **opcional, lo decides tú** |
| Oficina (Excel, presentaciones, reuniones) | 6 artículos largos y 15 fichas | alta: ganan los que venden | medio | solo lo hace el agente de los jueves; nada nuevo |
| IA china, «IA gratis», crear apps, novedades sueltas | 12 artículos | alta y caduca en semanas | bajo | nada nuevo; se cuida lo que tiene apariciones |

### 2.3 El tema de la casa sin red, comparado con la IA práctica

Ojo: el 07-10-2026 elegiste «solo IA práctica» y dejaste la casa para más adelante, quizá en una web aparte. Esto no lo
cambia: lo pone en cifras para que vuelvas a decidir. ^d-web-1007-nicho

| | IA práctica (Decodifica) | Casa sin red (solar, baterías, reguladores, domótica barata) |
|---|---|---|
| Búsquedas al mes sin marcas (planificador) | ES ~140.000 / LatAm ~330.000 | ES ~43.000 / LatAm ~74.000 (+ domótica 19.000 / 64.000) |
| Lo que pagan los anunciantes por visita | mediana 1,21 € | mediana 0,97 €; «placas solares con batería» 0,5-3,1 € y «placas para casa» 0,7-4,2 € |
| Anunciantes compitiendo | baja-media | **alta en el 94 % de las búsquedas** (ahí hay dinero) |
| Afiliados | pocos, casi todos en inglés | tiendas: p. ej. ALLPOWERS en Awin, 5 %, compra media ~500 € (hay que confirmarlo al darse de alta) |
| Quién sale en Google | webs oficiales y blogs; en oficina, los que venden | **tiendas e instaladores** (Autosolar, Teknosolar, Cambio Energético, SotySolar) y blogs pequeños; en «monitorizar batería solar» **solo tiendas** |
| Respuesta de IA arriba | 19 de 19 | 6 de 9 (no sale en «regulador mppt o pwm», «batería lifepo4…» ni «monitorizar batería solar») |
| Cuánto dura un artículo | meses (precios y versiones cambian) | años |
| Experiencia real (Google la premia) | se puede, si documentas tu uso de Claude Code y Jarvis | **única**: CasaSolar tiene datos diarios de voltaje, consumo, reserva y generador de una casa aislada de verdad |
| Lo que ya hay | 33 artículos y 95 páginas en Google | nada: una web nueva tarda 3-6 meses en salir |
| Lo que pide de ti | casi nada (los agentes) | fotos y alguna comprobación tuya (~30 min/semana) |

**Recomendación:**
1. **Decodifica sigue en IA práctica, pero concentrada**: grupos A y B para crecer, C para cuidar. Si quieres, también
   el D: es IA y estrena tu experiencia sin abrir otra web.
2. **La casa sin red sí, pero en una web aparte, desde enero de 2027**, empezando con 5 guías hechas con los datos
   reales de CasaSolar. Ideas: «Cuánto aguanta una batería de litio de 200 Ah en una casa aislada: datos de 30 días»,
   «Regulador MPPT: qué mide de verdad (Epever)», «Vigilar la batería solar con un móvil viejo», «Lo que gasta una casa
   sin red, aparato por aparato», «Batería de reserva y generador: cuándo hacen falta». Las búsquedas grandes («batería
   lifepo4», «placas solares precio») son de las tiendas y no se les gana. Se gana con lo que nadie más puede contar.
3. **No** meter placas y baterías dentro de Decodifica: Google premia las webs centradas en un tema, y mezclar ChatGPT con
   reguladores debilitaría las dos.
4. Cuándo empezar la web de la casa: cuando Decodifica lleve unas 8 semanas con este plan sin necesitarte más que para
   aprobar, o antes si te apetece dedicarle esa media hora a la semana.

---

## 3. Plan de posicionamiento

### 3.1 Pilares y apoyos
Un **pilar** es la guía grande del grupo: responde a lo general y enlaza a todos sus apoyos. Un **apoyo** responde a una
pregunta concreta, enlaza al pilar en el primer párrafo y en «Sigue leyendo», y enlaza a 1-2 apoyos hermanos.

**Grupo A · Claude en español**
- Pilar: **`/blog/claude-ia-que-es-gratis/`**, convertido en «Claude en español: guía completa (gratis, planes y cómo
  usarlo)». Como aún no está en Google, cambiarlo no pierde nada. Claude Skills sigue siendo su propio apoyo fuerte
  (no se toca su dirección).
- Apoyos que ya hay: `claude-skills-1000-gratis`, `claude-emails-sonar-humanos`, `alternativas-fable-5`,
  `/herramientas/chatgpt-vs-claude/`.
- Apoyos nuevos (por orden; el agente comprueba antes en la web oficial que cada función existe hoy y cómo se llama):
  1. Prompts para Claude con ejemplos (y cómo escribirlos según su guía oficial).
  2. Claude Code sin saber programar: primeros pasos. (Si quieres, con tu experiencia documentada: capturas tuyas.)
  3. Límites del plan gratis de Claude y cómo aprovecharlos.
  4. Proyectos de Claude: qué son y para qué sirven.
  5. Claude vs Gemini: cuál elegir según para qué.
  6. Conectores de Claude explicados sin jerga.
  7. Crear tu primera skill paso a paso (solo si no pisa a Claude Skills; si la pisa, va como sección dentro).

**Grupo B · IA en tu ordenador**
- Pilar nuevo: «IA local en español: cómo usar IA en tu ordenador sin internet» (qué programa elegir según tu
  ordenador, qué se puede hacer y qué no, privacidad).
- Apoyos que ya hay: `ollama-que-es-como-usar`, `lm-studio-que-es-como-usar`, `2026-07-25-ia-local-oculta-datos`
  (Presidio), `2026-08-01-qwen3-asr-transcribe-espanol`, `odysseus-pewdiepie-ia-gratis`, `2026-07-17-hermes-agent-chino`.
- Apoyos nuevos:
  1. Ollama o LM Studio: cuál elegir.
  2. Qué ordenador hace falta para la IA local (memoria y tarjeta gráfica, con las cifras oficiales de cada modelo).
  3. Chatear con tus PDF sin subirlos a internet (AnythingLLM).
  4. Pasar audio a texto en tu ordenador (Whisper y similares).
  5. Modelos que funcionan bien en español en local (con datos publicados, nunca «lo hemos probado» sin prueba tuya).

**Grupo C · Prompts y el generador (cuidar)**
- Pilar: **`/herramientas/generador-prompts/`**. Hoy tiene 129 palabras: se mantiene la herramienta arriba y debajo se
  añade una guía corta («cómo hacer un buen prompt», 5 ejemplos, errores típicos), 600-900 palabras con fuentes oficiales.
- Apoyos: `2026-07-16-prompts-secretos-web`, `2026-07-22-nano-banana-1000-prompts`, `/herramientas/evaluador/`.
- Nuevo, como mucho uno: «Cómo hacer un prompt: guía con ejemplos» (500 / 500 búsquedas; salen blogs y una biblioteca
  chilena). Los «prompts para fotos» no: ganan las apps de fotos y aportan poco.

**Grupo D · IA en casa sin nube (opcional, lo decides tú)**
- Pilar: «Asistente de voz con IA en casa, sin nube».
- Apoyos: Home Assistant con IA local · un asistente con un móvil viejo (tu Jarvis, contado con capturas y datos tuyos) ·
  avisos de la casa al móvil sin servicios de pago.
- Solo con pruebas tuyas: es lo que lo hace único y lo que la regla 3 exige.

### 3.2 Los enlaces
- Cada apoyo: enlace al pilar en el «En resumen» o en el primer párrafo, y en «Sigue leyendo».
- Cada pilar: una lista «Guías de este tema» con todos sus apoyos (se añade cada apoyo nuevo).
- Portada y `/blog/`: un bloque «Empieza aquí» con los 2-3 pilares. Ya existen los filtros `tema` (`chatbots`, `local`…):
  el pilar de cada grupo va el primero en su filtro.
- Desde las páginas fuertes (Claude Skills, generador) se enlaza a su pilar: así Google llega antes a lo nuevo.

### 3.3 Qué fusionar, rehacer o quitar
Regla de la casa: **nada con apariciones se borra sin redirigir**. La lista final la saca el agente del repaso mensual
con los datos de 3 meses por página. Lo de abajo se basa en los datos de hoy.

| Qué | Qué se hace |
|---|---|
| Fichas de los grupos A y B (`/herramientas/claude/`, `/ollama/`, `/anythingllm/`, `/casos/para-ia-local-abierta/`) | **Fusionar** en su pilar o apoyo, con redirección 301 |
| Fichas, comparativas, casos y workflows **sin apariciones en 3 meses** | **noindex** (se quedan en la web para quien llegue navegando; Google deja de juzgarlas) hasta que alguien las amplíe |
| Comparativas finas con apariciones (`manus-vs-chatgpt-apps` 38, `kimi-vs-glm` 7) | se quedan; el agente de los jueves las amplía solo si caen en un grupo |
| `/herramientas/comparativas/chatgpt-vs-gemini/` (posición 78, 240 palabras) | noindex, o fusionar en un «ChatGPT vs Claude vs Gemini» si el grupo A lo necesita |
| Workflow `reunion-a-decisiones-y-tareas` | fusionar en `ia-resumir-reuniones-tareas-revisables` (mismo tema) |
| Artículos largos de oficina (`ia-mejora-excel` 3.880 palabras, `ia-organiza-pendientes` 4.514, `ia-crea-presentaciones` 4.063) | no crecer; el jueves mejora título y respuesta corta; `ia-organiza-pendientes` sigue en la cola por el «caso real» sin prueba |
| Novedades viejas (Hy3, Kimi K3, Higgsfield, Google Maps con Gemini) | se quedan mientras tengan apariciones; nada nuevo de ese tipo fuera de los grupos |
| Emergent | no tocar hasta ver el informe del lunes 19-10 |

Calculado a ojo: unas **35-45 páginas a noindex o fusionadas** de 110. Va en **un solo pull request de «poda»** para que lo
apruebes viendo la lista.

### 3.4 El ritmo
- **Semana 1** (lunes 26-10, si apruebas antes): `docs/plan-seo.md` en el repositorio, el pilar A (rehacer la guía de
  Claude) y el pull request de la poda.
- **Semana 2:** el pilar B y la guía del generador (pilar C).
- **Semanas 3-12:** **2 piezas por semana**: normalmente 1 apoyo nuevo y 1 mejora o fusión, alternando A y B (y D si
  lo apruebas). Unos 10 apoyos nuevos en 10 semanas, todos dentro de los grupos.
- Novedades (martes y viernes): solo si caen dentro de un grupo; si no, no se escriben.
- Jueves: primero artículos de los grupos.
- Pide a Google que mire los pilares: en Search Console, «Inspección de URLs» → «Solicitar indexación» (1 minuto por
  dirección; lo puedes hacer tú o se le puede pedir a Jarvis con el navegador compartido).

### 3.5 Cómo cambia el agente de los lunes (texto exacto propuesto)

**a) En el repositorio, `docs/AGENTE-SEMANAL.md`: el paso 3 entero se cambia por esto:**
```
3. **Elegir el trabajo con docs/plan-seo.md** (el mapa de temas que aprobó Jordi):
   - Solo se escribe dentro de sus grupos, aunque fuera haya búsquedas con mucho más volumen.
   - Cada semana, 2 piezas del grupo que toque: si su pilar no está hecho, el pilar primero; si
     no, la siguiente de su cola (nueva) y una mejora o fusión de una página del mismo grupo.
   - Antes de escribir, mira los diez primeros de Google para esa búsqueda (España y México). Si
     solo salen la web oficial, medios grandes o quienes lo venden, y no hay nada concreto en que
     ganarles, pasa a la siguiente de la cola y dilo en el informe.
   - Nunca una búsqueda de marca sola («claude ia», «ollama», «deepseek»): esas las gana la web
     oficial. Se eligen preguntas concretas («ollama o lm studio», «límites de claude gratis»).
   - Cada pieza enlaza a su pilar en el primer párrafo y en «Sigue leyendo», y se añade a la
     lista del pilar.
   - Al acabar, marca en docs/plan-seo.md lo hecho y apunta ideas nuevas al final de la cola (no
     las escribas: Jordi las ve en el pull request).
```
**b) En `rutinas_web.json`, prompt de `deco-semanal`, después del punto 2, una línea:**
```
2b. Esta semana manda docs/plan-seo.md: elige solo de su cola (paso 3 de docs/AGENTE-SEMANAL.md), nunca por volumen de búsqueda.
```
**c) En el informe y en el resumen para Jordi, una línea:** «- cómo va cada grupo de docs/plan-seo.md (apariciones,
clics y páginas en Google) y qué pieza toca la semana que viene.»

**d) En los otros agentes, una línea a cada uno:**
- `deco-jueves`, punto 4: «Elige primero artículos de los grupos de docs/plan-seo.md.»
- `deco-novedades`, punto 4: «Solo si la novedad cae dentro de un grupo de docs/plan-seo.md; si no, no escribas.»
- `deco-mensual`, punto 5: «Saca la tabla por grupos (apariciones, clics, posición y páginas en Google, 28 días) y la lista
  de páginas sin apariciones en 3 meses (candidatas a noindex). Apúntalo en docs/repaso-mensual/.»

**e) `docs/plan-seo.md` (nuevo, ~3 KB):** los grupos con su pilar, sus apoyos (hechos ✔ o en cola), qué páginas cuenta
cada grupo (para medir) y la regla de oro: «Mejor una búsqueda pequeña que podemos ganar que una enorme que no».

Encaja con la otra propuesta de hoy («Web y redes más ambiciosas»): las cuatro preguntas y «mira los diez primeros» son la
misma idea. Si se aprueban las dos, el paso 3 de arriba sustituye a la línea 2b de aquella.

---

## 4. Lo técnico (solo lo que pesa)

1. **El informe de Search Console ve muy poco** (pesa mucho). Con 7 días se esconde el 76 % de las búsquedas. Propuesta,
   en un pull request aparte (los agentes no tocan los workflows):
   - que el flujo también guarde **28 y 90 días** (`latest_28d.json` y `latest_90d.json`; el script ya acepta `DAYS_BACK`);
   - que se ejecute en un minuto que no sea en punto (`'17 4 * * 1'`): el 12-10, el de las 07:00 corrió a las 16:29 UTC,
     después de que el agente de las 13:52 acabara sin datos.
2. **Indexación lenta y páginas finas** (pesa mucho): lo arreglan la poda (3.3) y los enlaces internos (3.2). Que el
   repaso mensual apunte cada mes el número de páginas en Google y fuera.
3. **Enlaces internos de pilar a apoyos** (pesa): apartado 3.2.
4. **Plantilla de títulos de las fichas** («X: guía práctica y cuándo usarla», igual en 36 páginas): pesa poco. Solo se
   cambia en las fichas que se queden indexadas.
5. **No hace falta tocar:** datos estructurados (ya hay un `Article` por página, `FAQPage`, `Organization`, 0 errores en el
   validador del 14-10), velocidad (LCP < 1 s en el móvil), sitemap con `lastmod`, robots y `llms.txt`.

---

## 5. Cómo medir si funciona

**Punto de partida** (Search Console, 28 días hasta el 15-10-2026): 1.620 apariciones, 19 clics, CTR 1,2 %; 95 páginas en
Google y 46 fuera. Por grupos (28 días hasta el 03-10): Claude 310 / 7 clics; IA local 28 / 0; prompts 69 / 1.

**Qué se mide, cada grupo por separado** (usando qué páginas son de cada grupo según `docs/plan-seo.md`):
apariciones, clics, posición media, cuántas de sus páginas tienen al menos una aparición y cuántas están en Google.
Y en toda la web: páginas en Google y páginas «rastreadas sin indexar».

**Cómo se compara:** siempre **28 días contra 28 días**, y por páginas, no por búsquedas (la mayoría están ocultas).
- Antes: 28-09 → 25-10-2026.
- Primera comparación: los 28 días que acaban 8 semanas después de empezar (~21-12-2026). Antes no se nota: las páginas
  nuevas tardan en entrar.
- Revisión grande: a las 12 semanas (~18-01-2027). Ojo con Navidad: en esos días se busca menos.

**Objetivos a 12 semanas** (realistas para una web de este tamaño):
- grupos A y B: de ~340 a **más de 1.000 apariciones en 28 días**, y de ~7 a **25 clics o más**;
- todo artículo nuevo, en Google en **14 días como mucho**;
- menos de 5 páginas «rastreada: actualmente sin indexar».

**Cada cuánto se mira:**
- cada lunes, una línea por grupo en el informe del agente (sin sacar conclusiones con una semana);
- cada mes (día 20), la tabla por grupos del repaso mensual;
- a las 12 semanas, decides tú: el grupo que no haya doblado sus apariciones se cambia; si va bien, se sube el ritmo o
  se arranca la web de la casa.

---

## 6. Lo que tienes que decidir
1. ¿Te parecen bien los grupos? A (Claude en español) y B (IA en tu ordenador) para crecer, C (prompts) para cuidar.
2. ¿Añadimos el grupo D (IA en casa sin nube, con tu experiencia y capturas tuyas)?
3. ¿La poda? Unas 35-45 páginas finas a noindex o fusionadas, en un pull request que verás antes con la lista.
4. ¿Se cambia el agente de los lunes como en 3.5? Y ¿se amplía el informe de Search Console a 28 y 90 días con la hora
   nueva? (Es un pull request aparte; lo apruebas tú.)
5. El tema de la casa sin red: ¿web aparte desde enero (lo que recomiendo), ahora, o no?

No hace falta Semrush ni Ahrefs: las cuentas gratuitas no dan datos (lo dice `_ESTADO.md`) y con Search Console, el
planificador y mirar Google basta. Si un día se quiere medir la dificultad con números, se pregunta antes.

**Límites de este estudio:** las búsquedas en Google son una muestra de 28, personalizada (tu sesión, Sabadell). Los
volúmenes del planificador van por tramos y son de antes de octubre. Las apariciones por grupo se sumaron a mano por
páginas. Los cuatro artículos de octubre llevan poco tiempo publicados: no se juzgan aún, solo se ve que no han entrado.
