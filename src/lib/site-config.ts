/**
 * Site configuration
 * Single source of truth for site-wide constants.
 */
export const siteConfig = {
  name: 'Decodifica',
  tagline: 'IA útil, probada y explicada en español.',
  description:
    'Cada semana filtramos herramientas, modelos y flujos de IA para que sepas qué merece la pena probar y cómo aplicarlo sin perder tiempo.',
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
      title: 'Herramientas y modelos que puedes probar',
      description:
        'Apps web, modelos abiertos, alternativas gratuitas y productos nuevos con utilidad real.',
      icon: 'apps',
    },
    {
      id: 'tips-productividad',
      title: 'Productividad práctica con IA',
      description:
        'Prompts, workflows y decisiones para ahorrar tiempo en tareas reales.',
      icon: 'lightning',
    },
  ],
  antiTopics: [
    'Cortometrajes IA / vídeo artístico',
    'Wearables / Ray-Ban Meta',
    'Geopolítica IA como tema central',
    'Tutorial técnico profundo sin utilidad inmediata',
    'Comparativa genérica sin prueba ni decisión',
  ],
} as const;

export type SiteConfig = typeof siteConfig;
