# Procedimiento paso a paso: cómo se generan las imágenes de producto NDB

Guía para repetir el proceso con cualquier prenda y obtener siempre el mismo resultado: imágenes de estudio listas para la web (frontal, trasera, lateral, flatlay, detalle de logo y detalle de cuello). Probado con la camiseta Calle blanca (TS-06).

## Reglas fijas (resumen)
- **Talla M siempre** en camisetas y sudaderas, con las medidas M y la etiqueta de cuello `NIDEBLAS M`.
- **Una prenda, una ficha:** no mezclar datos de dos SKUs.
- **Entrega:** un grid con todas las vistas + cada vista suelta, en **WebP** con **nombre SEO** y `alt-text.csv`.
- **Gana la foto real** sobre el techpack para color de hilo y textura; el techpack manda para la posición del logo en cm.

## Requisitos
- Acceso a la carpeta de Drive "Guia de Marca NDB" (Techpack, Medidas Ropa, Etiquetas, Referencias Visuales).
- Cuenta de kie.ai con créditos (generación de imágenes y subida de referencias).
- Python 3 con Pillow (`pip install pillow`) y macOS `sips` (o ImageMagick) para convertir HEIC.
- Esta skill: `ndb-garments/` (o `NDB_KIT_MAESTRO.md` para otras herramientas).

## Paso 1. Elegir el SKU
Abre `ndb-garments/references/catalog.md` y localiza la prenda (modelo + color). Copia su **Prompt-ficha** y anota color, logo (técnica, tamaño, posición) y etiquetas visibles. Revisa el apartado "Ajustes según fotos reales".

## Paso 2. Reunir datos de talla M
En `references/size-charts.md` → "Talla de referencia: M" copia pecho, largo, hombro y manga de la talla M de esa prenda y su lectura de fit (regular, relajado, boxy, entallado). Estos datos van en el prompt.

## Paso 3. Elegir las fotos de referencia
En `references/photo-references.md` busca las fotos reales del SKU y elige 3–4:
1. Prenda completa frontal (color y forma).
2. Macro del bordado o estampado (hilo, relieve, textura).
3. Cuello y etiqueta.
4. (Opcional) Vista cenital recta para el flatlay.
Si el SKU no tiene foto real, usa la lámina del techpack y márcalo como riesgo.

## Paso 4. Descargar y convertir las referencias
1. Descarga las fotos desde Drive (HEIC) a una carpeta de trabajo fuera del repositorio.
2. Conviértelas a JPG:
   ```bash
   for f in *.HEIC *.heic; do sips -s format jpeg -Z 2048 "$f" --out "${f%.*}.jpg"; done
   ```
3. Sube cada JPG a kie.ai (herramienta `upload_file`). Devuelve una URL pública que **caduca a los 3 días**.

## Paso 5. Generar el frontal (la imagen ancla)
- Modelo: **Nano Banana 2.1** (`nano-banana-2-1`), formato **3:4**, ~4 créditos por imagen.
- Referencias: foto completa + macro del bordado + cuello.
- Prompt: plantilla "Frontal" de `references/studio-shots-recipe.md` + Prompt-ficha del SKU + medidas M + `neck label reads "NIDEBLAS M"`.
- Revisa el resultado (checklist QA del playbook). Si algo falla, cambia **una sola cosa** por iteración. Si el logo sale simplificado o con otra silueta, repite añadiendo una referencia más clara del logo.
- Guarda la **URL del frontal aprobado**: es la referencia 1 del resto de vistas.

## Paso 6. Generar el resto de vistas
Con la URL del frontal aprobado como referencia 1 (así se mantienen prenda, luz y fondo):

| Vista | Formato | Referencias adicionales |
|---|---|---|
| Trasera | 3:4 | Cuello (cinta negra). Espalda lisa salvo SW-04 y TS-10 |
| Lateral | 3:4 | Macro del logo |
| Flatlay (cenital) | 3:4 | Foto cenital real |
| Detalle logo | 4:5 | Macro del bordado real |
| Detalle cuello | 4:5 | Foto de cuello y etiqueta |

Los prompts exactos de cada vista están en `references/studio-shots-recipe.md`. Fondo siempre `#E9E9EC`, luz difusa de estudio.

## Paso 7. Revisión de calidad
Marca el checklist del playbook:
- Color de tela igual que la foto real.
- Logo: silueta correcta (cabeza a la derecha), color y tamaño proporcional, posición correcta.
- Etiqueta `NIDEBLAS M` legible; sin textos añadidos.
- Largo y manga coherentes con la talla M.
- Sin bolsillos, capucha ni gráficos inventados.
- Consistencia entre vistas (mismo blanco, misma luz, mismo fondo).
Compara el avestruz con el **logo vectorial oficial** antes de aprobar. Anota en `references/open-questions.md` cualquier riesgo.

