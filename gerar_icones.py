# -*- coding: utf-8 -*-
"""Gera os ícones do app (PWA + apple-touch-icon): fundo azul, 'R$' branco."""
import os
from PIL import Image, ImageDraw, ImageFont

BASE = "#1F3864"   # azul do app
ACENTO = "#1F7A6D"  # verde (barra de crescimento)

img = Image.new("RGB", (512, 512), BASE)
d = ImageDraw.Draw(img)

# gráfico de barras subindo, no canto inferior (dentro da zona segura do ícone maskable)
d.rectangle([64, 330, 148, 448], fill="#2F5597")
d.rectangle([214, 260, 298, 448], fill="#2F5597")
d.rectangle([364, 180, 448, 448], fill=ACENTO)

# 'R$' centralizado
fonte = None
for caminho in [r"C:\Windows\Fonts\arialbd.ttf", r"C:\Windows\Fonts\calibrib.ttf"]:
    if os.path.exists(caminho):
        fonte = ImageFont.truetype(caminho, 190)
        break
if fonte is None:
    fonte = ImageFont.load_default()
bbox = d.textbbox((0, 0), "R$", font=fonte)
larg, alt = bbox[2] - bbox[0], bbox[3] - bbox[1]
d.text(((512 - larg) / 2 - bbox[0], 218 - alt / 2 - bbox[1]), "R$", font=fonte, fill="white")

img.save("icon-512.png")
img.resize((192, 192), Image.LANCZOS).save("icon-192.png")
img.resize((180, 180), Image.LANCZOS).save("apple-touch-icon.png")
for f in ["icon-512.png", "icon-192.png", "apple-touch-icon.png"]:
    print(f, os.path.getsize(f), "bytes")
