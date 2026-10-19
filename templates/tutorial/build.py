"""Build one premium tutorial composition from tool.json + the capture + the voice files.

    python build.py tools/<slug>       # writes tools/<slug>/premium/index.html (run tts_batch.py first)

Voice drives time: every beat starts when the last one's line has been said (or its action needs longer),
and every SFX cue is placed on the same clock as the action it belongs to.
"""
import html, json, re, shutil, subprocess, sys
from pathlib import Path
from bs4 import BeautifulSoup

HERE = Path(__file__).resolve().parent
REF = HERE / "shared"  # the approved v3: fonts, SFX, logos, music bed, project boilerplate
prem = (Path(sys.argv[1]) / "premium").resolve()
T = json.loads((prem / "tool.json").read_text(encoding="utf-8"))

GAP_LVL, DUCK_LVL = 0.158, 0.0708  # music bed about -26 LUFS between lines, 7 dB under the voice
KEYS = ["keypress-%03d.wav" % k for k in (3, 7, 11, 14, 18, 21, 25, 27, 30, 32)]
GAPS = [0.09, 0.08, 0.1, 0.075, 0.09, 0.11, 0.085, 0.07, 0.095, 0.08]
ENGINE_IMG = {"chatgpt": "chatgpt.svg", "gemini": "gemini.svg", "perplexity": "perplexity.svg", "claude": "claude.svg",
              "grok": "grok.svg", "google": "google-ai-overviews.png"}


def dur(f: Path) -> float:
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)]).decode())


# ---------- project scaffold and shared assets ----------
for d in ("fonts", "img", "audio/sfx"):
    shutil.copytree(REF / "assets" / d, prem / "assets" / d, dirs_exist_ok=True)
shutil.copy(REF / "assets/audio/music-bed.mp3", prem / "assets/audio/music-bed.mp3")
for f in ("hyperframes.json", "package.json", "CLAUDE.md", "AGENTS.md"):
    shutil.copy(REF / f, prem / f)
(prem / "meta.json").write_text(json.dumps({"id": prem.parent.name + "-premium", "name": prem.parent.name + "-premium"}), encoding="utf-8")
shutil.copy(prem / T["css"], prem / "assets/hyperank.css")

# ---------- the page: live markup, result from the recorded run ----------
soup = BeautifulSoup((prem / T["result"]).read_text(encoding="utf-8"), "html.parser")
sec = soup.find("section")
sec["class"] = sec.get("class", []) + ["sec"]
for t in soup.find_all(True):
    for a in ("href", "data-gtm-form-interact-id", "data-gtm-form-interact-field-id", "aria-describedby"):
        t.attrs.pop(a, None)
    st = t.get("style", "")
    if "filter: blur(0px)" in st or "transform: none" in st or st.startswith("opacity: 1"):
        del t["style"]
    if t.get("class"):  # no browser-clock transitions: every state change is on the timeline
        t["class"] = [c for c in t["class"] if c != "backdrop-blur-2xl" and not c.startswith(("transition", "duration-"))]
form = soup.find("form")
form["style"] = "background: rgba(255, 255, 255, 0.72)"
fields = form.find_all(lambda t: t.name == "textarea" or (t.name == "input" and t.get("type", "text") in ("text", "url")))
for n, (inp, val) in enumerate(zip(fields, T["inputs"]), 1):
    ph = inp.get("placeholder", "")
    lab = inp.find_parent("label") or inp.parent
    lab["id"] = f"f{n}"
    tall = inp.name == "textarea"
    box = BeautifulSoup(
        f'<div class="inwrap"><div id="in{n}" class="inbox min-h-12 w-full rounded-xl bg-white/70 px-4 text-[15px] font-medium text-neutral-900 ring-1 ring-line-strong ring-inset"'
        + (' style="height: auto; min-height: 96px; align-items: flex-start; padding-top: 13px"' if tall else "") + ">"
        f'<span id="typed{n}" class="typed">' + "".join(f"<span>{html.escape(c)}</span>" for c in val) + "</span></div>"
        f'<span id="ph{n}" class="ph">{html.escape(ph)}</span><i id="caret{n}" class="caret"></i></div>', "html.parser")
    inp.replace_with(box)
btn = form.find("button", attrs={"type": "submit"})
btn["type"], btn["id"] = "button", "btn"
btn["style"] = "white-space: nowrap"
btn.insert(0, BeautifulSoup('<span id="spin" class="spin"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M21 12a9 9 0 1 1-6.219-8.56"></path></svg></span>', "html.parser"))
res = soup.find(attrs={"aria-live": True})
res["id"] = "res"
del res["aria-live"]


