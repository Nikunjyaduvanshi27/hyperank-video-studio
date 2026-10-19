"""Trace the hyperank mark's three shapes (two slanted bars, one rounded square) into SVG outline paths for the draw-on.

    python capture/mark.py   # -> assets/img/mark-paths.json  (viewBox = the PNG's pixel box)
Each shape is convex, so its outline is the convex hull of its opaque pixels; the hull keeps the rounded corners.
"""
import json
from pathlib import Path
import numpy as np
from PIL import Image

HERE = Path(__file__).resolve().parent
im = np.array(Image.open(HERE.parent / "assets/img/hyperank-mark.png"))
a = im[:, :, 3] > 128
H, W = a.shape


def hull(pts):
    pts = sorted(set(map(tuple, pts)))
    cross = lambda o, p, q: (p[0] - o[0]) * (q[1] - o[1]) - (p[1] - o[1]) * (q[0] - o[0])
    lo, hi = [], []
    for p in pts:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], p) <= 0: lo.pop()
        lo.append(p)
    for p in reversed(pts):
        while len(hi) >= 2 and cross(hi[-2], hi[-1], p) <= 0: hi.pop()
        hi.append(p)
    return lo[:-1] + hi[:-1]


# split into the three shapes by empty columns, then the middle column band by rows
cols = a.any(axis=0)
bands, x = [], 0
while x < W:
    if cols[x]:
        x0 = x
        while x < W and cols[x]: x += 1
        bands.append((x0, x))
    x += 1
paths = []
for x0, x1 in bands:
    ys, xs = np.nonzero(a[:, x0:x1])
    edge = []  # boundary pixels only: leftmost/rightmost per row, top/bottom per column
    for y in np.unique(ys):
        row = xs[ys == y]; edge += [(row.min() + x0, y), (row.max() + x0 + 1, y), (row.min() + x0, y + 1), (row.max() + x0 + 1, y + 1)]
    h = hull(edge)
    paths.append("M" + " L".join(f"{px},{py}" for px, py in h) + " Z")
    print((x0, x1), len(h), "points")
order = [0, 2, 1]  # left bar, right bar, then the square
(HERE.parent / "assets/img/mark-paths.json").write_text(json.dumps({"w": W, "h": H, "paths": [paths[i] for i in order if i < len(paths)]}), encoding="utf-8")
