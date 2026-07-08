# Newsletter System — Cómo funciona todo

**Última actualización:** 2026-06-25
**Relacionado con:** `docs/PLAN-CRECIMIENTO-2026.md` y `docs/LEAD-MAGNETS.md`

---

## Stack

- **Plataforma:** Buttondown (`https://buttondown.email/decodifica`)
- **Nombre actual:** "Jordi" (personal brand)
- **Form embebido:** `src/components/NewsletterForm.astro` (doble opt-in)
- **Variable de entorno:** `PUBLIC_BUTTONDOWN_USERNAME` en `.env.local`

---

## Tipos de email

### 1. Newsletter semanal (sábado 8:00 Madrid)

- **Formato:** Fórmula Rundown (4 secciones fijas)
- **Tiempo de lectura:** 5 min
- **Plantilla:** `lead-magnets/newsletter-template.md`
- **Ejemplo:** `lead-magnets/newsletter-ejemplo-numero-1.md`
- **Generado por:** cron `weekly-decodifica-newsletter-draft` (DISABLED)

**Estructura Fórmula Rundown:**
1. **El tema de la semana** — 1 tema top con el ángulo de Jordi (2-3 párrafos)
2. **Y ADEMÁS · herramienta** — 1 herramienta con mini-tutorial de 3-5 pasos
3. **También esta semana** — 3-4 bullets curados
4. **Cierre** — 1-2 frases personales

### 2. Welcome email (inmediato al suscribirse)

- **Trigger:** nueva suscripción
- **Contenido actual:** "Aquí tienes tu PDF de 50 prompts" + secuencia de 3 nurturing
- **Plantilla:** `lead-magnets/buttondown-welcome-email.md`
- **Setup:** `lead-magnets/buttondown-setup-instructions.md`
- **Estado:** ⚠️ NO confirmado si está activado en Buttondown (requiere login manual)

### 3. Mini-curso 5 días (sustituye al PDF genérico)

- **Trigger:** nueva suscripción, secuencia automática
- **Formato:** 5 emails, 1 por día
- **Contenido:** `lead-magnets/mini-curso/dia-1-setup.md` a `dia-5-agentes.md`
- **Setup en Buttondown:** Automations → trigger "New subscriber" + 5 emails con delay
- **Estado:** 📋 Listo para activar (pendiente setup en Buttondown dashboard)

---

## Cron `weekly-decodifica-newsletter-draft`

- **Schedule:** sábado 8:00 Madrid (`0 8 * * 6`)
- **Modo:** sesión nueva (`session-mode new`)
- **Estado actual:** DISABLED
- **Reporta a:** root session (Jordi)
- **Next run:** sábado 27/06/2026 8:00 (si se activa)

**Lo que hace cuando se activa:**
1. Investiga novedades de IA con web_search + webfetch (8-10 fuentes)
2. Prioriza: modelos nuevos (Anthropic, OpenAI, Google, Meta, Mistral), herramientas trending, papers relevantes, regulación
3. Elige 1 tema top + 1 herramienta con mini-tutorial + 3-4 bullets
4. Redacta el número completo en Fórmula Rundown con voz de Jordi
5. Guarda en `lead-magnets/newsletter-drafts/numero-N-FECHA.md`
6. Reporta al root con: path del archivo, resumen por sección, URLs fuente consultadas, tiempo de lectura estimado, observaciones y claims a verificar
7. NO envía a Buttondown (Jordi valida y envía manualmente)

**Para activar:**
```bash
Activar desde Codex Automations: weekly-decodifica-newsletter-draft
```

**Para ver detalles:**
```bash
Consultar desde Codex Automations: weekly-decodifica-newsletter-draft
```

---

## Flujo semanal de Jordi

1. **Sábado 8:00** — el cron investiga y redacta el número (sesión nueva)
2. **Sábado ~9:00** — Jordi recibe el reporte del root en Telegram
3. **Sábado mañana** — Jordi abre el draft en `lead-magnets/newsletter-drafts/`, revisa claims, ajusta lo necesario
4. **Sábado mediodía** — Jordi copia-pega a Buttondown → New email → Draft → envía prueba a su email
5. **Sábado tarde** — Jordi envía a la lista
6. **Domingo-lunes** — Jordi revisa métricas en Plausible, feedback a la semana siguiente

---

## Métricas a vigilar

| Métrica | Target | Referencia |
|---|---|---|
| Open rate | >40% | The Rundown AI: 50% |
| Click rate | >5% | Media newsletters top: 5-8% |
| Unsubscribe rate | <0.5% por número | <0.5% es saludable |
| Crecimiento lista | +5-10% mensual en F2 | Newsletter top: 10-15% |
| Open rate welcome sequence | >50% | Buttondown docs: 50-60% |

---

## Comandos útiles

```bash
# Ver todos los crons del agente
Revisar automatizaciones desde Codex Automations o el dashboard local de Decodifica

# Habilitar cron específico
Activar la automatizacion correspondiente desde Codex Automations

# Trigger manual (testing)
Ejecutar manualmente la automatizacion correspondiente desde Codex Automations

# Info detallada de un cron
Consultar la automatizacion por nombre desde Codex Automations o dashboard local

# Actualizar prompt de un cron
Actualizar el prompt de la automatizacion desde Codex Automations
```

---

## Próximos pasos pendientes

- [ ] Activar cron `weekly-decodifica-newsletter-draft`
- [ ] Configurar welcome email en Buttondown con PDF o mini-curso
- [ ] Configurar secuencia mini-curso 5 días en Buttondown
- [ ] Probar el primer envío end-to-end
- [ ] Validar métricas después de 4 semanas