## Paso 8. Montar el grid
Junta todas las vistas en una sola imagen (2 filas × 3 columnas), para revisión rápida:
```python
from PIL import Image
names=['frontal','trasera','lateral','flatlay','detalle-logo','detalle-cuello']
ims=[Image.open(f'{n}.jpg').convert('RGB') for n in names]
h=600
ims=[i.resize((int(i.width*h/i.height),h)) for i in ims]
W=max(sum(i.width for i in ims[:3]), sum(i.width for i in ims[3:]))
sheet=Image.new('RGB',(W,h*2),'white')
x=0
for i in ims[:3]: sheet.paste(i,(x,0)); x+=i.width
x=0
for i in ims[3:]: sheet.paste(i,(x,h)); x+=i.width
sheet.save('grid.jpg',quality=88)
```

## Paso 9. Optimizar a WebP con nombre SEO
Formato de nombre: `<tipo-de-prenda>-<modelo>-<color>-<vista>.webp`, en minúsculas, sin tildes ni espacios.

Ejemplos: `camiseta-calle-blanca-frontal.webp`, `camiseta-calle-blanca-detalle-logo.webp`, `sudadera-calle-celeste-trasera.webp`.

```python
from PIL import Image
Image.open('frontal.jpg').convert('RGB').save('camiseta-calle-blanca-frontal.webp','WEBP',quality=82,method=6)
```
Resultado esperado: de 300–600 KB a 13–60 KB por imagen. Si se necesita más resolución, se reescala antes de convertir (herramienta de upscale de kie.ai).

## Paso 10. Texto alternativo
Crea `alt-text.csv` (columnas `archivo,alt`) con una descripción en español por imagen: prenda, color, vista y logo. El grid no lleva alt.

## Paso 11. Guardar en el repositorio
Estructura:
```
outputs/<SKU>_<nombre-prenda>/
  <tipo>-<modelo>-<color>-grid.webp
  <tipo>-<modelo>-<color>-frontal.webp
  ... (trasera, lateral, flatlay, detalle-logo, detalle-cuello)
  alt-text.csv
```
No se suben HEIC, logs de la herramienta ni pruebas intermedias (están en `.gitignore`).

## Paso 12. Subir a GitHub
```bash
git add -A
git commit -m "Add <SKU> studio shots"
git push origin main
```
Repositorio: https://github.com/OmarPumariega/ndb-garments

## Paso 13. Actualizar la documentación si algo cambió
Si el trabajo revela un dato nuevo (color real, medida, etiqueta, error), edítalo en el archivo de `references/` correspondiente y regenera el kit maestro:
```bash
{ echo "# NDB — Kit maestro para pegar en cualquier modelo de IA"; for f in brand catalog size-charts labels-trims photo-references prompt-playbook studio-shots-recipe open-questions; do echo; echo "---"; echo; cat "ndb-garments/references/$f.md"; done; } > NDB_KIT_MAESTRO.md
```

## Costes y tiempos de referencia
- Una serie de 6 vistas con Nano Banana 2.1: ~24 créditos (~0,12 $), unos minutos.
- Recomendación: generar primero el frontal de cada prenda, aprobarlo, y después el resto en bloque.

## Problemas conocidos y cómo resolverlos
| Problema | Solución |
|---|---|
| El logo sale más detallado o con otra silueta | Añadir referencia del macro real; repetir con prompt corto sobre el logo |
| Etiqueta con talla distinta de M | Añadir `neck label reads "NIDEBLAS M"` y `ignore the size letter in the photo`; regenerar |
| Macro del logo sale sobre tela crema | Pedir `PURE WHITE ... not cream or beige` |
| Espalda o lateral inventados | Seguro solo en prendas con espalda lisa; en SW-04 y TS-10 usar referencia propia |
| Fondo del flatlay más oscuro | Forzar `#E9E9EC` y luz difusa |
| Imagen recortada por arriba | Pedir margen generoso alrededor de la prenda |
| Resolución baja (~900×1200) | Reescalar a 2K antes de publicar |
| Foto de referencia en HEIC | Convertir a JPG antes de subir |

## Pendientes conocidos
- Validar el logo contra el vectorial oficial.
- Fotos con persona y de espalda para mejorar el realismo del fit (ver `open-questions.md`).
- Subir las imágenes a 2K antes de publicar.
