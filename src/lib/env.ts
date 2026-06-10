import { z } from 'zod';

/**
 * Validación de variables de entorno al arranque
 * Falla rápido si falta algo crítico
 */
const envSchema = z.object({
  PUBLIC_SUPABASE_URL: z.string().url(),
  PUBLIC_SUPABASE_ANON_KEY: z.string().min(20),
  PUBLIC_BUTTONDOWN_USERNAME: z.string().optional(),
  PUBLIC_PLAUSIBLE_DOMAIN: z.string().optional(),
  PUBLIC_SITE_URL: z.string().url().default('https://decodifica.net'),
  PUBLIC_SITE_NAME: z.string().default('Decodifica'),
});

const parsed = envSchema.safeParse(import.meta.env);

if (!parsed.success) {
  console.error('❌ Invalid environment variables:', parsed.error.flatten().fieldErrors);
  throw new Error('Invalid environment variables');
}

export const env = parsed.data;
export type Env = z.infer<typeof envSchema>;