def find_text(root, text: str, nth: int = 0, contains: bool = False):
    match = (lambda t: text in t.get_text(" ", strip=True)) if contains else (lambda t: t.get_text(" ", strip=True) == text)
    hits = [t for t in root.find_all(True) if match(t)]
    hits = [t for t in hits if not any(match(c) for c in t.find_all(True))]  # innermost
    if len(hits) <= nth:
        sys.exit(f"mark not found: {text!r}")
    return hits[nth]


# chips toggled during input (e.g. engines to simulate): id them, borrow the pressed look from a pressed sibling
toggles = []
for i, txt in enumerate(T.get("toggles", [])):
    b = find_text(form, txt)
    b = b if b.name == "button" else b.find_parent("button")
    on = next(x for x in form.find_all("button", attrs={"aria-pressed": "true"}) if x is not b)
    off = next(x for x in form.find_all("button", attrs={"aria-pressed": "false"}) if x is not b)
    b["id"], b["class"] = f"chip{i}", off["class"]  # starts unpressed, as on the live page
    toggles.append((f"chip{i}", " ".join(c for c in on["class"] if not c.startswith(("transition", "duration-")))))
# a second page state after a tab click: its panel goes in hidden, the tabs swap their looks
show_ops = {}
if "tab" in T:
    s2 = BeautifulSoup((prem / T["tab"]["result"]).read_text(encoding="utf-8"), "html.parser")
    p1, p2 = res.find(attrs={"role": "tabpanel"}), s2.find(attrs={"role": "tabpanel"})
    p1["id"], p2["id"] = "panel1", "panel2"
    p2["class"] = p2.get("class", []) + ["hide0", "over"]  # laid over panel 1, so nothing on the page moves
    p1.parent["style"] = "position: relative"
    p1.insert_after(p2)
    tabs1, tabs2 = res.find_all(attrs={"role": "tab"}), s2.find_all(attrs={"role": "tab"})
    cls = []
    for k, (a, b) in enumerate(zip(tabs1, tabs2)):
        a["id"] = f"tab{k}"
        cls.append([f"tab{k}", " ".join(c for c in b["class"] if not c.startswith(("transition", "duration-")))])
        if T["tab"]["name"] in a.get_text():
            show_ops["tab"] = {"target": f"tab{k}"}
    show_ops["tab"].update({"show": ["panel2"], "hide": ["panel1"], "cls": cls})
# a collapsed section opened at a beat (e.g. <details>): kept open, its body hidden until then
for i, txt in enumerate(T.get("open", [])):
    det = find_text(res, txt).find_parent("details")
    det["open"] = ""
    body = det.find("summary").find_next_sibling()
    body["id"] = f"open{i}"
    body["class"] = body.get("class", []) + ["hide0"]
    det.find("summary")["id"] = f"sum{i}"
    show_ops[f"open:{txt}"] = {"target": f"sum{i}", "show": [f"open{i}"]}
# the anonymous gate: the real card from the logged-out page, shown over the blurred report until "unlock"
gate_html = ""
if T.get("gate"):
    g = BeautifulSoup((prem / T["gate"]).read_text(encoding="utf-8"), "html.parser")
    card = find_text(g, "Your results are ready").find_parent("div")
    card["id"] = "gateCard"
    card["style"] = "width: 400px"
    card.find("button")["id"] = "unlock"
    gate_html = f'<div id="gateWrap">{card}</div>'
# lines inside a <pre> (a fetched file) that a beat points at: wrapped in a block span so they can lift out
for name, text in T.get("spans", {}).items():
    pre = next(p for p in res.find_all("pre") if text in p.get_text())
    body = pre.decode_contents()
    i = body.index(html.escape(text, quote=False))
    pre.clear()
    pre.append(BeautifulSoup(body[:i] + f'<span id="{name}" style="display: block">{html.escape(text, quote=False)}</span>' + body[i + len(html.escape(text, quote=False)):].lstrip(chr(10)), "html.parser"))
# named marks: the result parts the beats point at
alias = {}
for name, m in T.get("marks", {}).items():
    t = find_text(soup if m.get("anywhere") else res, m["text"], m.get("nth", 0), m.get("contains", False))
    for _ in range(m.get("up", 0)):
        t = t.parent
    if t.get("id"):  # already named (a tab panel, a summary): point the mark at that id
        alias[name] = t["id"]
    else:
        t["id"] = name
header = (HERE / "header.html").read_text(encoding="utf-8").strip()
page = str(soup).replace("—", "&#8212;")  # the live UI's own dashes stay as rendered

