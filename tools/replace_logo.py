#!/usr/bin/env python3
"""Sustituye el avestruz bordado de una foto con modelo por el logo real extraido del macro.
Uso: replace_logo.py --macro macro.jpg --img in.jpg --out out.jpg --center X,Y [--win 130] [--xscale 1.0] [--rot 0]
Detecta el logo generado (pixeles azul marino) en una ventana alrededor de --center, lo borra (inpaint) y pega el logo real
con la misma altura. Pensado para bordado oscuro sobre tela clara (TS-05/06). El --mode color (flock azul grande, sudaderas) es EXPERIMENTAL y dejo restos/huecos: no usar; en sudaderas el logo grande sale consistente con la referencia macro. Ejecutar con un venv con numpy+opencv.
"""
import argparse, cv2, numpy as np

MODE = 'dark'  # 'dark' = bordado oscuro sobre tela clara; 'color' = flock/color saturado (azul) sobre tela clara

def color_mask(img):
    b, r = img[..., 0].astype(int), img[..., 2].astype(int)
    return ((b - r) > 50) & (b > 110)

def navy_mask(img, thr=30):
    if MODE == 'color':
        return color_mask(img)
    # oscuro respecto al fondo local (la tela clara) y con tinte azul/neutro
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.float32)
    bg = cv2.medianBlur(gray.astype(np.uint8), 31).astype(np.float32)
    b, r = img[..., 0].astype(int), img[..., 2].astype(int)
    return ((bg - gray) > thr) & ((b - r) > 6)

def extract_logo(macro_path):
    m = cv2.imread(macro_path)
    g = cv2.cvtColor(m, cv2.COLOR_BGR2GRAY)
    if MODE == 'color':
        raw = color_mask(m).astype(np.uint8)
    else:
      raw = ((g < 150) & ((m[..., 0].astype(int) - m[..., 2].astype(int)) > 4)).astype(np.uint8)
    raw = cv2.morphologyEx(raw, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    merged = cv2.dilate(raw, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (45, 45)))
    n, lab, stats, _ = cv2.connectedComponentsWithStats(merged)
    big = 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])
    comp = (lab == big) & (raw > 0)
    ys, xs = np.where(comp)
    x0, x1, y0, y1 = max(xs.min() - 6, 0), xs.max() + 7, max(ys.min() - 6, 0), ys.max() + 7
    crop = m[y0:y1, x0:x1]
    a = comp[y0:y1, x0:x1].astype(np.float32)
    a = cv2.GaussianBlur(a, (0, 0), 1.2)
    return crop, a

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--macro', required=True); ap.add_argument('--img', required=True); ap.add_argument('--out', required=True)
    ap.add_argument('--center', required=True); ap.add_argument('--win', type=int, default=130)
    ap.add_argument('--xscale', type=float, default=1.0); ap.add_argument('--rot', type=float, default=0.0)
    ap.add_argument('--hscale', type=float, default=1.0); ap.add_argument('--mode', default='dark', choices=['dark', 'color'])
    ap.add_argument('--maxy', type=float, default=0.55, help='con --center auto: fraccion superior de la imagen donde buscar el logo')
    A = ap.parse_args()
    global MODE
    MODE = A.mode
    img = cv2.imread(A.img)
    if A.center == 'auto':
        mm = color_mask(img[:int(img.shape[0] * A.maxy)]).astype(np.uint8)
        n, lab, st, cen = cv2.connectedComponentsWithStats(cv2.dilate(mm, np.ones((15, 15), np.uint8)))
        k = 1 + np.argmax(st[1:, cv2.CC_STAT_AREA]); cx, cy = map(int, cen[k])
    else:
        cx, cy = map(int, A.center.split(','))
    x0, y0 = max(cx - A.win, 0), max(cy - A.win, 0)
    win = img[y0:cy + A.win, x0:cx + A.win]
    mk = navy_mask(win).astype(np.uint8)
    mk = cv2.morphologyEx(mk, cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8))
    ys, xs = np.where(mk > 0)
    if len(xs) < 20: raise SystemExit('logo no detectado en la ventana')
    bx0, bx1, by0, by1 = xs.min(), xs.max(), ys.min(), ys.max()
    h = (by1 - by0 + 1) * A.hscale
    full = np.zeros(img.shape[:2], np.uint8); full[y0:y0 + mk.shape[0], x0:x0 + mk.shape[1]] = mk
    # mascara de borrado mas laxa para no dejar restos del logo generado
    soft = (navy_mask(win, thr=14).astype(np.uint8))
    full[y0:y0 + soft.shape[0], x0:x0 + soft.shape[1]] |= soft
    full = cv2.dilate(full, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (17, 17)))
    clean = cv2.inpaint(img, full * 255, 9, cv2.INPAINT_TELEA)
    logo, alpha = extract_logo(A.macro)
    s = h / logo.shape[0]
    nw, nh = max(int(logo.shape[1] * s * A.xscale), 2), max(int(logo.shape[0] * s), 2)
    logo = cv2.resize(logo, (nw, nh), interpolation=cv2.INTER_AREA)
    alpha = cv2.resize(alpha, (nw, nh), interpolation=cv2.INTER_AREA)
    if A.rot:
        M = cv2.getRotationMatrix2D((nw / 2, nh / 2), A.rot, 1)
        logo = cv2.warpAffine(logo, M, (nw, nh), borderMode=cv2.BORDER_REPLICATE)
        alpha = cv2.warpAffine(alpha, M, (nw, nh))
    ccx, ccy = x0 + (bx0 + bx1) // 2, y0 + (by0 + by1) // 2
    X, Y = ccx - nw // 2, ccy - nh // 2
    roi = clean[Y:Y + nh, X:X + nw].astype(np.float32)
    a3 = alpha[..., None]
    out = roi * (1 - a3) + logo.astype(np.float32) * a3
    clean[Y:Y + nh, X:X + nw] = np.clip(out, 0, 255).astype(np.uint8)
    cv2.imwrite(A.out, clean, [cv2.IMWRITE_JPEG_QUALITY, 95])
    print('logo detectado', (bx1 - bx0 + 1, by1 - by0 + 1), '-> pegado', (nw, nh), 'en', (ccx, ccy))

if __name__ == '__main__':
    main()
