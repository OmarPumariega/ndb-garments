# NDB Garments

Fuente de verdad de la ropa de **NiDeBlas (NDB)** para generar imágenes y vídeo con IA de forma consistente y realista: catálogo, colores, logo, medidas, etiquetas y plantillas de prompt.

> **¿Quieres generar imágenes nuevas?** Sigue el [procedimiento paso a paso](PROCEDIMIENTO.md).

## Qué hay aquí

| Ruta | Para qué |
|---|---|
| `PROCEDIMIENTO.md` | Guía paso a paso para generar, optimizar y publicar las imágenes |
| `ndb-garments/` | **Skill** para Claude Code / Claude (`SKILL.md` + `references/`) |
| `outputs/` | Imágenes generadas y aprobadas por prenda: grid + cada vista suelta en WebP con nombre SEO (`camiseta-calle-blanca-frontal.webp`) y `alt-text.csv` |
| `NDB_KIT_MAESTRO.md` | Todo el contenido en un solo archivo, para pegar en cualquier modelo (Midjourney, Flux, Veo, Kling, Runway, etc.) |

Contenido de `ndb-garments/references/`:

- `brand.md`: identidad, logo (avestruz), wordmark y paleta
- `catalog.md`: 13 prendas con prompt-ficha listo para pegar
- `size-charts.md`: tablas de medidas en cm y traducción a fit
- `labels-trims.md`: etiquetas de cuello, composición, colgante y tabs
- `photo-references.md`: índice de las fotos reales y cómo usarlas
- `prompt-playbook.md`: plantillas de imagen y vídeo, negativos y checklist de calidad
- `studio-shots-recipe.md`: receta probada para generar la serie de estudio (frontal, trasera, lateral, flatlay y detalles)
- `open-questions.md`: huecos, erratas y fotos que faltan

## Cómo usarlo

**Con Claude Code:** copia la carpeta `ndb-garments/` a `~/.claude/skills/` (o a `.claude/skills/` de un proyecto). Se activa sola al pedir imágenes o vídeo con prendas NDB.

**Con otras herramientas:** abre `NDB_KIT_MAESTRO.md`, copia el bloque del SKU que necesites y adjunta fotos de referencia.

## Reglas de oro

1. Un SKU, una ficha. No mezclar datos de dos prendas.
2. Adjuntar siempre 2–3 fotos reales de referencia (frontal, macro del logo, cuello).
3. Si foto real y techpack discrepan, gana la foto real para color y textura; el techpack manda para la posición en cm.
4. Si falta un dato, mirar `open-questions.md`; no inventar.

## Imágenes y documentos originales

Las fotos de referencia, PDFs de medidas, etiquetas y techpacks **no están en este repositorio**: viven en Google Drive (carpeta "Guia de Marca NDB"). Aquí solo está la documentación derivada.

## Mantenimiento

Cuando cambie una prenda, color o medida, edita el archivo de `references/` correspondiente y regenera el kit maestro:

```bash
{ echo "# NDB — Kit maestro para pegar en cualquier modelo de IA"; for f in brand catalog size-charts labels-trims photo-references prompt-playbook studio-shots-recipe open-questions; do echo; echo "---"; echo; cat "ndb-garments/references/$f.md"; done; } > NDB_KIT_MAESTRO.md
```
