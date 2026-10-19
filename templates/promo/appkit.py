"""App-screen kit for the promo: the real hyperank shell (dock, section column, top bar, page header) wrapped around
screens rebuilt from the app source as static HTML partials in src/screens/*.html.

A partial starts with a JSON header comment, then the markup that goes inside the page's `.rk` region:
    <!-- {"section": "ai-visibility", "active": "Competitors"} -->
    <header class="hpr-pagehead">...</header> ...
`data-m="name"` attributes in the markup are the marks the scene scripts (stage.js) point the camera, cursor and lifts at.
The shell, the CSS and the fonts are the app's own (capture/app/*.css, copied from app.hyperank.ai), so a screen reads as the real app.
"""
import html, json, os, re
from pathlib import Path
from bs4 import BeautifulSoup

HERE = Path(__file__).resolve().parent
MAIN = Path(os.environ.get("PROMO_MAIN", HERE))  # scene work copies (_wk/*) read the shared capture, lucide icons and screens from the main project
CAP = MAIN / "capture"
BRAND, DOMAIN, ORG = "Lumen", "lumenhq.com", "Lumen"
Z = 1.125  # screens are authored at a 1280 px viewport and shown 1.125x on the 1440 x 900 laptop screen

# dock order and the side column of each nested section (lib/*-nav-items.ts)
DOCK = {"control-center": ("Control Center", 1, None), "brand": ("Brand Hub", 2, None), "ai-visibility": ("AI Visibility", 3, "ai-visibility"),
        "content": ("Article", 4, "content"), "reddit": ("Reddit Agent", 5, "reddit"), "social": ("LinkedIn Agent", 6, "social"),
        "analytics": ("Analytics", 8, "analytics"), "reports": ("Reports", 10, None)}
SIDE = {
    "ai-visibility": [("AI Readiness", "bot"), ("Brand Visibility", "zap"), ("Prompts Monitor", "speech"), ("Competitors", "swords"), ("Query Fanout", "git-branch"),
                      ("Citations", "book-marked"), ("Sentiments", "heart"), ("Hallucinations", "shield-alert"), ("Configurations", "sliders-horizontal")],
    "content": [("Statistics", "notebook-text"), ("Writer", "pen-line"), ("Opportunities", "siren"), ("Auto-Pilot", "calendar"), ("Connectors", "cable"), ("Syndication", "share-2")],
    "reddit": [("Overview", "layout-grid"), ("Inbox", "inbox"), ("Writer", "pen-line"), ("Opportunities", "sparkles"), ("Monitors", "activity")],
    "social": [("Overview", "notebook-text"), ("Writer", "pen-line"), ("Studio", "image"), ("Opportunities", "siren"), ("Calendar", "calendar"), ("Accounts", "cable")],
    "analytics": [("Search Traffic", "search"), ("AI Citations", "file-text"), ("AI Traffic", "bot"), ("LinkedIn Traffic", "linkedin"), ("Leads", "users")],
}


def icon(name: str, size: int = 16, cls: str = "", sw: float = 2, style: str = "") -> str:
    """A lucide icon (capture/lucide, lucide-static 0.468) inlined at `size` px."""
    svg = (CAP / "lucide" / f"{name}.svg").read_text(encoding="utf-8")
    svg = re.sub(r"<!--.*?-->\s*", "", svg, flags=re.S)
    svg = re.sub(r'class="[^"]*"', f'class="lucide lucide-{name} {cls}"', svg, count=1)
    svg = re.sub(r'width="24"', f'width="{size}"', svg, count=1)
    svg = re.sub(r'height="24"', f'height="{size}"' + (f' style="{style}"' if style else ""), svg, count=1)
    svg = svg.replace('stroke-width="2"', f'stroke-width="{sw}"')
    return re.sub(r"\s+", " ", svg).replace("> <", "><").strip()


def _skin() -> BeautifulSoup:
    s = BeautifulSoup((CAP / "v26/readiness.html").read_text(encoding="utf-8"), "html.parser")
    skin = s.select_one("div.hpr-skin")
    for t in skin(["script", "noscript", "iframe", "style", "link"]):
        t.decompose()
    for t in skin.select("nav.hpr-mobnav"):
        t.decompose()
    for img in skin.find_all("img"):
        src = img.get("src", "")
        if "hyperank-logo" in src:
            img["src"] = "assets/img/hyperank-logo.png"
            for a in ("srcset", "style"):
                img.attrs.pop(a, None)
        elif "duckduckgo" in src:
            img["src"] = "assets/img/lumen-mark.svg"
        else:
            img.replace_with(BeautifulSoup('<span class="rounded-full relative flex shrink-0 items-center justify-center size-8" style="background:#2f7d6b;color:#fff;font-size:14px;font-weight:600">L</span>', "html.parser"))
    for t in skin.find_all(True):
        for a in ("href", "id", "aria-controls", "aria-labelledby", "aria-describedby", "for", "srcset"):
            t.attrs.pop(a, None)
        if t.get("class"):  # no browser-clock motion: every state change is on the timeline
            t["class"] = [c for c in t["class"] if not c.startswith(("transition", "duration-", "animate-"))]
    return skin


