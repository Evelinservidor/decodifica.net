---
tipo: propuesta
creado: 2026-10-18
estado: borrador para Jordi (no se ha cambiado nada: ni rutinas_web, ni redes.py, ni el repositorio)
---
# Web y redes más ambiciosas: esfuerzo de cada tarea y las ideas de Felix Rieseberg

**Para Jordi, en corto.** La web y las redes ya trabajan con cuidado (los informes de los agentes son honrados:
dicen lo que no pudieron comprobar). Lo que falta es **alguien de fuera que lo compruebe**: hoy el único que revisa
lo que se publica eres tú, y apruebas en unos minutos (el PR #11 se fusionó 10 minutos después de abrirse), así que
nadie abre las fuentes una por una. Propongo cuatro cosas, nada más:
1. **Un juez de fuentes** que abre cada fuente y marca cada precio o dato como «confirmado» o «no lo dice la
   fuente», en los artículos nuevos o cambiados (lunes, novedades y repaso mensual).
2. **Una prueba a ciegas de los títulos** en el agente de los jueves: se mezclan nuestros títulos con los diez
   primeros de Google, sin decir cuáles son los nuestros, y un juez elige en cuál haría clic. Si el nuevo no gana, no
   se cambia.
3. **Un lector escéptico para la tarjeta de valor de las 20:30**: antes de publicar, otro Claude (que no la ha
   escrito) dice si la guardaría o si no le sirve. El viernes 16 habría parado una tarjeta con el título repetido
   («Lo de la semana: Lo de la semana») y con dos de sus cuatro novedades solo en inglés de EE. UU. y de pago.
4. **Poner el esfuerzo a cada tarea**: más en el agente de los lunes (escribe lo que se publica), menos en lo
   mecánico (el repaso mensual y el texto de las 13:15).
Gasto: unos **+7 $ de referencia a la semana** (de ~21 a ~28, estimado; un solo montaje de vídeo gasta 46). Antes de ponerlo,
una prueba pequeña (punto 6) con tres títulos reales que salen en Google y nadie pulsa.

**Fuente de las ideas.** Felix Rieseberg (Anthropic), «How to be more ambitious: A tutorial for humans with models»,
13-10-2026, https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/ . Lo de cada idea
ya está explicado en «2026-10-18 · Fases más ambiciosas (propuesta)» (la de los canales): aquí no se repite, solo se
aplica a la web y a las redes.

---

## 1. Cómo está hoy cada tarea

| Tarea | Qué hace | Cuándo | Modelo y esfuerzo | Quién revisa lo que sale |
|---|---|---|---|---|
| ✍️ deco-semanal | Lee Search Console, escribe 2 artículos, arregla 1 antiguo, cambia hasta 3 títulos | lunes 13:52 (nube) | Opus 5.5, **esfuerzo sin fijar** (el de por defecto de la nube: ni `rutinas_web.py` ni el repositorio lo dicen) | `seo_preflight.py` (longitud, ≥2 fuentes, frases prohibidas) y build; luego **solo Jordi** |
| 📰 deco-novedades | Si hay algo grande y oficial de IA, 1 artículo o sección | martes y viernes 13:37 (nube) | Opus 5.5, sin fijar (el chat del 16-10 no tiene esfuerzo apuntado; gastó ~2,9 $ de referencia) | preflight y build; **solo Jordi** (aprobado el mismo día) |
| 🖱️ deco-jueves | Mejora título, descripción y preguntas de hasta 3 artículos con pocos clics | jueves 13:47 (nube) | Opus 5.5, sin fijar | preflight; **nadie mide si el título nuevo es mejor** (con 6 clics a la semana, Search Console tarda meses en decirlo) |
| 🩺 deco-mensual | Pone al día precios de hasta 5 artículos, enlaces rotos, fallos | día 20, 18:43 (nube) | Opus 5.5, sin fijar | preflight y build; solo Jordi |
| Redes 13:15 | Texto de Bluesky y Facebook sobre un artículo de la web (con su portada) | cada día (móvil viejo, `redes.py publicar`) | Sonnet, **alto** (no lo dice `redes.py`: sale del ajuste general del Debian, `/root/.claude/settings.json`) | el programa solo mira el largo (≤ 290) y que esté el enlace; **nadie más, se publica solo** |
| Redes 20:30 «valor» | Tarjeta + texto útil por sí mismo (lunes prompt… domingo mito), buscando en internet | cada día (móvil viejo, `redes.py valor`) | Sonnet, alto (igual), con WebSearch/WebFetch | solo el largo y que el JSON esté completo; **se publica solo** |
| Redes domingo 21:30 | Cifras de la semana | domingos | sin IA | — |

Lo bueno que ya hay y no se toca: las reglas de la casa en `docs/AGENTE-SEMANAL.md`, el preflight con frases
prohibidas («he probado», «increíble», «brutal»…), «Publicar sola: NO», y los informes honrados de los agentes (el
del 12-10 dice qué precios no pudo abrir y que no se ha probado nada).

**Lo que se ha visto al mirar** (para que la propuesta no sea a ciegas):
- Google: semana 03-09/10, 417 impresiones, 6 clics, CTR 1,4 %, posición 7,5. La búsqueda que más sale es
  «decodifica» (89 impresiones, 1 clic). Hay artículos que salen y **nadie pulsa**: `deepseek-app-oficial-espanol`
  (22 impresiones, posición 7,9), `ia-mejora-excel` (18; 8,5), `ia-organiza-pendientes` (15; 6,4) y Google Maps con
  Gemini (10; 7,3).
- El problema grande no es solo el CTR: con 417 impresiones a la semana **la web casi no sale**. El agente del lunes
  eligió el 12-10 «claude ia» (unas 500.000 búsquedas en España) y «ollama»: búsquedas enormes donde mandan la propia
  Anthropic y los medios grandes. Un buen editor de SEO miraría antes los diez primeros de Google y elegiría donde se
  puede ganar. Eso es justo la pregunta 1 de Felix.
- Hay restos que el preflight no caza: la descripción de `ia-mejora-excel` empieza por «**Comparamos** Copilot,
  Gemini…» (insinúa prueba propia; regla 3) y `_ESTADO.md` ya apunta un «Probamos» en `qwen3-asr`.
- Redes, tarjeta del 16-10: título «Lo de la semana: *4 novedades de IA* de Google» debajo de la etiqueta «LO DE LA
  SEMANA» (repetido) y dos de las cuatro novedades «solo de pago y en inglés de EE. UU.»: poco útil para quien lee en
  España o Latinoamérica. Las del 14 y 15 (audio a texto, datos inventados) sí eran buenas.
- Las portadas están bien hechas (plantilla clara, logo oficial, gancho corto): no necesitan equipo, solo una medida.
- El 16-10 la cuenta ya iba con aviso del límite de 7 días (`allowed_warning`): el cupo está justo de verdad.

---

## 2. Esfuerzo recomendado para cada una

| Tarea | Hoy | Propuesto | Por qué |
|---|---|---|---|
| ✍️ deco-semanal | sin fijar | **muy alto** (`xhigh`) | Es lo que se publica y lo que decide de qué escribe la web; elegir bien el tema y comprobar cada dato es pensar, no teclear. Como la fase 2 de los vídeos (`xhigh`). |
| 📰 deco-novedades | sin fijar | **alto** (`high`) | La mitad de los días acaba en «no hay nada»; cuando escribe es un artículo corto. Lo que más falla en las novedades son los datos, y eso lo para el juez de fuentes, no pensar más. |
| 🖱️ deco-jueves | sin fijar | **alto** (`high`) | Son 3 títulos y 3 descripciones: la mejora viene de la prueba a ciegas, no de pensar más tiempo. |
| 🩺 deco-mensual | sin fijar | **medio** (`medium`) | Casi todo es mecánico (enlaces, comparar precios con la web oficial) y lo miden herramientas. Si el juez de fuentes le encuentra fallos dos meses seguidos, se sube a `high`. |
| Redes 13:15 | alto (por el ajuste general) | **medio**, escrito en `redes.py` | Resume un artículo ya comprobado en dos textos cortos: mecánico. Sigue con Sonnet (Jordi lo prefiere a Haiku). |
| Redes 20:30 valor | alto (por el ajuste general) | **alto**, escrito en `redes.py` | Busca y comprueba datos en internet y decide qué es útil: aquí está el valor que pidió Jordi. |
| Lector escéptico (nuevo) | — | **medio**, Sonnet | Leer una tarjeta y opinar es corto. |
| Arreglos nocturnos de los canales (tda/as-incidencias) | sin fijar | no se tocan aquí | Son de los canales, no de la web. |

**Cómo ponerlo.**

a) **Las rutinas de la nube** (`jarvis-cabeza/cabeza/rutinas_web.py` y `~/.local/state/jarvis-cabeza/rutinas_web.json`).
Hoy `orden()` pide a Jarvis un `create_session` con el encargo como `prompt`: no hay sitio para el esfuerzo. Se hace
igual que el piloto desde el 17-10 (`piloto.py`, líneas ~320-345, probado): primer mensaje «/effort X» y el encargo
después con `claude -p … --cloud <id>`.

