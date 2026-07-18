import sys
path = r'D:\gpt decodifica\_web\decodifica.net\src\pages\blog\ia-gratis-silicon-valley.astro'
data = open(path, 'r', encoding='utf-8').read()
print('=== QUALITY GATES CHECK ===')
print('1. Tag herramientas ia gratis in frontmatter:', 'herramientas ia gratis' in data)
print('1b. IA gratis appears in H1:', 'IA gratis' in data or 'IA GRATIS' in data)
print('1c. H1 count:', data.count('<h1'))
print('1d. H2 count:', data.count('<h2'))
print('1e. H3 count:', data.count('<h3'))
print('2. FAQPage schema:', 'FAQPage' in data)
print('2b. Question schema:', 'Question' in data)
print('3. table present:', '<table' in data)
print('3b. table rows (<tr):', data.count('<tr'))
print('4. Sources cited:')
for url in ['huggingface.co', 'deepseek.com', 'chat.mistral.ai', 'chat.qwen.ai', 'mistral.ai', 'chat.deepseek.com', 'huggingface.co/chat']:
    if url in data: print(f'  {url}: yes')
print('5. Anti-tema scan:')
for anti in ['Sora', 'Veo 3', 'Kling', 'Ray-Ban Meta', 'microchips', 'cortometraje', 'wearable', 'Apple Vision Pro', 'smart glasses']:
    if anti.lower() in data.lower():
        idx = data.lower().find(anti.lower())
        ctx = data[max(0,idx-40):idx+len(anti)+40]
        print(f'  ANTI-TEMA [{anti}]: {ctx!r}')
    else:
        print(f'  OK - {anti}: not present')
print('6. Internal links:')
print('  /recursos:', '/recursos' in data)
print('  /blog/alternativas-gratis-chatgpt-2026:', '/blog/alternativas-gratis-chatgpt-2026' in data)
print('  buttondown (newsletter):', 'buttondown' in data)
print()
print('7. Total words (rough):', len(data.split()))
print('8. File size bytes:', len(open(path, "rb").read()))
print('9. char count:', len(data))
