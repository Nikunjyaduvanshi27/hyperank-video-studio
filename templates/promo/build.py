"""Build the v3 promo: voice files + scene sources -> index.html and compositions/*.html.

    python build.py --cut b2b                      # every scene that has a source (cuts: content/<cut>.json)
    python build.py --cut b2b --only s01,s02,s03   # a subset, laid out from t=0 (style frames, previews)

Voice drives time: each scene's sentences (assets/audio/vo/<scene>-NN.wav, from tts.py) are laid out with a 0.06 s gap
plus the scene's lead, holds and tail. Problem scenes s01-s06 share one continuous depth stage (src/problem.html, one
JSON header per scene); every other scene is src/sNN.html (JSON header, markup, <style>, <script> using src/stage.js).
Header time expressions see B[i] / E[i] (line start / end), at(i, f), w(i, "word", k) (spoken word start), D and cues.
"""
import argparse, html, json, re, subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
A = HERE / "assets"
GAP, LEAD, TAIL, CLEAR = 0.06, 0.4, 0.4, 0.75
GAP_LVL, DUCK_LVL = 0.158, 0.0708  # bed about -26 dB between lines, ducked 7 dB under the voice (V26 levels)
PROBLEM = ["s01", "s02", "s03", "s04", "s05", "s06"]
SFX = {"whoosh": "whoosh-soft.wav", "click": "mouseclick1.ogg", "click2": "click2.ogg", "tick": "click_003.ogg", "impact": "impactSoft_medium_001.ogg",
       "impact4": "impactSoft_medium_004.ogg", "roll": "rollover2.ogg", "bong": "bong_001.ogg", "swell": "swell.wav", "air": "air.wav", "sparkle": "sparkle.wav"}
KEYS = ["keypress-%03d.wav" % k for k in (3, 7, 11, 14, 18, 21, 25, 27, 30, 32)]

ap = argparse.ArgumentParser()
ap.add_argument("--only", default="")
ap.add_argument("--cut", default="b2b")
args = ap.parse_args()
CUT = json.loads((HERE / f"content/{args.cut}.json").read_text(encoding="utf-8"))
VOD = "assets/audio/vo/" + CUT["cut"]


def dur(f: Path) -> float:
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)]).decode())


# ---------- the two recurring objects, one markup each ----------
ARROW = '<svg viewBox="0 0 24 24"><path d="M12 19V5M5.5 11.5L12 5l6.5 6.5" stroke="#fff" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>'
LINK = '<svg viewBox="0 0 24 24"><path d="M10 14a4.5 4.5 0 0 0 6.4 0l3-3a4.5 4.5 0 0 0-6.4-6.4l-1.2 1.2M14 10a4.5 4.5 0 0 0-6.4 0l-3 3a4.5 4.5 0 0 0 6.4 6.4l1.2-1.2" stroke="#5e4bf6" stroke-width="2.2" fill="none" stroke-linecap="round"/></svg>'
def composer(cid: str, texts: str) -> str:
    qs = "".join(f'<span class="q">{html.escape(t)}</span>' for t in (CUT["typed"] if texts == "@typed" else texts.split("|")))
    return (f'<div class="cmp glass" id="{cid}"><div class="eng"><img src="assets/img/logos/chatgpt.svg" alt="" /></div>'
            f'<div class="txt"><span class="ph">Ask anything</span>{qs}<i class="caret"></i></div><div class="send">{ARROW}</div></div>')


