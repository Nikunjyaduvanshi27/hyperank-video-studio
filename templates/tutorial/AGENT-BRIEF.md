# Brief: prepare premium tool tutorials (for a Claude Code agent)

You prepare premium tutorial videos for hyperank.ai free tools in an approved, locked style. You take each of your tools to READY. Rendering is done separately, one tool at a time (`cd tools/<slug>/premium && npx --yes hyperframes@0.8.113 render -o out/premium-16x9.mp4`, with `HYPERFRAMES_SKIP_SKILLS=1`).

- Work from `templates/tutorial/` in this repo (Git Bash; quote paths that contain spaces). Tool folders live in `tools/<slug>/premium/`.
- Invoke these skills with the Skill tool before starting (they do not auto-fire): `hyperframes`, `hyperframes-cli` (snapshot, check), `content-writer` (the voice script).

## Study first (read, never edit)
- `README.md` (steps 1-9), `build.py` (the beat vocabulary: hook, name, type, press, fan, gate, result, read with lifts/push/scroll/click, close; tool.json keys inputs, toggles, open, tab, spans, marks, engines, zoom).
- Finished example kept in this repo: `tools/robots-txt-checker` (the others, such as `chatgpt-visibility-checker` with its logged-in neo capture, engines, gate and fan, are described by their scripts in `../../docs/scripts/`). Each `premium/tool.json` and `../../docs/scripts/tutorial-<slug>.md`.
- Look at a rendered `out/contact-sheet.jpg` to see the look.

## Per tool
1. Probe the page: `python capture.py <url> tools/<slug>/premium/capture`. Read controls.json and page-text.txt.
2. Pick the demo input: try 2-3 real candidates with `python capture.py <url> tools/<slug>/premium/capture/try-<name> <input...>` and pick the richest, most legible real result. Use well-known, neutral real brands, sites or topics (real third-party brands are approved). Check `inputs-used.txt` first and never reuse an input another video used; append `<slug>: <input>` once chosen. Anonymous runs are rate-limited: at most 3 anonymous runs per tool.
3. Result gated or rate-limited? `python neo_capture.py <url> <dir> <input...> --page <YOUR TAB> [--engines "A,B"]` runs it logged in through BrowserOS neo in the hyperank.ai profile; it refuses unless chrome://version shows Profile 1.
   - Use ONLY your own tab number. Never touch any other tab.
   - Read-only: only run free tools and read results. Never create, edit or delete sites, settings or account data. Never enter credentials.
   - If it refuses (wrong profile), do not try to switch profiles. Capture anonymously if possible, otherwise mark BLOCKED, and say so in your report.
4. Write `tools/<slug>/premium/tool.json` (start from the closest example). Shape: hook, name, type, press, (fan when the tool fans out), gate or result, 2-4 read beats with lifts or pushes on the real result, close. Aim for 35-50 s.
5. Write `../../docs/scripts/tutorial-<slug>.md` (pattern: `../../docs/scripts/tutorial-apple-v1.md` section 3 and the finished tutorial-*.md files).
6. `python tts_batch.py tools/<slug>` then `python build.py tools/<slug>` (it prints beat starts).
7. Snapshot: `cd tools/<slug>/premium && HYPERFRAMES_SKIP_SKILLS=1 npx --yes hyperframes@0.8.113 snapshot --at <t1,t2,...> --no-end --describe false` at mid-points of every beat. Read the PNGs. Fix tool.json and rebuild until:
   - every lift and push lands on the intended element and is readable at phone size;
   - supers never overlap; no blank or near-white frame; the full laptop is visible in wide shots;
   - no two conflicting numbers on screen.
8. `python qa.py tools/<slug>` (without an mp4 it runs `hyperframes check`) must print PASS. Then `touch tools/<slug>/premium/READY`. If you change a READY tool later, rebuild and touch READY again.

## House rules (founder, non-negotiable)
- Super: 2-5 words with exactly one `|accent|` word. VO: short and plain, one idea per line.
- `tts` lines: write "A-I", never "AI"; "Hyper-rank" for hyperank; spell files and acronyms phonetically ("robots dot t-x-t", "L-L-M-s dot t-x-t", "S-S-L", "X-M-L", "R-S-S", "U-R-L", "four-oh-four"). `vo` (the captions) keeps normal spelling.
- NEVER say or show "no signup", "no account needed", "no login" or similar. Never cite a tool count. No em dashes anywhere.
- Every claim comes from the captured run or page. No invented metrics, no superlatives about the result.
- Close beat exactly: `{"type": "close", "vo": "Free to run. Hyper-rank dot A-I."}` (the end card carries "Full report with a free account." and hyperank.ai).
- Never change the look: do not edit anything in `` (except appending to inputs-used.txt) or any other tool's folder. If build.py cannot handle a tool (no `main form`, no `[aria-live]` result region, an interaction the pipeline lacks), write `tools/<slug>/premium/BLOCKED.md` with the exact cause and the smallest pipeline feature that would fix it, then move to your next tool.
- Sibling agents prepare similar tools in parallel. Make each of your videos distinct: a different hook angle, demo input and callouts.
- Pronunciation risk (brand names, Grok, Yandex, Perplexity, Claude): convert a line with `ffmpeg -y -i vo-NN.wav -ar 16000 -ac 1 <scratch>.wav` and check it with `~/tools/whisper.cpp/Release/whisper-cli.exe -m ~/.cache/hyperframes/whisper/models/ggml-small.en.bin -f <scratch>.wav`; adjust the tts spelling if it is misheard.

## Final report (at most 15 lines, no process narration)
Per tool: READY or BLOCKED (exact reason), demo input, length D, neo used yes or no, and anything weak or needing the founder's call.
