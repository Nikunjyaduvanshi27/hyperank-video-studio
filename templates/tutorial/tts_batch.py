"""Voice every beat of one or more tools in ONE process (Kokoro loaded once), voice af_heart.

    python tts_batch.py tools/robots-txt-checker tools/<slug> ...

Reads <tool>/premium/tool.json -> beats[].tts (falls back to beats[].vo), writes <tool>/premium/assets/audio/vo/vo-NN.wav
and lines.txt. A line whose text is unchanged since the last run is not regenerated.
"""
import json, sys
from pathlib import Path
import soundfile as sf
from kokoro_onnx import Kokoro

CACHE = Path.home() / ".cache/hyperframes/tts"
kokoro = Kokoro(str(CACHE / "models/kokoro-v1.0.onnx"), str(CACHE / "voices/voices-v1.0.bin"))

for tool in sys.argv[1:]:
    prem = Path(tool) / "premium"
    beats = json.loads((prem / "tool.json").read_text(encoding="utf-8"))["beats"]
    vo = prem / "assets/audio/vo"
    vo.mkdir(parents=True, exist_ok=True)
    old = (vo / "lines.txt").read_text(encoding="utf-8").splitlines() if (vo / "lines.txt").exists() else []
    lines = [b.get("tts") or b["vo"] for b in beats]
    for i, text in enumerate(lines):
        wav = vo / f"vo-{i + 1:02d}.wav"
        if wav.exists() and i < len(old) and old[i] == text:
            continue
        samples, sr = kokoro.create(text, voice="af_heart", speed=1.0, lang="en-us")
        sf.write(wav, samples, sr)
        print(prem.parent.name, f"vo-{i + 1:02d}", round(len(samples) / sr, 2), text)
    for f in vo.glob("vo-*.wav"):  # drop lines a shorter script no longer uses
        if int(f.stem[3:]) > len(lines):
            f.unlink()
    (vo / "lines.txt").write_text("\n".join(lines), encoding="utf-8")