def card(cid: str, variant: str) -> str:
    """the answer card: 'blur' (s02, names unreadable), 'known' (s08 on, with the empty Your brand row)"""
    e = html.escape
    rows = "".join(f'<div class="row"><div class="rk">{i}</div><div class="tx"><div class="pn"><span class="nmv">{e(r["name"])}</span></div><div class="why">{e(r["why"])}</div></div>'
                   f'<span class="chip">{LINK}{e(r["src"])}</span></div>' for i, r in enumerate(CUT["rows"], 1))
    if variant == "won":  # weeks later: your brand is named first, with its own citation
        rows = (f'<div class="row win"><div class="rk">1</div><div class="tx"><div class="pn"><span class="nmv">{e(CUT["you"])}</span></div><div class="why">{e(CUT["win_why"])}</div></div>'
                f'<span class="chip win">{LINK}yourbrand.com</span></div>' +
                "".join(f'<div class="row"><div class="rk">{i}</div><div class="tx"><div class="pn"><span class="nmv">{e(r["name"])}</span></div><div class="why">{e(r["why"])}</div></div>'
                        f'<span class="chip">{LINK}{e(r["src"])}</span></div>' for i, r in enumerate(CUT["rows"][:2], 2)))
    if variant == "known":
        rows += f'<div class="row you"><div class="rk">4</div><div class="tx"><div class="pn">{e(CUT["you"])}</div><div class="why">Not in this answer</div></div></div>'
    return (f'<div class="ac glass{" blurred" if variant == "blur" else ""}" id="{cid}"><div class="hd"><img src="assets/img/logos/chatgpt.svg" alt="" /><span class="nm">ChatGPT</span>'
            f'<span class="tag">Illustrative</span></div><div class="intro">{e(CUT["intro"])}</div><div class="rows">{rows}</div></div>')


def tokens(markup: str) -> str:
    markup = re.sub(r"\{\{COMPOSER:([\w-]+):([^}]*)\}\}", lambda m: composer(m.group(1), m.group(2)), markup)
    markup = re.sub(r"\{\{CARD:([\w-]+):(\w+)\}\}", lambda m: card(m.group(1), m.group(2)), markup)
    return markup.replace("{{LAPTOP_OPEN}}", LAPTOP_OPEN).replace("{{LAPTOP_CLOSE}}", LAPTOP_CLOSE)


LAPTOP_OPEN = ('<div class="drift"><div class="cam"><div class="laptop"><div class="contact"></div><div class="ambient"></div>'
               '<div class="lid"><div class="lid-glass"><div class="webcam"></div></div></div><div class="screen">')
LAPTOP_CLOSE = '<div class="dim"></div></div><div class="glare"><div class="streak"></div></div><div class="hinge"></div><div class="deck"><div class="notch"></div></div></div></div></div><div class="veilT"></div><div class="veilB"></div>'


# ---------- timing ----------
script = json.loads((HERE / CUT["script"]).read_text(encoding="utf-8"))
lines = json.loads((HERE / VOD / "lines.json").read_text(encoding="utf-8"))
words = json.loads((HERE / VOD / "words.json").read_text(encoding="utf-8"))
stage_js = (HERE / "src/stage.js").read_text(encoding="utf-8")
stage_css = (HERE / "src/stage.css").read_text(encoding="utf-8")
FACES = "\n".join(l for l in stage_css.splitlines() if l.startswith("@font-face"))
prob_raw = (HERE / "src/problem.html").read_text(encoding="utf-8")
pm = re.match(r"\s*<!--(.*?)-->(.*)<script>(.*)</script>\s*$", prob_raw, re.S)
PHDR, PMARK, PJS = json.loads(pm.group(1)), pm.group(2), pm.group(3)


def source(sid: str):
    if sid in PROBLEM:
        return PHDR.get(sid)
    f = HERE / f"src/{sid}.html"
    if not f.exists():
        return None
    m = re.match(r"\s*<!--(.*?)-->(.*)<script>(.*)</script>\s*$", f.read_text(encoding="utf-8"), re.S)
    return {"hdr": json.loads(m.group(1)), "markup": m.group(2), "js": m.group(3)}


SUPER = {sc["id"]: sc["super"] for sc in script["scenes"]}
only = [s for s in args.only.split(",") if s]
scenes = [sc for sc in script["scenes"] if (sc["id"] in only if only else source(sc["id"]) is not None)]
assert all(source(sc["id"]) is not None for sc in scenes), "a requested scene has no source"


def ev(expr, env):
    return round(float(eval(str(expr), {"min": min, "max": max}, env)), 3) if not isinstance(expr, (int, float)) else float(expr)


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9%]", "", s.lower())


