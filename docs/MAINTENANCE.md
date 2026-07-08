# Maintenance — Tareas semanales, mensuales y trimestrales

**Última actualización:** 2026-06-25
**Relacionado con:** `docs/PLAN-CRECIMIENTO-2026.md`

---

## Semanal (lunes 9:30 Madrid)

**Cron:** `weekly-decodifica-web-check` (DISABLED, esperando OK para activar)

**Tareas automatizadas:**

- [ ] Ejecutar `weekly_gsc_report.py` y revisar las **10 queries con peor CTR**
- [ ] Revisar las **5 queries con mejor posición** (oportunidades de pillar pages)
- [ ] Detectar **links rotos** con `linkchecker` o `wget --spider`
- [ ] Validar **schema.org** en posts nuevos con `schema-validator`
- [ ] Verificar **indexación** de las URLs principales en GSC
- [ ] Commit + push de cualquier cambio menor detectado

**Output:** `data/gsc_weekly/YYYY-MM-DD_gsc_weekly.json` + reporte al root

**Para activar:**
```bash
Activar desde Codex Automations: weekly-decodifica-web-check
```

---

## Mensual (1er lunes del mes, 10:00 Madrid)

**Cron:** `monthly-decodifica-web-refresh` (DISABLED, esperando OK)

**Tareas:**

- [ ] **Refrescar 1-2 blog posts viejos:**
  - Añadir info nueva
  - Actualizar claims
  - Refrescar meta description
  - Verificar que los links siguen vivos
- [ ] Validar `public/sitemap-index.xml` contra rutas reales
- [ ] Verificar que schema y meta tags siguen correctos
- [ ] Revisar **backlinks nuevos** (Plausible referrals + GSC)
- [ ] Reportar al root con: posts refrescados + métricas del mes

**Criterios para elegir posts a refrescar:**
- Posts con peor CTR pero buena posición
- Posts con tema que ha cambiado mucho desde publicación
- Posts pilares que llevan 6+ meses sin actualizar

---

## Trimestral (cada 3 meses, manual o por trigger del agente)

**Sin cron automatizado. Trigger: revisión humana o auto-trigger cuando llega el momento.**

- [ ] Crear o actualizar 1 pillar page
- [ ] Revisar la estrategia de contenido (¿70/20/10 sigue funcionando?)
- [ ] Auditar competencia (webs de IA en español que estén creciendo)
- [ ] Planificar el siguiente mini-curso o lead magnet
- [ ] Revisar backlinks y oportunidades de outreach

---

## Checklist de deploy

**Cada vez que se hace push a `main`:**

- [ ] `astro build` se ejecuta sin errores
- [ ] GitHub Actions deploy OK
- [ ] Sitemap regenerado (en producción, no local — `sitemap-index.xml`)
- [ ] Newsletter form sigue funcionando (test con email)
- [ ] OG covers de posts nuevos visibles en Twitter/Facebook debugger
- [ ] Schema Article y FAQ válidos en cada post nuevo
- [ ] Sin 404 en internal links

---

## Comandos útiles

```bash
# Estado del repo
git -C "C:\Users\jordi\Documents\GitHub\decodifica.net" status
git -C "C:\Users\jordi\Documents\GitHub\decodifica.net" log --oneline -10

# Build local (sin commit)
cd "C:\Users\jordi\Documents\GitHub\decodifica.net" && npm run build

# Ver sitemap generado tras build
Get-ChildItem "C:\Users\jordi\Documents\GitHub\decodifica.net\dist" -Filter "sitemap*"

# Listar crons del agente
Revisar automatizaciones desde Codex Automations o el dashboard local de Decodifica

# Habilitar cron
Activar la automatizacion correspondiente desde Codex Automations

# Trigger manual (testing)
Ejecutar manualmente la automatizacion correspondiente desde Codex Automations

# Info detallada de un cron
Consultar detalles desde Codex Automations o el dashboard local
```

---

## Estado actual de los crons

| Cron | Schedule | Estado | Función |
|---|---|---|---|
| `weekly-decodifica-web-check` | lunes 9:30 Madrid | DISABLED | Reporte GSC semanal |
| `monthly-decodifica-web-refresh` | 1er lunes mes 10:00 Madrid | DISABLED | Refresco mensual |
| `weekly-decodifica-newsletter-draft` | sábado 8:00 Madrid | DISABLED | Draft newsletter semanal |

**Para activar todos (cuando Jordi dé OK):**
```bash
Activar desde Codex Automations: weekly-decodifica-web-check
Activar desde Codex Automations: monthly-decodifica-web-refresh
Activar desde Codex Automations: weekly-decodifica-newsletter-draft
```

**Para ver detalles:**
```bash
Consultar la automatizacion por nombre desde Codex Automations o dashboard local
```

---

## Reglas duras de mantenimiento

1. **NO borrar páginas sin OK explícito de Jordi**
2. **NO tocar `.env.local`** (claves Supabase, Buttondown, Plausible)
3. **NUNCA aceptar admin tokens** (service_role, restricted, AWS secret)
4. **SIEMPRE ortografía PASS** antes de commit (pass manual del archivo entero)
5. **NO deploys a producción sin OK** de Jordi (el CI/CD se activa con push, pero el contenido lo aprueba Jordi)
6. **NO improvisar claims** — todo dato con URL oficial
7. **SIEMPRE reportar al root** después de cualquier acción

---

## Resolución de problemas comunes

### El cron no se ejecuta
1. Verificar estado: `Consultar la automatizacion por nombre desde Codex Automations o dashboard local`
2. Si está DISABLED pero debería estar activo: `Codex Automations`
3. Si está activo pero no corre: revisar logs de Codex/automatizaciones locales.

### El deploy falla
1. Verificar build local: `npm run build`
2. Revisar errores en consola
3. Si es tema de dependencias: `npm install` y rebuild
4. Si persiste, escalar a Jordi

### GSC no muestra datos nuevos
1. Esperar 2-3 días (GSC tiene delay)
2. Verificar que el sitemap esté enviado: `Codex Automations` + revisar `data/gsc_weekly/`
3. Pedir indexación manual de URLs concretas en GSC dashboard

### Newsletter no llega
1. Verificar que el email del suscriptor no esté bounced
2. Comprobar que el contenido no esté en spam (asunto sin palabras spam-trigger)
3. Verificar DKIM/SPF/DMARC del dominio remitente
