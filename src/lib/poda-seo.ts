// Limpieza del plan SEO (docs/plan-seo.md): páginas con noindex y páginas fusionadas en otra.
// La lista está en src/data/poda-seo.json (también la lee astro.config.mjs para el sitemap y las redirecciones).
import poda from '../data/poda-seo.json';

const conBarra = (ruta: string) => (ruta.endsWith('/') ? ruta : `${ruta}/`);

const rutasNoindex = new Set(poda.noindex.map(conBarra));
const redirecciones: Record<string, string> = poda.redirigir;

/** ¿Esta página lleva noindex por la limpieza? */
export function esNoindex(ruta: string): boolean {
  return rutasNoindex.has(conBarra(ruta));
}

/** ¿Esta página se ha fusionado en otra? */
export function estaRedirigida(ruta: string): boolean {
  return conBarra(ruta) in redirecciones;
}

/** Enlace bueno: si la página se fusionó en otra, el destino; si no, la misma. */
export function enlace(ruta: string): string {
  return redirecciones[conBarra(ruta)] ?? ruta;
}
