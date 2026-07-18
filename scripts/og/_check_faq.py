# -*- coding: utf-8 -*-
import re

path = r'D:\gpt decodifica\_web\decodifica.net\dist\blog\ia-mejora-excel\index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# FAQ microdata check
faq_block = html.count('itemtype="https://schema.org/FAQPage"')
q_block = html.count('itemtype="https://schema.org/Question"')
ans_block = html.count('itemtype="https://schema.org/Answer"')
print('FAQPage microdata blocks:', faq_block)
print('Question microdata blocks:', q_block)
print('Answer microdata blocks:', ans_block)

# Author check (might be under different field)
m = re.search(r'"author":\s*\{[^}]*\}', html)
print('author JSON-LD block:', m.group(0)[:200] if m else 'NOT FOUND')

# Image check
m = re.search(r'"image":\s*"[^"]+"', html)
print('image JSON-LD:', m.group(0)[:200] if m else 'NOT FOUND')

# Word count
text = re.sub(r'<[^>]+>', ' ', html)
text = re.sub(r'\s+', ' ', text)
words = text.split()
print('Approx word count:', len(words))
