begin;

alter table public.profiles
  add column if not exists is_team boolean not null default false,
  add column if not exists community_badge text;

alter table public.posts
  add column if not exists category text not null default 'general',
  add column if not exists is_pinned boolean not null default false;

do $$
begin
  if not exists (
    select 1
    from pg_constraint
    where conname = 'profiles_community_badge_allowed'
      and conrelid = 'public.profiles'::regclass
  ) then
    alter table public.profiles
      add constraint profiles_community_badge_allowed
      check (community_badge is null or community_badge in ('Cuenta del equipo', 'Miembro fundador'));
  end if;

  if not exists (
    select 1
    from pg_constraint
    where conname = 'posts_category_allowed'
      and conrelid = 'public.posts'::regclass
  ) then
    alter table public.posts
      add constraint posts_category_allowed
      check (category in ('general', 'welcome', 'question', 'lab', 'vote', 'guide'));
  end if;
end
$$;

alter table public.profiles enable row level security;
alter table public.posts enable row level security;
alter table public.comments enable row level security;
alter table public.likes enable row level security;

drop policy if exists community_profiles_public_read on public.profiles;
create policy community_profiles_public_read
  on public.profiles
  for select
  to anon, authenticated
  using (true);

drop policy if exists community_posts_public_read on public.posts;
create policy community_posts_public_read
  on public.posts
  for select
  to anon, authenticated
  using (true);

drop policy if exists community_posts_insert_own on public.posts;
create policy community_posts_insert_own
  on public.posts
  for insert
  to authenticated
  with check ((select auth.uid()) = author_id);

drop policy if exists community_posts_update_own on public.posts;
create policy community_posts_update_own
  on public.posts
  for update
  to authenticated
  using ((select auth.uid()) = author_id)
  with check ((select auth.uid()) = author_id);

drop policy if exists community_posts_delete_own on public.posts;
create policy community_posts_delete_own
  on public.posts
  for delete
  to authenticated
  using ((select auth.uid()) = author_id);

drop policy if exists community_comments_public_read on public.comments;
create policy community_comments_public_read
  on public.comments
  for select
  to anon, authenticated
  using (true);

drop policy if exists community_comments_insert_own on public.comments;
create policy community_comments_insert_own
  on public.comments
  for insert
  to authenticated
  with check ((select auth.uid()) = author_id);

drop policy if exists community_comments_update_own on public.comments;
create policy community_comments_update_own
  on public.comments
  for update
  to authenticated
  using ((select auth.uid()) = author_id)
  with check ((select auth.uid()) = author_id);

drop policy if exists community_comments_delete_own on public.comments;
create policy community_comments_delete_own
  on public.comments
  for delete
  to authenticated
  using ((select auth.uid()) = author_id);

drop policy if exists community_likes_public_read on public.likes;
create policy community_likes_public_read
  on public.likes
  for select
  to anon, authenticated
  using (true);

drop policy if exists community_likes_insert_own on public.likes;
create policy community_likes_insert_own
  on public.likes
  for insert
  to authenticated
  with check ((select auth.uid()) = user_id);

drop policy if exists community_likes_delete_own on public.likes;
create policy community_likes_delete_own
  on public.likes
  for delete
  to authenticated
  using ((select auth.uid()) = user_id);

grant select on table public.profiles, public.posts, public.comments, public.likes to anon, authenticated;
grant insert (author_id, title, body) on table public.posts to authenticated;
grant insert (post_id, author_id, body) on table public.comments to authenticated;
grant insert (post_id, user_id) on table public.likes to authenticated;
grant update (title, body, updated_at) on table public.posts to authenticated;
grant update (body) on table public.comments to authenticated;
grant delete on table public.posts, public.comments, public.likes to authenticated;

revoke update on table public.profiles from authenticated;
grant update (display_name, avatar_url, bio, updated_at) on table public.profiles to authenticated;

create index if not exists community_posts_created_at_idx
  on public.posts (created_at desc);

create index if not exists community_comments_post_created_idx
  on public.comments (post_id, created_at);

alter view public.posts_with_author set (security_invoker = true);

create or replace view public.community_posts_with_author
with (security_invoker = true)
as
select
  posts.id,
  posts.author_id,
  posts.title,
  posts.body,
  posts.created_at,
  posts.updated_at,
  profiles.display_name as author_display_name,
  profiles.avatar_url as author_avatar_url,
  profiles.role as author_role,
  (
    select count(*)::integer
    from public.comments
    where comments.post_id = posts.id
  ) as comments_count,
  (
    select count(*)::integer
    from public.likes
    where likes.post_id = posts.id
  ) as likes_count,
  profiles.community_badge as author_badge,
  profiles.is_team as author_is_team,
  posts.is_pinned,
  posts.category
from public.posts
join public.profiles on profiles.id = posts.author_id;

create or replace view public.community_comments_with_author
with (security_invoker = true)
as
select
  comments.id,
  comments.post_id,
  comments.author_id,
  comments.body,
  comments.created_at,
  profiles.display_name as author_display_name,
  profiles.avatar_url as author_avatar_url,
  profiles.role as author_role,
  profiles.community_badge as author_badge,
  profiles.is_team as author_is_team
from public.comments
join public.profiles on profiles.id = comments.author_id;

grant select on table
  public.posts_with_author,
  public.community_posts_with_author,
  public.community_comments_with_author
to anon, authenticated;

do $$
declare
  profile_total integer;
  post_total integer;
begin
  select count(*) into profile_total from public.profiles;
  select count(*) into post_total from public.posts;

  if profile_total = 1 and post_total = 0 then
    update public.profiles
    set
      display_name = 'Jordi · Decodifica',
      is_team = true,
      community_badge = 'Cuenta del equipo',
      updated_at = now();
  end if;
end
$$;

commit;
