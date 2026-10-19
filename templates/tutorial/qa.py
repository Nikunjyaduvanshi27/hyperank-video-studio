"""Gates for one tool: hyperframes check, then (when out/premium-16x9.mp4 exists) white frames, silence, contact sheet.

    python qa.py tools/<slug>         # exits 1 if any gate fails
"""
import os, re, subprocess, sys
from pathlib import Path

prem = (Path(sys.argv[1]) / "premium").resolve()
mp4 = prem / "out/premium-16x9.mp4"
env = {**os.environ, "HYPERFRAMES_SKIP_SKILLS": "1"}
fails = []


def run(cmd: list[str], **k) -> str:
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=prem, env=env, shell=(os.name == "nt" and cmd[0] == "npx"), **k)
    return r.stdout + r.stderr


out = run(["npx", "--yes", "hyperframes@0.8.113", "check"])
if "Check passed" not in out:
    fails.append("hyperframes check:\n" + "\n".join(l for l in out.splitlines() if "✗" in l or "error" in l.lower())[:2000])

if mp4.exists():
    # near-white frames: negated, they turn black
    out = run(["ffmpeg", "-hide_banner", "-i", str(mp4), "-vf", "negate,blackdetect=d=0.1:pix_th=0.15:picture_black_ratio_th=0.97", "-an", "-f", "null", "-"])
    hits = re.findall(r"black_start:\S+ black_end:\S+", out)
    if hits:
        fails.append("white frames: " + "; ".join(hits))
    out = run(["ffmpeg", "-hide_banner", "-i", str(mp4), "-af", "silencedetect=noise=-28dB:d=0.45", "-vn", "-f", "null", "-"])
    hits = re.findall(r"silence_start: \S+", out)
    if hits:
        fails.append("silence over 0.45s: " + "; ".join(hits))
    dur = float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(mp4)]).strip())
    n = 20  # 20 evenly spaced frames, 5 x 4
    run(["ffmpeg", "-hide_banner", "-y", "-i", str(mp4), "-vf", f"fps={n / dur:.5f},scale=480:-1,tile=5x4", "-frames:v", "1", "-q:v", "3", str(prem / "out/contact-sheet.jpg")])
    print(f"{prem.parent.name}: {dur:.2f}s, contact sheet out/contact-sheet.jpg")

print("PASS" if not fails else "FAIL\n" + "\n".join(fails))
sys.exit(1 if fails else 0)
