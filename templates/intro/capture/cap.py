import json, sys
from pathlib import Path
from playwright.sync_api import sync_playwright
out = Path(".")
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=2)
    pg.goto("https://www.celebaltech.com/", wait_until="domcontentloaded", timeout=90000)
    pg.wait_for_timeout(6000)
    # trigger lazy content
    h = pg.evaluate("document.body.scrollHeight")
    for y in range(0, h, 600):
        pg.evaluate(f"window.scrollTo(0,{y})"); pg.wait_for_timeout(250)
    pg.evaluate("window.scrollTo(0,0)"); pg.wait_for_timeout(2000)
    (out/"page.html").write_text(pg.content(), encoding="utf-8")
    (out/"text.txt").write_text(pg.evaluate("document.body.innerText"), encoding="utf-8")
    pg.screenshot(path="top.png")
    pg.screenshot(path="full.png", full_page=True)
    imgs = pg.evaluate("""[...document.images].map(i=>({src:i.currentSrc||i.src,alt:i.alt,w:i.naturalWidth,h:i.naturalHeight,y:Math.round(i.getBoundingClientRect().top+scrollY)}))""")
    (out/"images.json").write_text(json.dumps(imgs, indent=1), encoding="utf-8")
    meta = pg.evaluate("""({title:document.title, desc:document.querySelector('meta[name=description]')?.content, h:document.body.scrollHeight,
      fonts:[...new Set([...document.querySelectorAll('h1,h2,h3,p,a,button')].map(e=>getComputedStyle(e).fontFamily))].slice(0,8),
      colors:[...new Set([...document.querySelectorAll('h1,h2,a,button,header,section')].map(e=>getComputedStyle(e).color+' | '+getComputedStyle(e).backgroundColor))].slice(0,25),
      svgs:[...document.querySelectorAll('header svg, header img')].map(e=>e.outerHTML.slice(0,300))})""")
    (out/"meta.json").write_text(json.dumps(meta, indent=1), encoding="utf-8")
    print(json.dumps(meta, indent=1)[:3000])
    b.close()
