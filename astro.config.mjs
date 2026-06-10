// @ts-check
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import mdx from '@astrojs/mdx';

// https://astro.build/config
export default defineConfig({
  site: 'https://decodifica.net',
  output: 'static',
  integrations: [
    tailwind({
      applyBaseStyles: true,
    }),
    mdx(),
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
    ssr: {
      noExternal: ['@supabase/ssr', '@supabase/supabase-js'],
    },
  },
  security: {
    checkOrigin: true,
  },
});
