---
name: ndb-garments
description: Fuente de verdad de la ropa de NiDeBlas (NDB) para generar imágenes y vídeo consistentes y realistas con IA. Contiene catálogo de prendas, colores Pantone/TCX, logo (avestruz) y su colocación exacta, tablas de medidas, etiquetas (cuello, composición, colgante) y plantillas de prompt. Úsala siempre que haya que generar, editar o revisar imágenes, vídeo, mockups, fotos de producto o anuncios con prendas NDB, o redactar prompts para Midjourney, Flux, Veo, Kling, Runway, Seedream, Nano Banana o similares.
---

# NDB Garments — consistencia de producto para IA generativa

Marca: **NiDeBlas** (NDB), "Born Asturias", est. 2019. Logo: avestruz corriendo. Fabricación: Arpic Performance S.L. / GBTX (Portugal), patronaje de Javier Herrero.

## Cuándo usar esta skill
Cualquier tarea que muestre una prenda NDB: foto de producto, lookbook, modelo vistiendo la prenda, vídeo, anuncio, mockup, ecommerce, o redacción de prompts para otro modelo.

## Flujo obligatorio
1. **Identifica el SKU** en `references/catalog.md` (modelo + color). Si el usuario no lo dice, pregunta cuál. No mezcles datos de dos SKUs.
2. **Copia el bloque "Prompt-ficha" del SKU** tal cual. Los colores, tamaño y posición del logo no se reinterpretan.
3. **Calcula el ajuste (fit)** con `references/size-charts.md` según talla y altura/complexión del modelo. Usa la traducción a lenguaje de fit que ahí se da, nunca "oversized" o "slim" a ojo.
4. **Añade etiquetas visibles** solo si el plano las muestra (cuello interior, tab del dobladillo, colgante) con `references/labels-trims.md`.
5. **Monta el prompt** con `references/prompt-playbook.md` (plantillas imagen / vídeo / multi-toma) incluyendo los negativos.
6. **Adjunta imágenes de referencia**: fotos reales de `references/photo-references.md` (2–3 por SKU: frontal, macro del logo, cuello) y la lámina del techpack. El texto solo no basta para el logo. Si foto y techpack discrepan, **gana la foto real** para color de hilo y textura; el techpack manda para cm de posición.
7. **Revisa con el checklist QA** del playbook antes de dar la imagen por buena.
8. **Entrega siempre un grid con todas las vistas y cada vista por separado**, numeradas, en `outputs/<SKU>_<nombre>/`, en WebP con nombre SEO y alt-text. Receta completa y probada en `references/studio-shots-recipe.md`.

## Reglas que nunca se rompen
- **Cada familia tiene su propio cuello y etiqueta** (camiseta Calle / sudadera / deportiva): canalé, cinta negra y tipo de etiqueta cambian. Usa la frase y la foto de cuello de la familia correcta (`references/labels-trims.md`, tabla "Cuello y etiqueta por familia"). Nunca copies el cuello de una familia en otra.
- **Etiqueta = NIDEBLAS, siempre bien escrito** (N-I-D-E-B-L-A-S + talla M). Subir como referencia `assets/etiqueta-cuello-real-talla-M.jpg` (foto real; también hay S, L y XL), pegar el bloque de ortografía de `references/studio-shots-recipe.md` y verificar con OCR (`tools/ocr_labels.swift`). Si sale `NIGEBLAS` u otra variante, se regenera. Generar a **2K**.
- **Talla M siempre** en camisetas y sudaderas: medidas de la talla M y etiqueta de cuello con la letra M (ver `size-charts.md`).
- El logo es el avestruz corriendo, **cabeza mirando a la derecha del dibujo**, tal como en el techpack; no rotar, no espejar, no cambiar la silueta ni añadir texto.
- El wordmark es **NIDEBLAS** en mayúsculas, condensada, cursiva y negrita; la versión de camisetas bordadas/etiquetas de composición usa esa; la versión mixta `NiDeBlas` aparece en nuca trasera, colgante y camiseta Carbono.
- Camisetas Calle y sudadera marino llevan el logo **bordado** (relieve de hilo, sin brillo plástico). Las sudaderas de logo grande lo llevan en **flock/terciopelo mate** (textura aterciopelada).
- Bordado de camisetas Calle: **azul marino oscuro** sobre blanca y beige, **crema** sobre azul rey (confirmado en fotos reales).
- Las medidas son de **prenda plana en cm** (ver size-charts). No inventes proporciones.
- Si falta un dato (ver `references/open-questions.md`), dilo en vez de inventarlo.

## Referencias visuales (Drive: carpeta "Guia de Marca NDB")
- `Techpack/1.png`–`12.png`: una lámina por SKU con foto frontal, logo y colocación. Mapa en catalog.md.
- `Medidas Ropa/*.pdf`: 5 tablas graded spec.
- `Etiqueta Cuello`, `Etiqueta de composición`, `Etiqueta Colgante`: PDFs de Etigui (proveedor de etiquetas).
Descarga estos archivos y súbelos como imágenes de referencia (character/product reference) al modelo de imagen o vídeo. Recomendado además: foto real plana frontal y trasera de cada prenda sobre fondo neutro.

## Mapa de archivos
| Archivo | Contenido |
|---|---|
| `references/brand.md` | Identidad, logo, wordmark, paleta, tono visual |
| `references/catalog.md` | 13 SKUs con prompt-ficha |
| `references/size-charts.md` | Medidas por talla, circunferencias, traducción a fit |
| `references/labels-trims.md` | Etiquetas y complementos con medidas y colores |
| `references/prompt-playbook.md` | Plantillas, negativos, vídeo, QA |
| `references/photo-references.md` | Índice de fotos reales, qué demuestran y cómo usarlas |
| `references/studio-shots-recipe.md` | Receta probada de serie de estudio para web (modelo, prompts por vista, entrega) |
| `assets/` | Fotos reales de cuello/etiqueta: camiseta Calle (S, M, L, XL), sudadera (M, L), deportiva (menta M y lavanda), y apoyo con el texto exacto NIDEBLAS M |
| `references/open-questions.md` | Huecos y erratas detectadas en la documentación |