def timing(sid: str, hdr: dict, first: bool):
    names = sorted(k for k in lines if k.startswith(sid + "-"))
    d = [dur(HERE / VOD / f"{n}.wav") for n in names]
    W = [words[n] for n in names]
    holds = {int(k): v for k, v in hdr.get("holds", {}).items()}
    B, E, t = [], [], hdr.get("lead", 0.3 if first else LEAD)
    for i in range(len(names)):
        B.append(round(t, 3)); E.append(round(t + d[i], 3))
        t += d[i] + GAP + holds.get(i, 0)
    D = round(E[-1] + hdr.get("tail", TAIL), 3)

    def w(i, word, k=0):
        for x, s in W[i]:
            if norm(x).startswith(norm(word)):
                if k == 0:
                    return B[i] + s
                k -= 1
        raise KeyError(f"{sid}: no word {word!r} in line {i}: {W[i]}")
    env = {"B": B, "E": E, "D": D, "at": lambda i, f: B[i] + f * (E[i] - B[i]), "w": w, "CT": CUT}
    C = {}
    for k, v in hdr.get("cues", {}).items():
        C[k] = ev(v, {**env, **C})
    env.update(C); env["C"] = C
    if "minD" in hdr:
        D = max(D, ev(hdr["minD"], env)); env["D"] = D
    return names, d, W, B, E, D, env, C


def supers(hdr, env, sid, shift=0.0):
    """header supers; text "@" is the scene's script super, "split": n lands its first n words, then the rest"""
    out = []
    for s in hdr.get("supers", []):
        t = [ev(x, env) + shift for x in (s["t"] if isinstance(s["t"], list) else [s["t"]])]
        text = s["text"]
        if text == "@":
            words = SUPER[sid].split(" ")
            text = " ".join(words[:s["split"]]) + " / " + " ".join(words[s["split"]:]) if s.get("split") else SUPER[sid]
        out.append({"t": t, "text": text, "out": (ev(s["out"], env) + shift) if "out" in s else None})
    return out


T, hosts, aud, subs, sfx_all, vo_global, report, tim = 0.0, [], [], [], [], [], [], {}
(HERE / "compositions").mkdir(exist_ok=True)
for f in (HERE / "compositions").glob("*.html"):
    f.unlink()


def chunks(text: str, limit: int = 62):
    out, cur = [], ""
    for w_ in text.split(" "):
        if cur and len(cur) + 1 + len(w_) > limit:
            out.append(cur); cur = w_
        else:
            cur = (cur + " " + w_).strip()
        if len(cur) > limit * 0.55 and re.search(r"[,:;.?]$", w_):
            out.append(cur); cur = ""
    if cur:
        out.append(cur)
    if len(out) > 1 and len(out[-1]) < 16:
        tail = out.pop(); out[-1] += " " + tail
    return out


def voice(sid, names, d, B, T0):
    for i, n in enumerate(names):
        g0 = round(T0 + B[i], 3)
        vo_global.append((g0, d[i]))
        aud.append(f'<audio id="vo-{n}" src="{VOD}/{n}.wav" data-start="{g0}" data-duration="{d[i]:.3f}" data-track-index="10" data-volume="1" data-audio-group="voiceover"></audio>')
        parts = chunks(lines[n]["vo"])
        n_ch, t0 = sum(len(p) for p in parts), g0
        for p in parts:
            t1 = t0 + d[i] * len(p) / n_ch
            subs.append([round(t0, 3), round(t1, 3), p]); t0 = t1


def sfx(hdr, env, C, T0):
    for f, at, v in hdr.get("sfx", []):
        files = [KEYS[k % 10] for k in range(int(f[4:]) if f[4:] else 1)] if f.startswith("keys") else [SFX[f]]
        sfx_all.append((files[0], round(T0 + ev(at, env), 3), v))
    for a, b, v in hdr.get("typing", []):  # one keystroke every ~0.11 s across a typed line
        a, b = ev(a, env), ev(b, env)
        k = 0
        while a + k * 0.11 < b:
            sfx_all.append((KEYS[(k * 3) % 10], round(T0 + a + k * 0.11, 3), v)); k += 1


_R = json.loads((A / "img/site/rects.json").read_text(encoding="utf-8"))
RECTS = json.dumps({**_R["shared"], **_R[CUT["cut"]]})
MARK = (A / "img/mark-paths.json").read_text(encoding="utf-8")


