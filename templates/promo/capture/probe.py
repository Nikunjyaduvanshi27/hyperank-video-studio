from pathlib import Path
from playwright.sync_api import sync_playwright
HERE = Path(__file__).resolve().parent
H = HERE / "home"
CHROME = next((Path.home() / ".cache/hyperframes/chrome").rglob("chrome-headless-shell.exe"))
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=str(CHROME))
    pg = b.new_page(viewport={"width": 1440, "height": 900})
    pg.goto((H / "_render.html").as_uri(), wait_until="networkidle", timeout=90000)
    pg.wait_for_timeout(1200)
    print(pg.evaluate((HERE / "probe.js").read_text(encoding="utf-8")))
    b.close()
