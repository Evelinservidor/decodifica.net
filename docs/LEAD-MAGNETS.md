# Lead Magnets — Pack de bienvenida y mini-curso

**Última actualización:** 2026-06-25
**Relacionado con:** `docs/NEWSLETTER-SYSTEM.md`

---

## Estado actual

- ⚠️ PDF de "50 prompts" (genérico) — sigue siendo el lead magnet configurado en Buttondown
- ✅ Mini-curso 5 días "dejar de usar ChatGPT como un junior" — listo para activar
- 📁 Archivos en `lead-magnets/`

---

## Estructura del directorio `lead-magnets/`

```
lead-magnets/
├── buttondown-setup-instructions.md       Instrucciones para configurar welcome
├── buttondown-welcome-email.md            Template del welcome email actual (PDF)
├── newsletter-template.md                 Plantilla Fórmula Rundown semanal
├── newsletter-ejemplo-numero-1.md         Ejemplo rellenado de newsletter
├── 50-prompts-ia.pdf                      PDF lead magnet actual (genérico)
├── claude-skills-desde-cero.pdf           Lead magnet adicional (a futuro)
├── workflows-ia-dia-a-dia.pdf             Lead magnet adicional (a futuro)
├── gen_lead_magnet.py                     Script para generar PDFs
├── verify.py                              Verificación de PDFs
├── prompts/                               Workflows sueltos en Markdown
│   ├── workflow-1-emails.md
│   ├── workflow-2-prompt-final.md
│   ├── workflow-2-prompt-parcial.md
│   ├── workflow-3-csv.md
│   ├── workflow-4-semana.md
│   └── workflow-5-aprender.md
├── mini-curso/                            Mini-curso 5 días (sustituye al PDF)
│   ├── README.md                          Overview del mini-curso
│   ├── dia-1-setup.md                     Email día 1
│   ├── dia-2-estructura-prompts.md        Email día 2
│   ├── dia-3-contexto-archivos.md         Email día 3
│   ├── dia-4-iteracion.md                 Email día 4
│   └── dia-5-agentes.md                   Email día 5
└── newsletter-drafts/                     Drafts generados por el cron
    └── numero-N-FECHA.md                  (vacío hasta que se active el cron)
```

---

## Decisión: PDF genérico vs mini-curso

**Análisis (junio 2026):**
- PDFs tradicionales convierten 8-12%
- Mini-curso (learning resources) convierte 27%
- 3× más engagement

**Decisión tomada:** sustituir el PDF de 50 prompts por el mini-curso 5 días.

**Por qué:**
- Más exclusivo (Jordi en 1ª persona)
- Engagement sostenido (5 emails vs 1 PDF)
- 3× más conversión
- Nativo de Buttondown (sequence ya configurada)
- Reutilizable: sacamos otro mini-curso cada trimestre

---

## Setup en Buttondown (mini-curso)

### Welcome email (día 0, inmediato)
- **Trigger:** New subscriber
- **Asunto:** "Mañana empieza tu curso de 5 días sobre ChatGPT"
- **Contenido:** bienvenida + "Mañana recibes el primer email"
- **Archivo:** `lead-magnets/mini-curso/README.md` (plantilla base)

### Emails día 1-5

Buttondown Free no incluye Automations nativas para secuencias relativas a cada
suscriptor. La opción activa es gestionarlo desde Codex con:

```powershell
python scripts\buttondown_curso_engine.py --inspect
python scripts\buttondown_curso_engine.py --execute
```

El script usa los drafts creados en Buttondown, envía solo el email que toca y
marca progreso en metadata:

- `curso_started_at`
- `curso_version`
- `curso_dia_1_sent_at` a `curso_dia_5_sent_at`
- `curso_completed_at`

Para probar solo con Jordi:

```powershell
python scripts\buttondown_curso_engine.py --inspect --test-email "<email>"
python scripts\buttondown_curso_engine.py --execute --test-email "<email>" --force-day 1
```

`--force-day` requiere siempre `--test-email`.

### Después del día 5
- El suscriptor pasa a recibir solo la newsletter semanal
- No más emails automáticos hasta nueva suscripción

---

## PDFs adicionales (a futuro)

Después de Fase 2, considerar:
- "10 prompts de productividad con IA" (PDF descargable en email día 3)
- "Comparativa de Custom GPTs del canal" (PDF descargable en email día 5)
- "Mi setup de IA personal 2026" (PDF descargable, post específico)

Cada PDF adicional debe tener:
- Contenido exclusivo (no duplicar posts del blog)
- Diseño dark mode coherente con el canal
- Tono Jordi, sin AI slop
- Disclaimer: "verificado a fecha de [mes año], las herramientas cambian"

---

## Estado de activación (checklist)

- [ ] Welcome email configurado en Buttondown (trigger "New subscriber")
- [x] Cron diario del mini-curso configurado en Codex (`decodifica-newsletter-minicurso-diario`)
- [ ] PDF de "50 prompts" desactivado (sustituido por mini-curso)
- [ ] Primer envío de prueba a email de Jordi
- [ ] Métricas abiertas después del primer envío real
- [ ] Decisión sobre si conservar el PDF de 50 prompts como bonus descargable

---

## Cómo crear un lead magnet nuevo

1. **Decidir tipo:** PDF descargable, mini-curso, herramienta interactiva, template Notion, etc.
2. **Brief de Jordi:** tema, promesa, formato, longitud, deadline
3. **Investigación:** el agente investiga el tema con web_search y verifica datos
4. **Drafting:** el agente redacta (o Jordi redacta + agente edita)
5. **Diseño:** PDF en dark mode, alineado con branding
6. **Validación:** Jordi revisa ortografía y claims
7. **Setup en Buttondown:** nueva sequence o automatización
8. **Métricas:** open rate, click rate, conversion al mes

---

## Métricas de un lead magnet efectivo

| Métrica | Target |
|---|---|
| Open rate (welcome email) | >50% |
| Click rate welcome → lead magnet | >30% |
| Open rate secuencia día 1-5 | decreciente natural (50% → 30%) |
| Conversión sequence → engagement | >40% abren los 5 emails |
| Suscriptores activos tras 30 días | >60% de los que entraron |
