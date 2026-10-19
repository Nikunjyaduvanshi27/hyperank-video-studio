"""Render every site and app crop the film needs, for each cut in content/, with the film's text rules applied.

    python capture/capture.py      # -> assets/img/site/*.png and assets/img/site/rects.json

Site crops come from the local hyperank.ai capture (capture/home/_render.html). Before any screenshot: no Grok,
no engine count, no Pricing link, no em dashes, no mono labels (set in sentence-case Inter), and the cut's names and examples
(content/<cut>.json "site"). The Control Center is v2's rebuilt app screen (appkit.py in this folder) with the cut's brands
and numbers (content/<cut>.json "cc"). Lifted elements are shot alone on a transparent page so their glass and shadow keep alpha.
"""
import json, os, sys
from pathlib import Path
from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
V3 = HERE.parent
SRC = V3 / "capture/home/_render.html"
OUT = V3 / "assets/img/site"
CHROME = next((Path.home() / ".cache/hyperframes/chrome").rglob("chrome-headless-shell.exe"))
EDIT = (HERE / "edit.js").read_text(encoding="utf-8")
FIND = (HERE / "find.js").read_text(encoding="utf-8")
CCJS = (HERE / "cc.js").read_text(encoding="utf-8")
CUTS = {f.stem: json.loads(f.read_text(encoding="utf-8")) for f in (V3 / "content").glob("*.json")}
M = 28  # css px around a lifted element, so its own shadow survives


def page(b, scale, site=None):
    pg = b.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=scale)
    pg.goto(SRC.as_uri(), wait_until="networkidle", timeout=90000)
    pg.add_style_tag(content="*{animation:none !important;transition:none !important}")
    pg.wait_for_timeout(1200)
    pg.evaluate(EDIT, site or {})
    pg.wait_for_timeout(300)
    return pg


def lifted(b, scale, site, find, name, margin=0):
    """one element alone on a transparent page; returns its rect (css px) and the parts asked for"""
    pg = page(b, scale, site)
    pg.evaluate(FIND, ["mark", find])
    r = pg.evaluate(FIND, ["isolatePicked", None])
    pg.wait_for_timeout(300)
    pg.screenshot(path=str(OUT / name), omit_background=True, clip={"x": r["x"] - margin, "y": r["y"] - margin, "width": r["w"] + 2 * margin, "height": r["h"] + 2 * margin})
    pg.close()
    return r


def screen(b, site, head, name):
    """the laptop's view of a site section: sticky header kept, the section under it"""
    pg = page(b, 2, site)
    y = pg.evaluate(FIND, ["scrollTo", head])
    pg.wait_for_timeout(1500)
    pg.screenshot(path=str(OUT / name))
    return pg, y


def control_center(b, cut, C):
    """v2's Control Center rebuilt from the app source, re-branded for the cut, as a 2x laptop screen plus its share-of-voice card"""
    os.environ["PROMO_MAIN"] = str(V3)
    sys.path.insert(0, str(V3))
    import appkit  # appkit.py in the template root
    faces = "\n".join(l for l in (V3 / "src/stage.css").read_text(encoding="utf-8").splitlines() if l.startswith("@font-face")).replace("assets/", (V3 / "assets").as_uri() + "/")
    pg_html = appkit.screen_pg("cc", "control-center", on=True)
    doc = (f'<!doctype html><html><head><meta charset="utf-8"><style>{faces}\nhtml,body{{margin:0;background:#f4f3f0}}'
           f'.pg{{position:relative;width:1440px;height:900px;overflow:hidden}}.scroller{{position:absolute;left:0;top:0;transform:scale(1.125);transform-origin:0 0}}'
           f'{appkit.app_css(pg_html)}</style></head><body>{pg_html}</body></html>').replace('src="assets/', 'src="' + (V3 / "assets").as_uri() + "/")
    f = HERE / f"_cc-{cut}.html"
    f.write_text(doc, encoding="utf-8")
    shots = {}
    for scale, part in ((2, "screen"), (3, "sov")):
        pg = b.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=scale)
        pg.goto(f.as_uri(), wait_until="networkidle")
        pg.wait_for_timeout(1200)
        info = pg.evaluate(CCJS, C["cc"])
        if part == "screen":
            pg.screenshot(path=str(OUT / f"screen-cc-{cut}.png"))
            shots["screen-cc"] = info
        else:
            r = pg.evaluate("""() => { const el = document.querySelector('[data-m="sov"]');
              for (let a = el; a.parentElement; a = a.parentElement) { [...a.parentElement.children].forEach(x => { if (x !== a && x.tagName !== 'STYLE') x.style.opacity = '0'; });
                Object.assign(a.parentElement.style, { background: 'transparent', boxShadow: 'none', borderColor: 'transparent' }); }
              const q = el.getBoundingClientRect(); return { x: q.x, y: q.y, w: q.width, h: q.height }; }""")
            pg.screenshot(path=str(OUT / f"sov-{cut}.png"), omit_background=True, clip={"x": r["x"] - M, "y": r["y"] - M, "width": r["w"] + 2 * M, "height": r["h"] + 2 * M})
        pg.close()
    f.unlink()
    return shots


