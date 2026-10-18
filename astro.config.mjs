// @ts-check
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import { readdirSync, readFileSync } from 'node:fs';

// Páginas que solo redirigen: fuera del sitemap.
const sitemapExcludedPaths = new Set([
  '/comunidad',
  '/comunidad/hilo',
  '/login',
  '/recursos-ia',
  '/quienes-somos',
  '/decodifica',
]);

// Limpieza del plan SEO (docs/plan-seo.md): fuera del sitemap las páginas con noindex
// y las fusionadas en otra (que pasan a ser redirecciones).
const poda = JSON.parse(readFileSync('./src/data/poda-seo.json', 'utf8'));
for (const ruta of [...poda.noindex, ...Object.keys(poda.redirigir)]) {
  sitemapExcludedPaths.add(ruta.replace(/\/$/, ''));
}
const redirects = Object.fromEntries(
  Object.entries(poda.redirigir).map(([desde, hasta]) => [desde.replace(/\/$/, ''), { status: /** @type {301} */ (301), destination: String(hasta) }]),
);

// lastmod real de cada artículo: modifiedDate si existe, si no pubDate.
const articleLastmod = new Map();
for (const file of readdirSync('./src/pages/blog')) {
  if (!file.endsWith('.astro') || file === 'index.astro') continue;
  const source = readFileSync(`./src/pages/blog/${file}`, 'utf8');
  if (/Astro\.redirect\(/.test(source)) {
    sitemapExcludedPaths.add(`/blog/${file.replace(/\.astro$/, '')}`);
    continue;
  }
  const date =
    source.match(/const\s+modifiedDate\s*=\s*["'](\d{4}-\d{2}-\d{2})["']/)?.[1] ??
    source.match(/const\s+pubDate\s*=\s*["'](\d{4}-\d{2}-\d{2})["']/)?.[1];
  if (date) articleLastmod.set(`/blog/${file.replace(/\.astro$/, '')}`, date);
}

// https://astro.build/config
export default defineConfig({
  site: 'https://decodifica.net',
  base: '/',
  output: 'static',
  redirects,
  integrations: [
    mdx(),
    sitemap({
      filter: (page) => !sitemapExcludedPaths.has(new URL(page).pathname.replace(/\/$/, '')),
      serialize(item) {
        const date = articleLastmod.get(new URL(item.url).pathname.replace(/\/$/, ''));
        if (date) item.lastmod = new Date(`${date}T00:00:00Z`).toISOString();
        return item;
      },
    }),
  ],
  build: {
    inlineStylesheets: 'auto',
  },
  prefetch: {
    prefetchAll: true,
    defaultStrategy: 'viewport',
  },
  vite: {
    build: {
      cssCodeSplit: true,
    },
  },
  security: {
    checkOrigin: true,
  },
});
