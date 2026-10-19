"""Render the captured hyperank.ai homepage at 2x and save the first viewport, to choose screen content."""
from pathlib import Path
from playwright.sync_api import sync_playwright
H = Path(__file__).resolve().parent / "home"
CHROME = next((Path.home() / ".cache/hyperframes/chrome").rglob("chrome-headless-shell.exe"))
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=str(CHROME))
    pg = b.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=1)
    pg.goto((H / "_render.html").as_uri(), wait_until="networkidle", timeout=90000)
    pg.add_style_tag(content="*{animation:none !important;transition:none !important}")
    pg.wait_for_timeout(1500)
    pg.screenshot(path=str(Path(__file__).parent / "peek-top.png"))
    print(pg.evaluate("() => [...document.querySelectorAll('h1,h2')].slice(0,6).map(h => h.textContent.trim() + ' @' + Math.round(h.getBoundingClientRect().top + scrollY))"))
    b.close()
