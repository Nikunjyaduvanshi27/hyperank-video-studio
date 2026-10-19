# Premium tool tutorials (the approved v3 look, one pipeline)

Making one tool, from `templates/tutorial/` (tool folders live in `tools/<slug>/premium/`; `tools/robots-txt-checker` is the worked example):

1. `python capture.py <tool-url> tools/<slug>/premium/capture/try-<site> <input>` for 2 or 3 candidate inputs (`--then "Tab name"` saves a second tab). Pick the richest real result. Anonymous runs are rate-limited: probe freely, run few.
2. Gated result? `python neo_capture.py <tool-url> <dir> <input> --page <N> [--engines "A,B"]` runs it logged in through the BrowserOS MCP (needs BrowserOS installed and signed in; `neo.py` talks to it). Skip this step if you do not have BrowserOS.
3. Write `tools/<slug>/premium/tool.json`: capture paths (`css`, `result`, optional `gate`, `tab`), `inputs`, optional `toggles`/`open`/`spans`, `engines` for the hook, `marks` (text + `up` levels) and `beats` (hook, name, type, press, fan, gate|result, read..., close). Copy an existing tool.json as the starting point.
4. Write the script to `../../docs/scripts/tutorial-<slug>.md` (pattern: `tutorial-apple-v1.md` section 3). Rules: no em dashes, "A-I" and "Hyper-rank" in TTS, never "no signup", no tool count, claims only from the run.
5. `python tts_batch.py tools/<slug> [tools/<slug2> ...]` (Kokoro af_heart, one process, only changed lines are regenerated).
6. `python build.py tools/<slug>` writes `tools/<slug>/premium/index.html` from `template.html`; voice length sets every beat, SFX and the ducked music bed follow the same clock. Shared fonts, logos, SFX and the music bed are copied in from `shared/`.
7. `cd tools/<slug>/premium && npx --yes hyperframes@0.8.113 snapshot --at <times> --no-end --describe false`; look at the sheet, fix tool.json, rebuild.
8. Render once: `npx --yes hyperframes@0.8.113 render -o out/premium-16x9.mp4` (set `HYPERFRAMES_SKIP_SKILLS=1`).
9. `python qa.py tools/<slug>` (or `sh qa.sh tools/<slug>`): hyperframes check, white-frame gate, silence gate (-28 dB, 0.45 s), writes `out/contact-sheet.jpg`. Look at it before calling it done.

`AGENT-BRIEF.md` is the standing brief for a Claude Code agent preparing tools; `inputs-used.txt` lists demo inputs already used by earlier videos (never reuse one).
