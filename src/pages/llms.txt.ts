import type { APIRoute } from 'astro';
import { blogPostIndex } from '~/lib/blog-post-index';
import { siteConfig } from '~/lib/site-config';

// llms.txt (https://llmstxt.org/): resumen de la web para asistentes de IA.
// La lista de artículos se genera en cada build a partir de src/pages/blog/.
export const prerender = true;

const SITE_URL = siteConfig.url;

const link = (title: string, path: string, note: string) => `- [${title}](${SITE_URL}${path}): ${note}`;

export const GET: APIRoute = () => {
  const articles = blogPostIndex.map((post) =>
    link(post.title, `/blog/${post.slug}/`, `${post.description} (actualizado el ${post.modifiedDate})`),
  );

  const body = [
    '# Decodifica',
    '',
    '> Decodifica es una web en español sobre inteligencia artificial práctica: guías, comparativas y flujos de trabajo para elegir y usar herramientas de IA (asistentes, modelos abiertos, automatización y productividad) sin perderse en el ruido.',
    '',
    'Para quién es: personas y pequeños equipos de España, Latinoamérica y la comunidad hispanohablante de Estados Unidos que quieren usar la IA en tareas reales sin conocimientos técnicos avanzados. Está escrita en español neutro.',
    '',
    'Cómo se hace: cada dato (precios, límites, funciones, fechas) se comprueba en la fuente oficial (documentación, página de precios, blog o repositorio oficial) y se enlaza al final del artículo en «Fuentes». Los precios indican el mes en que se consultaron y se revisan cada mes. Cada artículo muestra su fecha de publicación y la de su última revisión. Decodifica no afirma haber probado una herramienta si no hay una prueba documentada. Más detalles en https://decodifica.net/sobre/.',
    '',
    '## Artículos',
    '',
    ...articles,
    '',
    '## Herramientas y comparativas',
    '',
    link('Catálogo de herramientas de IA', '/herramientas/', 'fichas de herramientas con precio, privacidad, dificultad y plataformas.'),
    link('Comparador de herramientas de IA', '/herramientas/comparador/', 'compara hasta tres herramientas por tarea, precio, privacidad y dificultad.'),
    link('ChatGPT vs Claude', '/herramientas/chatgpt-vs-claude/', 'diferencias de uso para escritura, análisis, archivos y privacidad.'),
    link('NotebookLM vs Perplexity', '/herramientas/notebooklm-vs-perplexity/', 'trabajar con documentos propios frente a buscar en la web.'),
    link('Gamma vs Canva AI', '/herramientas/gamma-vs-canva-ai/', 'presentaciones con IA: estructura frente a diseño visual.'),
    link('Generador de prompts', '/herramientas/generador-prompts/', 'ayuda a escribir prompts por tarea, contexto y resultado esperado, sin enviar datos a ninguna API.'),
    '',
    '## Flujos de trabajo',
    '',
    link('Investigar un tema sin perder las fuentes', '/workflows/investigar-con-fuentes/', 'separar búsqueda, fuentes, análisis y redacción.'),
    link('Verificar una fórmula de hoja de cálculo', '/workflows/verificar-formula-hoja-calculo/', 'comprobar una fórmula generada por IA antes de usarla.'),
    '',
    '## Sobre Decodifica',
    '',
    link('Quiénes somos y cómo trabajamos', '/sobre/', 'quién está detrás, cómo se comprueban los datos y cómo pedir una corrección.'),
    link('Contacto', '/contacto/', `correcciones y consultas: ${siteConfig.author.publicEmailLabel}.`),
    link('Newsletter', '/newsletter/', 'resumen semanal de guías y herramientas.'),
    '',
    '## Optional',
    '',
    link('Mapa del sitio', '/sitemap-index.xml', 'lista completa de URLs públicas, regenerada en cada publicación.'),
    link('RSS', '/rss.xml', 'últimos artículos.'),
    '',
  ].join('\n');

  return new Response(body, {
    headers: { 'Content-Type': 'text/plain; charset=utf-8' },
  });
};