# ---------- timing: voice decides it ----------
beats = T["beats"]
vo = [dur(prem / f"assets/audio/vo/vo-{i + 1:02d}.wav") for i in range(len(beats))]
acts, sfx, supers, subs, vo_at, starts = [], [], [], [], [], []


def A(op: str, t: float, **k) -> None:
    acts.append({"op": op, "t": round(t, 3), **{a: (round(b, 3) if isinstance(b, float) else b) for a, b in k.items()}})


def X(f: str, t: float, v: float) -> None:
    sfx.append((f, round(t, 3), v))


def cursor_click(t: float, target: str, travel: float = 0.7, fx: float = 0.3, fy: float = 0.55) -> float:
    A("cursorTo", t, target=target, dur=travel, fx=fx, fy=fy)
    c = t + travel + 0.05
    A("click", c)
    return c


T0, spin_from, fine_from = 0.0, None, None
for i, b in enumerate(beats):
    kind, d = b["type"], vo[i]
    lead = b.get("lead", 0.3 if i == 0 else 0.22)
    s = T0 + lead
    need = lead + d + 0.28
    if kind == "hook":
        A("cam", 0, to="WIDE1", dur=1.9, ease="sine.inOut")
        A("bug", 0.1, t1=1.75)
        if T.get("engines"):
            A("engines", 0.15, t1=max(2.0, s + d + 0.1))
        A("streak", 0.3)
        X("impactSoft_medium_001.ogg", 0.3, 0.45); X("whoosh-soft.wav", 0.2, 0.35)
        need = max(need, 2.0)
    elif kind == "name":
        A("cam", T0 - 0.1, to="HOLD", dur=1.1)
        A("eyebrow", T0 + 0.05, t1=T0 + need - 0.2)
        X("whoosh-soft.wav", T0 - 0.2, 0.35)
    elif kind == "type":
        n_in = len(T["inputs"])
        A("cam", T0 - 0.05, to="INPUT:" + ":".join(f"f{k}" for k in range(1, n_in + 1)), dur=1.0)
        A("veils", T0, v=1)
        X("whoosh-soft.wav", T0 - 0.1, 0.35)
        A("cursorShow", T0, v=1)
        t = T0 + 0.05
        for n, val in enumerate(T["inputs"], 1):
            c = cursor_click(t, f"in{n}", 0.75 if n == 1 else 0.3)
            A("focus", c, target=f"in{n}", n=n, on=True)
            X("click2.ogg", c, 0.5)
            k = c + 0.15
            times = []
            for j in range(len(val)):
                times.append(round(k, 3)); X(KEYS[(j + n * 3) % 10], k, 0.55); k += GAPS[j % 10]
            A("type", times[0], n=n, times=times)
            if n < n_in:
                A("focus", k + 0.05, target=f"in{n}", n=n, on=False)
            t = k + 0.05
        for tid, cls in toggles:
            c = cursor_click(t + 0.1, tid, 0.55, 0.5, 0.5)
            A("toggle", c, target=tid, cls=cls)
            X("mouseclick1.ogg", c, 0.55)
            t = c + 0.1
        A("cursorTo", t, target=f"in{n_in}", dur=0.4, fx=0.55, fy=1.4)
        need = max(need, t - T0 + 0.5)
    elif kind == "press":
        A("cam", T0, to=f"PRESS:f1:btn", dur=0.8)
        P = cursor_click(T0 + 0.1, "btn", 0.7, 0.45, 0.55)
        A("focus", P, target=f"in{len(T['inputs'])}", n=len(T["inputs"]), on=False)
        X("mouseclick1.ogg", P, 0.55)
        spin_from, fine_from = P, P + 0.15
        A("cursorShow", P + 0.6, v=0)
        need = max(need, P - T0 + 0.9)
    elif kind == "fan":
        A("cam", T0, to="MED", dur=0.95)
        A("veils", T0 + 0.55, v=0, dur=0.45)  # page text stays veiled while the camera pulls out
        A("screenFx", T0 + 0.2, blur=6, dim=0.4)
        X("whoosh-soft.wav", T0 - 0.05, 0.35)
        n = len(b["items"])
        need = max(need, 0.35 + n * min(0.42, 2.0 / n) + 2.2)
        A("fan", T0, t0=T0, t1=T0 + need)
        for j in range(n):
            X("rollover2.ogg", T0 + 0.35 + j * min(0.42, 2.0 / n), 0.22)
        X("bong_001.ogg", T0 + need - 1.5, 0.25)
    elif kind in ("gate", "result"):
        A("cam", T0, to="HOLD", dur=1.0)
        A("veils", T0 + 0.55, v=0, dur=0.45)
        if beats[i - 1]["type"] == "fan":
            A("screenFx", T0 + 0.1, blur=0, dim=0)
        elif kind == "gate":  # straight from the zoomed white form: a short dim keeps the cut off near-white
            A("dim", T0 - 0.15, v=0.2, dur=0.15)
            A("dim", T0 + 0.7, v=0, dur=0.4)
        A("scroll", T0 + (0.0 if kind == "gate" else 0.1), to="res", top=b.get("top", 70), dur=0.05 if kind == "gate" else 0.9)
        R = T0 + (0.15 if kind == "gate" else 0.5)
        A("reveal", R, sel=b.get("stagger"))
        A("press", spin_from, t1=R)
        A("fine", fine_from, t1=R)
        X("bong_001.ogg", R + 0.05, 0.35)
        X("whoosh-soft.wav", T0, 0.3)
        if kind == "gate":
            A("cursorTo", T0 + 0.5, target="unlock", dur=0.01, fx=0.95, fy=2.4)
            A("cursorShow", T0 + 0.55, v=1)
            U = cursor_click(T0 + 0.6, "unlock", 0.8, 0.45, 0.55)
            A("gate", T0 + 0.1, t1=U)
            A("cursorShow", U + 0.25, v=0)
            X("mouseclick1.ogg", U, 0.55); X("bong_001.ogg", U + 0.3, 0.3)
            need = max(need, U - T0 + 0.8)
        elif b.get("push"):
            A("cam", T0 + 1.0, to="PUSH:" + b["push"], dur=1.0)
            A("veils", T0 + 1.0, v=1)
            X("whoosh-soft.wav", T0 + 0.95, 0.3)
            need = max(need, 3.2)
            A("cam", T0 + need - 0.9, to="HOLD", dur=0.9)
            A("veils", T0 + need - 0.4, v=0, dur=0.4)
            X("whoosh-soft.wav", T0 + need - 0.95, 0.25)
    elif kind == "read":
        t = T0
        lifts = b.get("lifts", [])
        if b.get("scroll"):  # bring a part of the page into view before acting on it
            A("scroll", t, to=b["scroll"], top=b.get("top", 300), dur=0.8)
            X("whoosh-soft.wav", t, 0.25)
            t += 0.85
        if b.get("click"):  # a tab or a section the viewer sees us open
            op = show_ops[b["click"]]
            A("cursorShow", t, v=1)
            c = cursor_click(t + 0.05, op["target"], 0.6, 0.5, 0.5)
            A("show", c, **{k: v for k, v in op.items() if k != "target"})
            A("cursorShow", c + 0.35, v=0)
            X("mouseclick1.ogg", c, 0.55)
            t = c + 0.25
        anchor = lifts[0]["mark"] if lifts else b.get("push")
        if anchor and (b.get("click") or not b.get("scroll")):
            A("scroll", t, to=anchor, top=b.get("liftTop", 380 if b.get("push") else 300), dur=0.8)
            X("whoosh-soft.wav", t, 0.25)
            t += 0.85
        if b.get("push"):  # after the scroll has landed, so the frame is measured on the scrolled page
            A("cam", t, to="PUSH:" + b["push"], dur=0.95)
            A("veils", t + 0.05, v=1)
            X("whoosh-soft.wav", t - 0.05, 0.3)
            need = max(need, t - T0 + 2.8)
            A("cam", T0 + need - 0.85, to="HOLD", dur=0.85)
            A("veils", T0 + need - 0.4, v=0, dur=0.4)
        if lifts:
            need = max(need, t - T0 + 2.2)
            end = T0 + need
            A("dim", t - 0.05, v=0.22)
            seq = b.get("seq", False)
            for j, L in enumerate(lifts):
                if seq:
                    span = (end - t) / len(lifts)
                    a0, a1, slot, nn = t + j * span, t + (j + 1) * span - 0.05, 0, 1
                else:
                    a0, a1, slot, nn = t + j * 0.25, end - 0.1, j, len(lifts)
                A("lift", a0, t0=a0, t1=a1, mark=L["mark"], label=L.get("label"), slot=slot, n=nn,
                  **{k: L[k] for k in ("scale", "maxW", "maxH", "cy", "fit") if k in L})
                X("impactSoft_medium_004.ogg" if j == 0 else "rollover2.ogg", a0 + 0.05, 0.4 if j == 0 else 0.25)
            A("dim", end - 0.45, v=0)
    elif kind == "close":
        E = T0
        A("veils", E, v=0, dur=0.4)
        A("end", E)
        X("whoosh-soft.wav", E - 0.05, 0.4); X("impactSoft_medium_001.ogg", E + 0.1, 0.45); X("bong_001.ogg", E + 1.3, 0.3)
        need = max(lead + d + 0.6, 2.8)
    vo_at.append((round(s, 3), vo[i]))
    starts.append(round(T0, 2))
    if b.get("super"):  # never two supers on screen: the next one waits for the last to clear
        a0 = max(T0 + (0.3 if i == 0 else -0.05), supers[-1][1] + 0.35 if supers else 0)
        supers.append([round(a0, 3), round(max(T0 + need - 0.3, a0 + 1.5), 3), b["super"]])
    if kind != "close":
        subs.append([round(s, 3), round(s + d, 3), b.get("sub", b["vo"])])
    T0 += need
