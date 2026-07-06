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
    publicEmailLabel: 'hola@decodifica.net',
  },
  social: {
    youtube: 'https://www.youtube.com/@decodificaia',
    facebook: 'https://www.facebook.com/JCAutomatizacionesIA',
    bluesky: 'https://bsky.app/profile/jc-ia.bsky.social',
    tiktok: 'https://www.tiktok.com/@decodificalaia',
  },
  newsletter: {
    url: 'https://buttondown.email/decodifica',
    username: 'decodifica',
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