def shell(meta: dict, content: str) -> str:
    """The app chrome for one section/page with `content` inside .rk."""
    skin = _skin()
    key = meta.get("section", "ai-visibility")
    title, idx, side = DOCK[key]
    dock = skin.select_one("nav.hpr-dock")
    for a in dock.select("a.hpr-dock-item"):
        a.attrs.pop("aria-current", None)
        a["class"] = [c for c in a["class"] if c != "is-active"]
        if a.get("title") == title:
            a["class"].append("is-active"); a["aria-current"] = "page"
    dock["style"] = f"--bubble-y: {8 + 45 * idx}px; --glide-from: 8px; --glide-to: 413px;"
    aside = skin.select_one("aside.hpr-side")
    if side is None:
        aside.decompose()
    else:
        aside["aria-label"] = f"{title} pages"
        skin.select_one(".hpr-side-heading").string = title
        skin.select_one(".hpr-side-switch-label").string = BRAND
        lst = skin.select_one(".hpr-section-list")
        lst.clear()
        items = "".join(
            f'<a class="hpr-side-item{" is-active" if lab == meta.get("active") else ""}">{icon(ic, 16, "size-4 shrink-0", 1.7)}<span class="truncate">{lab}</span></a>'
            for lab, ic in SIDE[side])
        lst.append(BeautifulSoup(items, "html.parser"))
    top = skin.select_one(".hpr-sheet-top")
    for sp in top.select("span.truncate"):
        if sp.get_text(strip=True) == "hyperank.ai":
            sp.string = DOMAIN
    for sp in top.find_all("span"):
        if "Organization" in sp.get_text():
            sp.clear(); sp.append(f"Viewing {ORG}'s Organization")
    rk = skin.select_one(".rk")
    rk.clear()
    rk.append("@@CONTENT@@")
    out = str(skin).replace("&amp;", "&").replace("@@CONTENT@@", content).replace("—", "&#8212;")
    return out.replace("viewbox=", "viewBox=")


def load_partial(name: str):
    raw = (MAIN / "src/screens" / f"{name}.html").read_text(encoding="utf-8")
    m = re.match(r"\s*<!--(.*?)-->(.*)$", raw, re.S)
    return json.loads(m.group(1)), m.group(2)


def screen_pg(key: str, name: str, z: float = Z, on: bool = False) -> str:
    """The `.pg` page block stage.js expects: one scroller at its own zoom holding the whole app screen."""
    meta, body = load_partial(name)
    return (f'<div class="pg" data-page="{key}"{" data-on" if on else ""}><div class="scroller" data-z="{z}" style="width: {round(1440 / z)}px">'
            f'<div class="font-sans antialiased __variable_f367f3 __variable_9cf113 __variable_1f5468">{shell(meta, body)}</div></div></div>')


# ---------- the app stylesheet: captured sheets + the control-center sheets, cleaned and purged to the classes in use ----------
def _purge(text: str, used: set) -> str:
    """Keep only rules whose class selectors all occur in the film's markup (the full sheet makes lint take minutes)."""
    out, i, n = [], 0, len(text)
    while i < n:
        j = text.find("{", i)
        if j < 0:
            break
        pre = text[i:j].strip()
        depth, k = 1, j + 1
        while depth and k < n:
            depth += {"{": 1, "}": -1}.get(text[k], 0); k += 1
        body = text[j + 1:k - 1]
        if pre.startswith(("@keyframes", "@-webkit-keyframes", "@font-face")):
            pass
        elif pre.startswith("@"):
            inner = _purge(body, used)
            if inner:
                out.append(pre + "{" + inner + "}")
        else:
            keep = []
            for sel in re.split(r",(?![^(]*\))", pre):
                s2 = re.sub(r":(not|is|where|has)\([^()]*\)", "", re.sub(r"(?<!\\)\[[^\]]*?(?<!\\)\]", "", sel))
                cls = {re.sub(r"\\(.)", r"\1", c) for c in re.findall(r"\.((?:\\.|[\w-])+)", s2)}
                if cls <= used:
                    keep.append(sel)
            if keep:
                out.append(",".join(keep) + "{" + body + "}")
        i = k
    return "".join(out)


EXTRA_CSS = ["control-center.css", "control-center-charts.css", "control-center-tiered.css"] + sorted(p.name for p in (CAP / "app").glob("x-*.css"))


def app_css(markup: str) -> str:
    css = "\n".join((CAP / "app" / f"app-{i}.css").read_text(encoding="utf-8") for i in range(1, 6))
    assert all((CAP / "app" / f"app-{i}.css").stat().st_size > 1000 for i in range(1, 6)), "an app stylesheet is empty"
    css += "\n" + "\n".join((CAP / "app" / f).read_text(encoding="utf-8") for f in EXTRA_CSS)
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"@font-face\{[^}]*\}", "", css)  # faces ship locally (stage.css), never from the app's CDN
    css = re.sub(r"(?<![-\w])(transition|animation)(-[a-z-]+)?:[^;}]*;?", "", css)  # every state change is on the timeline
    used = {c for v in re.findall(r'class="([^"]*)"', markup) for c in html.unescape(v).split()}
    return _purge(css, used)
