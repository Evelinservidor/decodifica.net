import type { APIRoute } from 'astro';
import { blogPostIndex } from '~/lib/blog-post-index';

export const prerender = true;

const SITE_URL = 'https://decodifica.net';
function xml(value: string): string {
  return value
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&apos;');
}

export const GET: APIRoute = () => {
  const items = blogPostIndex.map((post) => {
    const url = `${SITE_URL}/blog/${post.slug}/`;
    return [
      '<item>',
      `<title>${xml(post.title)}</title>`,
      `<link>${url}</link>`,
      `<guid isPermaLink="true">${url}</guid>`,
      `<description>${xml(post.description)}</description>`,
      `<pubDate>${new Date(`${post.pubDate}T12:00:00Z`).toUTCString()}</pubDate>`,
      '</item>',
    ].join('');
  }).join('');

  const body = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<rss version="2.0"><channel>',
    '<title>Decodifica</title>',
    `<link>${SITE_URL}/</link>`,
    '<description>Guías prácticas y análisis de inteligencia artificial en español.</description>',
    '<language>es</language>',
    `<lastBuildDate>${new Date().toUTCString()}</lastBuildDate>`,
    items,
    '</channel></rss>',
  ].join('');

  return new Response(body, {
    headers: {
      'Content-Type': 'application/rss+xml; charset=utf-8',
      'Cache-Control': 'public, max-age=3600',
    },
  });
};