D = round(T0, 2)
acts.sort(key=lambda a: a["t"])

# ---------- audio: voice, ducked bed, SFX ----------
aud = [f'<audio id="vo-{i + 1:02d}" src="assets/audio/vo/vo-{i + 1:02d}.wav" data-start="{s}" data-duration="{d:.3f}" data-track-index="10" data-volume="1" data-audio-group="voiceover"></audio>'
       for i, (s, d) in enumerate(vo_at)]
pts = [{"t": 0.0, "v": 0.0}, {"t": 0.15, "v": GAP_LVL}]
for s, d in vo_at:
    pts += [{"t": round(s - 0.12, 2), "v": GAP_LVL}, {"t": round(s + 0.08, 2), "v": DUCK_LVL},
            {"t": round(s + d - 0.05, 2), "v": DUCK_LVL}, {"t": round(s + d + 0.2, 2), "v": GAP_LVL}]
pts = [p for p in pts if p["t"] < D - 0.35] + [{"t": round(D - 0.35, 2), "v": GAP_LVL}, {"t": D, "v": 0.0}]
pts = sorted({p["t"]: p for p in pts if p["t"] >= 0}.values(), key=lambda p: p["t"])
auto = html.escape(json.dumps({"version": 1, "lanes": [{"target": "volume", "points": pts}]}))
aud.append(f'<audio id="music-bed" src="assets/audio/music-bed.mp3" data-start="0" data-media-start="4" data-duration="{D}" data-track-index="20" data-volume="1" data-audio-group="music" data-automation="{auto}"></audio>')
sdur = {}
for j, (f, s, v) in enumerate(sorted(sfx, key=lambda x: x[1])):
    sdur.setdefault(f, dur(prem / "assets/audio/sfx" / f))
    aud.append(f'<audio id="sfx-{j:02d}" src="assets/audio/sfx/{f}" data-start="{max(0.0, s)}" data-duration="{sdur[f]:.3f}" data-track-index="{30 + j % 4}" data-volume="{v}" data-audio-group="sfx"></audio>')

