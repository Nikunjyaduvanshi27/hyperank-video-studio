import json
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=2)
    pg.goto("https://www.celebaltech.com/", wait_until="networkidle", timeout=120000)
    h = pg.evaluate("document.body.scrollHeight")
    for y in range(0, h, 500):
        pg.evaluate(f"window.scrollTo(0,{y})"); pg.wait_for_timeout(300)
    pg.evaluate("window.scrollTo(0,0)")
    pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(4000)
    print("fonts", pg.evaluate("[...document.fonts].filter(f=>f.status=='loaded').map(f=>f.family).join(',')"))
    rects = pg.evaluate("""() => {
      const out = {};
      const byText = (t) => [...document.querySelectorAll('h1,h2,h3,h4,p,span,div,button,a')].filter(e => e.innerText && e.innerText.trim() === t && e.offsetParent);
      for (const t of ['Our Valued Partners','Our Industry Expertise','Awards & Recognitions','Our Distinctive Strengths','Insights & Resources','Generative AI','Enterprise Data Analytics','Migrations & Lakehouse','Industry Data Model','Trusted Partnerships','Service Partners','Solution Partners','Become a client','Talk to us']) {
        const e = byText(t)[0]; if (!e) continue;
        const r = e.getBoundingClientRect(); out[t] = [r.x, r.y + scrollY, r.width, r.height];
        let s = e.closest('section'); if (s) { const q = s.getBoundingClientRect(); out[t + ' §'] = [q.x, q.y + scrollY, q.width, q.height]; }
      }
      const h1 = document.querySelector('h1'); if (h1) { const r = h1.getBoundingClientRect(); out.h1 = [r.x, r.y + scrollY, r.width, r.height]; }
      const hd = document.querySelector('header, nav'); if (hd) { const r = hd.getBoundingClientRect(); out.header = [r.x, r.y, r.width, r.height]; }
      out.H = document.body.scrollHeight;
      return out; }""")
    json.dump(rects, open("rects.json", "w"), indent=1)
    print(json.dumps(rects, indent=0))
    pg.screenshot(path="full.png", full_page=True)
    pg.screenshot(path="top.png")
    b.close()
