# SEO Checklist — Pre-publish para cada post

**Última actualización:** 2026-06-25
**Usar:** antes de hacer commit de cualquier post nuevo en `/blog/`

Marca cada item cuando esté verificado. Si falla algún item crítico, no commitear hasta resolverlo.

---

## Antes de redactar

- [ ] Keyword principal identificada (long-tail, no genérica)
- [ ] Intención de búsqueda clara (informacional, comparativa, tutorial, transaccional)
- [ ] Posts relacionados identificados para internal linking
- [ ] OG cover planeado (1200×630 dark mode, con título visible)

---

## Estructura del post

- [ ] Title (H1) con keyword principal, <60 chars
- [ ] Meta description <160 chars con keyword
- [ ] URL slug corto, con keyword, sin palabras vacías
- [ ] Jerarquía H2 → H3 correcta (no saltar niveles)
- [ ] Al menos 1 imagen por cada 500 palabras
- [ ] Tabla comparativa o resumen si el post es de "ranking" o "comparativa"
- [ ] Tiempo de lectura entre 3-7 min (target)

---

## Schema y meta

- [ ] Schema `Article` en frontmatter
- [ ] Schema `FAQ` si el post tiene 3+ preguntas (recomendado en todos)
- [ ] canonical URL apuntando a sí mismo
- [ ] `lang="es"` en el HTML
- [ ] Open Graph image 1200×630 con texto
- [ ] Twitter card type="summary_large_image"
- [ ] Meta robots correcto (index, follow)

---

## Links

- [ ] **3+ internal links** a otros posts/pillars de Decodifica
- [ ] **1-2 external links** a fuentes oficiales
- [ ] Anchor text descriptivo (no "click aquí" ni "esto")
- [ ] Ningún link roto (verificar con `linkchecker` o manual)
- [ ] Si mencionas una herramienta o modelo: link oficial, no link de afiliado sin marcar

---

## Contenido

- [ ] Tono Jordi (1ª persona, directo, sin AI slop, español de España)
- [ ] Sin clickbait en title o meta description
- [ ] Claims verificables con URL oficial
  - Si no verificable: marcar como "VERIFICAR" o eliminar
- [ ] Sin plagio (verificar con herramienta o manual)
- [ ] Ortografía correcta (pass manual del archivo entero)
- [ ] Prompts copy-paste probados manualmente (1-2 verificados)
- [ ] Sin emojis decorativos innecesarios

---

## Engagement

- [ ] CTA claro al final:
  - Suscripción newsletter
  - Link a post relacionado
  - Link a pillar page si aplica
  - Link al video original si es ampliación
- [ ] 1 pregunta al lector o elemento interactivo (si aplica)
- [ ] 1-2 frases de cierre personal (no genérico)
- [ ] Sin CTA de "compártelo en redes" (eso lo hace Jordi manualmente)

---

## OG cover (1200×630 dark mode)

- [ ] Generada con `matrix_generate_image` siguiendo estilo JC (ver `decodifica-thumbnail-generator`)
- [ ] No texto en el prompt, composición HTML con texto blanco + ámbar
- [ ] Tipografía Impact/Anton bold con text-shadow outline
- [ ] "2026" metal plate en top-right corner
- [ ] Title del post visible y legible
- [ ] Guardada en `public/og/blog/<slug>.png`

---

## Post-publish

- [ ] Commit con mensaje descriptivo: `blog: <título del post>`
- [ ] Push a `main` (con OK de Jordi)
- [ ] Verificar deploy en `https://decodifica.net/blog/<slug>/`
- [ ] Indexar manualmente en GSC (URL Inspection → Request Indexing)
- [ ] Compartir en redes (link en Mastodon, X, LinkedIn — Jordi decide)
- [ ] Si es ampliación de video: añadir link al post en la descripción del video

---

## Errores comunes a evitar

❌ Title demasiado largo (>60 chars) — Google lo corta
❌ Meta description repetida en varios posts — Google lo penaliza
❌ Keyword stuffing — escribir para humanos, no para robots
❌ Links internos "huérfanos" (posts sin ningún link desde otras páginas)
❌ Imágenes sin alt text
❌ Schema mal formado (validar con `schema-validator` antes de commit)
❌ Prompts copy-paste que NO funcionan (verificar 1-2 manualmente)
❌ Posts con <500 palabras — Google los considera thin content
❌ Posts duplicando otros posts del canal (canibalización de keywords)

---

## Comando útil para validar

```bash
# Validar schema JSON-LD de un post
cd "C:\Users\jordi\Documents\GitHub\decodifica.net" && npm run build && npx astro check

# Detectar links rotos en posts (requiere linkchecker)
linkchecker https://decodifica.net/blog/
```

---

## Resumen: niveles de severidad

**Bloquea commit:**
- Claims no verificables sin marcar
- Schema mal formado
- Links rotos a URLs importantes
- Tono no Jordi (genérico, AI slop)

**Warning (se puede commitear pero resolver):**
- Title >60 chars
- Meta description duplicada
- <3 internal links
- Sin OG cover

**Nice-to-have (no bloquea):**
- Schema FAQ (suma, pero no obligatorio)
- Tabla comparativa (solo si aplica al tema)
- Pregunta al lector (opcional)