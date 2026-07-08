# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import os

OUT = r"C:\Users\jordi\Documents\GitHub\decodifica.net\public\og\blog\notebooklm-guia-2026.png"

W, H = 1200, 630
BG = (10, 10, 10)
ACCENT = (11, 61, 145)
WHITE = (255, 255, 255)
GRAY = (180, 180, 190)

FONT_BOLD = r"C:\Windows\Fonts\arialbd.ttf"
FONT_REG = r"C:\Windows\Fonts\arial.ttf"

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# Accent bar top
for y in range(0, 6):
    shade = (11 + y * 2, 61 + y * 4, 145 + y * 3)
    draw.rectangle([(0, y), (W, y + 1)], fill=shade)

def text_w(s, f):
    b = draw.textbbox((0, 0), s, font=f)
    return b[2] - b[0], b[3] - b[1]

# Title - auto-fit (try 80pt first, down to 56pt)
title = "NotebookLM 2026:"
title2 = "la IA de Google que"
title3 = "solo lee tus documentos"

font_size = 80
while font_size >= 56:
    title_font = ImageFont.truetype(FONT_BOLD, font_size)
    max_line_w = max(text_w(title, title_font)[0], text_w(title2, title_font)[0], text_w(title3, title_font)[0])
    if max_line_w <= W - 128:
        break
    font_size -= 4

lines = [title, title2, title3]
line_sizes = [text_w(l, title_font) for l in lines]
total_h = sum(s[1] for s in line_sizes) + 16 * (len(lines) - 1)
start_y = (H - total_h) // 2 - 30
y = start_y
for l, (lw, lh) in zip(lines, line_sizes):
    x = (W - lw) // 2
    draw.text((x, y), l, font=title_font, fill=WHITE)
    y += lh + 16

# Subtitle
sub_font = ImageFont.truetype(FONT_REG, 26)
sub = "100 cuadernos gratis  -  3 audio overviews al dia  -  Gemini 3.5"
sw, sh = text_w(sub, sub_font)
draw.text(((W - sw) // 2, y + 6), sub, font=sub_font, fill=GRAY)

# Brand mark (bottom right)
brand_font = ImageFont.truetype(FONT_BOLD, 26)
brand = "DECODIFICA"
bb = draw.textbbox((0, 0), brand, font=brand_font)
bw_ = bb[2] - bb[0]
draw.text((W - bw_ - 64, H - 60), brand, font=brand_font, fill=WHITE)

mark_size = 36
mx = W - 64 - bw_ - mark_size - 12
my = H - 60 - 4
draw.rectangle([(mx, my), (mx + mark_size, my + mark_size)], fill=ACCENT)
inner = ImageFont.truetype(FONT_BOLD, 28)
draw.text((mx + 8, my + 1), "D", font=inner, fill=WHITE)

img.save(OUT, "PNG", optimize=True)
print("WROTE", OUT, "size_bytes=", os.path.getsize(OUT))
