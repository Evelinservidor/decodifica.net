# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import os

OUT = r"D:\gpt decodifica\_web\decodifica.net\public\og\blog\odysseus-pewdiepie-ia-gratis.png"

W, H = 1200, 630
BG = (10, 10, 10)
ACCENT = (11, 61, 145)
WHITE = (255, 255, 255)
GRAY = (200, 200, 210)

FONT_BOLD = r"C:\Windows\Fonts\arialbd.ttf"
FONT_REG = r"C:\Windows\Fonts\arial.ttf"

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# Subtle accent gradient bar at top
for y in range(0, 6):
    shade = (11 + y * 2, 61 + y * 4, 145 + y * 3)
    draw.rectangle([(0, y), (W, y + 1)], fill=shade)

# Badge: PILAR 1 - APPS WEB
badge_font = ImageFont.truetype(FONT_BOLD, 22)
badge_text = "PILAR 1  -  APPS WEB GRATIS"
bbox = draw.textbbox((0, 0), badge_text, font=badge_font)
bw = bbox[2] - bbox[0] + 32
bh = bbox[3] - bbox[1] + 16
bx, by = 64, 64
draw.rounded_rectangle([(bx, by), (bx + bw, by + bh)], radius=4, fill=ACCENT)
draw.text((bx + 16, by + 4), badge_text, font=badge_font, fill=WHITE)

# Main title (2 lines, large)
title_font = ImageFont.truetype(FONT_BOLD, 88)
line1 = "Odysseus de PewDiePie:"
line2 = "¿la IA gratis que"
line3 = "todos están probando?"

# Center vertically with stack
def text_w(s, f):
    b = draw.textbbox((0, 0), s, font=f)
    return b[2] - b[0], b[3] - b[1]

# Use 3 lines
lines = [line1, line2, line3]
line_sizes = [text_w(l, title_font) for l in lines]
max_w = max(s[0] for s in line_sizes)
total_h = sum(s[1] for s in line_sizes) + 24 * (len(lines) - 1)

start_y = (H - total_h) // 2 - 30
y = start_y
for l, (lw, lh) in zip(lines, line_sizes):
    x = (W - lw) // 2
    draw.text((x, y), l, font=title_font, fill=WHITE)
    y += lh + 24

# Subtitle / kicker
sub_font = ImageFont.truetype(FONT_REG, 28)
sub = "Self-hosted, AGPL-3.0, 67.5k stars en GitHub en 10 días"
sw, sh = text_w(sub, sub_font)
draw.text(((W - sw) // 2, y + 10), sub, font=sub_font, fill=GRAY)

# Decodifica brand (bottom right)
brand_font = ImageFont.truetype(FONT_BOLD, 26)
brand = "DECODIFICA"
bb = draw.textbbox((0, 0), brand, font=brand_font)
bw_ = bb[2] - bb[0]
draw.text((W - bw_ - 64, H - 60), brand, font=brand_font, fill=WHITE)

# Small "D" stylized mark at bottom right corner
mark_size = 36
mx = W - 64 - bw_ - mark_size - 12
my = H - 60 - 4
draw.rectangle([(mx, my), (mx + mark_size, my + mark_size)], fill=ACCENT)
inner = ImageFont.truetype(FONT_BOLD, 28)
draw.text((mx + 8, my + 1), "D", font=inner, fill=WHITE)

img.save(OUT, "PNG", optimize=True)
print("WROTE", OUT, "size_bytes=", os.path.getsize(OUT))