- En `rutinas_web.json`, a cada rutina de Decodifica un campo nuevo: `"esfuerzo": "xhigh"` (deco-semanal), `"high"`
  (deco-novedades y deco-jueves), `"medium"` (deco-mensual). Las que no lo tengan siguen como hoy.
- En `rutinas_web.py`, `orden()` (unas 20 líneas; copia de seguridad `rutinas_web.py.antes_esfuerzo`):

```python
ENCARGOS_DIR = Path("/data/data/com.termux/files/usr/var/lib/proot-distro/containers/debian/rootfs/root/.rutinas_encargos")

def orden(r, informe=None):
    prompt = r["prompt"] + (EXTRA_AUDITORIA.format(informe=informe) if informe else "")
    cab = ("[RUTINA] Abre un chat nuevo en la NUBE con la herramienta create_session, con estos datos exactos:\n"
           f"- environment_id: {r['entorno']}\n- source_url: {r['repo']}\n- title: {r['titulo']}\n"
           "- permission_mode: auto (si no te deja, sin permission_mode)\n"
           f"- model: {r.get('modelo', 'claude-opus-5-5')}\n")
    fichero = None
    if r.get("esfuerzo"):                       # 18-10-2026: como el piloto, «/effort X» primero y el encargo después
        try:
            ENCARGOS_DIR.mkdir(parents=True, exist_ok=True)
            (ENCARGOS_DIR / f"{r['id']}.txt").write_text(prompt)
            fichero = f"/root/.rutinas_encargos/{r['id']}.txt"
        except OSError:
            pass
    if fichero:
        cuerpo = (f"- prompt: exactamente «/effort {r['esfuerzo']}» (nada más: es el esfuerzo de esta rutina).\n"
                  "Después mándale el encargo como mensaje normal, con Bash: "
                  f"`/root/.local/bin/claude -p \"$(cat {fichero})\" --cloud <session_id>` y comprueba que dice "
                  "«Sent to cloud session» (si falla, reinténtalo una vez; si sigue fallando, mándale ese mismo texto "
                  "con send_message).\n")
    else:
        cuerpo = "- prompt: el texto que va entre <<< y >>>, tal cual, sin las marcas.\n" + f"<<<{prompt}>>>\n"
    return (cab + cuerpo + "Cuando esté abierto, avisa con: curl -s -X POST 127.0.0.1:8430/rutina_web -d '"
            + json.dumps({"id": r["id"], "enlace": "ENLACE"})
            + "' (cambiando ENLACE por https://claude.ai/code/<session_id>). Contesta solo con el enlace.")
