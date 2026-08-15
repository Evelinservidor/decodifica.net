export type BlogPostIndexEntry = {
  slug: string;
  title: string;
  description: string;
  pubDate: string;
};

const sources = import.meta.glob('../pages/blog/*.astro', {
  eager: true,
  import: 'default',
  query: '?raw',
}) as Record<string, string>;

function field(source: string, name: string): string | null {
  const match = source.match(new RegExp(`const\\s+${name}\\s*=\\s*(["'])(.*?)\\1\\s*;`));
  return match?.[2]?.trim() || null;
}

export const blogPostIndex: BlogPostIndexEntry[] = Object.entries(sources)
  .map(([path, source]) => {
    const slug = path.split('/').pop()?.replace(/\.astro$/, '') ?? '';
    return {
      slug,
      title: field(source, 'title'),
      description: field(source, 'description'),
      pubDate: field(source, 'pubDate'),
    };
  })
  .filter((post): post is BlogPostIndexEntry =>
    Boolean(post.slug && post.title && post.description && post.pubDate),
  )
  .sort((left, right) => right.pubDate.localeCompare(left.pubDate));