# ---------- engines (hook) and the fan beat ----------
def tile(cls: str, eid: str, key: str, label: str) -> str:
    img = ENGINE_IMG[key]
    return (f'<div class="{cls}" id="{eid}"><div class="tile"><img{" class=\"oai\"" if key == "chatgpt" else ""} src="assets/img/engines/{img}" alt="" /></div>'
            f'<div class="lb">{html.escape(label)}</div></div>')


engines = "".join(tile("weng", f"e{k}", key, lab) for k, (key, lab) in enumerate(T.get("engines", [])))
fanb = next((b for b in beats if b["type"] == "fan"), None)
fan = ""
if fanb:
    fan = "".join(f'<div class="qp" id="q{k}" data-layout-allow-overlap><b>{k + 1:02d}</b>{html.escape(q)}</div>' for k, q in enumerate(fanb["items"]))
    fan += "".join(tile("eng", f"g{k}", key, lab) for k, (key, lab) in enumerate(fanb["engines"]))

Z = T.get("zoom", 1.2)
data = {"D": D, "Z": Z, "supers": supers, "subs": subs, "acts": acts, "alias": alias}
out = ((HERE / "template.html").read_text(encoding="utf-8")
       .replace("__VW__", str(round(1440 / Z))).replace("__Z__", str(Z)).replace("__D__", str(D))
       .replace("__PAGE__", header + "\n" + page).replace("__ENGINES__", engines).replace("__FAN__", fan).replace("__GATE__", gate_html)
       .replace("__AUDIO__", "\n".join("      " + a for a in aud)).replace("__DATA__", json.dumps(data)))
(prem / "index.html").write_text(out, encoding="utf-8")
print(prem.parent.name, "D", D, "beat starts", starts)
