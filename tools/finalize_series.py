#!/usr/bin/env python3
"""Monta grid, convierte a WebP con nombre SEO y escribe alt-text.csv.

Uso:
  python tools/finalize_series.py --src work-ts05 --prefix ts05m \
    --sku TS-05 --slug camiseta-calle-beige \
    --name "Camiseta Calle beige NiDeBlas talla M" \
    --logo "con avestruz bordado en azul marino en el pecho izquierdo"

Entradas en --src: <prefix>_front, _back, _side, _flatlay, _logo_detail*, _neck_detail (.jpg).
Si hay varias versiones de logo_detail se usa la más reciente.
Salida: outputs/<SKU>_<slug>/<slug>-<vista>.webp + grid + alt-text.csv
"""
import argparse, glob, os
from PIL import Image

VIEWS = [('frontal', 'front'), ('trasera', 'back'), ('lateral', 'side'),
         ('flatlay', 'flatlay'), ('detalle-logo', 'logo_detail'), ('detalle-cuello', 'neck_detail')]

def newest(src, prefix, key):
    c = glob.glob(os.path.join(src, f'{prefix}_{key}*.jpg'))
    if not c:
        raise SystemExit(f'Falta {prefix}_{key} en {src}')
    return max(c, key=os.path.getmtime)

def main():
    a = argparse.ArgumentParser()
    a.add_argument('--src', required=True); a.add_argument('--prefix', required=True)
    a.add_argument('--sku', required=True); a.add_argument('--slug', required=True)
    a.add_argument('--name', required=True); a.add_argument('--logo', required=True)
    a.add_argument('--logo-detail-alt', default=None); a.add_argument('--out', default='outputs')
    a.add_argument('--quality', type=int, default=82)
    a = a.parse_args()
    out = os.path.join(a.out, f'{a.sku}_{a.slug}'); os.makedirs(out, exist_ok=True)
    ims = []
    for view, key in VIEWS:
        im = Image.open(newest(a.src, a.prefix, key)).convert('RGB'); ims.append(im)
        n = f'{a.slug}-{view}.webp'
        im.save(os.path.join(out, n), 'WEBP', quality=a.quality, method=6)
        print(n, im.size, os.path.getsize(os.path.join(out, n)) // 1024, 'KB')
    h = 600; r = [i.resize((int(i.width * h / i.height), h)) for i in ims]
    W = max(sum(i.width for i in r[:3]), sum(i.width for i in r[3:]))
    g = Image.new('RGB', (W, h * 2), 'white'); x = 0
    for i in r[:3]: g.paste(i, (x, 0)); x += i.width
    x = 0
    for i in r[3:]: g.paste(i, (x, h)); x += i.width
    g.save(os.path.join(out, f'{a.slug}-grid.webp'), 'WEBP', quality=a.quality, method=6)
    g.convert('RGB').save(os.path.join(a.src, f'{a.prefix}_grid.jpg'), quality=88)
    alt = {'frontal': f'{a.name}, vista frontal, {a.logo}',
           'trasera': f'{a.name}, vista trasera',
           'lateral': f'{a.name}, vista lateral',
           'flatlay': f'{a.name} en flatlay, {a.logo}',
           'detalle-logo': a.logo_detail_alt or f'Detalle del logo de {a.name}',
           'detalle-cuello': f'Detalle del cuello de {a.name} con etiqueta negra NIDEBLAS talla M'}
    with open(os.path.join(out, 'alt-text.csv'), 'w') as f:
        f.write('archivo,alt\n')
        for view, _ in VIEWS:
            f.write(f'{a.slug}-{view}.webp,"{alt[view]}"\n')
    print('OK ->', out)

if __name__ == '__main__':
    main()
