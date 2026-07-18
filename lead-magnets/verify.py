import os
from pypdf import PdfReader

fp = r'D:\gpt decodifica\_web\decodifica.net\lead-magnets\50-prompts-ia.pdf'
print(f'File: {fp}')
print(f'Size: {os.path.getsize(fp) / 1024:.1f} KB')

reader = PdfReader(fp)
print(f'Pages: {len(reader.pages)}')
if reader.metadata:
    print(f'Title: {reader.metadata.title}')
    print(f'Author: {reader.metadata.author}')

# Print first lines of first page to verify content
print('\n--- First page text (first 500 chars) ---')
text = reader.pages[0].extract_text()[:500]
print(text)
