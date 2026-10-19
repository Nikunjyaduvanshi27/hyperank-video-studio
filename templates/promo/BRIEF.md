# hyperank sales promo v3: "Be the answer"

## Why v3 exists
v2 (the earlier v2 render, 2:42) failed the founder on two counts:
1. **It does not look premium.** It reads as AI-generated next to the Celebal film (the Celebal intro film, `templates/intro`).
2. **It does not pitch with impact.** It is a feature tour: 18 scenes, a new visual system in every one, tiny UI, mono label pills everywhere, and no single idea a prospect walks away with.

v3 fixes the pitch with a story and fixes the look with a strict visual system. The script is `script.json`. Use each `vo` verbatim; Kokoro reads `tts`.

## The pitch (one idea, one example, founder 2026-10-19)
**AI is the new shortlist. hyperank gets you mentioned and cited, so buyers find you and become clients.**

**The hook is about YOUR category and uncertainty (founder, 2026-10-19):**
- A buyer asks AI about the category you sell in, and it could be anything. The composer cycles CRM, accounting and project management questions.
- AI answers with a shortlist whose names are BLURRED: is it you, or your competitor? You don't know (s02, s03).
- That's where hyperank comes in (s07).
- s08 un-blurs the answer: that is the product's first value, "now you know".

**TWO FILMS, one build (founder, 2026-10-19).** Both films share every scene, component and motion. Only the content differs, so make the scenes data-driven: one content file per variant.
- **B2B cut, built first:** `script.json`.
  - The buyer asks "Who's the best IT partner for a cloud migration?".
  - The un-blurred answer (s08) names the real Infosys, TCS and Accenture, tagged "Illustrative".
  - Output: `out/promo-b2b.mp4`.
- **Consumer cut:** `script-consumer.json`.
  - The shopper asks "What are the best running shoes for flat feet?".
  - The answer names the real Nike, ASICS and Brooks.
  - s04 and s05 use consumer stats: OpenAI 900M weekly ChatGPT users, and Pew 8% vs 15% clicks. Their source lines are in the script.
  - Output: `out/promo-consumer.mp4`.
- **In both cuts:**
  - The hero is the viewer, "Your brand": missing in s08, named with a yourbrand.com citation in s13, and the click becomes a client (B2B) or a sale (consumer) in s14.
  - Real brands appear only as what AI recommends today, never as a hyperank client.
  - App screens track yourbrand.com, with that cut's three rivals and consistent numbers (Your brand share of voice 9%).

**Interactive device (the founder wants viewers engaged and asking along):**
- Each act opens with a question to the viewer, typed letter by letter into the same glass chat composer, with a blinking cursor:
  - "Is my product in the answer?"
  - "What does AI say about my product?"
  - "Why does AI pick them?"
  - "No team for this?"
  - "What does AI say about my product right now?"
