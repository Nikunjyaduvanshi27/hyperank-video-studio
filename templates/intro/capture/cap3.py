import base64, json
from pathlib import Path
from playwright.sync_api import sync_playwright
fam = {"SupremeRegular": ("Supreme-Regular", 400), "SupremeMedium": ("Supreme-Medium", 500), "SupremeLight": ("Supreme-Light", 300),
       "SupremeBold": ("Supreme-Bold", 600), "ReciaSemibold": ("Recia-Semibold", 600)}
css = "".join(f'@font-face{{font-family:{k};src:url(data:font/otf;base64,{base64.b64encode(Path("fonts/"+f+".otf").read_bytes()).decode()}) format("opentype");font-weight:{w}}}' for k, (f, w) in fam.items())
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=2)
    pg.goto("https://www.celebaltech.com/", wait_until="networkidle", timeout=120000)
    pg.add_style_tag(content=css)
    h = pg.evaluate("document.body.scrollHeight")
    for y in range(0, h, 500):
        pg.evaluate(f"window.scrollTo(0,{y})"); pg.wait_for_timeout(250)
    pg.evaluate("window.scrollTo(0,0)")
    pg.wait_for_timeout(3000)
    print(pg.evaluate("[...document.fonts].filter(f=>f.status=='loaded').map(f=>f.family).join(',')"))
    pg.screenshot(path="top.png")
    pg.screenshot(path="full.png", full_page=True)
    b.close()
