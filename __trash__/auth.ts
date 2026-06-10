import type { SupabaseClient, User } from '@supabase/supabase-js';

export type SignInProvider = 'google' | 'email';

export interface AuthResult {
  user: User | null;
  error: string | null;
}

/**
 * Sign in with OAuth provider (Google, GitHub, etc)
 */
export async function signInWithOAuth(
  supabase: SupabaseClient,
  provider: 'google' = 'google',
  redirectTo: string = '/'
): Promise<AuthResult> {
  const { error } = await supabase.auth.signInWithOAuth({
    provider,
    options: {
      redirectTo: `${window.location.origin}${redirectTo}`,
    },
  });

  if (error) {
    return { user: null, error: error.message };
  }

  return { user: null, error: null };
}

/**
 * Sign in with magic link (email)
 */
export async function signInWithMagicLink(
  supabase: SupabaseClient,
  email: string,
  redirectTo: string = '/'
): Promise<AuthResult> {
  const { error } = await supabase.auth.signInWithOtp({
    email,
    options: {
      emailRedirectTo: `${window.location.origin}${redirectTo}`,
    },
  });

  if (error) {
    return { user: null, error: error.message };
  }

  return { user: null, error: null };
}

/**
 * Sign out
 */
export async function signOut(supabase: SupabaseClient): Promise<{ error: string | null }> {
  const { error } = await supabase.auth.signOut();
  return { error: error?.message ?? null };
}

/**
 * Get current user
 */
export async function getCurrentUser(supabase: SupabaseClient): Promise<User | null> {
  const { data } = await supabase.auth.getUser();
  return data.user;
}
