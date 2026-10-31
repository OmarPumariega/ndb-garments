# Fondo de estudio oficial NDB (UNICO para producto y modelos)

> **Decisión del equipo (31/10/2026):** a partir de ahora **toda imagen de estudio** (producto con maniquí fantasma, flatlay, detalles, avatares) usa **el fondo de los avatares**. Así web, fichas de producto y galerías se ven con la misma luz y no hay saltos de tono entre la foto de la prenda y la del modelo.

## Qué fondo es
Cíclorama continuo (pared que se curva en el suelo, sin línea de horizonte), **gris perla cálido, no blanco puro y no azulado**, con luz de softbox frontal muy suave y un ligero degradado (más claro en el centro, más tenue en los bordes). Referencia de estilo: foto del modelo en negro (`assets/ref-estudio-modelo-negro.jpg`). **Imagen de referencia obligatoria: `assets/placa-estudio-ndb.jpg`** (estudio vacío).

Valores medidos (sRGB):
| Zona | Color |
|---|---|
| Pared, centro de la placa | `#DFDCD9` |
| Pared, bordes de la placa | `#CBC7C4` |
| Suelo de la placa | `#E0DEE0` |
| Pared lateral en los 12 sets con modelo (media) | **`#D4CECC`** (±7 por canal entre sets) |
| Antes, producto (frontal, media de 13 series) | `#DADEE3` → **azulado/frío: ya NO se usa** |

El tono es cálido: `R ≥ B + 2`. Si sale azulado (`R < B`) o casi blanco, la imagen falla.

## Bloque de fondo (pegar en TODOS los prompts de estudio)
Sube la placa como imagen de referencia y pega este bloque (cambia `image N` por el número de la placa):
```
BACKGROUND (official NDB studio, copy image N exactly): seamless warm pearl-gray cyclorama, no horizon line, wall about #DFDCD9 in the center fading softly to about #CBC7C4 at the edges, floor about #E0DEE0, very soft even frontal softbox light. NOT pure white, NOT cool or bluish gray. Ignore any floating shadow in image N; draw a soft diffused contact shadow instead.
```
Según el tipo de imagen se añade:
- **Persona de pie:** `a CLEARLY VISIBLE soft gray shadow under and behind both feet, falling back and to the right, feet firmly grounded.`
- **Producto con maniquí fantasma (frontal/trasera/lateral):** `garment floating centered in front of the backdrop with a soft diffused contact shadow beneath it, same wall tone as image N.`
- **Flatlay (cenital):** `top-down on the same warm pearl-gray matte paper (about #DFDCD9), soft even light, very soft shadow under the garment edges, no visible floor line.`
- **Detalles y macros (logo, cuello):** `shallow depth of field, out-of-focus background in the same warm pearl-gray (#D4CECC).`
- **Grid:** el fondo del lienzo del grid debe ser `#DFDCD9` (no `#EEEEEC` ni blanco).

## Cómo aplicarlo
1. **Siempre** incluir `assets/placa-estudio-ndb.jpg` entre las referencias (junto a la foto de prenda, el grid o la lámina del avatar).
2. Pegar el bloque de fondo. No usar nunca más `#E9E9EC`, `light-gray`, `white seamless` ni `pure white background`.
3. **Comprobar con `tools/check_background.py`** (frontales, traseras, tres cuartos, flatlay): debe dar `OK`. Si da `FRIO/AZULADO` o `FALLA`, se regenera.
4. Para exterior (más adelante) este fondo no aplica; se definirá aparte.

## Estado actual y migración pendiente
- Los **12 sets con modelo** ya usan este fondo: 11 de las 12 frontales dan `OK` con `tools/check_background.py`; la frontal de Alex con TS-08 (`MODELO-ALEX_TS-08…-frontal`) sale algo más clara y fría (`#E7E4E7`). Las 13 frontales de producto dan `FALLA` (frías).
- Las **13 series de producto** (`outputs/<SKU>_…`: frontal, trasera, lateral, flatlay, detalles, grid) se generaron antes con el fondo frío `#DADEE3`. **No se regeneran ahora** (decisión del equipo: "por ahora lo dejamos así"). Cuando se toquen o se hagan productos nuevos, ya se generan con este fondo. Si se quiere unificar toda la web de golpe, hay que rehacer las 13 series con la placa (≈ 78 imágenes).
- Productos nuevos y avatares nuevos: **siempre este fondo desde la primera imagen**.
