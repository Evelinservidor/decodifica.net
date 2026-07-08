# Buttondown — Welcome email setup para Decodifica

**Tiempo estimado:** 5-10 minutos (1 vez).

## Paso 1 — Accede al dashboard de Buttondown

1. Ve a https://buttondown.email/manager/
2. Login con la cuenta administradora de Decodifica en Buttondown.

## Paso 2 — Crear el welcome email automatizado

1. En el menú lateral, ve a **"Automated emails"** (o "Emails" → "Automated").
2. Click **"New automated email"**.
3. En **"Trigger"**, selecciona **"New subscriber"**.
4. En **"Subject"**, pega EXACTAMENTE:
   ```
   Aquí tienes tu PDF de 50 prompts (y 3 regalos extra)
   ```
5. En **"Email body"**, pega lo siguiente (markdown o HTML, Buttondown auto-detecta):

   ```markdown
   Hola {{ subscriber.first_name | default: "allá" }},

   ¡Bienvenido/a a Decodifica! Soy Jordi, gracias por sumarte.

   Como prometí, aquí va tu lead magnet:

   **📄 50 Prompts para IA** — 13 páginas con plantillas listas para usar en ChatGPT, Claude o Gemini. Categorías:
   - Productividad y trabajo
   - Escritura y contenido
   - Programación y código
   - Análisis y decisión
   - Aprendizaje y estudio

   👉 **Descarga directa:** https://vsczmjjtesenlqruqoqv.supabase.co/storage/v1/object/public/recursos/50-prompts-ia.pdf

   He probado cada prompt personalmente. Funcionan con ChatGPT (cualquier plan), Claude (incluso el free) y Gemini. Copia, pega, adapta.

   ---

   **Para los próximos 7 días, te envío 3 emails más:**

   1. **Mañana**: mis 3 videos favoritos del canal (los que mejor explican qué es la IA en este momento)
   2. **En 3 días**: cómo elijo los temas del canal (mi proceso editorial, transparent)
   3. **En 7 días**: mi setup de herramientas — el stack que uso para producir 5 videos/semana

   Si en algún momento quieres dejar de recibirlos, hay un link de unsubscribe al final de cada email. Sin dramas.

   ---

   Por cierto, ¿qué caso de uso te interesa más? Responde a este email con una frase y lo tendré en cuenta para los próximos videos.

   Gracias por estar al otro lado,
   Jordi

   — Decodifica · https://decodifica.net
   ```

6. Click **"Save"** o **"Activate"**.

## Paso 3 — Verificar que el email remitente está configurado

1. Ve a **"Settings"** → **"Email"** (en el menú lateral).
2. Comprueba que tienes un dominio remitente verificado o al menos un email remitente personal configurado.
3. Si NO lo tienes configurado, Buttondown usará `noreply@buttondown.email` (no ideal, los emails llegan a spam). Para FASE 1 vale, para FASE 2 mejor configurar el dominio `decodifica.net` (FASE 5+ según el business plan, FASE 3 si quieres newsletter decente).

## Paso 4 — Test

1. En la página de automated emails, click **"Send test email"**.
2. Pon tu email personal.
3. Revisa que el email llega bien, los links funcionan, el formatting se ve OK.
4. Si todo OK, **activar** el trigger.

## Automatización opcional

Los scripts locales de Buttondown son seguros por defecto:

```powershell
python scripts\buttondown_upload_curso.py
python scripts\buttondown_curso_engine.py
```

Sin `--execute` no crean drafts, no consultan suscriptores y no envían emails.
Usar `--execute` solo cuando Jordi apruebe esa acción concreta.

## Lo que NO necesita Buttondown

- La URL del PDF (`https://vsczmjjtesenlqruqoqv.supabase.co/...`) es pública, no requiere auth.
- El template `{{ subscriber.first_name }}` se rellena automáticamente con el nombre del subscriber (o "allá" si no lo proporcionó).

## Próximo paso (FASE 2)

Cuando quieras automatizar emails programados (los 3 de la secuencia de 7 días), son automated emails adicionales con trigger "After X days since subscription". Mismo proceso, otro email body.
