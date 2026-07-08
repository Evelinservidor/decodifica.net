# Día 5 — Agentes y automatizaciones: Custom GPTs y Projects para escalar tu trabajo

**Asunto:** Día 5 de 5: tu primer Custom GPT en 10 minutos (sin programar)
**Cuándo se envía:** día 5 desde la suscripción
**Tiempo de lectura:** 4-5 min

---

Último día\. Llevas 4 días configurando setup, escribiendo prompts con RTF, subiendo archivos e iterando\. Hoy cerramos el círculo con lo que escala todo: agentes\.

La diferencia entre "uso ChatGPT yo" y "tengo un asistente":
- **Yo solo:** cada vez que lo uso, tengo que darle contexto, ajustar el prompt, revisar el output
- **Asistente:** ya tiene el contexto, sigue mis instrucciones, produce output listo para usar

Eso es un Custom GPT \(ChatGPT\) o un Project \(Claude\)\.

---

## Custom GPT vs Project

**Custom GPT \(ChatGPT\):**
- Vive en `chatgpt.com/create`
- Tiene nombre, descripción, instrucciones fijas
- Puede tener archivos de conocimiento
- Puede tener Actions \(conectar a APIs externas\)
- Compartible: otros pueden usarlo
- Necesita plan ChatGPT Plus o superior

**Project \(Claude\):**
- Vive dentro de Claude
- Similar: instrucciones, archivos, Projects separados
- Más enfocado a uso individual, menos compartible
- Disponible en plan Pro

Para empezar: **Custom GPT**\. Es más versátil y puedes compartirlo con tu equipo\.

---

## Las 5 partes de un Custom GPT

**1\. Nombre** — claro, descriptivo\. Ej: "Email follow-up comercial"
**2\. Descripción** — qué hace, para quién\. 1-2 frases\. La usa ChatGPT para decidir cuándo invocarlo
**3\. Instrucciones** — el system prompt\. Aquí va TODO lo que quieres que recuerde\. 200-500 palabras\. Tono, formato, ejemplos, lo que NO debe hacer
**4\. Archivos de conocimiento** — PDFs, docs, CSV\. Se convierten en "memoria" del GPT
**5\. Acciones \(opcional\)** — conectar a APIs externas \(tu CRM, tu email, etc\.\). Requiere programar\. Para el 90% no hace falta al principio

---

## Mi primer Custom GPT: 10 minutos

**Caso:** "Brief semanal de marketing"

**Nombre:** Brief Semanal Marketing
**Descripción:** Genera briefs de campañas de marketing en formato estándar con título, objetivo, público, canales, mensaje clave, CTA y KPIs sugeridos\. Para equipos de marketing que necesitan producir briefs consistentes cada semana\.
**Instrucciones:**
> Eres un estratega de marketing con 10 años de experiencia en B2B y B2C\.
>
> Cuando el usuario te pida un brief, genera SIEMPRE este formato:
> - Título de campaña
> - Objetivo \(1 frase\)
> - Público objetivo \(demografía + psicografía\)
> - Canales \(3-5 máx\)
> - Mensaje clave \(1 frase\)
> - CTA
> - KPIs sugeridos \(3-5, con métricas concretas\)
>
> Tono: directo, sin jerga, español de España\.
> Longitud: máx 300 palabras\.
>
> Si el usuario no te da producto o audiencia, pregunta antes de generar el brief\.
**Archivos:** subir 2-3 briefs anteriores como referencia de formato y tono

Listo\. Cada lunes, "Brief Semanal Marketing" me da un brief consistente sin tener que explicarle desde cero\.

---

## Errores comunes con Custom GPTs

**1\. Instrucciones demasiado genéricas**
Mal: "Ayuda con marketing"
Bien: las instrucciones detalladas del ejemplo de arriba

**2\. Sin archivos de referencia**
Un GPT sin archivos produce respuestas genéricas\. Sube 3-5 ejemplos de lo que quieres que genere

**3\. No iterarlo**
Los primeros outputs no van a ser perfectos\. Itera las instrucciones\. Cuando un output te guste, cópialo al campo de instrucciones como ejemplo

**4\. Querer hacerlo todo en el primer GPT**
Empieza con UN caso de uso concreto\. Cuando funcione, haz el segundo\. No intentes crear un GPT que haga 10 cosas

---

## El siguiente nivel: Custom GPTs con Actions

Si quieres que el GPT conecte con tus herramientas:
- **Zapier Actions** \(sin código\): conectar a 5000\+ apps
- **API custom** \(requiere desarrollo\): conectar a tu CRM, tu BD, etc\.

Para el 90% de casos, Zapier Actions llega\. 30 min de setup y tienes un GPT que:
- Lee emails de tu Gmail
- Crea eventos en Calendar
- Guarda leads en tu CRM
- Manda mensajes a Slack

No es magia, es plumbing\. Pero cambia cómo trabajas\.

---

## Prompt útil del día

Para diseñar tu primer Custom GPT en 10 minutos:

> Quiero crear un Custom GPT para [caso de uso concreto]\.
>
> Hazme 5 preguntas para entender:
> 1\. ¿Qué tarea concreta quiero que automatice?
> 2\. ¿Quién lo va a usar \(yo solo / mi equipo / clientes\)?
> 3\. ¿Qué inputs necesita \(qué le pido yo\)?
> 4\. ¿Qué output quiero que produzca \(formato exacto\)?
> 5\. ¿Qué NO debe hacer \(límites, cosas fuera de scope\)?
>
> Con mis respuestas, genera:
> - Nombre del GPT \(3 opciones\)
> - Descripción \(1-2 frases\)
> - Instrucciones completas \(300 palabras máx\)
> - Lista de archivos de conocimiento que debería subir

10 minutos\. GPT listo\. Empieza a usarlo\.

---

## Cierre del curso

Has pasado 5 días configurando tu setup, aprendiendo el framework RTF, subiendo contexto, iterando respuestas y montando tu primer agente\.

Esto no es teoría\. Es el workflow real que uso yo cada semana para producir los videos del canal, los posts del blog y esta misma newsletter\.

Si quieres seguir avanzando:
- **El blog** tiene guías largas de cada tema que hemos visto: https://decodifica.net/blog
- **La newsletter semanal** \(esta que estás leyendo\) sale cada sábado con lo que realmente funciona
- **YouTube**: 5 videos nuevos cada semana sobre apps IA que puedes aplicar ya

Si te lo han pasado, suscríbete gratis: https://buttondown.email/decodifica

Gracias por llegar hasta aquí\. Nos vemos el sábado\.

— Jordi · https://decodifica.net
