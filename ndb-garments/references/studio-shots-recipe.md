# Receta probada: serie de estudio para la web (piloto TS-06, camiseta Calle blanca)

Resultado aprobado por el equipo. Repetir este método para el resto de prendas.

## Estándar de calidad (actualizado)
- **Resolución 2K** (`model_options: {"resolution": "2K"}`, ~6 créditos por imagen): con más píxeles la etiqueta es legible y se puede verificar con OCR; además la imagen ya sirve para web con zoom.
- **Imagen de referencia de la etiqueta** en todas las vistas donde salga (frontal, flatlay, detalle cuello, sudaderas): `ndb-garments/assets/etiqueta-cuello-real-talla-M.jpg` (foto real de la etiqueta M; si hace falta apoyo, también `etiqueta-cuello-plana-NIDEBLAS-M.jpg`).
- **Bloque de ortografía obligatorio** en todo prompt con etiqueta (ver abajo).
- **Verificación OCR** de cada imagen con etiqueta antes de aprobarla; si falla, se regenera.

### Bloque de ortografía (pegar en TODOS los prompts con etiqueta)
```
LABEL TEXT RULE (critical): any visible label reads exactly "NIDEBLAS" followed by the size letter "M". The brand word has eight letters in this exact order: N-I-D-E-B-L-A-S. It is NOT "NIGEBLAS", NOT "NIDEBIAS", NOT "NIDEBLAZ", NOT "MIDEBLAS", NOT "NIDEBLAS XL". Copy the lettering exactly from the label reference image (white italic condensed capitals on black).
```

### Cuello según la familia (obligatorio elegir bien)
Las tres familias tienen cuello y etiqueta distintos. **Antes de generar, elige la frase de cuello de la familia en `labels-trims.md`** (camiseta Calle / sudadera / deportiva) y sube como referencia la **foto de cuello de esa familia** (no la de otra):
- Camiseta Calle → `assets/etiqueta-cuello-real-talla-M.jpg`
- Sudadera → `assets/etiqueta-cuello-sudadera-M.jpg`
- Deportiva → `assets/etiqueta-cuello-deportiva-M.jpg`
Error ocurrido: las sudaderas SW-01/02/03 se generaron con el cuello de camiseta (cinta negra y canalé fino). Corregido.

## Herramienta y modelo
- **Nano Banana 2.1** (`nano-banana-2-1`, kie.ai): ~4 créditos a 1K / ~6 a 2K (~0,03 $) por imagen, multi-referencia, buen detalle de bordado. Elegido frente a GPT Image 2.5 Sunburst (6 cr), que simplificó el logo.
- Resolución: **2K** (ver estándar). Formatos: **3:4** para frontal, trasera, lateral y flatlay; **4:5** para detalles.
- Coste de una serie de 6 vistas: ~24 créditos (~0,12 $).

## Proceso
1. Descargar 3–4 fotos reales del SKU desde Drive y convertir HEIC a JPG (`sips -s format jpeg -Z 2048`).
2. Subirlas a kie (`upload_file`; caducan en 3 días).
3. Generar primero el **frontal** con refs: foto completa + macro del bordado + cuello.
4. Usar la **URL del frontal aprobado** como referencia 1 en el resto de vistas (mantiene prenda, luz y fondo).
5. Revisar con el checklist QA del playbook y entregar según la regla de entrega.

> **Talla M obligatoria.** Añadir a cada prompt las medidas M del SKU y que la etiqueta de cuello diga `NIDEBLAS M`. En el piloto TS-06 la etiqueta salió con `XL` porque la foto de referencia era XL: corregido en la regeneración con `neck label reads M (not XL)` en frontal, flatlay y detalle de cuello.

