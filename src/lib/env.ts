import { z } from 'zod';

const emptyToUndefined = (value: unknown) => (value === '' ? undefined : value);

const envSchema = z.object({
  PUBLIC_SUPABASE_URL: z.preprocess(emptyToUndefined, z.string().url().catch('')),
  PUBLIC_SUPABASE_ANON_KEY: z.preprocess(emptyToUndefined, z.string().optional().default('')),
  PUBLIC_BUTTONDOWN_USERNAME: z.preprocess(emptyToUndefined, z.string().optional().default('decodifica')),
  PUBLIC_PLAUSIBLE_DOMAIN: z.preprocess(emptyToUndefined, z.string().optional().default('')),
  PUBLIC_SITE_URL: z.preprocess(emptyToUndefined, z.string().url().default('https://decodifica.net')),
  PUBLIC_SITE_NAME: z.preprocess(emptyToUndefined, z.string().default('Decodifica')),
});

const parsed = envSchema.safeParse(import.meta.env);
const fallbackEnv = envSchema.parse({});

if (!parsed.success && import.meta.env.DEV) {
  console.warn('Missing public env vars:', parsed.error.flatten().fieldErrors);
}

export const env = parsed.success
  ? {
      ...fallbackEnv,
      ...parsed.data,
    }
  : fallbackEnv;

if ((!env.PUBLIC_SUPABASE_URL || !env.PUBLIC_SUPABASE_ANON_KEY) && import.meta.env.DEV) {
  console.warn('Supabase public env vars are not configured; login/community features will be inactive.');
}

export type Env = z.infer<typeof envSchema>;
