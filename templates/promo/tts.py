"""Voice every sentence of script.json (Kokoro af_heart, speed 1.15), then whisper each one for pronunciation and word times.

    python tts.py --cut b2b    # writes assets/audio/vo/<cut>/<scene>-NN.wav, lines.json and words.json; unchanged lines are skipped

Each scene's `vo` (shown in captions) and `tts` (what Kokoro reads) are split into sentences; the build lays them
out with a 0.06 s gap. words.json holds whisper's word start times per line, so reveals can land on their word.
"""
import argparse, json, re, subprocess
from pathlib import Path
import numpy as np
import soundfile as sf

HERE = Path(__file__).resolve().parent
ap = argparse.ArgumentParser()
ap.add_argument("--cut", default="b2b")
CUT = json.loads((HERE / f"content/{ap.parse_args().cut}.json").read_text(encoding="utf-8"))
VO = HERE / "assets/audio/vo" / CUT["cut"]
VO.mkdir(parents=True, exist_ok=True)
CACHE = Path.home() / ".cache/hyperframes"
WHISPER = Path.home() / "tools/whisper.cpp/Release/whisper-cli.exe"
SPLIT = re.compile(r"(?<=[.?!])\s+")


def shorten_pauses(x: np.ndarray, sr: int, thr: float = 0.025, longest: float = 0.3, keep: float = 0.18) -> np.ndarray:
    """A comma pause longer than `longest` s inside a line is cut to `keep` s (the bed ducks under the voice, so a long pause reads as silence)."""
    w = int(sr * 0.01)
    quiet = np.array([np.abs(x[i:i + w]).max() < thr for i in range(0, len(x) - w, w)])
    out, i, n = [], 0, len(quiet)
    while i < n:
        j = i
        while j < n and quiet[j] == quiet[i]:
            j += 1
        seg = x[i * w:j * w]
        if quiet[i] and 0 < i and j < n and (j - i) * 0.01 > longest:
            seg = seg[:int(keep * sr)]
        out.append(seg)
        i = j
    out.append(x[n * w:])
    return np.concatenate(out)


def lines():
    """script.json scenes -> [(name, vo sentence, tts sentence)]"""
    out = []
    for sc in json.loads((HERE / CUT["script"]).read_text(encoding="utf-8"))["scenes"]:
        vo, tts = SPLIT.split(sc["vo"].strip()), SPLIT.split(sc["tts"].strip())
        assert len(vo) == len(tts), (sc["id"], vo, tts)
        for k, (v, t) in enumerate(zip(vo, tts), 1):
            for a, b in CUT.get("tts_fix", {}).items():  # pronunciation fixes for this cut; captions keep the written word
                t = t.replace(a, b)
            out.append((f"{sc['id']}-{k:02d}", v, t))
    return out


def whisper(wav: Path) -> list:
    """[(word, start s)] from whisper.cpp small.en, one word per segment."""
    tmp = wav.with_suffix(".16k.wav")
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(wav), "-ar", "16000", "-ac", "1", str(tmp)], check=True)
    base = wav.with_suffix("")
    subprocess.run([str(WHISPER), "-m", str(CACHE / "whisper/models/ggml-small.en.bin"), "-f", str(tmp), "-ml", "1", "-sow", "-oj", "-of", str(base), "-np"],
                   check=True, capture_output=True)
    segs = json.loads(Path(str(base) + ".json").read_text(encoding="utf-8"))["transcription"]
    tmp.unlink(); Path(str(base) + ".json").unlink()
    return [(s["text"].strip(), s["offsets"]["from"] / 1000) for s in segs if s["text"].strip()]


if __name__ == "__main__":
    from kokoro_onnx import Kokoro
    old = json.loads((VO / "lines.json").read_text(encoding="utf-8")) if (VO / "lines.json").exists() else {}
    words = json.loads((VO / "words.json").read_text(encoding="utf-8")) if (VO / "words.json").exists() else {}
    kokoro = Kokoro(str(CACHE / "tts/models/kokoro-v1.0.onnx"), str(CACHE / "tts/voices/voices-v1.0.bin"))
    done = {}
    for name, vo, text in lines():
        done[name] = {"vo": vo, "tts": text}
        wav = VO / f"{name}.wav"
        if old.get(name) == done[name] and wav.exists() and name in words:
            continue
        samples, sr = kokoro.create(text, voice="af_heart", speed=1.15, lang="en-us")
        sf.write(wav, shorten_pauses(samples, sr), sr)
        words[name] = whisper(wav)
        print(f"{name} {len(samples) / sr:5.2f}s  heard: {' '.join(w for w, _ in words[name])}")
    (VO / "lines.json").write_text(json.dumps(done, indent=1), encoding="utf-8")
    (VO / "words.json").write_text(json.dumps(words, indent=1), encoding="utf-8")
