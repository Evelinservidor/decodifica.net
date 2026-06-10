import type { APIRoute } from 'astro';
import { z } from 'zod';
import { createSupabaseServerClient } from '~/lib/supabase';

const schema = z.object({
  email: z.string().email('Email inválido'),
});

export const POST: APIRoute = async ({ request, url, cookies, redirect }) => {
  const formData = await request.formData();
  const parse = schema.safeParse({ email: formData.get('email') });

  if (!parse.success) {
    return redirect('/login?error=invalid_email');
  }

  const supabase = createSupabaseServerClient(cookies);
  const { error } = await supabase.auth.signInWithOtp({
    email: parse.data.email,
    options: {
      emailRedirectTo: `${url.origin}/api/auth/callback`,
    },
  });

  if (error) {
    return redirect(`/login?error=${encodeURIComponent(error.message)}`);
  }

  return redirect('/login?check_email=1');
};
