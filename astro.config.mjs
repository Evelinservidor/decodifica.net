// @ts-check
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';

const sitemapExcludedPaths = new Set(['/comunidad/hilo', '/login', '/recursos-ia']);

// https://astro.build/config
export default defineConfig({
  site: 'https://decodifica.net',
  base: '/',
  output: 'static',
  integrations: [
    mdx(),
    sitemap({
      filter: (page) => !sitemapExcludedPaths.has(new URL(page).pathname.replace(/\/$/, '')),
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
