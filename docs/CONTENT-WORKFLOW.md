# Content Workflow — Cómo producir cada tipo de contenido

**Última actualización:** 2026-06-25
**Relacionado con:** `docs/PLAN-CRECIMIENTO-2026.md` (modelo 70/20/10)

---

## Modelo 70/20/10 (resumen)

| % | Tipo | Cuándo | Quién | Output |
|---|---|---|---|---|
| 70% | Ampliación del video | 24-48h tras subir video | Jordi produce, agente edita | 1 post en `/blog/` |
| 20% | Listicle quincenal | Cada 2 sábados alternos | Brief de Jordi, agente redacta | 1 post en `/blog/` |
| 10% | Pillar page | Trimestral (2-3 al año) | Agente redacta, Jordi valida | 1 página pilar |

---

## Tipo 1: Ampliación del video (70%)

**Cuándo se produce:** 24-48h tras subir el video a YouTube.

**Estructura del post:**
- Title con keyword principal del video
- Intro: por qué este tema importa (1 párrafo)
- Versión expandida de lo que se dijo en el video
- Prompts extra: 3-5 prompts listos para copiar-pegar
- Trucos avanzados que no entraron en el video
- Casos de uso reales
- Comparativas con alternativas
- Conclusión: resumen + CTA al video
- **Longitud:** 1500-2500 palabras

**Diferencia con el video:**
- El post es 2-3× más largo
- Incluye prompts copy-paste (el video los muestra pero no los "entrega")
- Trucos que no cupieron en el video por tiempo
- Internal linking a otros posts
- SEO optimizado (el video no)

**Workflow:**
1. Jordi sube video a YouTube
2. Jordi me pasa: título del video, link, ideas principales, prompts que usó
3. Yo redacto el post completo
4. Jordi revisa, ajusta claims, aprueba
5. Commit + push + indexar en GSC

---

## Tipo 2: Listicle quincenal (20%)

**Cuándo se produce:** cada 2 sábados alternos (entre medio de los números de newsletter).

**Estructura del post:**
- Title: "Las/Los [N] mejores [X] para [Y] en [año]"
- Intro: por qué este tema, a quién va dirigido (1 párrafo)
- 5-7 items, cada uno con:
  - Nombre + link oficial
  - Qué es (1 frase)
  - Por qué mola (1-2 frases)
  - Para quién (1 frase)
  - Precio/plan free (1 línea si aplica)
- Conclusión: recomendación por caso de uso
- **Longitud:** 1200-1800 palabras

**Brief de Jordi (cuando arranca uno nuevo):**
Jordi me pasa 5-7 herramientas o temas con:
- Nombre
- Link oficial
- 1 frase de por qué mola
- Para quién va dirigida

Yo redacto el post completo, Jordi valida y publica.

**Primeros 3 listicles candidatos:**
- "Las 7 mejores alternativas a ChatGPT gratuitas en 2026"
- "5 herramientas de IA para crear imágenes sin pagar"
- "10 prompts de Excel con IA que sí funcionan"

---

## Tipo 3: Pillar page (10%)

**Cuándo se produce:** 1 por trimestre (4 al año), o 2-3 al año.

**Estructura de la página:**
- Title: "[Tema]: la guía completa [año]"
- Hero: promesa clara + índice navegable
- Secciones (5-7), cada una 200-400 palabras
- Tabla comparativa o resumen al final
- FAQ con 5-8 preguntas (schema FAQ obligatorio)
- Conclusión + CTA newsletter
- **Longitud:** 2000-3500 palabras

**Las 2-3 pillars planificadas:**
1. *"Productividad con IA: la guía completa 2026"*
2. *"Apps IA para el día a día: qué usar y para qué"*
3. *(tercera por definir según resultado de las dos primeras)*

**Diferencia con posts normales:**
- Más largas (2000+ vs 1500)
- Schema FAQ obligatorio
- Internal linking masivo (a todos los posts relacionados)
- Se actualizan con sección, no se rehacen
- Son el "hub" al que apuntan todos los posts del tema

**Cuándo actualizar una pillar:**
- Cuando un modelo/herramienta mencionada cambia de versión o desaparece
- Cuando aparece una categoría nueva relevante
- Cada 3-6 meses como máximo, no antes

---

## Reglas comunes a todos los tipos

- **Tono:** Jordi en 1ª persona, directo, sin AI slop, español de España
- **Claims:** todo dato con URL oficial. Si no verificable, NO incluir o marcar como "VERIFICAR"
- **Ortografía:** pass manual antes de commit
- **OG cover:** obligatorio en cada post (1200×630 dark mode)
- **No clickbait:** subject lines y titles honestos
- **Schema Article:** en cada post (ver `docs/SEO-CHECKLIST.md`)

---

## Cómo Jordi arranca cada tipo

**Para ampliación de video:**
> "He subido el video '[título]' (link). Idea principal: [1 frase]. Prompts que usé: [3-5]"

**Para listicle:**
> "Listicle nuevo, tema: '[tema]'. 5-7 candidatos: [nombre + link de cada uno]"

**Para pillar page:**
> "Quiero pillar page sobre '[tema]'. Pásame 5-7 secciones que debería cubrir"

---

## Calendario semanal típico (Fase 2 en adelante)

| Día | Acción |
|---|---|
| Lunes | Reporte automático del cron GSC + planificar contenido semana |
| Martes | Jordi sube video → me pasa brief de ampliación |
| Miércoles | Redacto post de ampliación + Jordi revisa |
| Jueves | Commit + push + indexar |
| Viernes | Brief de listicle (si toca) o descanso |
| Sábado | Cron newsletter draft (8:00) + envío newsletter manual |
| Domingo | Métricas, descanso |

---

## Estado de los templates

- ✅ Plantilla newsletter Fórmula Rundown: `lead-magnets/newsletter-template.md`
- 📋 Plantilla post de blog: a crear en `docs/templates/post-blog-template.md`
- 📋 Plantilla listicle: a crear
- 📋 Plantilla pillar page: a crear