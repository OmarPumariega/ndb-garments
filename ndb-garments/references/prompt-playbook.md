# Prompt playbook (imagen y vídeo)

Escribe los prompts finales en **inglés** (los modelos responden mejor); la conversación con el usuario, en español.

## Principios de consistencia
1. **Ancla visual > texto.** Sube siempre como referencia: lámina del techpack del SKU, foto plana real de la prenda, logo aislado. Di en el prompt qué hace cada referencia ("image 1 = garment, image 2 = logo placement").
2. **Una prenda, una ficha.** Pega el Prompt-ficha del SKU sin parafrasear. Cambia solo escena, pose y luz.
3. **Fija el modelo** (cara, pelo, altura, talla que lleva) y reutilízalo; usa seed o "character reference" cuando exista.
4. **Fit con números.** Convierte tabla a lenguaje: "chest ease ≈ 14 cm, hem at mid-hip, shoulder seam 2 cm below the natural shoulder".
5. **Logo pequeño = detalle macro aparte.** En planos generales el bordado de 5 cm mide ≈ 1/6 del ancho del pecho; no lo agrandes. Haz un plano de detalle si importa.
6. **Un cambio por iteración** (color, pose o escena), nunca los tres.

## Plantilla A · Foto de producto (ghost mannequin / plano)
```
Studio e-commerce photo, front view, [GARMENT PROMPT-FICHA], laid flat / on invisible mannequin, soft diffused light, seamless light-gray background (#E9E9EC), natural fabric texture visible (cotton jersey weave / heavy interlock), crisp seams, accurate color, shot at 85 mm, no props.
Proportions: chest width [PEITO] cm flat, body length [LARGO] cm, sleeve [MANGA] cm, shoulder-to-shoulder [HOMBRO] cm (size [TALLA]).
References: image 1 = real garment; image 2 = logo, keep exact silhouette and placement.
Negative: wrong logo shape, mirrored logo, extra text, extra graphics, blurry embroidery, plastic shine on embroidery, misspelled NIDEBLAS, wrinkled distortion, brand logos of other companies, extra pockets, drawstrings (on sweatshirts).
```

## Plantilla B · Modelo vistiendo la prenda (lifestyle)
```
[Shot type: full-body / three-quarter / waist-up] photo of [MODEL: gender, age, height, build, hair, skin tone] wearing [GARMENT PROMPT-FICHA] in size [TALLA] (chest circumference [PEITO×2] cm vs model chest [X] cm → [relaxed/regular/fitted] fit), [POSE], [SCENE: e.g. Asturian coastline, grey sea, wet stone, soft overcast light], natural skin texture, shallow depth of field, 35 mm, editorial streetwear look.
The logo must read clearly and in the exact position: [POSICIÓN DEL LOGO].
Negative: oversized if not specified, wrong sleeve length, logo too big, logo centered if it should be on the left chest, text artifacts, warped hands.
```

## Plantilla C · Detalle bordado / etiqueta (macro)
```
Macro close-up, [bordado 5 cm de avestruz sobre tejido X], raised satin stitch, directional thread sheen, tiny fabric fibers, shallow depth of field, soft side light, the stitched ostrich keeps the exact silhouette from the reference.
```
Para etiquetas: usar los prompts de `labels-trims.md` e indicar tamaño real ("60 mm wide label, roughly the width of a matchbox").

## Plantilla D · Vídeo (Veo / Kling / Runway / Seedream / Wan)
```
[Duration 5–8 s]. [CAMERA: slow dolly-in / handheld / orbit 45°]. [MODEL] wearing [GARMENT PROMPT-FICHA], [ACTION: walks toward camera, turns, adjusts sleeve], [SCENE]. Fabric moves realistically (drape, light motion in hem), logo stays crisp and fixed in position on the garment, no morphing, no text change.
Start frame: [IMAGEN YA APROBADA]. Keep garment color, logo, and fit identical throughout.
```
- Genera el **primer fotograma como imagen aprobada** y úsalo como start frame (image-to-video). Para varias tomas, reutiliza el mismo start frame con distinto movimiento de cámara.
- Prohibido en vídeo: giros de 360° sobre la prenda con logo (el modelo reinventa el reverso). Si hay espalda, mostrarla con el SKU que la documenta (SW-04, TS-10) y subir la referencia.

## Plantilla E · Serie multi-prenda (misma escena, varios colores)
Congela escena + modelo + pose y cambia **solo** el bloque "[GARMENT PROMPT-FICHA]". Generar de uno en uno; no pedir varios colores en la misma imagen.

## Negativos universales
`distorted ostrich logo, mirrored logo, extra legs on logo, text misspelling, extra letters, fake brand logos, Nike swoosh, three stripes, gradient fill on solid logo, glossy plastic embroidery, wrong garment color, extra pockets, hood, zipper, drawstring, graphic print where none exists, inconsistent sleeve length`.

## Checklist QA (marcar antes de aprobar)
- [ ] Color de tela coincide con el SKU (comparar con foto del techpack).
- [ ] Logo: silueta correcta, cabeza a la derecha, sin texto añadido, color correcto.
- [ ] Tamaño del logo proporcional (5 cm ≈ 1/6 del ancho del pecho; 20 cm ≈ 1/3 del pecho).
- [ ] Posición: pecho izquierdo (5 cm) o centro a 11 cm del cuello (20 cm).
- [ ] Largo de manga y cuerpo coherentes con la tabla (manga corta; sudadera hasta cadera).
- [ ] Rib en puños, cuello y cintura de sudaderas; sin capucha ni bolsillos.
- [ ] Etiqueta de cuello negra con NIDEBLAS visible si se ve el interior.
- [ ] Wordmark escrito exactamente: NIDEBLAS / NiDeBlas.
- [ ] Manos, costuras y bajos sin deformaciones.
- [ ] En vídeo: el logo no cambia de forma ni se desplaza entre fotogramas.
