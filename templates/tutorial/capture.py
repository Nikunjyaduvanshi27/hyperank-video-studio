"""Capture a hyperank.ai tool page (DOM, CSS, crops) and optionally run it once.

    python capture.py <tool-url> <out-dir>                 # probe: page only
    python capture.py <tool-url> <out-dir> VALUE [VALUE..]  # fill visible text fields in order, submit, save the result
    ... --then "Tab name"                                  # after the run, click that tab/button and save result-sec-2.html

Writes to <out-dir>: page.html, sec.html (the tool section), hyperank.css, controls.json, page-top.png,
and after a run: api.json (every JSON response from /api/), result-sec.html, result-text.txt, result-full.png,
result@2x.png (crisp crop of the result region). The site rate-limits anonymous runs: probe freely, run once.
"""
import json, re, sys, time
from pathlib import Path
from playwright.sync_api import sync_playwright

url, out = sys.argv[1], Path(sys.argv[2])
values = sys.argv[3:]
then = None
if "--then" in values:
    i = values.index("--then"); then = values[i + 1]; del values[i:i + 2]
out.mkdir(parents=True, exist_ok=True)
w = lambda name, s: (out / name).write_text(s, encoding="utf-8")

SECTION_JS = "() => { const f = document.querySelector('main form'); const s = f && (f.closest('section') || f.parentElement); return s ? s.outerHTML : ''; }"
CONTROLS_JS = """() => [...document.querySelectorAll('main input, main textarea, main select, main button')]
  .filter(e => e.offsetParent && e.type !== 'hidden')
  .map(e => ({tag: e.tagName, type: e.type, name: e.name, ph: e.placeholder || '', text: (e.innerText || '').slice(0, 60),
              label: (e.closest('label')?.innerText || '').split('\\n')[0], value: e.value, r: e.getBoundingClientRect().toJSON()}))"""

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=2)
    api = []

    def on_response(r):
        if "/api/" in r.url and "json" in (r.headers.get("content-type") or ""):
            try:
                api.append({"url": r.url, "status": r.status, "method": r.request.method,
                            "req": r.request.post_data, "body": r.json()})
            except Exception as e:  # streaming or empty body: keep the record, flag it
                api.append({"url": r.url, "status": r.status, "error": str(e)})
    pg.on("response", on_response)
    pg.goto(url, wait_until="networkidle", timeout=90000)
    pg.wait_for_timeout(1500)

    # page DOM, CSS (font faces stripped: the template ships local fonts), header, tool section
    w("page.html", pg.content())
    css = []
    for href in pg.eval_on_selector_all("link[rel=stylesheet]", "els => els.map(e => e.href)"):
        body = pg.request.get(href).text()
        css.append(f"/* source: {href} */\n" + re.sub(r"@font-face\{[^}]*\}", "", body))
    w("hyperank.css", "\n".join(css))
    w("sec.html", pg.evaluate(SECTION_JS))
    w("page-text.txt", pg.evaluate("() => document.querySelector('main').innerText"))
    controls = pg.evaluate(CONTROLS_JS)
    w("controls.json", json.dumps(controls, indent=1))
    pg.screenshot(path=str(out / "page-top.png"))
    print(json.dumps([{k: c[k] for k in ("tag", "type", "label", "ph", "text")} for c in controls], indent=0))

    if values:
        fields = pg.locator("main form input[type=text], main form input[type=url], main form input:not([type]), main form textarea")
        for i, v in enumerate(values):
            fields.nth(i).fill(v)
        api.clear()
        t0 = time.time()
        pg.locator("main form button[type=submit]").first.click()
        # done when the submit button is enabled again and the page has stopped growing
        last, stable = 0, 0
        for _ in range(180):
            pg.wait_for_timeout(1000)
            n = pg.evaluate("() => document.querySelector('main').innerText.length")
            busy = pg.evaluate("() => { const b = document.querySelector('main form button[type=submit]'); return !b || b.disabled || /ing\\b/i.test(b.innerText); }")
            stable = stable + 1 if (n == last and not busy) else 0
            last = n
            if stable >= 3:
                break
        print("run seconds", round(time.time() - t0, 1))
        w("api.json", json.dumps(api, indent=1))
        w("result-sec.html", pg.evaluate(SECTION_JS))
        w("result-text.txt", pg.evaluate("() => document.querySelector('main').innerText"))
        pg.screenshot(path=str(out / "result-full.png"), full_page=True)
        if then:
            pg.locator("main [aria-live]").get_by_text(then, exact=True).first.click()
            pg.wait_for_timeout(1200)
            w("result-sec-2.html", pg.evaluate(SECTION_JS))
            w("result-text-2.txt", pg.evaluate("() => document.querySelector('main [aria-live]').innerText"))
            pg.locator("main [aria-live]").first.screenshot(path=str(out / "result-2@2x.png"))
        region = pg.locator("main [aria-live]").first
        if region.count() and region.bounding_box():
            region.screenshot(path=str(out / "result@2x.png"))
    b.close()
