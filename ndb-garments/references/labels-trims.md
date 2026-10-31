# Etiquetas y complementos

## REGLA CRÍTICA: el texto de la etiqueta
La marca en cualquier etiqueta, colgante o cinta se escribe **siempre `NIDEBLAS`** (mayúsculas; en colgante y espalda de Carbono, `NiDeBlas`). Ocho letras, en este orden: **N-I-D-E-B-L-A-S**. Errores vistos en generación y prohibidos: `NIGEBLAS`, `NIDEBIAS`, `NIDEBLAZ`, `MIDEBLAS`, `HIDEBLAS`.
- La etiqueta de cuello lleva además la talla: **`NIDEBLAS` + `M`** (siempre M).
- **Fotos reales de la etiqueta (referencia principal)** en `ndb-garments/assets/`: `etiqueta-cuello-real-talla-S.jpg`, `-M.jpg`, `-L.jpg`, `-XL.jpg` (macro de la etiqueta cosida, aportadas por el equipo). **Para toda imagen se sube `etiqueta-cuello-real-talla-M.jpg`** y se dice en el prompt que copie el texto y la forma de ahí. Como apoyo, `etiqueta-cuello-plana-NIDEBLAS-M.jpg` (texto exacto, plana) y `etiqueta-cuello-NIDEBLAS-M.jpg` (macro generado).
- **Cómo es la etiqueta real (talla M):** rectángulo de satén negro cosido bajo la cinta negra del cuello, con borde derecho ligeramente inclinado; texto blanco tejido en cursiva condensada: `NIDEBLAS` a la izquierda y la letra de talla a la derecha, separada por un hueco amplio (`NIDEBLAS    M`). Sin más texto.
- Toda imagen con etiqueta visible pasa el comprobador OCR (`tools/ocr_labels.swift`) antes de aprobarse.

## CUELLO Y ETIQUETA POR FAMILIA DE PRENDA (crítico: cada familia es distinta)
La etiqueta de talla es la misma (`NIDEBLAS` + `M`), pero **el cuello y cómo va colocada cambian por familia**. Nunca usar el cuello de una familia en otra. Fotos reales en `ndb-garments/assets/`.

| | Camiseta Calle (algodón) | Sudadera Calle | Camiseta deportiva (poliéster) |
|---|---|---|---|
| SKUs | TS-05…TS-10, TS-13 | SW-01…SW-04 | SP-11, SP-12 |
| Cuello | **Canalé fino** (≈1–2,5 cm) del mismo color, costura vista | **Canalé grueso** (≈2,5–3 cm) con costillas verticales marcadas, mismo color, sobre un cuerpo más voluminoso | **Sin canalé**: cuello redondo rematado con un ribete estrecho del mismo tejido liso |
| Cinta negra interior | **Sí**: cinta negra (twill/sarga) por el borde interior del cuello | **No hay cinta negra**. Solo una cinta/ribete del mismo color de la prenda sobre la costura | **Sí**: cinta elástica negra con `NIDEBLAS` blanco cursiva **repetido** cosida por el interior |
| Etiqueta de talla | Etiqueta tejida de satén negro `NIDEBLAS  M`, colgando **bajo la cinta negra** | Etiqueta tejida negra `NIDEBLAS  M` cosida **plana sobre el tejido del cuerpo**, centrada en la espalda **justo bajo la costura interior del cuello** (debajo del canalé), borde derecho algo inclinado | **No lleva etiqueta tejida**: etiqueta **estampada** negra sobre el tejido, centrada bajo la cinta: icono de avestruz, `NiDeBlas`, talla (`M`), una línea fina y `MADE IN PORTUGAL` |
| Foto de referencia | `etiqueta-cuello-real-talla-M.jpg` (también S, L, XL) | `etiqueta-cuello-sudadera-M.jpg` (también `-L.jpg`) | `etiqueta-cuello-deportiva-M.jpg` (menta) y `etiqueta-cuello-deportiva-lavanda.jpg` |

