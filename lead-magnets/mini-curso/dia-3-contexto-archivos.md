# Día 3 — Contexto y archivos: el multiplicador que convierte ChatGPT en tu asistente

**Asunto:** Día 3 de 5: cómo hacer que ChatGPT lea TUS documentos (no los de internet)
**Cuándo se envía:** día 3 desde la suscripción
**Tiempo de lectura:** 3-4 min

---

RTF te dio consistencia en los prompts\. Hoy vamos al multiplicador de productividad real: hacer que ChatGPT trabaje con TUS documentos, no con info genérica de internet\.

La mayoría usa ChatGPT como buscador\. Le pregunta "¿qué es X?" y acepta lo que responda\. Eso es el 10% de lo que puede hacer\.

El 90% restante es: subir archivos y dejar que los lea\. PDFs, CSVs, código, imágenes, audio\. Aquí es donde ChatGPT deja de ser un buscador y se convierte en tu asistente de verdad\.

---

## Los 4 tipos de archivo que más uso

**1\. PDFs (informes, papers, contratos, ebooks)**
Sube el PDF al chat\. ChatGPT lo lee en segundos y puedes preguntarle lo que quieras sobre él\. Truco: en lugar de "resume este PDF", di "actúa como X y dime qué información de este PDF es relevante para Y".

**2\. CSVs (datos)**
Sube el CSV\. ChatGPT puede hacer análisis, encontrar patrones, generar resúmenes\. Truco: pide que primero te diga las columnas y cuente filas para verificar que cargó bien\.

**3\. Código**
Pega o sube el archivo\. Pide revisión, refactor, tests, documentación\. Truco: pide siempre "explica qué hace este código antes de cambiar nada".

**4\. Imágenes y audio**
Screenshot de un error, foto de un documento, audio de una reunión\. ChatGPT los lee directamente\. Truco: la transcripción de audio + análisis en un solo paso\.

---

## El truco clave: el contexto antes del archivo

**Malo:** "Resume este PDF"
**Bien:** "Actúa como consultor de marketing\. Voy a subirte el PDF de mi último informe de ventas\. Dame 3 puntos débiles que veas y 2 oportunidades que yo no haya visto\."

La diferencia: en el segundo le das **rol + contexto + tarea concreta**\. Sin eso, ChatGPT hace un resumen genérico que no te sirve\.

Patrón que uso siempre:
> Actúa como [rol experto]\.
> Voy a subirte [tipo de archivo]\.
> Dame [número] [tipo de insight] sobre [tema específico]\.
> Formato: [bullets / tabla / párrafo]\.

---

## Caso real: auditar un contrato en 5 minutos

Sin IA: 30-45 min leyéndolo, marcando cláusulas raras, preguntando al abogado\.
Con este patrón:

> Actúa como abogado mercantilista español con 10 años de experiencia\.
> Voy a subirte un contrato de prestación de servicios en PDF\.
> Dame una lista con:
> - 3 cláusulas que revisarías con lupa
> - 1 cláusula que falta y debería estar
> - 1 riesgo que el proveedor probablemente quiere ocultar
>
> Formato: tabla con columnas "Apartado", "Qué dice", "Por qué me preocupa"\.

5 minutos\. Output accionable\. Cambia cómo gestionas proveedor\.

---

## Prompt útil del día

El patrón universal para análisis de archivos:

> Actúa como [rol experto concreto]\.
> Te voy a subir [tipo de archivo]\.
> Dame [número] [insights / problemas / oportunidades] sobre [tema]\.
> Si necesitas más contexto antes de responder, pregunta\.
> Formato: [bullets / tabla / párrafo]\.

Pégalo\. Sube el archivo\. Adapta el rol y el tema\. Funciona con cualquier archivo\.

---

## Mañana: Día 4 — Iteración y refinamiento

Ya tienes el setup, los prompts bien estructurados y el contexto de tus archivos\. Mañana vamos al truco que separa juniors de seniors: cómo pedirle a ChatGPT que MEJORE su propia respuesta\. El 90% acepta la primera\. El 10% que itera saca 10× más valor\.

Si te lo han pasado, suscríbete gratis: https://buttondown.email/decodifica

— Jordi · https://decodifica.net