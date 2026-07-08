# -*- coding: utf-8 -*-
import json
path = r'C:\Users\jordi\.minimax\projects\jc-ia-news\_state\decodifica-content-tracking.json'
with open(path, 'r', encoding='utf-8') as f:
    obj = json.load(f)

# Search Odysseus brief across entire weeks object
def find_brief(obj, brief_id):
    if isinstance(obj, dict):
        if obj.get('brief_id') == brief_id:
            return obj
        for v in obj.values():
            r = find_brief(v, brief_id)
            if r:
                return r
    elif isinstance(obj, list):
        for item in obj:
            r = find_brief(item, brief_id)
            if r:
                return r
    return None

b = find_brief(obj, 'vd_2026-06-15_odysseus-pewdiepie')
if b:
    yv = b['assets']['youtube_video']
    print('Odysseus youtube_video:')
    print('  video_id_youtube:', yv.get('video_id_youtube'))
    print('  estado:', yv.get('estado'))
    print('  url_public:', yv.get('url_public'))
    print('  embed_en_blog:', yv['distribucion']['embed_en_blog'])
    print('  embed_added_to_blog:', yv.get('embed_added_to_blog'))
else:
    print('Odysseus brief not found')
