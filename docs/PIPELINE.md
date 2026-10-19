# hyperank video pipeline

> Repo map: this file was written in the original `hyperank-videos` workspace. In this repo `kit/` is `kit/`, `brief/product-brief.md` is `docs/product-brief.md` (plus the 2026-10-18 refresh), tutorials are `templates/tutorial`, the laptop intro is `templates/intro`, the promo is `templates/promo`, and example scripts are `docs/scripts/`. Examples named `examples/a-cinematic` and `smoke-test/` were not carried over.

One spine, three outputs. Every video (promo, explainer, tutorial) runs through the same
stages and reads the same kit, so the brand compounds instead of being re-invented per video.

```
brief/ + kit/  ->  1 script  ->  2 voice  ->  3 footage  ->  4 compose  ->  5 captions  ->  6 QA  ->  7 render
```

## Kit vs fresh direction

- **Tutorials and demos** use the full kit (`kit/frame.md`, `MOTION.md`, `scenes/`): a series must look like one series.
- **Promos and explainers** get a NEW visual direction every time (3D, kinetic type, etc.). They take only the
  brand truths from the kit: the hyperank.ai name, violet `#5e4bf6` as an accent, and the claims rules. Before
  choosing a direction, read `directions-ledger.md` and do not repeat either of the last two directions.
  After delivery, append one row: date, video, direction name, display font, verdict.

## Shared inputs

| Path | What it is | Rule |
|---|---|---|
| `brief/product-brief.md` | Scraped hyperank.ai copy, features, pricing tiers, brand tokens | Only claims in here may appear on screen or in narration. No invented metrics, testimonials or logos. |
| `kit/frame.md` | HyperFrames design spec (colors, type ramp, components) | Copied into every project as `frame.md`. Frontmatter values are law. |
| `kit/MOTION.md` | Easings, durations, staggers, signature move | Every animation uses these; no ad-hoc easing. |
| `kit/BLOCKS.md` | Official registry blocks we use, re-skinned to our tokens | Check here before hand-building any visual. |
| `kit/scenes/` | Reusable sub-compositions: engine-fanout (signature), logo-sting, cta-endcard | Copied in, never rebuilt. New recurring scenes get added here. |

## Stages

| # | Stage | Tool | Model / owner |
|---|---|---|---|
| 1 | Script + beat plan | `media-content-strategist` (hook, structure), `copywriting` skill, `hyperframes-creative` (narration, beats) | Opus |
| 2 | Voice, per scene | `npx hyperframes tts` (local Kokoro). Write the brand as "Hyper-rank" for TTS. Chatterbox (MIT) later if we clone the founder's voice. | Sonnet |
| 3 | Footage | Promo: `npx hyperframes capture https://hyperank.ai`. Tutorial: Recordly (manual) or a scripted Playwright run (featurecast / demowright) against a demo account. Explainer: none, motion only. | Sonnet |
| 4 | Compose | Promo: `product-launch-video`. Explainer: `faceless-explainer`. Tutorial: `general-video` with screen clip + `ui-focus-zoom` / `cursor-zoom-follow`. All load `kit/frame.md` + `kit/scenes/`. | Opus |
| 5 | Captions | `npx hyperframes transcribe` (whisper.cpp small.en, word timestamps) -> caption style from `kit/BLOCKS.md` | Sonnet |
| 6 | QA | `npx hyperframes check` + `snapshot`, then `design-critic` (does it look generic?) before any final render | Opus |
| 7 | Render | Draft while iterating, `--quality high` for delivery. 16:9 master, 9:16 and 1:1 variants. `render --batch` with variables for per-feature / per-engine versions. | Sonnet |

Taste checks at stage 6 (the portable subset of `taste-skill`; its web-only rules and its
Instrument Serif / purple default bans do not apply, those are our real brand):
- Zero em-dashes or en-dash separators in any on-screen string.
- Max one uppercase mono eyebrow per three scenes.
- Re-read every visible string: nothing broken, cute-but-wrong, or fake-precise.
- Every animation justified in one sentence; nothing moves just to move.
- One accent, one radius system, one theme across the whole video.
- CTA text at WCAG AA contrast.

Audio drives time: voice is generated before composing, and scene durations come from the
voice files, not the other way round.

## Why this order of videos

1. **Promo (30-60s)** first: needs no login, proves the kit end to end.
2. **Explainer (60-90s)**: "what is AI visibility", reuses engine-fanout heavily.
3. **Tutorial series**: needs a demo account on app.hyperank.ai; scripted recording means a UI change is a re-run, not a re-shoot.

## Leverage

- One promo template + `render --batch` = a variant per feature, per engine, per persona.
- Every new recurring scene goes back into `kit/scenes/`, so video N+1 is cheaper than video N.
- Tutorials recorded from a script stay current when the app changes.

## Machine notes

Windows 11, RTX 3050 4GB. Render Chrome is HyperFrames' own (v152). whisper.cpp at
`~/tools/whisper.cpp/Release` (on user PATH). Kokoro via pip `kokoro-onnx`.
