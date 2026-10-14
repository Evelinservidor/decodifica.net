import datos from '~/data/portadas.json';

// Portadas generadas con scripts/imagenes/portada.py a partir de src/data/portadas.json.
export type Portada = {
  slug: string;
  alt: string; // describe la versión limpia (sin texto)
  altOg: string; // la versión con gancho: alt + el texto que se lee en ella
  og: string; // 1200x630 con gancho (redes)
  tarjeta: string; // 640x360 con gancho (lista del blog)
  tarjeta960: string; // 960x540 con gancho
  cabecera: string; // 1600x900 limpia (artículo y Google)
  cabecera800: string; // 800x450 limpia
  ld: string[]; // 16x9, 4x3 y 1x1 limpias para los datos estructurados
};

const entradas = datos as Record<string, { alt?: string; gancho?: string } | string>;

export function portada(slug: string): Portada | null {
  const d = entradas[slug];
  if (slug.startsWith('_') || !d || typeof d === 'string' || !d.alt) return null;
  const base = `/og/blog/${slug}`;
  return {
    slug,
    alt: d.alt,
    altOg: d.gancho ? `${d.alt}. Texto: «${d.gancho.replace(/\*/g, '')}»` : d.alt,
    og: `${base}.jpg`,
    tarjeta: `${base}-tarjeta.webp`,
    tarjeta960: `${base}-tarjeta-960.webp`,
    cabecera: `${base}-16x9.webp`,
    cabecera800: `${base}-16x9-800.webp`,
    ld: [`${base}-16x9.webp`, `${base}-4x3.webp`, `${base}-1x1.webp`],
  };
}

/** Portada a partir de la ruta de og:image (/og/blog/<slug>.jpg). */
export function portadaDeOg(ogImage: string | undefined): Portada | null {
  const m = ogImage?.match(/^\/og\/blog\/([^/]+)\.jpg$/);
  return m ? portada(m[1]) : null;
}
