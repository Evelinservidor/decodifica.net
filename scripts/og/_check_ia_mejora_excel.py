# -*- coding: utf-8 -*-
import re
import os

path = r'D:\gpt decodifica\_web\decodifica.net\dist\blog\ia-mejora-excel\index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# JSON-LD counts
print('--- JSON-LD blocks ---')
print('"@type":"Article":', html.count('"@type":"Article"'))
print('"@type":"Organization":', html.count('"@type":"Organization"'))
print('"@type":"WebSite":', html.count('"@type":"WebSite"'))
print('"@type":"FAQPage":', html.count('"@type":"FAQPage"'))

# Meta tags
print()
print('--- Meta tags ---')
m = re.search(r'<meta name="keywords" content="([^"]+)"', html)
print('keywords:', m.group(1) if m else 'NOT FOUND')

m = re.search(r'<meta property="og:image" content="([^"]+)"', html)
print('og:image:', m.group(1) if m else 'NOT FOUND')

m = re.search(r'<meta property="og:title" content="([^"]+)"', html)
print('og:title:', m.group(1) if m else 'NOT FOUND')

# Article schema fields
print()
print('--- Article JSON-LD fields ---')
for field in ['datePublished', 'articleSection', 'headline', 'author', 'image', 'keywords']:
    m = re.search(r'"' + field + r'":"([^"]+)"', html)
    print(f'  {field}:', m.group(1) if m else 'NOT FOUND')

# H1
print()
print('--- H1 ---')
m = re.search(r'<h1[^>]*>([^<]+)</h1>', html)
print(m.group(1) if m else 'NOT FOUND')

# Internal links
print()
print('--- Internal links ---')
internal_links = re.findall(r'href="(/[^"#]+)"', html)
internal_set = sorted(set(internal_links))
for link in internal_set:
    print(' ', link)

# Mojibake check
print()
print('--- Mojibake check ---')
mojibake = re.findall(r'Ã[¡-¿]', html)
print('Mojibake hits:', len(mojibake))

# File size
print()
print('--- File stats ---')
print('Size:', os.path.getsize(path), 'bytes')
