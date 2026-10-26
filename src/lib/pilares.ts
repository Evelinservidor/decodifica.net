// Guías principales («pilares») de los grupos de docs/plan-seo.md.
// Salen en el bloque «Empieza aquí» (portada y /blog/) y, al filtrar /blog/ por tema, van las primeras.
// Al crear el pilar de un grupo nuevo, se añade aquí.
export type Pilar = {
  grupo: string;
  titulo: string;
  texto: string;
  href: string;
  slug?: string; // solo si es un artículo del blog
  color: 'indigo' | 'verde' | 'rosa' | 'azul' | 'naranja' | 'noche';
};

export const pilares: Pilar[] = [
  {
    grupo: 'Claude en español',
    titulo: 'Claude: guía completa, gratis y planes',
    texto: 'Qué incluye gratis, cuánto cuestan los planes y cómo pedirle las cosas.',
    href: '/blog/claude-ia-que-es-gratis/',
    slug: 'claude-ia-que-es-gratis',
    color: 'indigo',
  },
  {
    grupo: 'IA en tu ordenador',
    titulo: 'IA local en tu PC, sin internet',
    texto: 'Qué programa elegir, qué ordenador hace falta y qué hace sin conexión.',
    href: '/blog/ia-local-sin-internet/',
    slug: 'ia-local-sin-internet',
    color: 'verde',
  },
  {
    grupo: 'Prompts',
    titulo: 'Generador de prompts y cómo escribirlos',
    texto: 'Crea un prompt claro en un minuto y aprende con 5 ejemplos.',
    href: '/herramientas/generador-prompts/',
    color: 'naranja',
  },
];

export const slugsPilar = new Set(pilares.flatMap((pilar) => (pilar.slug ? [pilar.slug] : [])));