def comp(cid, D, T0, body, js, data):
    js = js.replace("__RECTS__", RECTS).replace("__MARK__", MARK).replace("__CUT__", CUT["cut"])
    body = body.replace("__CUT__", CUT["cut"])
    data = {**data, "CT": CUT}
    return (f'<!doctype html>\n<html lang="en">\n<head><meta charset="UTF-8" /></head>\n<body>\n<template>\n<style>\n{FACES}\n</style>\n'
            f'<div data-composition-id="{cid}" data-width="1920" data-height="1080" data-duration="{D}" style="position: absolute; inset: 0">\n'
            f'<div class="scene{" pw" if cid == "problem" else ""}"><div class="ground"></div><div class="bloom0"></div><div class="vig"></div>\n{body}\n</div>\n</div>\n'
            f'<script>\n{stage_js}\n(function () {{\n  function build() {{\n    const DATA = {json.dumps(data)};\n    const S = Stage("{cid}", DATA);\n{js}\n    S.done();\n  }}\n'
            f'  document.fonts.ready.then(build);\n}})();\n</script>\n</template>\n</body>\n</html>\n')


i = 0
while i < len(scenes):
    sid = scenes[i]["id"]
    first = i == 0
    if sid in PROBLEM:  # one continuous depth stage for consecutive problem scenes
        group = []
        while i < len(scenes) and scenes[i]["id"] in PROBLEM:
            group.append(scenes[i]["id"]); i += 1
        SC, sup, t = {}, [], 0.0
        for k, g in enumerate(group):
            hdr = PHDR[g]
            names, d, W, B, E, D, env, C = timing(g, hdr, first and k == 0)
            SC[g] = {"t0": round(t, 3), "D": D, "B": [round(t + b, 3) for b in B], "E": [round(t + e, 3) for e in E], "W": [[[x, s] for x, s in L] for L in W],
                     "C": {k2: round(t + v, 3) for k2, v in C.items()}}
            sup += supers(hdr, env, g, t)
            voice(g, names, d, B, T + t)
            sfx(hdr, env, C, T + t)
            report.append((g, round(T + t, 2), D)); tim[g] = {"start": round(T + t, 3), "D": D}
            t += D
        DD = round(t + (CLEAR if i < len(scenes) else 0), 3)
        data = {"D": DD, "T0": round(T, 3), "B": [], "E": [], "W": [], "SC": SC, "order": group, "clear": round(t, 3) if i < len(scenes) else None, "supers": sup}
        (HERE / "compositions/problem.html").write_text(comp("problem", DD, T, tokens(PMARK.strip()), PJS, data), encoding="utf-8")
        hosts.append(f'<div id="h-problem" data-composition-id="problem" data-composition-src="compositions/problem.html" data-start="{round(T, 3)}" data-duration="{DD}" '
                     f'data-track-index="2" data-track-kind="graphics" data-width="1920" data-height="1080" style="z-index: 3"></div>')
        T += t
        continue
    src = source(sid)
    hdr = src["hdr"]
    names, d, W, B, E, D, env, C = timing(sid, hdr, first)
    data = {"D": D, "T0": round(T, 3), "B": B, "E": E, "W": [[[x, s] for x, s in L] for L in W], "C": C, "cam0": hdr.get("cam0", "HOLD"), "supers": supers(hdr, env, sid)}
    (HERE / f"compositions/{sid}.html").write_text(comp(sid, D, T, tokens(src["markup"].strip()), src["js"], data), encoding="utf-8")
    hosts.append(f'<div id="h-{sid}" data-composition-id="{sid}" data-composition-src="compositions/{sid}.html" data-start="{round(T, 3)}" data-duration="{D}" '
                 f'data-track-index="1" data-track-kind="graphics" data-width="1920" data-height="1080" style="z-index: 2"></div>')
    voice(sid, names, d, B, T)
    sfx(hdr, env, C, T)
    report.append((sid, round(T, 2), D)); tim[sid] = {"start": round(T, 3), "D": D}
    T += D; i += 1
TOTAL = round(T, 3)

