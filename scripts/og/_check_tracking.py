# -*- coding: utf-8 -*-
import json
path = r'C:\Users\jordi\.minimax\projects\jc-ia-news\_state\decodifica-content-tracking.json'
with open(path, 'r', encoding='utf-8') as f:
    obj = json.load(f)
print('last_updated:', obj['last_updated'])
print('updated_by:', obj['updated_by'])
print()
print('--- Posts published ---')
for wkey, w in obj.get('weeks', {}).items():
    for b in w.get('briefs', []):
        bp = b.get('assets', {}).get('blog_post', {})
        if bp.get('estado') == 'published' and 'slug' in bp:
            label = w.get('week_label', wkey)
            print(f'  {label} | {b["brief_id"]} | {bp["slug"]}')
for p in obj.get('post_orfanos', {}).get('posts', []):
    if p.get('estado') == 'published':
        print(f'  HUERFANO | {p["slug"]}')

# Also count drafts and skipped
drafts = 0
skipped = 0
pending = 0
for wkey, w in obj.get('weeks', {}).items():
    for b in w.get('briefs', []):
        bp = b.get('assets', {}).get('blog_post', {})
        if bp.get('estado') == 'draft':
            drafts += 1
        elif bp.get('estado') == 'skipped_per_jordi':
            skipped += 1
        elif bp.get('estado') == 'pending':
            pending += 1
for p in obj.get('post_orfanos', {}).get('posts', []):
    if p.get('estado') == 'draft':
        drafts += 1
    elif p.get('estado') == 'skipped_per_jordi':
        skipped += 1
print()
print(f'Totals: drafts={drafts} pending={pending} skipped={skipped}')
