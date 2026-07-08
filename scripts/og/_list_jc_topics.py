# -*- coding: utf-8 -*-
import json
import os
from pathlib import Path

path = Path(os.environ.get(
    'DECODIFICA_DAILY_TOPICS_PATH',
    Path.home() / '.codex' / 'decodifica' / 'db' / 'daily_blog_topics.json',
))
with path.open('r', encoding='utf-8') as f:
    obj = json.load(f)
topics = [t for t in obj.get('topics', []) if t.get('channel') == 'jc' and t.get('date', '') >= '2026-06-10']
print('Total jc topics from 2026-06-10:', len(topics))
for t in topics:
    line = '  ' + t['date'] + ' | ' + t['status'] + ' | ' + t['topic']
    print(line)
