# hyperank video studio

Private, portable kit for making the same kind of films on another Windows 11 machine with Claude Code and HyperFrames:

- premium bright promo films (`templates/promo`, two cuts from one build)
- a laptop product intro for a client site (`templates/intro`, worked example: Celebal)
- tool tutorials (`templates/tutorial`, one pipeline, one folder per tool)

Everything runs locally: HyperFrames (pinned to `0.8.113`), Kokoro TTS, whisper.cpp, ffmpeg. No API keys are needed and none are stored here.

## Layout

```
setup/setup.ps1      one-shot Windows setup (idempotent)
skills/              Claude Code skills, copied into ~/.claude/skills by setup
templates/promo/     18-scene promo, cuts in content/*.json + script*.json
templates/intro/     premium laptop intro (Celebal worked example)
templates/tutorial/  tool tutorial pipeline, shared assets in shared/, example in tools/robots-txt-checker
kit/                 brand kit: frame.md, MOTION.md, BLOCKS.md, reusable scenes, showcase project
docs/                PIPELINE.md, directions-ledger.md, STYLE-RULES.md, PITCH-RULES.md, STACK.md,
                     product briefs, music licenses, scripts/ (example voice scripts)
CLAUDE.md            playbook Claude Code reads on this machine
```

## Set up a new machine

1. Install Claude Code, then clone this repo.
2. In PowerShell from the repo root:

   ```powershell
   powershell -ExecutionPolicy Bypass -File setup\setup.ps1
   ```

   Add `-Yes` to install missing tools without being asked. The script installs (via winget) Git, Node.js LTS, Python 3.13 and ffmpeg if missing, pip-installs `kokoro-onnx soundfile numpy beautifulsoup4 pillow playwright`, downloads whisper.cpp `b5130` into `~/tools/whisper.cpp`, the whisper `ggml-small.en.bin` model (488 MB) and the Kokoro model files (about 350 MB) into `~/.cache/hyperframes`, copies `skills/*` into `~/.claude/skills` (existing folders are backed up to `~/.claude/_backups/skills-<timestamp>/`), and warms the pinned CLI. Re-running it skips whatever is already done.
3. Open a new terminal (so PATH picks up the installs) and open this folder in Claude Code.
4. The first HyperFrames `check` or `render` downloads its own Chrome into `~/.cache/hyperframes/chrome`. That is expected. The promo capture scripts need that Chrome to exist, so run one `check` before using them.

Do not bump `hyperframes@0.8.113`. It is pinned so films re-render identically.

Set `HYPERFRAMES_SKIP_SKILLS=1` in the shell before rendering, as the QA scripts do:

```powershell
$env:HYPERFRAMES_SKIP_SKILLS = "1"
```

## Make a promo (`templates/promo`)

Two cuts ship: `b2b` and `consumer`. A cut is `content/<cut>.json` (typed questions, answer rows, brand names, stats, site text edits) plus the `script*.json` it names (scene voice lines). Scene markup is `src/s07.html` etc. and `src/problem.html`; `BRIEF.md` is the creative brief and the Gate 1 / Gate 2 plan.

New cut: copy `content/b2b.json` to `content/<name>.json`, copy `script.json` to `script-<name>.json`, point `"script"` and `"out"` at them, then edit the text. Keep every `vo` verbatim; `tts` is what Kokoro reads ("A-I", "Hyper-rank").

```powershell
cd templates\promo
python tts.py --cut <name>                 # voice every sentence, whisper word times (unchanged lines skipped)
python build.py --cut <name>               # writes index.html, compositions/*.html, timing.json
python build.py --cut <name> --only s02,s07,s10   # style frames only, laid out from t=0
npx --yes hyperframes@0.8.113 check
npx --yes hyperframes@0.8.113 snapshot --at 2,5,8 --no-end --describe false
npx --yes hyperframes@0.8.113 render --workers 1 -o out/promo-<name>.mp4
python qa.py --cut <name>                  # check, white/black frames, silence, 5x4 contact sheet
```

