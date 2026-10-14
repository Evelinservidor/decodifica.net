import { blogPostIndex, type BlogPostIndexEntry } from '~/lib/blog-post-index';

// «Lo más leído»: artículos con más clics (y luego impresiones) en el último informe
// de Search Console (data/gsc_weekly/latest.json, lo actualiza el workflow de los lunes).
// Si falta el informe, devuelve los más recientes.
type Fila = { page: string; clicks: number; impressions: number };
type Informe = { per_site?: Record<string, { pages?: { current?: Fila[] } }> };

const informes = import.meta.glob('../../data/gsc_weekly/latest.json', { eager: true, import: 'default' }) as Record<string, Informe>;

export function masLeidos(n = 5): BlogPostIndexEntry[] {
  const informe = Object.values(informes)[0];
  const sitio = Object.entries(informe?.per_site ?? {}).find(([clave]) => clave.includes('decodifica'))?.[1];
  const filas = [...(sitio?.pages?.current ?? [])].sort(
    (a, b) => b.clicks - a.clicks || b.impressions - a.impressions,
  );
  const porSlug = new Map(blogPostIndex.map((post) => [post.slug, post]));
  const elegidos: BlogPostIndexEntry[] = [];
  for (const fila of filas) {
    const slug = fila.page.match(/\/blog\/([^/]+)\/?$/)?.[1];
    const post = slug ? porSlug.get(slug) : undefined;
    if (post && !elegidos.includes(post)) elegidos.push(post);
    if (elegidos.length === n) break;
  }
  for (const post of blogPostIndex) {
    if (elegidos.length >= n) break;
    if (!elegidos.includes(post)) elegidos.push(post);
  }
  return elegidos;
}