# ---------- captions: one track ----------
cap_js = "\n".join(f"    sub({a}, {b}, {json.dumps(txt)});" for a, b, txt in subs)
(HERE / "compositions/captions.html").write_text(f'''<!doctype html>
<html lang="en">
<head><meta charset="UTF-8" /></head>
<body>
<template>
<style>
{FACES}
</style>
<div data-composition-id="captions" data-width="1920" data-height="1080" data-duration="{TOTAL}" style="position: absolute; inset: 0; pointer-events: none">
<div class="caps"></div>
</div>
<script>
(function () {{
  const all = document.querySelectorAll('[data-composition-id="captions"]'), root = all[all.length - 1];
  const box = root.querySelector(".caps");
  const tl = gsap.timeline({{ paused: true }});
  function sub(a, b, txt) {{
    const d = document.createElement("div");
    d.className = "sub"; d.textContent = txt; d.setAttribute("data-layout-allow-overlap", "");
    box.appendChild(d);
    tl.fromTo(d, {{ opacity: 0, y: 8 }}, {{ opacity: 1, y: 0, duration: 0.15, ease: "power2.out" }}, a);
    tl.to(d, {{ opacity: 0, duration: 0.1, ease: "power1.in" }}, b - 0.12);
  }}
{cap_js}
  tl.set({{}}, {{}}, {TOTAL});
  window.__timelines["captions"] = tl;
}})();
</script>
</template>
</body>
</html>
''', encoding="utf-8")

# ---------- root: scenes, captions, voice, ducked bed, SFX ----------
pts = [{"t": 0.0, "v": 0.0}, {"t": 0.4, "v": GAP_LVL}]
for s, d_ in vo_global:
    pts += [{"t": round(s - 0.12, 2), "v": GAP_LVL}, {"t": round(s + 0.08, 2), "v": DUCK_LVL}, {"t": round(s + d_ - 0.05, 2), "v": DUCK_LVL}, {"t": round(s + d_ + 0.2, 2), "v": GAP_LVL}]
pts = [p for p in pts if p["t"] < TOTAL - 0.6] + [{"t": round(TOTAL - 0.6, 2), "v": GAP_LVL}, {"t": TOTAL, "v": 0.0}]
pts = sorted({p["t"]: p for p in pts if p["t"] >= 0}.values(), key=lambda p: p["t"])
auto = html.escape(json.dumps({"version": 1, "lanes": [{"target": "volume", "points": pts}]}))
aud.append(f'<audio id="music-bed" src="assets/audio/music-bed-long.mp3" data-start="0" data-duration="{TOTAL}" data-track-index="20" data-volume="1" data-audio-group="music" data-automation="{auto}"></audio>')
sdur, lanes = {}, []  # each SFX takes the first track that is free at its start
for j, (f, s, v) in enumerate(sorted(sfx_all, key=lambda x: x[1])):
    sdur.setdefault(f, dur(A / "audio/sfx" / f))
    s0 = max(0.0, s); d_ = min(sdur[f], TOTAL - s0)
    k = next((n for n, end in enumerate(lanes) if end <= s0), len(lanes))
    lanes[k:k + 1] = [s0 + d_]
    aud.append(f'<audio id="sfx-{j:03d}" src="assets/audio/sfx/{f}" data-start="{s0}" data-duration="{d_:.3f}" data-track-index="{30 + k}" data-volume="{v}" data-audio-group="sfx"></audio>')

root = f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>
{stage_css}
      #root {{ position: relative; width: 100%; height: 100%; overflow: hidden; background: var(--ground); }}
      [data-composition-id="main"] > div[data-composition-src] {{ position: absolute; inset: 0; }}
    </style>
  </head>
  <body>
    <!-- generated by build.py from script.json, src/ and the voice files -->
    <div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="1920" data-height="1080">
{chr(10).join("      " + h for h in hosts)}
      <div id="h-captions" data-composition-id="captions" data-composition-src="compositions/captions.html" data-start="0" data-duration="{TOTAL}" data-track-index="3" data-track-kind="captions" data-width="1920" data-height="1080" style="z-index: 10"></div>
{chr(10).join("      " + a for a in aud)}
    </div>
    <script>
      window.__timelines["main"] = gsap.timeline({{ paused: true }});
    </script>
  </body>
</html>
'''
(HERE / "index.html").write_text(root, encoding="utf-8")
(HERE / "timing.json").write_text(json.dumps(tim, indent=1), encoding="utf-8")
print("TOTAL", TOTAL, "s =", f"{int(TOTAL // 60)}:{TOTAL % 60:04.1f}")
for sid, st, d_ in report:
    print(f"  {sid} start {st:7.2f}  len {d_:6.2f}")
