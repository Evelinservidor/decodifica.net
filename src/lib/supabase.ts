import { createBrowserClient, createServerClient, type CookieOptionsWithName } from '@supabase/ssr';
import type { AstroCookies } from 'astro';

// Environment variables validation
const SUPABASE_URL = import.meta.env.PUBLIC_SUPABASE_URL;
const SUPABASE_ANON_KEY = import.meta.env.PUBLIC_SUPABASE_ANON_KEY;

if (!SUPABASE_URL || !SUPABASE_ANON_KEY) {
  throw new Error(
    'Missing Supabase environment variables. Check .env.local has PUBLIC_SUPABASE_URL and PUBLIC_SUPABASE_ANON_KEY.'
  );
}

const cookieOptions: CookieOptionsWithName = {
  path: '/',
  httpOnly: true,
  sameSite: 'lax',
  secure: import.meta.env.PROD,
};

/**
 * Cliente para el navegador (componentes con interactividad)
 * Usa cookies de Supabase Auth para mantener la sesión
 */
export function createSupabaseBrowserClient() {
  return createBrowserClient(SUPABASE_URL, SUPABASE_ANON_KEY, {
    cookieOptions,
  });
}

/**
 * Cliente para el servidor (SSR, API endpoints)
 * Pasa las cookies de Astro para que la sesión se mantenga
 */
export function createSupabaseServerClient(cookies: AstroCookies) {
  return createServerClient(SUPABASE_URL, SUPABASE_ANON_KEY, {
    cookieOptions,
    cookies: {
      get(name: string) {
        return cookies.get(name)?.value;
      },
      set(name: string, value: string, options: Record<string, unknown>) {
        cookies.set(name, value, options);
      },
      remove(name: string, options: Record<string, unknown>) {
        cookies.delete(name, options);
      },
    },
  });
}