with sync_playwright() as p:
    b = p.chromium.launch(executable_path=str(CHROME))
    rects = {"shared": {}}

    # the first viewport (s07 screen) and the two engine chips that lift out of it, before and after
    pg = page(b, 2)
    pg.screenshot(path=str(OUT / "top.png"))
    rects["shared"]["top"] = pg.evaluate(FIND, ["chips", None])
    pg.close()
    for name in ("ChatGPT", "Claude"):
        for suffix in ("", "-you"):
            pg = page(b, 4)
            if suffix:
                pg.evaluate(FIND, ["chipYou", name])
            r = pg.evaluate(FIND, ["isolate", name])
            pg.wait_for_timeout(300)
            pg.screenshot(path=str(OUT / f"chip-{name.lower()}{suffix}.png"), omit_background=True, clip={"x": r["x"] - M, "y": r["y"] - M, "width": r["w"] + 2 * M, "height": r["h"] + 2 * M})
            pg.close()
    # the publishing destinations (s12), one card each
    for nm in ("WordPress", "Webflow", "Ghost", "Shopify"):
        rects["shared"]["int-" + nm.lower()] = lifted(b, 3, {}, [nm, 150], f"int-{nm.lower()}.png", M)

    for cut, C in CUTS.items():
        S = C["site"]
        R = rects[cut] = {}
        # s10: the sources section and its table
        pg, y = screen(b, S, "Fix the sources, not the symptoms", f"screen-sources-{cut}.png")
        R["screen-sources"] = {"scrollY": y, **pg.evaluate(FIND, ["box", "Sources deciding the answer"])}
        pg.close()
        pg = page(b, 3, S)
        print(cut, "source icons:", pg.evaluate(FIND, ["icons", "Sources deciding the answer"]))
        R["sources-table"] = pg.evaluate(FIND, ["parts", "Sources deciding the answer"])
        r = pg.evaluate(FIND, ["isolate", "table"])
        pg.wait_for_timeout(200)
        pg.screenshot(path=str(OUT / f"sources-table-{cut}.png"), omit_background=True, clip={"x": r["x"], "y": r["y"], "width": r["w"], "height": r["h"]})
        pg.close()
        # s08: every answer kept, and the tracked prompts card
        pg, y = screen(b, S, "Every answer, kept word for word", f"screen-answers-{cut}.png")
        R["screen-answers"] = pg.evaluate(FIND, ["mark", ["Tracked prompts", 400]])
        pg.close()
        R["tracked"] = lifted(b, 3, S, ["Tracked prompts", 400], f"tracked-{cut}.png", M)
        # s11: the content engine and its publish list
        pg, y = screen(b, S, "Make the sources you are missing", f"screen-content-{cut}.png")
        R["screen-content"] = pg.evaluate(FIND, ["mark", ["Content", 400]])
        pg.close()
        # s15: the traffic AI sends you, and the referrals card
        pg, y = screen(b, S, "The traffic AI sends you, separated from the traffic it does not", f"screen-analytics-{cut}.png")
        R["screen-analytics"] = pg.evaluate(FIND, ["mark", ["AI referrals", 400]])
        pg.close()
        R["referrals"] = lifted(b, 3, S, ["AI referrals", 400], f"referrals-{cut}.png", M)
        pg = page(b, 3, S)
        pg.evaluate(FIND, ["mark", ["AI referrals", 400]])
        R["referral-parts"] = pg.evaluate(FIND, ["partsOf", ["ChatGPT", "Perplexity", "Gemini", "Claude", "1,284", "612", "341", "208"]])
        pg.close()
        # s09: the Control Center for yourbrand.com
        R.update(control_center(b, cut, C))

    (OUT / "rects.json").write_text(json.dumps(rects, indent=1), encoding="utf-8")
    print(json.dumps({k: list(v) for k, v in rects.items()}, indent=1))
    b.close()
