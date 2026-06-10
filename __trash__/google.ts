import type { APIRoute } from 'astro';
import { createSupabaseServerClient } from '~/lib/supabase';

export const GET: APIRoute = async ({ cookies, url, redirect }) => {
  const supabase = createSupabaseServerClient(cookies);
  const redirectTo = url.searchParams.get('redirectTo') ?? '/comunidad';

  const { data, error } = await supabase.auth.signInWithOAuth({
    provider: 'google',
    options: {
      redirectTo: `${url.origin}/api/auth/callback?next=${encodeURIComponent(redirectTo)}`,
    },
  });

  if (error || !data.url) {
    return redirect('/login?error=oauth_failed');
  }

  return redirect(data.url);
};
