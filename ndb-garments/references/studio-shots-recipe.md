# Receta probada: serie de estudio para la web (piloto TS-06, camiseta Calle blanca)

Resultado aprobado por el equipo. Repetir este método para el resto de prendas.

## Herramienta y modelo
- **Nano Banana 2.1** (`nano-banana-2-1`, kie.ai): ~4 créditos (~0,02 $) por imagen, multi-referencia, buen detalle de bordado. Elegido frente a GPT Image 2.5 Sunburst (6 cr), que simplificó el logo.
- Formatos: **3:4** para frontal, trasera, lateral y flatlay; **4:5** para detalles.
- Coste de una serie de 6 vistas: ~24 créditos (~0,12 $).

## Proceso
1. Descargar 3–4 fotos reales del SKU desde Drive y convertir HEIC a JPG (`sips -s format jpeg -Z 2048`).
2. Subirlas a kie (`upload_file`; caducan en 3 días).
3. Generar primero el **frontal** con refs: foto completa + macro del bordado + cuello.
4. Usar la **URL del frontal aprobado** como referencia 1 en el resto de vistas (mantiene prenda, luz y fondo).
5. Revisar con el checklist QA del playbook y entregar según la regla de entrega.

## Prompts por vista (sustituir [PRENDA] y color del hilo)
- **Frontal:** `Professional e-commerce studio product photo, front view, of the [PRENDA] from the reference photos, on an invisible ghost mannequin, centered, full garment with margin. [descripción del prompt-ficha]. Soft diffused studio lighting, gentle natural shadow, seamless light-gray background (#E9E9EC), crisp seams, fine fabric weave, true-to-life color, 85mm. Reference 1: full garment; reference 2: embroidery macro; reference 3: neck label and tape. No text, extra graphics, pockets or other logos. Do not change or mirror the logo.`
- **Trasera:** `Same exact [PRENDA] as reference 1, seen from the BACK, ghost mannequin, same lighting, background and scale. Plain back, NO logo/print/text (salvo SW-04 y TS-10, que tienen espalda propia). Back neckline with black neck tape visible.`
- **Lateral:** `Same [PRENDA] as reference 1, SIDE view (90° left profile), ghost mannequin, same lighting and scale; show side seam, sleeve and drape; the front logo only barely visible at the edge, do not enlarge it.`
- **Flatlay:** `Flat lay, top-down 90°, same [PRENDA] as reference 1, smoothed on a seamless light-gray surface (#E9E9EC), sleeves relaxed, generous margin, soft even light, very subtle contact shadow; logo, neck tape and label as in reference 1.`
- **Detalle logo (4:5):** `Macro close-up of the embroidered/printed logo on [TEJIDO]: [técnica y color de hilo], raised satin-stitch with directional sheen, visible fabric weave; silhouette identical to reference. Shallow depth of field, soft side light, no other elements.`
- **Detalle cuello (4:5):** `Close-up of the neckline: ribbed crew collar, black woven neck label with white italic condensed "NIDEBLAS" and size, black neck tape along the inner edge. Soft diffused light, clean light-gray background.`

## Qué vigilar (aprendido en el piloto)
- El **logo** sale algo más detallado que el real: validar siempre contra el logo vector.
- La **trasera y el lateral** los inventa el modelo si no hay foto real; seguros en prendas con espalda lisa.
- El **fondo del flatlay** tiende a salir más oscuro: pedir `#E9E9EC` y revisar.
- Dejar **margen** arriba en el frontal (a veces recorta).
- Resolución de salida ~900×1200: subir a 2K para web con reescalado antes de publicar.

## Entrega
Grid único + cada vista suelta, numeradas, en `outputs/<SKU>_<nombre>/` (ver playbook).