```

  Vale al reiniciar Jarvis; apuntarlo en `~/CAMBIOS-SIN-SUBIR.md`. Ventaja añadida: el encargo deja de ir copiado
  dentro de la orden (era lo que hacía el piloto antes del 17-10).
- No conviene ponerlo en el repositorio (`.claude/settings.json` con `effortLevel`): sería el mismo esfuerzo para las
  cuatro rutinas y para cualquier chat que se abra a mano con la web.

b) **Las redes** (`/root/tareas/redes/redes.py`, en el Debian; copia `redes.py.antes_esfuerzo`). Escribir el
esfuerzo en cada llamada, para que no cambie si alguien toca el ajuste general:
- en `escribir()`: `["/root/.local/bin/claude", "-p", prompt, "--model", "sonnet", "--effort", "medium"]`
- en `escribir_valor()`: `[..., "--model", "sonnet", "--effort", "high", "--allowedTools", "WebSearch WebFetch"]`
- en el juez nuevo (punto 3.5): `"--effort", "medium"`, sin herramientas.

---

## 3. Dónde encaja cada idea (y dónde no)

Coste: **poco** = unas líneas más que leer; **medio** = un subagente o una llamada más. Prioridad **A** primero.

| Sitio | Idea que encaja | Por qué | Coste | Prio |
|---|---|---|---|---|
| **deco-semanal** | 4 preguntas al elegir temas + meta alta + **juez de fuentes** | Elegir dónde se puede ganar (hoy elige búsquedas enormes) y que nadie de fuera abre las fuentes | medio | **A** |
| **deco-novedades** | **Juez de fuentes** + pregunta 2 (fuente primaria) | Lo nuevo es lo que más se equivoca, y se aprueba deprisa | medio | **A** |
| **deco-jueves** | **Equipo de 3 miradas + equipo rojo + juez a ciegas con los diez de Google** | Es el sitio donde un título se puede medir antes de publicarlo; Search Console tarda meses con 6 clics a la semana | medio | **A** |
| **Redes 20:30 valor** | **Lector escéptico** (juez de fuera, otro `claude -p`) + meta alta (una línea) | Se publica sola, sin nadie que la mire; el 16-10 salió una floja | poco | **A** |
| deco-mensual | Solo herramientas que miden (fuentes, enlaces, velocidad) | Es mecánico: no necesita preguntas ni equipos | poco | B |
| Redes 13:15 | Solo una comprobación en código (sin IA): cada número del texto está en el artículo | Ya dice «solo lo que dice el artículo»; falta medirlo | nada | B |
| Portadas | Solo una medida (se lee a tamaño pequeño; el gancho no repite el título) | Ya están bien y Google casi no las enseña en la búsqueda normal | poco | C |
| Cifras del domingo | **Ninguna** | Sin IA | — | — |
| Las reglas de estilo de `AGENTE-SEMANAL.md` | **Ninguna** | Ya son buenas y duras; no se añaden reglas nuevas | — | — |
| Equipo rojo en los artículos | **No** | Cuesta mucho cupo; el juez de fuentes ya hace de «rojo» en lo que importa (datos y relleno) | — | — |

Los textos para la nube tienen que estar **en el repositorio** (la nube no ve la bóveda): un bloque corto común y
dos encargos de juez. Los prompts de `rutinas_web.json` solo ganan 2-4 líneas que los citan.

### 3.0 El bloque común (nuevo): `docs/pensar-como-los-mejores.md` (~2 KB)

```
# Pensar como los mejores (lo citan algunos pasos de AGENTE-SEMANAL.md)