- The voice then answers it.
- Several supers are questions too.
- The composer and the AI answer card it produces are the film's two recurring objects. Same components every time:
  - s01 and s02: the buyer asks about your category, and the answer streams with its names blurred.
  - s03: "You don't know", with the blurred card held.
  - s08: the answer card un-blurs (the cut's three real brands; the 'Your brand' row is empty).
  - s10: the answer card returns and unfolds into its sources.
  - s13: same question, and the answer now names Your brand (the payoff).
  - s14: the click leads to a booked call (B2B) or an order (consumer).
  - s17: the closing question appears beside "Book a call".

**Good text (founder):**
- The on-screen words are the pitch, so they must be large, crisp and well set.
- Supers: Inter at weight 600, about 68 to 76 px, tight tracking.
- Composer text: about 34 px.
- Answer card text: at least 26 px.
- Captions: larger and higher-contrast than in v2.
- No text is ever smaller than 22 px at 1080p unless it is a source line.

**hyperank.ai main-page graphics are heroes** (`assets/img/site/`, re-render at 2x from `capture/home/_render.html` with `capture/capture.py` as needed):
- hero.png: the reveal, s07.
- card-answers.png: s08.
- sources-deciding.png: s10, with the rival labels set to the cut's three brands.
- card-content.png: s11.
- integrations4.png: s12.
- card-analytics.png: s15.
- prompts-stats and audit: optional.

**Structure:**
- Hook (s01 to s03).
- Stakes (s04 to s06).
- Reveal (s07).
- See (s08 and s09).
- Fix (s10 to s12).
- Win (s13 and s14).
- Prove (s15).
- Offer (s16).
- Close (s17 and s18).

The tagline "Be the answer." bookends the reveal and the end card.

## The look: bright and professional, start to finish (founder, 2026-10-19)
**No dark scenes anywhere.** The founder wants the whole film bright because it must look professional.
1. **Problem scenes (s01 to s05):**
   - the bright Apple-light stage with real depth: soft white space, layered planes at different focal depths, depth-of-field blur, soft shadows;
   - glass cards (frosted, violet rim light), official engine marks on focal planes, big violet numbers with a depth shadow;
   - you may borrow the depth and focus-pull ideas from the earlier cinematic 3D example (not in this repo, see `docs/directions-ledger.md`), but render them in daylight, never on a dark background.
2. **The reveal (s06), the signature moment, bright throughout:**
   - the stage clears to white;
   - the hyperank mark draws itself with a soft violet glow;
   - a gentle light sweep crosses the frame;
   - the full silver laptop rises and settles, with a specular sweep across the lid.
3. **Product scenes (s06 to s16):** exactly the Celebal grammar (`../intro/premium/index.html`, `../intro/template.html`):
   - super top centre, full laptop centred, caption bottom;
   - real, designed website content on the screen;
   - one element lifts out of the screen at a time.

## Premium rules (each one is a v2 failure)
1. **Website first.** The hyperank.ai site graphics are professionally designed. They are the hero visuals of the bright world, as the Celebal site was.
   - They live in `assets/img/site/` (hero, card-answers, sources-deciding, card-content, card-analytics, integrations4, prompts-stats, audit, calendar). Re-render any you need from `promo-sales/capture/home/page.html` at deviceScaleFactor 2.
   - Rebuilt app screens (`src/screens/`) appear only where the script names them (s09 Control Center for yourbrand.com), and only pushed in so they read.
2. **Readable at phone size.** Any text the viewer should read is at least 22 px at 1080p after the camera push. Never show a full dense table at wide-shot size as decoration.
3. **No decorative mono label pills.** No letter-spaced uppercase monospace tags such as "SOURCE GRAPH", "AI ANSWER" or "WORKSPACE MEMBERS". They are the strongest AI-slop tell in v2. At most one small label in a scene, only when essential, in sentence case Inter.
4. **One idea per beat:**
   - at most 2 lifted elements on screen;
   - no free-floating card piles;
   - no grey skeleton lines;
   - no translucent stacking;
   - no opacity crossfade between two UIs: use wipes and match cuts.
5. **Light and depth in the bright world:**
   - soft key-light gradient;
   - a contact shadow under the laptop;
   - depth-of-field blur on far layers when a lift is in focus;
   - lifts tilt slightly (rotateX) with a real shadow.
6. **Typography:**
   - supers in Inter at weight 600, tracking -0.035em, about 68 px, centred, one violet accent word;
   - one headline size in every scene;
   - check for double spaces.
7. **Motion:**
   - eases power3.out or expo.out, 0.6 to 0.9 s;
   - a slow continuous camera move in every scene;
   - every reveal lands on its VO word.
8. **Audio:**
   - voice dominant, Kokoro af_heart at speed 1.15, line gap 0.06 s;
   - the same quiet bed and ducking as V26 (about -26 dB, ducked 7 dB);
   - CC0 SFX on motion starts;
   - the s06 reveal gets the one big swell;
   - no loud music (founder rule).

## Hard rules (unchanged)
- No pricing.
- Never "no signup".
- No tool count, no engine count.
- No em or en dashes on screen.
- No superlatives.
- No invented customer results or testimonials. The s13 "after" answer names "Your brand", tagged "Illustrative".
- Third-party stats only as scripted, with their source line.
- Never Grok.
- Real brand names are allowed by the founder: the answer card names each cut's three real brands, tagged "Illustrative". Never make a real company the "you" brand or a hyperank customer.

## Build
- Work in `templates/promo/` (everything the build needs is vendored here: build.py, tts.py, qa.py, src/stage.js, src/stage.css, assets, src/screens).
- HyperFrames pinned: `npx --yes hyperframes@0.8.113`, env `HYPERFRAMES_SKIP_SKILLS=1`. Three.js must be seek-deterministic: drive it from the timeline time, with no clock or random.
- Pronunciation: whisper-check every line with Hyper rank, A-I, G-2, C-R-M, Claude, Perplexity, Copilot. Use `~/tools/whisper.cpp/Release/whisper-cli.exe -m ~/.cache/hyperframes/whisper/models/ggml-small.en.bin`, and convert to 16 kHz mono first.
- QA gates, as `qa.py`:
  - `hyperframes check` passes;
  - no white or black frames;
  - no silence over 0.45 s;
  - a 5x4 contact sheet.

## Gate 1: style frames before the full build
1. Build the B2B cut's s02 (composer and blurred answer card), s07 (the reveal) and s10 (the match cut, answer card to sources) to final quality.
2. Snapshot each at 4 points.
3. Render a low-res preview of s01 to s03 plus s07 (hook, then reveal) to `out/preview-reveal.mp4`.
4. Stop and report. Do not build the other scenes until the EA approves.

## Gate 2: full film
- Render the B2B cut to `out/promo-b2b.mp4`, then the consumer cut to `out/promo-consumer.mp4`, one at a time, and run QA on each. Target about 2:10 each.
- Keep finished films in `out/` (gitignored); never commit renders.
- Report in at most 12 lines: path, length, QA, scene start times, weak spots.
- About 16 GB RAM: render with nothing else heavy running. If the render is killed, say so and do not loop.
