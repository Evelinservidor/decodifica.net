# -*- coding: utf-8 -*-
import json
path = r'C:\Users\jordi\.minimax\projects\jc-ia-news\_state\decodifica-content-tracking.json'
with open(path, 'r', encoding='utf-8') as f:
    obj = json.load(f)

# Walk entire JSON
def walk(o, path=()):
    if isinstance(o, dict):
        if o.get('brief_id') == 'vd_2026-06-15_odysseus-pewdiepie':
            return path, o
        for k, v in o.items():
            r = walk(v, path + (k,))
            if r:
                return r
    elif isinstance(o, list):
        for i, v in enumerate(o):
            r = walk(v, path + (str(i),))
            if r:
                return r
    return None

r = walk(obj)
if r:
    p, b = r
    yv = b['assets']['youtube_video']
    print('Path in JSON:', '/'.join(p))
    print('video_id_youtube:', yv.get('video_id_youtube'))
    print('estado:', yv.get('estado'))
    print('url_public:', yv.get('url_public'))
    print('embed_en_blog:', yv['distribucion']['embed_en_blog'])
    print('embed_added_to_blog:', yv.get('embed_added_to_blog'))
    print('_nota_embed present:', '_nota_embed' in yv)
else:
    print('NOT FOUND')