(Idea de Felix Rieseberg, Anthropic, 13-10-2026. Son preguntas, no reglas de estilo: las reglas
de la casa ganan siempre. Lo que contestes vale para esta semana, no se convierte en norma.)

ANTES DE EMPEZAR, CUATRO PREGUNTAS. Contéstalas en 5-8 líneas al principio de tu informe:
1. ¿Qué haría aquí el mejor editor de guías prácticas en español, que sabe de SEO, que no se me
   está pidiendo?
2. ¿De qué material más EN BRUTO partiría, en vez de lo ya masticado? (La página oficial de
   precios y la ayuda oficial, el anuncio de la empresa, su registro de cambios, los datos de
   Search Console y las sugerencias de Google por país; los diez primeros resultados de Google
   para esa búsqueda. No otros artículos que ya lo resumen.)
3. ¿Qué métodos y herramientas usaría? (Mirar quién sale en los diez primeros y qué les falta;
   buscar por país: España, México, Colombia, Argentina; capturas de la web oficial; los scripts
   de scripts/.)
4. ¿Qué, aparte de ti, demostraría que está bien? (scripts/comprobar_fuentes.py,
   scripts/seo_preflight.py, el juez de fuera de docs/jueces/ y, con el tiempo, los clics.)
Después, haz el trabajo según esas respuestas.

LA META, NO LA TAREA. No escribes «un artículo sobre X»: haces que quien busca X en España o en
Latinoamérica encuentre aquí la respuesta más clara y fiable en español, la use hoy y vuelva.

