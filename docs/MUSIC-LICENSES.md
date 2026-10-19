# Music licenses

| File | Title | Artist | Source | License | Content ID | Mood use |
|---|---|---|---|---|---|---|
| `audiodollar-ambient-piano-ambient-technology-554832.mp3` | Ambient Piano Ambient Technology | AudioDollar | https://pixabay.com/music/ambient-ambient-piano-ambient-technology-554832/ | Pixabay Content License, https://pixabay.com/service/license-summary/ (commercial use allowed, no attribution required) | Not registered (checked on the track page's schema.org data) | Demo bed, AI-visibility category ("calm cinematic tech") |

Rejected for YouTube safety: Ambient Technology (The_Mountain), Technology Chill (The_Mountain) and six other search hits are
marked "Content ID Registered" on Pixabay, which triggers claims on uploads.

# SFX licenses (premium tutorial, `ai-brand-visibility-checker/premium/assets/audio/sfx/`)

Taken from the brag repo's CC0 bank (https://github.com/latent-spaces/brag, commit `cb89b9f44309b0bf4e3cb89e685fadf80c7999ed`, `skills/brag/assets/sfx/`). brag ships no licence file inside the SFX folder; its `references/audio.md` states the sources, and each upstream page was checked on 2026-10-04. brag's bundled music mp3s are NOT used.

| File | Upstream pack | License (verified on the upstream page) |
|---|---|---|
| `keypress-003/007/011/014/018/021/025/027/030/032.wav` | Keyboard Soundpack #1 by unicae_games, https://opengameart.org/content/keyboard-soundpack-1-typing-and-single-keystrokes | CC0 |
| `click2.ogg`, `mouseclick1.ogg`, `rollover2.ogg` | Kenney UI Audio, https://kenney.nl/assets/ui-audio | CC0 |
| `click_003.ogg`, `bong_001.ogg` | Kenney Interface Sounds, https://kenney.nl/assets/interface-sounds | CC0 |
| `impactSoft_medium_001.ogg`, `impactSoft_medium_004.ogg` | Kenney Impact Sounds, https://kenney.nl/assets/impact-sounds | CC0 |
| `whoosh-soft.wav` | Made here: filtered pink noise rendered with ffmpeg (brag has no whoosh) | Own work, no third-party rights |

# Logo and mark sources (premium tutorial, `premium/assets/img/`)

Each AI-engine mark is the unmodified official file, shown small and only to name the engine (nominative use; no endorsement implied). Only ChatGPT is shown receiving the questions, because this run asked ChatGPT only (`api.json` platforms).

| File | Brand page | Direct asset | Notes |
|---|---|---|---|
| `engines/chatgpt.svg` | https://openai.com/brand/ | https://cdn.openai.com/brand/openai-logos.zip (`OpenAI-logos/SVGs/OAI_OpenAI-Blossom_Black.svg`) | OpenAI Blossom, black |
| `engines/claude.svg` | https://www.anthropic.com/press-kit | same URL (zip), `Claude logos/3 Claude Spark/SVG/Claude Spark - Clay.svg` | Claude Spark, Clay |
| `engines/grok.svg` | https://x.ai/legal/brand-guidelines | https://data.x.ai/logos/SpaceXAI_Grok_Assets.zip (`Grok_Logomark_Dark.svg`) | Guideline: use exactly as provided, only to refer to the service |
| `engines/perplexity.svg` | https://live.standards.site/perplexity/logo (linked from https://www.perplexity.ai/hub/legal) | Perplexity_AllLogos_Final.zip (`Perplexity/Symbol/SVG/perplexity-icon-dark.svg`) | Dark symbol for light backgrounds |
| `engines/gemini.svg` | https://gemini.google/ (official brand kit is login-gated) | https://www.gstatic.com/lamda/images/gemini_sparkle_aurora_33f86dc0c0257da337c63.svg | Weaker source: Google's own product page asset, not a brand kit download |
| `engines/google-ai-overviews.png` | https://developers.google.com/identity/branding-guidelines | https://developers.google.com/static/identity/images/g-logo.png | Google "G" standing in for AI Overviews (no separate product mark), labelled "AI Overviews" |
| `hyperank-logo.png`, `hyperank-mark.png` | https://www.hyperank.ai | https://www.hyperank.ai/_next/static/media/hyperanklogo.0cefb69b.png | hyperank's own mark |
| `notion-favicon.png` | rendered in the real report's competitor row | https://www.google.com/s2/favicons?domain=notion.com&sz=128 | Shown only where the live report shows it |

# Reuse: LLMs.txt Generator premium tutorial (`tutorials/llms-txt-generator/premium/assets/`)

Copied unchanged from the AI Brand Visibility Checker premium project; sources and licenses are the rows above.

| Asset | Used as |
|---|---|
| `audiodollar-ambient-piano-ambient-technology-554832.mp3` (as `audio/music-bed.mp3`) | Score bed, starting 4s into the track (skips the quiet intro), about 20 dB down and dipped under the voice |
| SFX: `keypress-*`, `click2`, `mouseclick1`, `rollover2`, `click_003`, `bong_001`, `impactSoft_medium_001/004`, `whoosh-soft` | Typing, clicks, callouts, transitions |
| `engines/chatgpt.svg`, `gemini.svg`, `perplexity.svg`, `claude.svg`, `grok.svg`, `google-ai-overviews.png` | Hook only, floating around the laptop to name the AI engines; no claim that any of them reads llms.txt |
| `hyperank-mark.png`, `hyperank-logo.png` | Brand bug, rebuilt site header, end card |

Voiceover: generated locally with Kokoro-82M (`npx hyperframes tts`, voice af_heart). No third-party audio beyond the rows above.
