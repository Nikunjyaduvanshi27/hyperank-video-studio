"""Build the Celebal intro: tool.json beats + voice files -> premium/index.html (voice length sets every beat)."""
import html, json, subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
prem = HERE / "premium"
beats = json.loads((prem / "tool.json").read_text(encoding="utf-8"))["beats"]
GAP_LVL, DUCK_LVL = 0.158, 0.0708  # same quiet score as the hyperank films: ~-26 dB, 7 dB under the voice
PAGE_H = 6278


def dur(f: Path) -> float:
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)]).decode())


vo = [dur(prem / f"assets/audio/vo/vo-{i + 1:02d}.wav") for i in range(len(beats))]
acts, sfx, supers, subs, vo_at = [], [], [], [], []


def A(op, t, **k):
    acts.append({"op": op, "t": round(t, 3), **k})


def X(f, t, v):
    sfx.append((f, round(t, 3), v))


T0 = 0.0
for i, b in enumerate(beats):
    kind, d = b["type"], vo[i]
    lead = 0.3 if i == 0 else 0.22
    s = T0 + lead
    need = lead + d + 0.28
    if kind == "hook":
        A("cam", 0, to="WIDE1", dur=1.9, ease="sine.inOut")
        A("bug", 0.1, t1=1.9)
        need = max(need, 2.0)
        A("logos", 0.15, t1=T0 + need + 0.1)
        A("streak", 0.3)
        X("impactSoft_medium_001.ogg", 0.3, 0.45); X("whoosh-soft.wav", 0.2, 0.35)
    elif kind == "name":
        A("cam", T0 - 0.1, to="HOLD", dur=1.1)
        A("eyebrow", T0 + 0.05, t1=T0 + 1.6)
        X("whoosh-soft.wav", T0 - 0.2, 0.35)
        need = max(need, 3.8)
        A("cam", T0 + 1.3, to="PUSH", rect=[60, 380, 1320, 240], dur=1.0)
        A("veils", T0 + 1.35, v=1)
        X("whoosh-soft.wav", T0 + 1.25, 0.3)
        A("cam", T0 + need - 0.85, to="HOLD", dur=0.85)
        A("veils", T0 + need - 0.4, v=0, dur=0.4)
    elif kind == "strengths":
        A("scroll", T0, to=3267, dur=1.0); X("whoosh-soft.wav", T0, 0.3)
        need = max(need, 3.4)
        L0 = T0 + 1.05
        A("dim", L0 - 0.05, v=0.3)
        A("lift", L0, t0=L0, t1=T0 + need - 0.1, img="crop-strengths.png", rect=[80, 3490, 1280, 400], cx=960, cy=600, maxW=1500, maxH=470)
        X("impactSoft_medium_004.ogg", L0 + 0.05, 0.4)
        A("dim", T0 + need - 0.45, v=0)
    elif kind == "partners":
        A("scroll", T0, to=1082, dur=1.0); X("whoosh-soft.wav", T0, 0.3)
        need = max(need, 3.4)
        L0, end = T0 + 1.05, T0 + need - 0.1
        A("dim", L0 - 0.05, v=0.3)
        A("lift", L0, t0=L0, t1=end, img="crop-svc.png", rect=[70, 1395, 1290, 110], cx=960, cy=455, maxW=1560, maxH=200, label="Service partners")
        A("lift", L0 + 0.3, t0=L0 + 0.3, t1=end, img="crop-sol.png", rect=[70, 1648, 1260, 110], cx=960, cy=735, maxW=1560, maxH=200, label="Solution partners")
        X("impactSoft_medium_004.ogg", L0 + 0.05, 0.4); X("rollover2.ogg", L0 + 0.35, 0.25)
        A("dim", T0 + need - 0.45, v=0)
    elif kind == "industries":
        A("scroll", T0, to=1718, dur=1.0); X("whoosh-soft.wav", T0, 0.3)
        need = max(need, 3.6)
        A("dim", T0 + 0.9, v=0.45)
        A("chips", T0 + 1.0, t1=T0 + need - 0.05, cy=580)
        for j in range(9):
            X("rollover2.ogg", T0 + 1.05 + j * 0.12, 0.18)
        A("dim", T0 + need - 0.45, v=0)
    elif kind == "awards":
        A("scroll", T0, to=2738, dur=1.0); X("whoosh-soft.wav", T0, 0.3)
        need = max(need, 3.6)
        L0, end = T0 + 1.0, T0 + need - 0.1
        A("dim", L0 - 0.05, v=0.3)
        for j in range(4):
            A("lift", L0 + j * 0.2, t0=L0 + j * 0.2, t1=end, img=f"crop-aw{j}.png", rect=[76 + 278 * j, 2941, 254, 342],
              cx=960 + (j - 1.5) * 400, cy=590, maxW=360, maxH=470)
            X("impactSoft_medium_004.ogg" if j == 0 else "rollover2.ogg", L0 + j * 0.2 + 0.05, 0.4 if j == 0 else 0.25)
        X("bong_001.ogg", L0 + 0.9, 0.3)
        A("dim", T0 + need - 0.45, v=0)
    elif kind == "close":
        A("veils", T0, v=0, dur=0.4)
        A("end", T0)
        X("whoosh-soft.wav", T0 - 0.05, 0.4); X("impactSoft_medium_001.ogg", T0 + 0.1, 0.45); X("bong_001.ogg", T0 + 1.3, 0.3)
        need = max(lead + d + 0.6, 2.8)
    vo_at.append((round(s, 3), d))
    if b.get("super"):  # never two supers on screen
        a0 = max(T0 + (0.3 if i == 0 else -0.05), supers[-1][1] + 0.35 if supers else 0)
        supers.append([round(a0, 3), round(max(T0 + need - 0.3, a0 + 1.5), 3), b["super"]])
    if kind != "close":
        subs.append([round(s, 3), round(s + d, 3), b["vo"]])
    T0 += need
D = round(T0, 2)
acts.sort(key=lambda a: a["t"])

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

LOGOS = ["microsoft", "databricks", "aws-updated", "sap", "nvindia", "confluent"]
logos = "".join(f'<div class="wlogo" id="lg{k}"><div class="tile"><img src="assets/img/logos/{n}.png" alt="" /></div></div>' for k, n in enumerate(LOGOS))
INDUSTRIES = ["Banking, Financial Services, and Insurance", "Retail & Consumer Packaged Goods", "Oil & Gas",
              "Manufacturing", "Communications, Media, and Entertainment", "Renewables",
              "Power, Utilities, & Energies", "Health & Life Sciences", "Information Technology Enabled Services"]  # the site's nine, rows balanced
chips = "".join(f'<div class="chip" id="ch{k}" data-layout-allow-overlap><b>{k + 1:02d}</b>{html.escape(n)}</div>' for k, n in enumerate(INDUSTRIES))

out = ((HERE / "template.html").read_text(encoding="utf-8")
       .replace("__D__", str(D)).replace("__PH__", str(PAGE_H)).replace("__LOGOS__", logos).replace("__CHIPS__", chips)
       .replace("__AUDIO__", "\n".join("      " + a for a in aud))
       .replace("__DATA__", json.dumps({"D": D, "supers": supers, "subs": subs, "acts": acts})))
(prem / "index.html").write_text(out, encoding="utf-8")
print("D", D, [round(s, 2) for s, _ in vo_at])
