# CLAUDE.md: hyperank video studio playbook

You are working in a portable kit for hyperank.ai films made with HyperFrames. Read `README.md` for commands. Read `docs/STYLE-RULES.md`, `docs/PITCH-RULES.md` and `docs/STACK.md` before any creative or tooling decision. The founder is Nikunj; he gives short briefs and expects you to execute end to end.

## First thing on a new machine

If `~/.cache/hyperframes/tts/models/kokoro-v1.0.onnx`, `~/tools/whisper.cpp/Release/whisper-cli.exe` or `~/.claude/skills/hyperframes` is missing, the user has not run `setup\setup.ps1`. Tell them to run it (`powershell -ExecutionPolicy Bypass -File setup\setup.ps1`) rather than installing pieces by hand. Skills do not auto-fire in subagents: name the skills a subagent must invoke (`hyperframes`, `hyperframes-cli`, `hyperframes-core`, and for design work `taste-skill`, `anti-ai-slop`, `premium-animation`, `interactive-3d`).

## Which template for which ask

| Ask | Use | Notes |
|---|---|---|
| Sales or promo film, client-facing | `templates/promo` | Data-driven 18 scenes. A new audience is a new cut: `content/<cut>.json` + `script-<cut>.json`, same scenes and motion. Read `templates/promo/BRIEF.md` first. |
| "Intro for client X", laptop product film of a website | `templates/intro` | Celebal is the worked example. Crops, logos and lift rectangles are site-specific and must be rebuilt for a new site. |
| "Tutorial for tool Y" | `templates/tutorial` | One folder per tool in `tools/<slug>/premium/`. Copy `tools/robots-txt-checker/premium/tool.json` as the start. |
| Reusable scene, brand frame, motion rules | `kit/` | `frame.md`, `MOTION.md`, `BLOCKS.md`, `scenes/`. Tutorials and demos use the full kit. Promos and explainers take only brand truths and a NEW direction each time; check `docs/directions-ledger.md` and do not repeat either of the last two. |

New web UI work also follows the design skills named above. Banned looks for the founder: cream + rust + Playfair, and Inter + purple gradient + default shadcn as a lazy default. Kinetic-type title sequences were rejected; cinematic 3D depth was loved (but client-facing films stay bright).

## Gate 1 / Gate 2 flow (promo, from `templates/promo/BRIEF.md`)

Gate 1, style frames before the full build:
1. Build the B2B cut's s02 (composer and blurred answer card), s07 (the reveal) and s10 (the match cut, answer card to sources) to final quality: `python build.py --cut b2b --only s02,s07,s10`.
2. Snapshot each at 4 points.
3. Render a low-res preview of s01 to s03 plus s07 (hook, then reveal) to `out/preview-reveal.mp4`.
4. Stop and report to the user. Do not build the other scenes until they approve.

Gate 2, full film:
1. Render the B2B cut to `out/promo-b2b.mp4`, then the consumer cut to `out/promo-consumer.mp4`, one at a time, and run `python qa.py --cut <cut>` on each. Target about 2:10 each.
2. Report in at most 12 lines: path, length, QA result, scene start times, weak spots.
3. If the render is killed (memory), say so and do not loop.

Never skip a gate for a new cut or a new direction. Ask before anything outbound (publishing, posting, sending).

## Model split

- Opus: visual styling, scene composition, motion, the pitch and script, QA judgment ("does this look AI-generated"), anything creative or ambiguous.
- Sonnet: mechanical steps (tts, build, snapshot, render, qa runs, file copies, capture runs, fixing a path or a typo).
- Never hand implementation or composition to a model above Opus; do not use the largest model for bulk work.

## Style rules that decide approval (short form; the full text is `docs/STYLE-RULES.md`)

- Bright, professional, Apple-light, start to finish for client-facing films. No dark scenes.
- Product UI is the hero. Use real elements from hyperank.ai (captured crops, rebuilt app screens), never invented abstractions only. Generic silver laptop, no Apple logo. The FULL laptop (base, keyboard, hinge) stays visible in wide shots.
- One idea per beat; at most 2 lifted elements; no mono-label pills, no skeleton lines, no card piles, no opacity crossfades between UIs (use wipes and match cuts).
- Text readable at phone size: at least 22 px at 1080p after any camera push. Supers about 68 to 76 px, Inter 600, one accent word. Never two conflicting numbers on screen.
- Audio: voice dominant (Kokoro af_heart, speed 1.15 for the promo), quiet bed about -26 dB ducked 7 dB under the voice, CC0 SFX on motion starts. No loud music.
- Hard rules: no pricing in the promo; never "no signup" or "no account needed"; never cite a tool count or engine count; no superlatives; no invented customers, testimonials or metrics; third-party stats only with their source line; never show Grok; real brands only as what AI recommends today, tagged "Illustrative", never as a hyperank customer. No em or en dashes on screen or in prose. TTS spelling: "A-I", "Hyper-rank".
- Apply only the change asked. Never re-frame an approved video unasked.

## QA gates (every video, before calling it done)

`hyperframes check` passes; no near-white or black frames; no silence over 0.45 s at -28 dB; no music-only tail; contact sheet reviewed by eye. `qa.py` does the first three and writes the sheet, but looking at the sheet is on you. Run the `verification-loop` skill before reporting done.

## Low-RAM render rules

The target laptop has a 4 GB GPU and tight memory, and Claude Code kills background jobs under memory pressure.
- One render at a time, nothing heavy alongside it, other Chrome windows closed.
- `npx --yes hyperframes@0.8.113 render --workers 1 -o out/<name>.mp4` (each worker is a Chrome, about 256 MB). Use `--quality draft` for previews and the default `standard` for delivery.
- Set `HYPERFRAMES_SKIP_SKILLS=1` in the shell before rendering.
- Do not run `check`, `render`, `preview` or `snapshot` in parallel with another agent's render. Copying, grep, git and `python -m py_compile` are always safe.
- Preview for a human: `npx hyperframes@0.8.113 preview --background`, then `preview --status`, and stop it with `preview --stop`.

## Rules for editing this repo

- Keep `hyperframes@0.8.113` pinned everywhere. Do not bump it without the founder's say.
- Paths: relative to the script (`Path(__file__).resolve().parent`) or `Path.home()` for `~/tools/whisper.cpp` and `~/.cache/hyperframes`. No absolute `C:/Users/...` paths.
- Read and write files with `utf-8` explicitly. Use forward slashes in code.
- Do not commit renders, generated voice, model weights, `.env` files, cookies or session state. `.gitignore` covers them; check before `git add`.
- Do not push to GitHub or create a remote without the founder's explicit yes.
- The tutorial `build.py` copies `templates/tutorial/shared/` into each tool; change shared look there, not per tool.
