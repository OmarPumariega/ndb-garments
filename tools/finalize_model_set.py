#!/usr/bin/env python3
"""Genera el set final de una prenda con modelo: WebP q82 (nombres SEO), grid 3x2 y alt-text.csv.
Uso: finalize_model_set.py --src work-models/alex-ts05 --out outputs/MODELO-ALEX_TS-05_camiseta-calle-beige \
       --base modelo-alex-camiseta-calle-beige --desc "camiseta Calle beige NiDeBlas" [--logo-alt "avestruz bordado azul marino"]
Usa fix/<vista>.jpg si existe (logo corregido) y si no <vista>.jpg. Vistas: front, threeq, back, medium, logo.
"""
import argparse, csv, os
from PIL import Image

VIEWS = [('front', 'frontal', 'vista frontal'), ('threeq', 'tres-cuartos', 'vista en tres cuartos'),
         ('back', 'trasera', 'vista trasera'), ('medium', 'media-distancia', 'plano medio'),
         ('logo', 'detalle-logo', 'primer plano del logo')]

ap = argparse.ArgumentParser()
ap.add_argument('--src', required=True); ap.add_argument('--out', required=True); ap.add_argument('--base', required=True)
ap.add_argument('--desc', required=True); ap.add_argument('--logo-alt', default='logo avestruz')
A = ap.parse_args()
os.makedirs(A.out, exist_ok=True)
rows, files = [], []
for k, slug, label in VIEWS:
    f = f'{A.src}/fix/{k}.jpg'
    if not os.path.exists(f): f = f'{A.src}/{k}.jpg'
    name = f'{A.base}-{slug}.webp'
    Image.open(f).convert('RGB').save(f'{A.out}/{name}', 'WEBP', quality=82, method=6)
    alt = f'Modelo con {A.desc}, {label}' if k != 'logo' else f'Primer plano del {A.logo_alt} en {A.desc}'
    rows.append([name, alt]); files.append(f)
W, H = 700, 900
g = Image.new('RGB', (W * 3, H * 2), (238, 238, 236))
for i, f in enumerate(files):
    im = Image.open(f).convert('RGB'); im.thumbnail((W, H)); g.paste(im, ((i % 3) * W + (W - im.width) // 2, (i // 3) * H + (H - im.height) // 2))
g.save(f'{A.out}/{A.base}-grid.webp', 'WEBP', quality=82, method=6)
w = csv.writer(open(f'{A.out}/alt-text.csv', 'w', newline='')); w.writerow(['archivo', 'alt']); w.writerows(rows)
print('OK', A.out)