METAS ALTAS, SIN HUMO. Apunta a ser el mejor resultado en español para esa búsqueda, no uno más.
Si no puedes ganar a los diez primeros en algo concreto (más claro, más al día, mejor comprobado,
pensado para Latinoamérica), elige otra búsqueda: mejor una donde se puede ganar que una enorme
donde no.

NO TE JUZGUES TÚ. El visto bueno no te lo das tú: te lo dan las herramientas y el juez de fuera.
Lo que diga una herramienta no se discute: se arregla y se vuelve a pasar.

Trabaja sin prisas: mejor bien que pronto.
```

### 3.1 El juez de fuentes (nuevo): `docs/jueces/fuentes.md` (~1,5 KB) — prioridad A

```
# Juez de fuentes

CÓMO SE LANZA (lo hace el agente que ha escrito o cambiado datos de un artículo): herramienta
Agent, tipo general-purpose (nunca uno que herede tu conversación), con esta línea y nada más:
  Lee docs/jueces/fuentes.md (apartado «Tu encargo») y hazlo con src/pages/blog/<slug>.astro.
No le pases tus notas, tu informe ni por qué escribiste cada cosa. Antes, pasa
scripts/comprobar_fuentes.py <slug>: su salida la verá él en el mismo artículo.

## Tu encargo
Eres un verificador de datos de una agencia seria y un lector exigente. No has escrito este
artículo. Lee SOLO ese archivo y abre sus fuentes (las de «Fuentes»; si una da 403, ábrela con el
navegador sin pantalla, como scripts/imagenes/captura.py).
1. Cada dato que se pueda comprobar (precio, límite, plan, fecha, versión, país, idioma, «gratis»):
   CONFIRMADO (qué fuente y qué frase), NO LO DICE LA FUENTE, LA FUENTE NO ABRE o DESFASADO.
2. Relleno: cada párrafo que no aporta un dato, un paso ni una decisión.
3. Lo prohibido: decir o insinuar que se ha probado («comparamos», «probamos», «en nuestra
   experiencia») sin prueba de Jordi; titulares sensacionalistas o prisas falsas.
4. Quien lee en Latinoamérica: ¿algo solo vale en EE. UU. o en España y no se dice?
Escribe el veredicto en /tmp/juez_<slug>.md (no en el repositorio): ordenado por gravedad, como
mucho 15 puntos, cada uno con la frase exacta del artículo. Si todo está bien, dilo en una línea:
es un buen resultado. No reescribas nada ni des reglas nuevas.
```

**Dónde se cita** — en `docs/AGENTE-SEMANAL.md`, paso 5 («Revisión SEO y editorial»), detrás de la orden del
preflight (3 líneas; vale para los cuatro agentes porque todos dicen «respeta las revisiones»):

```
   Después, en cada artículo nuevo o con datos cambiados: scripts/comprobar_fuentes.py <slug> y el
   juez de fuentes (docs/jueces/fuentes.md). Contesta cada punto en el informe: «arreglado» o
   «no, porque…». Como mucho dos vueltas; lo que quede, en «Lo que no se pudo comprobar».
```

### 3.2 deco-semanal (prompt de `rutinas_web.json`) — prioridad A

Detrás del punto 2 («Lee docs/AGENTE-SEMANAL.md…»), una línea nueva (4 líneas):

```
2b. Antes de elegir temas, lee docs/pensar-como-los-mejores.md y contesta sus cuatro preguntas
para esta semana al principio del informe. La meta no son «2 artículos»: es que quien busque esos
temas en España o Latinoamérica encuentre aquí la mejor respuesta en español. Mira los diez
primeros de Google de cada tema antes de elegirlo; si no hay nada concreto en que ganarles, elige otro.
```

Y en el resumen para Jordi, una línea: «- qué dijo el juez de fuentes y qué se arregló.»

### 3.3 deco-novedades — prioridad A

En el punto 5 («Escribe el artículo…»), al final (2 líneas):

```
La fuente es el anuncio de la propia empresa (blog, nota, ayuda oficial), no la prensa que lo
cuenta. Antes de entregar, el juez de fuentes (paso 5 de docs/AGENTE-SEMANAL.md).
```

### 3.4 deco-jueves: tres miradas, equipo rojo y juez a ciegas — prioridad A

**Nuevo** `docs/jueces/titulos.md` (~1,5 KB):

```
# Títulos: tres miradas, el equipo rojo y la prueba a ciegas

