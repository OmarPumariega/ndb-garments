# Modelos (avatares) en estudio NDB

## Fondo de estudio oficial (decidido 31/10)
Referencia: `Referencia Modelo Ropa Deportiva.jpg` (Drive › Referencia Estudio Fotográfico › Referencia Ropa Deportiva; copia de trabajo `work-models/ref-studio-bg.jpg`).
- Cíclorama continuo blanco roto/gris perla (~#F0F0EE), nunca blanco puro; sin horizonte.
- Luz de softbox frontal, suave, sin sombras duras.
- Sombra suave y difusa en el suelo bajo y detrás de los pies; pies apoyados.
- Cuerpo entero 3:4, 2K, mismo margen arriba/abajo. Exterior: pendiente.

## Avatares (láminas en Drive › Fotos Ropa NDB › Avatar NDB)
Alex (castaño ondulado, barba ligera, ojos marrones), Oscar (rapado, barba de varios días, mandíbula marcada), Pablo (rubio ondulado, ojos azules). Todos 1,80 m / 72 kg, atléticos. No hay mujeres.

## Receta (referencias en este orden)
1 lámina del avatar · 2 grid de la prenda (`outputs/<SKU>/…-grid.webp` → jpg) · 3 fondo · 4 etiqueta/cuello de su familia si se ve la nuca.
Prompt: "SAME man as image 1 … wearing the garment of image 2 (copy color, fit, logo) … remove the white t-shirt of image 1 completely … studio of image 3 exactly". Mantener chinos beige y zapatillas blancas. Talla M.
Pruebas: `outputs/_pruebas-modelos/` (Alex+TS-06, Oscar+SW-01, Pablo+TS-13).

## Actualización 31/10 (v2)
- **Placa de estudio**: `assets/placa-estudio-ndb.jpg` (cíclorama vacío). Se sube SIEMPRE como ref. 3 y se dice "ignora la sombra flotante de la placa; dibuja la sombra de SUS pies, hacia atrás y a la derecha". Foto de estilo original: `assets/ref-estudio-modelo-negro.jpg`.
- **Outfit fijo por SKU** (no repetir el chino beige):
  | Prenda | Pantalón | Calzado |
  |---|---|---|
  | Camisetas blanca / beige | vaquero índigo oscuro o negro | zapatilla blanca |
  | Azul marino / celeste / azul rey | vaquero claro o chino crema | blanca / ante marrón oscuro |
  | Verde salvia | vaquero oscuro o chino arena | blanca |
  | Sudaderas crema | vaquero azul medio | blanca |
  | Sudaderas celeste / petróleo | gris carbón o negro | blanca |
  | Carbono | vaquero claro o gris claro | blanca |
  | Deportivas | short/malla técnica negra o gris | running |
- **Pose**: una distinta por foto (mano en bolsillo, paso al caminar, brazos cruzados con cuerpo en 3/4); trasera con cabeza girada.
- **Orden**: frontal (ancla) → trasera usando la frontal como ref. 1 + grid + placa. Las traseras de camiseta/sudadera no muestran etiqueta (va por dentro); la etiqueta se enseña solo en detalle de cuello (OCR).
- **Pendiente**: tab del bajo de la sudadera sale con texto ilegible (pasar OCR si se ve de cerca); modelo femenino para SP-11; tres cuartos, media distancia y primer plano; exterior.

## Set completo con modelo (probado: Alex + TS-06, 31/10)
Orden: 1 frontal (ancla, ref: lámina + frontal v2 + placa + macro de logo del grid) → 2 trasera → 3 tres cuartos → 4 media distancia → 5 primer plano logo (4:5, ref macro del logo) → 6 detalle cuello (4:5, ref foto de cuello de la familia + etiqueta real M + bloque de ortografía + OCR). Todas con la frontal como ref 1. 2K.
Salida: `outputs/MODELO-<AVATAR>_<SKU>_<slug>/` con `modelo-<avatar>-<prenda>-<vista>.webp`, grid y `alt-text.csv`.

### Ajustes que mejoraron el resultado
- Expresión: pedir "labios cerrados con asomo de sonrisa", "sonrisa natural con dientes", "mirada fuera de cámara"; variar por vista.
- Sombra: "CLEARLY VISIBLE soft gray shadow under and behind both feet, falling back and to the right".
- Ajuste M: "hem at the hip bone, sleeves end mid-bicep, natural folds".
- Logo: dar el macro del logo como referencia y decir "5 cm, head facing right, thread texture".
- Cuello con modelo: nuca desde atrás con la mano doblando el cuello hacia abajo para mostrar cinta + etiqueta.

### Checklist QA por imagen (antes de aprobar)
[ ] cara = lámina del avatar [ ] manos 5 dedos [ ] color y corte de la prenda = grid [ ] logo: tamaño 5 cm, orientación (cabeza a la derecha), técnica [ ] etiqueta NIDEBLAS M (OCR `OK` o recorte visual) [ ] fondo = placa [ ] sombra visible [ ] sin texto inventado [ ] pantalón/calzado según tabla.
OCR: la frontal y el logo dan `NO` porque no hay etiqueta visible (correcto); el detalle de cuello dio `OK`.
