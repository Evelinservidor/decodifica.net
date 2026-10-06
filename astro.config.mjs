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