## Prompts por vista (sustituir [PRENDA] y color del hilo)
> **Fondo (obligatorio, cambio 31/10):** todas las vistas llevan como última referencia `assets/placa-estudio-ndb.jpg` y el bloque de fondo de `references/fondo-estudio.md` (gris perla cálido de los avatares). Los prompts de abajo ya lo mencionan; no volver al gris `#E9E9EC`.
- **Frontal:** `Professional e-commerce studio product photo, front view, of the [PRENDA] from the reference photos, on an invisible ghost mannequin, centered, full garment with margin. [descripción del prompt-ficha]. Soft diffused studio lighting, gentle natural shadow, OFFICIAL NDB BACKGROUND (paste the background block of fondo-estudio.md; reference N = studio plate assets/placa-estudio-ndb.jpg), crisp seams, fine fabric weave, true-to-life color, 85mm. Reference 1: full garment; reference 2: embroidery macro; reference 3: neck label and tape; reference 4: studio plate (background). No text, extra graphics, pockets or other logos. Do not change or mirror the logo.`
- **Trasera:** `Same exact [PRENDA] as reference 1, seen from the BACK, ghost mannequin, same lighting, same official NDB background (studio plate) and scale. Plain back, NO logo/print/text (salvo SW-04 y TS-10, que tienen espalda propia). Back neckline with black neck tape visible.`
- **Lateral:** `Same [PRENDA] as reference 1, SIDE view (90° left profile), ghost mannequin, same lighting and scale; show side seam, sleeve and drape; the front logo only barely visible at the edge, do not enlarge it.`
- **Flatlay:** `Flat lay, top-down 90°, same [PRENDA] as reference 1, smoothed on a seamless warm pearl-gray matte surface (about #DFDCD9, same as the official NDB studio plate), sleeves relaxed, generous margin, soft even light, very subtle contact shadow; logo, neck tape and label as in reference 1.`
- **Detalle logo (4:5):** `Macro close-up of the embroidered/printed logo on [TEJIDO]: [técnica y color de hilo], raised satin-stitch with directional sheen, visible fabric weave; silhouette identical to reference. Shallow depth of field, soft side light, no other elements.`
- **Detalle cuello (4:5):** `Close-up of the neckline: ribbed crew collar, black woven neck label with white italic condensed "NIDEBLAS" and size, black neck tape along the inner edge. Soft diffused light, out-of-focus background in the warm pearl-gray of the official NDB studio (#D4CECC), not white and not bluish.`

## Verificación de etiquetas (obligatoria)
```bash
swiftc -O tools/ocr_labels.swift -o /tmp/ocr_labels
/tmp/ocr_labels work-xxx/*_front.jpg work-xxx/*_flatlay.jpg work-xxx/*_neck_detail.jpg
```
- `OK` = lee NIDEBLAS. `SOSPECHOSO: NIGEBLAS` (u otra variante) = **regenerar**.
- `NO` sin sospechosos = etiqueta ilegible (poco tamaño): subir resolución o ampliar la etiqueta; no se da por buena sin mirar un recorte (`OCR_CROPS=/tmp/crops` guarda recortes ampliados).
- `SOSPECHOSO` puede ser un falso positivo con letra muy pequeña (p. ej. `HIDEBLAS` por una N mal ampliada) y `NO` puede ser un falso negativo con etiqueta negra sobre tela oscura/azul: en ambos casos se mira el recorte ampliado (`OCR_CROPS=/tmp/crops /tmp/ocr_labels imagen.jpg`) y se decide a ojo. Se aprueba solo con `OK` o con recorte verificado visualmente.
- La vista trasera no lleva etiqueta visible por fuera: no se comprueba.
- Ocurrió en TS-09 verde (`NIGEBLAS` en frontal, flatlay y detalle de cuello) y en TS-08 flatlay.

## Qué vigilar (aprendido en el piloto)
- **Macro del logo en tejido blanco:** pedir `PURE WHITE ... not cream or beige`, o sale sobre crema.
- **Etiqueta:** si la referencia muestra otra talla, indicar explícitamente `ignore the size letter in the photo; use M`.
- El **logo** sale algo más detallado que el real: validar siempre contra el logo vector.
- La **trasera y el lateral** los inventa el modelo si no hay foto real; seguros en prendas con espalda lisa.
- **Fondo:** usar SIEMPRE el fondo oficial de estudio (gris perla cálido de los avatares): subir `assets/placa-estudio-ndb.jpg` como referencia y pegar el bloque de `references/fondo-estudio.md`; comprobar con `tools/check_background.py`. El fondo antiguo `#E9E9EC` (azulado) queda prohibido.
- Dejar **margen** arriba en el frontal (a veces recorta).
- Resolución de salida ~900×1200: subir a 2K para web con reescalado antes de publicar.

## Entrega
Grid + cada vista suelta en **WebP** con **nombre SEO** (`<tipo>-<modelo>-<color>-<vista>.webp`) y `alt-text.csv`, en `outputs/<SKU>_<nombre>/`. Reglas completas en el playbook. En el piloto TS-06 el peso bajó de ~300–600 KB (JPG) a 13–58 KB por imagen.
