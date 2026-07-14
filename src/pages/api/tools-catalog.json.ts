import type { APIRoute } from 'astro';
import { tools } from '~/data/tools';

export const prerender = true;

export const GET: APIRoute = () => {
  const payload = {
    schemaVersion: '1.0.0',
    generatedAt: new Date().toISOString(),
    policy: {
      dateChangesRequireRealReview: true,
      sourceChangeIsOnlyAReviewSignal: true,
      usefulChangesAreNeverForced: true,
    },
    tools: tools.map((tool) => ({
      slug: tool.slug,
      name: tool.name,
      useCase: tool.useCase,
      price: tool.price,
      privacy: tool.privacy,
      difficulty: tool.difficulty,
      platforms: tool.platforms,
      status: tool.status,
      evidenceLevel: tool.evidenceLevel,
      verifiedAt: tool.verifiedAt,
      nextReviewAt: tool.nextReviewAt,
      reviewCadenceDays: tool.reviewCadenceDays,
      reviewedFields: tool.reviewedFields,
      officialUrl: tool.officialUrl,
      officialSources: tool.detail?.sources ?? [{ label: 'Página oficial', href: tool.officialUrl }],
      freshnessStatus: tool.freshnessStatus,
    })),
  };

  return new Response(JSON.stringify(payload, null, 2), {
    headers: { 'Content-Type': 'application/json; charset=utf-8' },
  });
};
