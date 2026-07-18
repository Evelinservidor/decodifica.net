# -*- coding: utf-8 -*-
path = r'D:\gpt decodifica\_web\decodifica.net\src\pages\blog\notebooklm-guia-2026.astro'
data = open(path, 'r', encoding='utf-8').read()
print('=== QUALITY GATES: notebooklm-guia-2026 ===')
print('1. NotebookLM in frontmatter:', 'NotebookLM' in data)
print('2. H1 count:', data.count('<h1'))
print('3. H2 count:', data.count('<h2'))
print('4. H3 count:', data.count('<h3'))
print('5. FAQPage schema:', 'FAQPage' in data)
print('6. Question schema:', 'Question' in data)
print('7. Article type on BaseLayout:', 'type="article"' in data)
print('8. pubDate on BaseLayout:', 'pubDate={pubDate}' in data)
print('9. section on BaseLayout:', 'section={pillarLabel}' in data)
print('10. keywords on BaseLayout:', 'keywords={tags}' in data)
print('11. table present:', '<table' in data)
print('12. table rows:', data.count('<tr'))
print('13. Sources cited:')
for url in ['notebooklm.google', 'blog.google', 'support.google.com', 'theverge.com', 'digitalocean.com']:
    if url in data:
        print(f'  {url}: yes')
    else:
        print(f'  {url}: MISSING')
print('14. Anti-tema scan:')
for anti in ['Sora', 'Veo 3', 'Kling', 'Ray-Ban Meta', 'microchip', 'cortometraje', 'wearable', 'smart glasses', 'Vision Pro', 'geopolitica', 'Huawei', 'DeepSeek V4', 'Qwen 3.7', 'ASML', 'TSMC', 'crypto', 'NFT']:
    if anti.lower() in data.lower():
        idx = data.lower().find(anti.lower())
        ctx = data[max(0,idx-40):idx+len(anti)+40]
        print(f'  ANTI-TEMA [{anti}]: {ctx!r}')
    else:
        print(f'  OK - {anti}: not present')
print('15. Internal links:')
print('  /recursos:', '/recursos' in data)
print('  /blog/alternativas-gratis-chatgpt-2026:', '/blog/alternativas-gratis-chatgpt-2026' in data)
print('  /blog/ia-gratis-silicon-valley:', '/blog/ia-gratis-silicon-valley' in data)
print('  buttondown (newsletter):', 'buttondown' in data)
print('16. TL;DR block:', 'TL;DR' in data)
print('17. Total words (rough):', len(data.split()))
print('18. File size bytes:', len(open(path, "rb").read()))
print('19. Description length:', len(data.split('description = "')[1].split('"')[0]) if 'description = "' in data else 'N/A')
print('20. Title length:', len(data.split('title = "')[1].split('"')[0]) if 'title = "' in data else 'N/A')
