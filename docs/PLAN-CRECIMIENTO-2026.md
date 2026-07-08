# Plan de crecimiento web — Decodifica 2026

**Estado:** En ejecución.
**Última actualización:** 2026-06-20.
**Responsable técnico:** `decodifica-web-maintainer` (agente Deco Web).
**Responsable editorial:** Jordi.

---

## Contexto

Decodifica es un canal de IA en español con:
- Web estática en Astro 4 + Tailwind 3 + TypeScript, desplegada en GitHub Pages
- 9 posts en el blog (amplificación de videos)
- Newsletter semanal en Buttondown (`https://buttondown.email/decodifica`)
- Branding claro: "IA en español, sin fluff, sin AI slop"
- Pilares editoriales: Pilar 1 (apps IA día a día), Pilar 2 (productividad con IA)

Este documento define el plan de crecimiento a 6 meses en 3 fases, con tareas concretas, métricas esperadas y modelo editorial.

---

## Estado actual (auditado 2026-06-20)

### Lo que está bien
- Sitemap generado por Astro (`@astrojs/sitemap`) en build → `sitemap-index.xml`
- `robots.txt` apunta correctamente al sitemap generado
- Buttondown integrado en 11 páginas (home, /recursos, /blog, 9 posts)
- Schema JSON-LD: `Article`, `WebSite`, `Organization` instalados
- 9 posts con OG cover 1200×630 dark mode
- Cron semanal de GSC documentado; los checks web principales viven en Codex Automations
- Lead magnets, mini-curso y newsletter drafts versionados en `lead-magnets/`

### Problemas detectados
- Repo limpio tras separar scripts OG, docs, lead magnets y artefactos locales
- Blog sigue los videos: ya posiciona bien, pero el contenido adicional (no atado a video) está ausente
- Welcome email funcionando en Buttondown
- Mini-curso 5 días activo con Codex + Buttondown Free
- Newsletter semanal preparada como draft automático revisable
- Sin acceso API directo a Plausible ni GSC desde la sesión del agente

---

## Modelo editorial 70/20/10

El modelo de contenido se divide así:

| % | Tipo | Calendario | Keywords | Esfuerzo |
|---|---|---|---|---|
| 70% | Ampliación del video | Cada video → 1 post | Atadas al video (ya investigadas) | El actual — no tocar |
| 20% | Listicles quincenales | Cada 2 semanas | Long-tail independientes | 1-2h/post |
| 10% | Pillar pages | 2-3 al año | Authority topics del canal | 4-6h/page |

**Por qué 70/20/10:**
- El 70% ya funciona (keywords atadas a videos, calendario editorial)
- El 20% cubre huecos que el video no toca (long-tail nuevo tráfico)
- El 10% construye autoridad topical (pillar pages = Google premia)

---

## FASE 1 — Fundamentos (0-30 días)

**Objetivo:** limpiar el repo, asegurar SEO técnico, arrancar newsletter.

### Tareas técnicas

- [x] Verificar sitemap y robots.txt (sin discrepancia real — Astro genera el sitemap al build)
- [x] **Cerrar archivos pendientes** (lead-magnets, scripts OG) — limpiar el repo
- [x] **Push del commit local** a `main`
- [ ] Activar cron `weekly-decodifica-web-check` (reporte automático cada lunes)
- [x] Activar cron `decodifica-newsletter-semanal-draft` (viernes 11:30 Madrid)
- [ ] Auditar indexación GSC de las 11 páginas públicas
- [ ] Validar schema y meta tags en cada página
- [x] Configurar welcome email automatizado en Buttondown

### Tareas de contenido

- [x] Activar newsletter semanal con Fórmula Rundown en modo draft revisable
- [x] Activar secuencia mini-curso 5 días (sustituye al PDF genérico)
- [ ] Primer listicle: candidato *"Las 7 mejores alternativas a ChatGPT gratuitas en 2026"*

### Métricas esperadas F1

- 0 errores de indexación en GSC
- Newsletter con primera emisión enviada
- Lead magnet activado en Buttondown
- Repo limpio, todos los archivos relevantes en `main`

---

## FASE 2 — Crecimiento (30-90 días)

**Objetivo:** posicionar el blog como referencia del nicho en español.

### Tareas

- [ ] Crear 2 pillar pages:
  - *"Productividad con IA: la guía completa 2026"*
  - *"Apps IA para el día a día: qué usar y para qué"*
- [ ] Cada pillar page: 2000+ palabras, schema FAQ, internal linking a 5+ posts
- [ ] 4-6 listicles quincenales (siguiendo el modelo 70/20/10)
- [ ] Internal linking estratégico entre posts y pillar pages
- [ ] Optimización GEO (AI-citable): estructura que ChatGPT cite los posts
- [ ] Schema FAQ en posts con preguntas reales
- [ ] Habilitar comentarios reales en el blog (engagement + contenido generado)
- [ ] Outreach a 3-5 webs amigas (Monos Estocásticos, IA en Español, Mentes Artificiales)
- [ ] 1-2 lead magnets adicionales (ej: plantillas Notion, swipes file)

### Métricas esperadas F2

- Tráfico orgánico: +30-50% vs F1
- Posts rankeando en top 10 para long-tail keywords
- Pillar pages posicionadas para authority topics
- 1-2 menciones o backlinks de webs amigas

---

## FASE 3 — Escala (90-180 días)

**Objetivo:** monetización y crecimiento defensible.

### Tareas

- [ ] Herramienta interactiva: selector de IA por caso de uso
- [ ] Programa de afiliados (Amazon, herramientas IA con referral)
- [ ] Producto digital de pago (mini-curso premium o comunidad)
- [ ] Colaboraciones con 2-3 canales YouTube del nicho
- [ ] Considerar traducción al inglés para mercado global
- [ ] Paid ads solo si el orgánico está afinado
- [ ] A/B testing en CTAs del blog y del newsletter

### Métricas esperadas F3

- 1 fuente de monetización activa
- Tráfico total: x2 vs inicio del plan
- Lista de newsletter: x3 vs inicio del plan
- 1+ herramienta interactiva en uso

---

## Cómo reporto el progreso

- Cada lunes: reporte automático del cron `weekly-decodifica-web-check`
- Cuando hay cambios: commit descriptivo + push
- Cuando hay bloqueos: escalo al root (Jordi) por Telegram
- Mensualmente: revisión del plan, ajuste de F1/F2/F3 según resultados

---

## Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| Jordi se sobrecarga con producción 70/20/10 | Empezar con 1 listicle, validar antes de escalar |
| Contenido adicional canibaliza keywords del video | Internal linking explícito + schema bien diferenciado |
| Cambios de algoritmo Google penalizan | Enfoque white-hat, contenido útil, EEAT |
| Pérdida de calidad al añadir más posts | Checklist pre-publish (ver `docs/SEO-CHECKLIST.md`) |
| Cron falla silenciosamente | Self-reminder + log en repo |

---

## Documentación relacionada

- `docs/CONTENT-WORKFLOW.md` — Cómo producir cada tipo de contenido
- `docs/NEWSLETTER-SYSTEM.md` — Sistema de newsletter + cron + Buttondown
- `docs/LEAD-MAGNETS.md` — Pack de bienvenida + mini-curso 5 días
- `docs/MAINTENANCE.md` — Tareas de mantenimiento semanal/mensual
- `docs/SEO-CHECKLIST.md` — Checklist pre-publish para cada post