### Frases de prompt por familia (pegar la que corresponda)
- **Camiseta Calle:** `narrow ribbed crew collar in the garment color; black twill neck tape along the inside edge of the collar and, below it, a small black satin woven label reading NIDEBLAS and M (copy reference photo)`
- **Sudadera:** `thick vertically-ribbed (rib knit) crew collar about 2.5 to 3 cm wide in the garment color; NO black tape anywhere; a small black woven label reading NIDEBLAS and M sewn flat on the body fabric inside the back, centered just below the inner collar seam (copy reference photo)`
- **Deportiva:** `no rib collar: smooth round neckline finished with a narrow self-fabric binding; a black woven elastic tape printed with repeating white italic NIDEBLAS sewn along the inside edge; NO woven label: instead a black heat-transfer printed label directly on the inside back fabric, centered below the tape: small ostrich icon, the word NiDeBlas, the size M, a thin horizontal line and MADE IN PORTUGAL in small capitals (copy reference photo)`
- **Vista trasera** de sudadera: canalé grueso sin cinta negra. De camiseta Calle: cinta negra en el borde interior. De deportiva: cinta negra con NIDEBLAS repetido en el borde interior del cuello.

Proveedor: **Etigui Acessórios** (fichas de producción). Mínimos 250–500 uds. Fechas de las fichas: marzo–mayo 2026.

## 1. Etiqueta de cuello (talla) — `Etiqueta Cuello NDB`
- Tejido alta definición (woven damask), **negro con texto blanco**. Medida de corte **60 × 44 mm**, se dobla por el centro y se cose al cuello con **corte y vinco (doblez) en los lados**; queda visible como una banda negra de ≈ **60 × 22 mm** con borde inclinado en un extremo.
- Texto: `NIDEBLAS` en blanco, cursiva condensada, a la izquierda; **talla** (XS, S, M, L, XL) a la derecha en el mismo tipo. Una variante por talla.
- Hilos: negro y blanco.
- Prompt: `black woven neck label, 60 mm wide, white italic condensed "NIDEBLAS" on the left and the size letter on the right, stitched flat inside the back neck, folded edges clean.`

## 2. Etiquetas decorativas de dobladillo (tab) — `Etiqueta color azul` / `Etiqueta color rosa`
- Rectángulo tejido de **15 × 50 mm**, texto `NIDEBLAS` blanco cursiva condensada sobre fondo plano.
- Azul: **PANTONE 2728 C** (cobalto). Rosa: **PANTONE 233 C** (fucsia). Hilo blanco. Acabado: corte (borde cortado).
- Uso: sudaderas SW-01/02/03 en el bajo, a 4 cm de la costura lateral y 4 cm del dobladillo inferior (lado izquierdo de quien la lleva según la foto).
- El rosa se usa en la sudadera beige/fucsia; el azul en las otras.

## 3. Etiqueta de composición y cuidados — `Etiqueta de composición`
- Cetim (satén) **negro** estampado en blanco, **40 × 86,333 mm**, se dobla por la marca superior (bucle) y se cose en la costura lateral interior.
- Cabecera `NIDEBLAS` (cursiva condensada), después composición, luego cuidados bilingües EN/PT:
  - Machine wash at 30 °C, gentle cycle · Do not bleach · Do not tumble dry · Iron at maximum 110 °C · Do not dry clean · Do not iron badges and decorations.
  - Símbolos: lavado 30 °, no lejía, no secadora, plancha baja, no limpieza en seco. Pie: `nideblas.com`.
- 4 variantes: `100 % COTTON`, `100 % POLYESTER`, `89 % POLYESTER / 11 % ELASTANE`, `81 % COTTON / 15 % POLYESTER / 4 % ELASTANE`.
- Mapa: camisetas Calle = 100 % algodón; sudaderas = 81/15/4; deporte hombre = 100 % poliéster; deporte mujer = 89/11.

## 4. Etiqueta colgante (hang tag) — `Etiqueta colgante`
- Cartulina **60 × 100 mm**, cara frontal **negra** con avestruz **blanco** y `NiDeBlas` debajo (blanco, cursiva condensada), agujero para cordón en el borde superior; reverso blanco/en blanco (borde rosa de corte en la ficha). Cordón: por definir.
- Datos de la ficha incompletos ("A Definir" en material, acabado y Pantone). Ver open-questions.
- Prompt: `black rectangular cardboard hang tag 60×100 mm, white running-ostrich centered, white italic condensed "NiDeBlas" below, small punched hole at the top center with a thin cord.`

## 5. Cinta de cuello deportivas
- Cinta elástica **negra** con `NIDEBLAS` en blanco cursiva repetido a lo largo (se ven 4 repeticiones en el interior del cuello). Aplica a SP-11 y SP-12. Etiqueta estampada (no tejida) bajo la cinta; ver tabla de familias.

## 6. Tab lateral Carbono
- Pequeña etiqueta negra, **3 cm alto × 2 cm ancho (doblada)**, texto `NiDeBlas` en blanco **rotado 90°**, en la costura lateral, **10 cm por encima del bajo**.
