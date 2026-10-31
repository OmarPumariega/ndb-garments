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
Sets definitivos: `outputs/MODELO-<AVATAR>_<SKU>_<slug>/` (las pruebas antiguas se eliminaron del repositorio el 31/10).

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
Orden: 1 frontal (ancla, ref: lámina + frontal v2 + placa + macro de logo del grid) → 2 trasera → 3 tres cuartos → 4 media distancia → 5 primer plano logo (4:5, ref macro del logo). Todas con la frontal como ref 1. 2K.
**NO se genera detalle de cuello/etiqueta con modelo** (decisión del equipo 31/10: la toma de la nuca con el cuello doblado a mano se ve falsa/IA). El cuello y la etiqueta se enseñan solo con las fotos de la prenda sola (flatlay y detalle de cuello de la serie de producto).
Salida: `outputs/MODELO-<AVATAR>_<SKU>_<slug>/` con `modelo-<avatar>-<prenda>-<vista>.webp`, grid y `alt-text.csv`.

### Ajustes que mejoraron el resultado
- Expresión: pedir "labios cerrados con asomo de sonrisa", "sonrisa natural con dientes", "mirada fuera de cámara"; variar por vista.
- Sombra: "CLEARLY VISIBLE soft gray shadow under and behind both feet, falling back and to the right".
- Ajuste M: "hem at the hip bone, sleeves end mid-bicep, natural folds".
- Logo: dar el macro del logo como referencia y decir "5 cm, head facing right, thread texture".

### Checklist QA por imagen (antes de aprobar)
[ ] cara = lámina del avatar [ ] manos 5 dedos [ ] color y corte de la prenda = grid [ ] logo: tamaño 5 cm, orientación (cabeza a la derecha), técnica [ ] etiqueta NIDEBLAS M (OCR `OK` o recorte visual) [ ] fondo = placa [ ] sombra visible [ ] sin texto inventado [ ] pantalón/calzado según tabla.
OCR: las fotos de modelo no muestran etiqueta, no se pasa OCR; si algún plano deja ver texto, se verifica.

## Consistencia del logo bordado (aprendido 31/10)
El avestruz **bordado pequeño** (camisetas Calle, 5 cm) NO sale idéntico en cada toma: el modelo de imagen lo redibuja distinto (patas, cola, grosor) en frontal, 3/4 y media distancia. El macro del logo sí sale perfecto.
**Solución obligatoria tras generar:** `tools/replace_logo.py` borra el logo generado (inpaint) y pega el logo real extraído del macro aprobado (`--macro` = la imagen de detalle de logo del mismo set), a la misma altura y con `--xscale 0.9` en tres cuartos.
```bash
python3 -m venv work-models/venv && work-models/venv/bin/pip install numpy opencv-python-headless pillow
work-models/venv/bin/python tools/replace_logo.py --macro logo.jpg --img front.jpg --out fix/front.jpg --center X,Y [--win 170 --xscale 0.9]
```
Revisar el recorte ampliado de cada toma (restos del logo viejo, borde). Funciona con bordado oscuro sobre tela clara (TS-05/06/08/09…). Para logo claro/crema sobre tela oscura (TS-07, TS-13) usar `--mode light` y centro/ventana ajustados (`--win 62` en pecho de frontal/3/4: una ventana mayor coge piel). Probado con Pablo + TS-13. El flock grande de las sudaderas sale consistente sin parche.
Orden de trabajo: generar el macro del logo primero y aprobarlo; las demás tomas se corrigen con él.

## Reparto de modelos (completado 31/10, prendas masculinas)
| Modelo | Prendas |
|---|---|
| Alex | TS-06 blanca (vaquero índigo), TS-05 beige (vaquero negro), TS-08 celeste (chino arena), SW-02 crema/fucsia (vaquero oscuro) |
| Oscar | SW-01 crema/cobalto (vaquero azul medio), TS-07 azul marino (vaquero claro), SW-03 celeste (pantalón gris carbón), SP-12 deportiva menta (short negro de running, zapatillas de correr) |
| Pablo | TS-13 azul rey (chino crema), TS-09 verde salvia (vaquero oscuro), SW-04 azul petróleo (chino negro), TS-10 Carbono (vaquero claro) |
Pendiente: SP-11 (mujer) con modelo femenina; exterior.

## Aprendido en la tanda de 9 sets
- `replace_logo.py`: la detección del logo generado usa la **mediana de la ventana** como fondo. Para logos muy oscuros sobre tela clara o media (TS-05, TS-08, TS-09, SP-12) funciona mejor `--mode darkany --thr 90`; `--mode dark` falla en logos finos. Para crema/gris-violeta sobre tela oscura (TS-07, SW-04) `--mode light`. Siempre `--win` pequeño (60–110) y centro exacto: con centro/ventana mal puestos coge piel o cuello.
- Deportivas: vestir al modelo con short de running, calcetines bajos blancos y zapatillas de correr; poses de ejercicio (manos en cintura, zancada, estiramiento, secándose la frente). Pedir "NO sweat stains / wet patches": si no, salen manchas de sudor en la tela.
- TS-10 Carbono: el estampado grande (avestruz mecánico) cambia de tamaño y detalle entre tomas; no hay parche automático. El rótulo trasero `NiDeBlas / Born Asturias` se lee bien. SW-04: el wordmark bordado de la nuca sale legible (`NiDeBlas`).
- Herramienta de cierre: `tools/finalize_model_set.py` (WebP, grid 3x2, alt-text) usa `fix/` si existe.
