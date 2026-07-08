# Día 2 — Estructura de prompts: el framework que hace que las respuestas sean reproducibles

**Asunto:** Día 2 de 5: el framework RTF para escribir prompts que funcionan siempre
**Cuándo se envía:** día 2 desde la suscripción
**Tiempo de lectura:** 3-4 min

---

Ayer configuramos tu setup\. Hoy vamos a la skill core: cómo escribir prompts que dan respuestas consistentes\.

El problema del 90%: aceptan la primera respuesta\. O peor, reformulan la pregunta cada vez\. La respuesta cambia, no es reproducible, y pierdes el control\.

Hay un framework que uso desde hace 2 años y nunca me falla\. Se llama **RTF**\.

---

## El framework RTF

**R — Role:** quién quieres que sea
**T — Task:** qué tiene que hacer exactamente
**F — Format:** en qué formato lo quieres

Esos 3 elementos\. Siempre\. Sin extras\.

---

## Ejemplo real

Malo:
> "Escribe un email para un cliente que se queja"

Bien:
> "Actúa como comercial de SaaS B2B con 5 años de experiencia\.
> Escribe un email de respuesta a un cliente que lleva 3 días quejándose por email de un bug que ya está resuelto\.
> Formato: asunto + saludo + 1 párrafo que reconozca el problema + 1 pregunta para confirmar que está resuelto + despedida\.
> Tono: profesional pero cercano\. Máx 120 palabras\."

Misma idea\. Misma intención\. Resultado completamente distinto\.

**Por qué funciona:**
- **Role** activa el tono y conocimiento que necesitas
- **Task** quita ambigüedad ("queja" puede ser 10 cosas; "queja por bug ya resuelto" es 1)
- **Format** te da el output que esperas (no tienes que reescribir nada)

---

## Cuándo NO usar RTF

- Preguntas simples tipo "¿qué hora es?" — no necesitas estructura
- Brainstorming abierto — la estructura mata la creatividad
- Conversaciones de exploración — está bien que sean vagas

Úsalo cuando el output va a producción\. Email, post, informe, código, análisis\. Ahí es donde la consistencia importa\.

---

## Variantes del framework

**Para análisis:** Role + Task + Format + "Cita fuentes si las usas"

**Para código:** Role + Task + Format + "Lenguaje X, sin comentarios, máx N líneas"

**Para decisiones:** Role + Task + Format + "Dame 3 opciones con pros/contras de cada una"

**Para refactorizar prompts largos:** Role + Task + Format + "Si no tienes info suficiente, pregunta antes de responder"

La regla es: si el output va a producción, usa RTF\. Si es curiosidad, no hace falta\.

---

## Prompt útil del día

Para convertir una idea vaga en un prompt RTF listo para usar:

> Tengo esta idea suelta: "[pega aquí tu idea]"
>
> Conviértela en un prompt profesional usando el framework RTF (Role + Task + Format)\.
> - Role: el experto que mejor puede resolver esto
> - Task: la acción concreta, sin ambigüedad
> - Format: el formato exacto del output que esperas
> - 1 línea adicional si necesito contexto extra
>
> Devuélveme SOLO el prompt final, nada más\.

Copia, pega tu idea, copia el resultado\. Listo para producción\.

---

## Mañana: Día 3 — Contexto y archivos

RTF te da consistencia\. Mañana vamos al multiplicador: cómo hacer que ChatGPT lea TUS documentos \(PDFs, CSVs, código\) y los use para responder\. Esto es donde pasa de ser un buscador a ser tu asistente\.

Si te lo han pasado, suscríbete gratis: https://buttondown.email/decodifica

— Jordi · https://decodifica.net