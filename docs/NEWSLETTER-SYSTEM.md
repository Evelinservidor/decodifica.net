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

### 1. Newsletter semanal (draft viernes 11:30 Madrid)

- **Formato:** Fórmula Rundown (4 secciones fijas)
- **Tiempo de lectura:** 5 min
- **Plantilla:** `lead-magnets/newsletter-template.md`
- **Ejemplo:** `lead-magnets/newsletter-ejemplo-numero-1.md`
- **Generado por:** cron Codex `decodifica-newsletter-semanal-draft` (ACTIVE)
- **Envío:** manual desde Buttondown tras revisión de Jordi

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

- **Trigger:** nueva suscripción + cron diario propio
- **Formato:** 5 emails, 1 por día
- **Contenido:** `lead-magnets/mini-curso/dia-1-setup.md` a `dia-5-agentes.md`
- **Setup en Buttondown:** welcome email nativo + motor Codex para el mini-curso
- **Estado:** listo para probar con email de Jordi y activar cron diario

Buttondown Free no incluye Automations nativas para welcome sequences completas.
Por eso la secuencia la gestiona `scripts/buttondown_curso_engine.py` usando la
API gratuita y metadata de suscriptor. El motor crea emails privados y no
archivados para evitar el prefijo `[PREVIEW]` que Buttondown añade al enviar
drafts.

Cron Codex activo:

```text
decodifica-newsletter-minicurso-diario
```

Horario: diario a las 11:20. Primero ejecuta `--inspect`; si no hay errores,
ejecuta `--execute`. No usa `--force-day`.

El engine usa `curso_version=decodifica_codex_v2`; si encuentra metadata antigua
de curso, resetea solo las claves `curso_*` y empieza limpio.

---

## Cron `decodifica-newsletter-semanal-draft`

- **Schedule:** viernes 11:30 Madrid
- **Modo:** Codex Automations, worktree del repo web
- **Estado actual:** ACTIVE
- **Reporta a:** root session (Jordi)
- **Output:** `lead-magnets/newsletter-drafts/numero-YYYY-MM-DD.md`

**Lo que hace cuando se activa:**
1. Investiga novedades de IA con web_search + webfetch (8-10 fuentes)
2. Prioriza: modelos nuevos (Anthropic, OpenAI, Google, Meta, Mistral), herramientas trending, papers relevantes, regulación
3. Elige 1 tema top + 1 herramienta con mini-tutorial + 3-4 bullets
4. Redacta el número completo en Fórmula Rundown con voz de Jordi
5. Guarda en `lead-magnets/newsletter-drafts/numero-N-FECHA.md`
6. Reporta al root con: path del archivo, resumen por sección, URLs fuente consultadas, tiempo de lectura estimado, observaciones y claims a verificar
7. NO envía a Buttondown (Jordi valida y envía manualmente)

El prompt del cron exige fuentes primarias cuando sea posible, evita temas fuera
del canon de Decodifica y añade al final una checklist de revisión.

---

## Flujo semanal de Jordi

1. **Viernes 11:30** — el cron investiga y redacta el número.
2. **Viernes tarde** — Jordi abre el draft en `lead-magnets/newsletter-drafts/`, revisa claims y ajusta tono.
3. **Sábado mañana** — Jordi copia-pega a Buttondown → New email → Draft → envía prueba a su email.
4. **Sábado tarde** — Jordi envía a la lista si todo está correcto.
5. **Domingo-lunes** — Jordi revisa métricas y feedback para la semana siguiente.

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

- [x] Activar cron `decodifica-newsletter-semanal-draft`
- [ ] Configurar welcome email en Buttondown con PDF o mini-curso
- [ ] Probar `scripts/buttondown_curso_engine.py --execute --test-email "<email>" --force-day 1`
- [ ] Configurar cron diario del mini-curso en Codex
- [ ] Revisar el primer draft semanal generado por Codex
- [ ] Probar el primer envío semanal end-to-end
- [ ] Validar métricas después de 4 semanas
