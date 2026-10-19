# Video stack: decisions and lessons

Toolchain chosen for hyperank.ai tutorial, explainer and promo videos (October 2026). Built for a 4 GB RTX 3050 laptop, so memory is tight: one render at a time, nothing heavy alongside it.

## Decisions

- Composer: HyperFrames (Apache-2.0, no headcount fee). Remotion only as a fallback (free only up to 3 employees). The CLI is pinned to `hyperframes@0.8.113` on purpose so films re-render identically. Do not bump it without a founder decision.
- Voice: HyperFrames' built-in local Kokoro (`npx hyperframes tts`, pip `kokoro-onnx soundfile`). Kokoro-FastAPI and "Kokoro Studio" GUIs are redundant. Chatterbox (MIT) is the fallback if voice cloning or emotion is needed. F5-TTS, IndexTTS and Fish Speech are non-commercial: skip.
- Captions and pronunciation checks: whisper.cpp prebuilt `whisper-bin-x64.zip` (release b5130) in `~/tools/whisper.cpp`, model `ggml-small.en.bin` in `~/.cache/hyperframes/whisper/models`. The model is downloaded by hand because the CLI's 30 s download timeout fails on it. Parakeet is Apple-only.
- Recording: Recordly (manual, AGPL, app use is fine) for tutorials. featurecast and demowright for scripted re-recordable demos are unproven (0 to 13 stars).
- Render Chrome: HyperFrames uses its own Chrome (152 at the time) under `~/.cache/hyperframes/chrome`. A stray puppeteer chrome-headless-shell 131 on the machine broke renders; if renders misbehave, check that nothing else shadows it.
- HyperFrames skills are the v0.8.113 set (`npx hyperframes skills update ...`). They are vendored in this repo under `skills/`.
- Ecosystem borrow list: official registry blocks (ai-answer-rank, ui-focus-zoom, caption-*), heygen-com/hyperframes-launches (structure refs), tugrawork-creator/saas-motion-kit, nateherkai/hyperframes-student-kit, nutllwhy/hyperframes-motion-library (MIT, patterns only). The brand kit is `kit/` (frame.md, MOTION.md, BLOCKS.md).
- Founder preference: every promo or explainer is a NEW, immersive visual direction; the kit is only for tutorials and demos. Rotation is tracked in `directions-ledger.md`. Styling and composition work goes to Opus (founder's call), mechanical steps to Sonnet.

## Brand and voice facts

- Kokoro reads "Hyperank" badly (whisper heard "HyperAnk"). Write it phonetically as "Hyper-rank" in TTS lines, and "A-I" for AI.
- Brand: violet `#5e4bf6`, ground `#f0eee9`, ink `#1f1e1b`, Instrument Serif / Inter / JetBrains Mono. The site has no testimonials or real metrics; never invent them.
- Never cite a tool count. Never say "no signup".

## Pipeline lessons

- Capture pages are hidden tabs: no page `setTimeout` (throttled) and entrance styles stay at opacity 0, so the capture script has to settle them itself.
- Run one logged-in capture at a time, with a gap between runs and backoff on rate limits.
- Never shrink a tool with zoom below 0.9 (white frames, unreadable). Scroll the form instead.
- Claude Code kills background jobs under memory pressure. Close spare browser windows before a render.
- Some tool pages can fail on the hyperank backend itself ("couldn't finish just now", "busy right now"). That is not a pipeline bug; write `BLOCKED.md` in the tool folder and move on.
- Sales promo: the product source of truth is the app repo `github.com/Nikunjyaduvanshi27/hyperank-app`, not the website. The app queries 7 engines (ChatGPT, Claude, Gemini, Perplexity, Copilot, AI Overviews, Meta AI). Grok is NOT live despite site copy, so never show Grok. Social Sentiment is flag-off. When there is no app login, rebuild app screens from the repo source with a fictional brand (that is what `templates/promo/appkit.py` does).
- Sales promo brief from the founder: a 2:30 to 3:00 client-facing film, laptop plus motion graphics, real logos and graphics, mixed audience, CTA "Book a call" then "Check your brand free". No pricing in the video.
