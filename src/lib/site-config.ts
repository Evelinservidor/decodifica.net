/**
 * Site configuration
 * Single source of truth for site-wide constants
 */
export const siteConfig = {
  name: 'Decodifica',
  tagline: 'IA en español, sin fluff.',
  description: 'Cada semana curamos las mejores herramientas de IA y te enseñamos a usarlas de verdad. Todo gratis en la web.',
  url: 'https://decodifica.net',
  ogImage: '/og-default.png',
  author: {
    name: 'Jordi',
    email: 'hola@decodifica.net',
    twitter: '@decodificaia',
  },
  social: {
    youtube: 'https://youtube.com/@decodificaia',
    tiktok: 'https://tiktok.com/@decodificaia',
    x: 'https://x.com/decodificaia',
    linkedin: 'https://linkedin.com/in/decodificaia',
  },
  pillars: [
    {
      id: 'apps-web',
      title: 'Pilar 1: Curación de apps web',
      description: 'Las mejores IAs gratis, accesibles desde el navegador, sin coste de entrada.',
      icon: 'apps',
    },
    {
      id: 'tips-productividad',
      title: 'Pilar 2: Tips de productividad',
      description: 'Prompts, trucos y workflows para aplicar IA a tu día a día.',
      icon: 'lightning',
    },
  ],
  antiTopics: [
    'Cortometrajes IA / video artístico',
    'Wearables / Ray-Ban Meta',
    'Geopolítica IA',
    'Modelos chinos específicos',
    'Tutoriales técnicos profundos (n8n, Claude Code, agentes)',
  ],
} as const;

export type SiteConfig = typeof siteConfig;