PARA CADA ARTÍCULO (lo hace el agente que cambia títulos, el de los jueves o el del lunes):
1. Saca de Search Console su búsqueda principal y el país que más la busca.
2. Mira los diez primeros resultados de Google para esa búsqueda (título y descripción).
3. Escribe tres candidatos, cada uno haciendo el trabajo de una mirada (no imitando su voz):
   - quien busca deprisa desde el móvil en México o Colombia: ¿ve su pregunta respondida?;
   - quien no sabe qué es la herramienta: ¿entiende de qué va?;
   - el editor de titulares de un periódico serio: claro, exacto, sin cebo.
4. EQUIPO ROJO: para cada candidato, ¿por qué alguien NO pulsaría? ¿promete algo que el artículo
   no da? Si promete de más, fuera (regla 4: sin sensacionalismo).
5. JUEZ A CIEGAS: escribe en /tmp/titulos/<slug>.md la búsqueda y una lista numerada y barajada
   con los diez de Google, nuestro título de hoy y los candidatos que queden, todos con el mismo
   formato («título — descripción») y SIN nombre de web. Lanza un subagente general-purpose
   (nunca uno que herede tu conversación) con esta línea y nada más:
     Lee docs/jueces/titulos.md (apartado «Tu encargo») y hazlo con /tmp/titulos/<slug>.md.
6. Solo se cambia si un candidato queda por delante de nuestro título de hoy y entre los tres
   primeros del juez. Si no, no se toca: dilo en docs/repaso-jueves/ con lo que eligió el juez.

## Tu encargo
Eres una persona normal del país que dice el archivo; acabas de buscar eso en Google y ves esta
lista. ¿En cuál pulsarías primero, segundo y tercero? Una línea por qué de cada uno. ¿Cuál te
parece un cebo o te da desconfianza? No sabes quién ha escrito cada uno y no te importa.
```

**En el prompt de deco-jueves** (`rutinas_web.json`), punto 5, cambiar «mejora el título y la descripción…» por
(3 líneas):

```
5. En cada uno: título y descripción nuevos según docs/jueces/titulos.md (tres miradas, equipo
rojo y juez a ciegas con los diez de Google; si el nuevo no gana, no se cambia). Después, …
```
(sigue igual: preguntas y respuestas, enlaces internos). Y en el punto 6, apuntar también lo que eligió el juez.
En `AGENTE-SEMANAL.md`, paso 6 del lunes, media línea: «…con el método de docs/jueces/titulos.md».

### 3.5 Redes 20:30: el lector escéptico — prioridad A

En `redes.py`, una llamada más, aparte (un `claude -p` nuevo no ha visto cómo se escribió: es un juez de fuera de
verdad). Prompt nuevo `PROMPT_JUEZ_VALOR`:

```
Eres un seguidor escéptico de cuentas de IA en Bluesky y Facebook. Vives en {pais}, usas el móvil,
no pagas ninguna IA y ves cincuenta publicaciones al día. NO has escrito esto. Hoy es {hoy}.
Esta es la publicación de hoy (lo que pone la tarjeta y el texto):
{publicacion}
Contesta SOLO con un JSON:
{{"la_guardaria": true, "me_sirve": "...", "sobra": ["..."], "dudoso": ["dato que suena raro"],
  "veredicto": "publicar", "por_que": "una frase"}}