`python capture\capture.py` re-renders the hyperank.ai site crops and app screens into `assets\img\site\` from the vendored `capture\home\_render.html` (needs the Chrome from step 4 and `playwright`). The crops are already checked in, so you only run it after changing the `site` or `cc` blocks of a cut.

## Make a laptop intro (`templates/intro`)

This is a worked example for celebaltech.com. Its crops, partner logos, award badges and `PAGE_H` are specific to that site, so for a new client copy the folder, re-run the capture scripts against the new URL (`capture/cap.py`, `cap2.py`, `cap3.py` hard-code the Celebal URL; edit them), regenerate the crops and logos in `premium/assets/img`, then edit `premium/tool.json` (the beats: hook, name, strengths, partners, industries, awards, close) and the lift rectangles in `build.py`.

```powershell
cd templates\intro
python ..\tutorial\tts_batch.py .          # Kokoro voice for every beat in premium/tool.json
python build.py                            # writes premium/index.html
cd premium
npx --yes hyperframes@0.8.113 snapshot --at 5,12,20,30 --no-end --describe false
npx --yes hyperframes@0.8.113 render --workers 1 -o out/premium-16x9.mp4
cd ..
python ..\tutorial\qa.py .                 # check, white frames, silence, out/contact-sheet.jpg
```

## Make a tool tutorial (`templates/tutorial`)

One folder per tool under `tools/<slug>/premium/`. `tools/robots-txt-checker` is the example (tool.json plus the recorded capture). Full steps are in `templates/tutorial/README.md`; the short version:

```powershell
cd templates\tutorial
python capture.py <tool-url> tools\<slug>\premium\capture\try-<site> <input>   # record a real run (anonymous, rate-limited)
# write tools\<slug>\premium\tool.json (copy the example), and docs\scripts\tutorial-<slug>.md
python tts_batch.py tools\<slug>
python build.py tools\<slug>               # copies shared/ assets in and writes premium/index.html
cd tools\<slug>\premium
npx --yes hyperframes@0.8.113 snapshot --at <beat midpoints> --no-end --describe false
npx --yes hyperframes@0.8.113 render --workers 1 -o out/premium-16x9.mp4
cd ..\..\..
python qa.py tools\<slug>
```

`neo.py` and `neo_capture.py` capture logged-in results through the BrowserOS MCP. They only work if BrowserOS is installed and signed in on that machine; without it, use `capture.py` (anonymous) instead.

## What is not in the repo

Rendered videos, snapshots, generated voiceover (`assets/audio/vo/`), generated HTML (`index.html`, `compositions/`, per-tool `assets/`), model weights and logs are gitignored or excluded. Generate them with the commands above. The music bed and SFX in `assets/audio` are included on purpose (CC0 or free licenses, see `docs/MUSIC-LICENSES.md`).

## Troubleshooting

- `python` opens the Microsoft Store: Python is not installed, or the Store alias shadows it. Re-run `setup.ps1`, then open a new terminal.
- `kokoro_onnx` import error or model not found: re-run `setup.ps1`. The model files must be at `~/.cache/hyperframes/tts/models/kokoro-v1.0.onnx` and `~/.cache/hyperframes/tts/voices/voices-v1.0.bin`.
- whisper model download times out inside HyperFrames: that is why setup downloads it with `Invoke-WebRequest`. Check `~/.cache/hyperframes/whisper/models/ggml-small.en.bin` is about 488 MB.
- `build.py` fails on a missing `.wav`: run `tts.py` (promo) or `tts_batch.py` (intro, tutorial) first. Voice length sets every scene's duration.
- `StopIteration` from `capture.py`, `peek.py` or `probe.py`: HyperFrames' Chrome is not in `~/.cache/hyperframes/chrome` yet. Run `npx --yes hyperframes@0.8.113 check` once in a project folder.
- Render killed or the machine freezes: close other Chrome windows, keep `--workers 1`, add `--quality draft` for previews, render one video at a time.
- White frames or unreadable text in QA: do not shrink a tool page with zoom below 0.9; scroll the form instead.
- Voice mispronounces the brand: write "Hyper-rank" and "A-I" in `tts` fields, keep normal spelling in `vo`. Check a line with `~/tools/whisper.cpp/Release/whisper-cli.exe -m ~/.cache/hyperframes/whisper/models/ggml-small.en.bin -f <16 kHz mono wav>`.
- Skills missing in Claude Code: setup copies them to `~/.claude/skills`. Restart the Claude Code session after setup so they load.
