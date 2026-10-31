#!/usr/bin/env python3
"""Comprueba que una imagen usa el fondo oficial NDB (gris perla CALIDO, no blanco ni azulado).
Uso: check_background.py imagen.webp [mas.jpg ...]   (necesita Pillow y numpy)
Mide la pared en el lateral izquierdo del encuadre (25-45 % de alto, 12 % de ancho) y la compara con el objetivo.
Objetivo medido en los 12 sets con modelo: #D4CECC (tolerancia +-14 por canal) y tono calido (R >= B + 2).
Los frontales de producto antiguos salen azulados (~#DADEE3, R < B): FALLAN y hay que regenerarlos con la placa.
En fotos de detalle/macro o con la prenda pegada al borde no es fiable: usar solo en frontal/trasera/3-4/flatlay.
"""
import sys
import numpy as np
from PIL import Image

TARGET = np.array([0xD4, 0xCE, 0xCC], float)
TOL = 14

for p in sys.argv[1:]:
    a = np.array(Image.open(p).convert('RGB')).astype(float)
    h, w = a.shape[:2]
    c = a[int(.25 * h):int(.45 * h), :int(.12 * w)].reshape(-1, 3).mean(0)
    d = np.abs(c - TARGET)
    warm = c[0] >= c[2] + 2
    ok = bool((d <= TOL).all() and warm)
    print(('OK   ' if ok else 'FALLA'), '#%02X%02X%02X' % tuple(int(x) for x in c),
          'calido' if warm else 'FRIO/AZULADO', p)
