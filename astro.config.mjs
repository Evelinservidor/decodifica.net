// @ts-check
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  site: 'https://decodifica.net',
  base: '/',
  output: 'static',
  integrations: [
    tailwind({
      applyBaseStyles: true,
    }),
    mdx(),
    sitemap(),
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