«rehacer» solo si: casi nada te sirve donde vives (solo en inglés, solo en EE. UU., solo de pago)
y no lo dice claro; algo está repetido o mal escrito; un dato suena falso; o no aprenderías nada
que no sepa cualquiera.
```

- `{pais}` cambia con el día (España, México, Colombia, Argentina…), para no escribir solo para uno.
- Si dice «rehacer»: **una** vuelta más de `escribir_valor()` con «Un lector escéptico dijo: {por_que}; {sobra};
  {dudoso}. Corrígelo o cambia de tema». La segunda se publica sí o sí (que no se quede el día sin publicación) y el
  veredicto se guarda en `estado.json` (`"juez"`), para la revisión de la estrategia del 28-10.
- En `PROMPT_VALOR`, una línea de meta alta al principio: «La meta: que alguien de Valencia o de Lima lo use hoy mismo y
  lo guarde. Si lo que encuentras solo sirve en EE. UU. o en inglés, busca otra cosa.» Y un campo `"fuentes"` (las URL
  que usó) que se guarda en `estado.json` sin publicarse, para poder comprobarlo después.

### 3.6 Lo pequeño (prioridad B y C)

- **Redes 13:15** (B, en código, sin IA): después de `escribir()`, sacar los números del texto (precios, GB,
  minutos…) y mirar que estén en `art["texto"]`; si alguno no está, una vuelta más con «OJO: el número X no está en
  el artículo». Unas 8 líneas.
- **deco-mensual** (B), en su punto 5, una línea: «No te des por bueno: lo que digas que está arreglado, que lo diga
  la herramienta (comprobar_fuentes, enlaces, velocidad), con el número antes y después.»
- **Portadas** (C): `portada.py --muestra` ya existe; añadir que el gancho no repita el título y que se lea con la
  portada a 400 px de ancho (lo que se ve en el móvil en Bluesky). Sin juez.

### 3.7 Lo que NO se toca

- Las reglas de la casa y de estilo de `AGENTE-SEMANAL.md` (no se añaden reglas: solo los dos pasos que citan a los
  jueces). «Publicar sola: NO» sigue igual: los jueces **no sustituyen a Jordi**, le llegan los PR más limpios.
- Nada de «date prisa» en nada que se publique.
- Nada de equipos de miradas en los artículos ni en el repaso mensual (cupo).
- Las cifras del domingo y las rutinas de los canales.

---

## 4. Medidas que se comprueban sin opinar

| Qué se mide | Con qué | Estado | Umbral |
|---|---|---|---|
| **Las fuentes existen y dicen lo citado**: cada enlace de «Fuentes» contesta (y si da 403, se abre con el navegador sin pantalla); cada precio o número del artículo aparece en el texto de alguna de sus fuentes | `scripts/comprobar_fuentes.py <slug>` | **nuevo** (~120 líneas, Python + Playwright, que ya usa `captura.py`) | 0 enlaces muertos; los números que no aparezcan van al juez (no bloquean solos: un precio puede salir en una tabla) |
| Largo del título y la descripción, ≥ 2 fuentes, ≥ 2 enlaces internos, frases prohibidas | `scripts/seo_preflight.py` | existe | título 35-60, descripción 110-165 |
| Frases que insinúan prueba propia | añadir «comparamos», «probamos», «hemos probado», «nuestra prueba» a la lista del preflight | **1 línea** | hoy lo tienen `ia-mejora-excel` («Comparamos…») y `qwen3-asr` («Probamos») |
| Enlaces rotos de toda la web | `scripts/web_health_check.py` (existe; comprobar que corre en la nube: por defecto busca su configuración en una ruta de Windows) | existe | 0 internos rotos |
| Velocidad en el móvil (LCP, saltos de la página) | Lighthouse o el script de capturas del rediseño, en el repaso mensual, sobre las 5 páginas con más impresiones | a medias (se midió el 14-10: LCP ~0,78 s) | LCP < 1 s, CLS < 0,1 |
| El juez a ciegas de los títulos | `docs/jueces/titulos.md` | **nuevo** | el nuevo, entre los 3 primeros y por delante del de hoy |
| CTR de Search Console antes y después | `docs/repaso-jueves/` ya apunta las cifras del momento | existe | **Ojo:** con 6 clics a la semana y 15-22 impresiones por página, un cambio de CTR no se nota en semanas. Comparar **28 días antes y 28 después**, solo páginas con ≥ 100 impresiones; antes de eso, el juez a ciegas es la única medida rápida |
| Redes: reacciones por clase (artículo / valor) y por tipo de día | `redes.py cifras` (añadir el reparto por clase) | a medias | para la revisión del 28-10 |
| El lector escéptico | `estado.json` → `"juez"` | **nuevo** | cuántas «rehacer» al mes |

---

## 5. Gasto de cupo aproximado a la semana

En «dólares de referencia» (lo que la nube apunta en cada chat; sirve para comparar, no es dinero que se pague).
Solo hay un dato medido de la web (novedades del 16-10: 2,9 $); lo demás es estimado a partir de él y de los chats
grandes del 14-10 (portadas 10 $, imágenes 19 $). Para comparar: **el montaje del vídeo 13 gastó 46 $**.

| Tarea | Antes | Después | Qué sube o baja |
|---|---|---|---|
| deco-semanal (1/semana) | ~8 $ | ~13 $ | `xhigh` (+2-3 $) y el juez de fuentes, ~1 $ por artículo (2-3) |
| deco-novedades (2/semana) | ~4 $ (un día con artículo, otro sin) | ~5 $ | juez de fuentes solo cuando hay artículo |
| deco-jueves | ~3 $ | ~4,5 $ | tres miradas y el juez a ciegas (~1 $ en total) |
| deco-mensual (÷ 4) | ~1,5 $ | ~1,2 $ | baja a `medium` |
| Redes 13:15 (7) | ~1 $ | ~0,7 $ | baja a `medium` |
| Redes 20:30 (7) | ~3 $ | ~3,5 $ | el lector escéptico, unos céntimos al día, y alguna segunda vuelta |
| **Total** | **~21 $** | **~28 $** | **+7 $/semana (+33 %)**, menos de una sexta parte de un montaje |

Si el cupo aprieta, lo primero que se quita es el `xhigh` del lunes (vuelve a `high`): el juez de fuentes da más
calidad por menos cupo que pensar más tiempo. Lo último que se quitaría es el lector escéptico (casi no gasta).

---

## 6. Prueba pequeña antes de ponerlo

Nada de esto entra en `rutinas_web.json`, `redes.py` ni el repositorio hasta pasar estas pruebas. Nada se publica.

1. **Títulos a ciegas (la principal, ~3 $).** Un chat de la nube aparte con el repositorio, sin pull request, en
   `/tmp`. Con los tres artículos que salen en Google y nadie pulsa:
   `deepseek-app-oficial-espanol` (22 impresiones, posición 7,9), `ia-mejora-excel` (18; 8,5) e
   `ia-organiza-pendientes` (15; 6,4).
   - Tanda A: título y descripción nuevos con el punto 5 de hoy del agente de los jueves.
   - Tanda B: con `docs/jueces/titulos.md` (tres miradas y equipo rojo).
   - Un juez a ciegas (subagente aparte) ve, para cada búsqueda, los diez de Google + el de hoy + el A + el B,
     barajados y sin nombres. Y **Jordi** ve A y B mezclados, sin saber cuál es cuál, y elige.
   - Sirve si B gana en al menos 2 de 3 (al juez y a Jordi) y ninguno rompe la regla del sensacionalismo.
2. **Calibrar el juez de fuentes (~2 $).** En una copia de `claude-ia-que-es-gratis` se meten a propósito dos
   errores (Pro a 25 $ en vez de 20; «lo hemos probado» en un párrafo). Tiene que cazar los dos y como mucho dos
   falsas alarmas. Después, sobre el artículo real de la novedad del 16-10 (PR #17), para ver qué encuentra.
3. **Lector escéptico (~0,5 $, en el móvil).** Pasarle la tarjeta del 16-10 tal cual: tiene que decir «rehacer» (título
   repetido, dos de cuatro solo en inglés de EE. UU.); y la del 15-10 (datos inventados): tiene que decir
   «publicar». Luego `redes.py valor --prueba 5` (no publica) con y sin él, y Jordi elige a ciegas.
4. **Si sale bien:** un pull request a `decodifica.net` con `docs/pensar-como-los-mejores.md`, `docs/jueces/`,
   `scripts/comprobar_fuentes.py`, las 3 líneas del paso 5 y la línea del preflight (lo aprueba Jordi, como todo);
   y en el móvil, `rutinas_web.py/.json` (esfuerzo y las líneas de los prompts) y `redes.py` (esfuerzo, lector
   escéptico, comprobación de números), apuntados en `~/CAMBIOS-SIN-SUBIR.md`. Se estrena el jueves 22-10 (títulos) y
   el lunes 26-10 (semanal). Lo de prioridad B y C, solo si Jordi quiere, después.

**Lo que Jordi tiene que decidir:** ¿se hacen las pruebas 1, 2 y 3 (unos 5-6 $ en total)? ¿Le parece bien el esfuerzo
de cada tarea (punto 2), aunque no se haga lo demás? Eso se puede poner ya: es pequeño y tiene vuelta atrás.
