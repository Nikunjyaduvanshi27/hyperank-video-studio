# promo-01: "None of them is you"

Status: draft v1, script and beat plan only. Feeds stage 1 of `PIPELINE.md`, then `product-launch-video` Step 3 (`STORYBOARD.md` + `SCRIPT.md`).
Master: 16:9 (1920x1080). Cut: 9:16 (1080x1920). Target runtime: about 47s.
Only source of claims: `brief/product-brief.md`. Section references below (B1, B3...) point to its numbered sections.

---

## 1. Angle and viewer

**Angle:** Your buyers ask AI who to buy from, and six engines name your competitors. hyperank shows you what they say and which sources to fix, and it is honest that the answer moves over weeks, not days.

**Target viewer:** the person who owns pipeline or brand at a marketing team or agency (SaaS, fintech, ecommerce first). They have SEO covered and have never checked what ChatGPT says about them. ("Most brands have never checked." B2)

**Arc:** PAS, compressed. Hook, shift, promise, three proof beats (see, change, publish), honest payoff, CTA.

**The one action at the end:** Check your brand free at hyperank.ai.

---

## 2. Hook options (first 3 seconds)

| # | Spoken line | Type | Visual (first frame already moving) | Source |
|---|---|---|---|---|
| A | "Every engine has an answer. None of them is you." | Contrast, names the viewer's loss | engine-fanout: buyer question already typing, fans out to six answer cards, each "Recommends Competitor A/B/C", none violet | Hero headline, B1 |
| B | "Ask AI who to buy from in your category. Is it you?" | Direct question | Prompt typing in a bare composer, cursor blinks on submit | Paraphrase of B2 "situation" |
| C | "Your buyers stopped clicking. They started asking." | Category shift | Ten blue links collapse into one answer card | "01 / The situation", B2 |

**Recommended: A.**
- It is the homepage hero line, so a viewer who clicks through lands on the exact sentence they just heard. Message match from video to page is free here.
- It maps one to one onto the signature scene: six cards land, none of them is the viewer. Words and picture make the same point at the same moment.
- Ten words, stakes about the viewer, no feature vocabulary.

B is the variant to test in 9:16 feed placements, where a question reads natively. C is too abstract for a cold open (a trend, not a loss) and is folded into scene 2 instead.

---

## 3. Final script and beat plan

Display spelling: lowercase "hyperank" on screen, matching the wordmark. Spoken count: 110 words. At 2.5 words per second that is about 44s of speech, about 47s with the CTA hold.

Kit scenes live in `kit/scenes/` (engine-fanout, logo-sting, cta-endcard). `kit/MOTION.md` and `kit/BLOCKS.md` did not exist when this was written: blueprint ids below are candidates from the product-launch blueprint bank and must be confirmed against `kit/BLOCKS.md` at Step 4. Captures come from `npx hyperframes capture https://hyperank.ai`; filenames are not known until capture runs, so captures are named by site section.

| # | Time | Beat | Words |
|---|---|---|---|
| 1 | 0.0 to 4.0s | Hook | 10 |
| 2 | 4.0 to 10.5s | Shift | 16 |
| 3 | 10.5 to 14.5s | Promise + brand | 10 |
| 4 | 14.5 to 22.5s | See | 20 |
| 5 | 22.5 to 30.5s | Change | 20 |
| 6 | 30.5 to 37.0s | Publish | 17 |
| 7 | 37.0 to 40.5s | Honest payoff | 7 |
| 8 | 40.5 to 47.0s | CTA + hold | 10 |

Timings are guides. Audio drives time: real scene lengths come from the TTS files.

### Scene 1: Hook (0.0 to 4.0s)

**VO:** "Every engine has an answer. None of them is you."

**On screen:**
- Question card typing from frame 1 (no logo, no fade-from-black): `Best accounting software for a small agency?` (illustrative buyer question; make it a `render --batch` variable per industry page: SaaS, Fintech, Ecommerce, News and media, Travel and lifestyle)
- Six answer cards fan out, each an engine chip plus `Recommends Competitor A` / `B` / `C`: ChatGPT, Gemini, Perplexity, Claude, Grok, Google AI Overviews.
- Headline lands with the last card: `Every engine has an answer.` / `None of them is you.` (second sentence in violet italic Instrument Serif, as on the site)

**Uses:** `kit/scenes/engine-fanout`, first half only (fan-out, no violet light-up yet). Engine logos via `/media-use resolve --type logo`, never redrawn.
**Sync:** "Every engine has an answer" over the fan-out; "None of them is you" lands as the sixth card settles.
**Transition out:** continuity handoff; the cards stay on screen into scene 2.

### Scene 2: Shift (4.0 to 10.5s)

**VO:** "Your buyers stopped clicking. They ask AI, and act on the one answer that comes back."

**On screen:**
- Eyebrow (JetBrains Mono): `01 / The situation`
- The six cards collapse into one answer card naming `Competitor A` and `Competitor B` ("That answer names two or three companies", B1 About).
- Line: `The shortlist is made before anyone visits a website.` (B2, verbatim)

**Uses:** engine-fanout cards carried over (handoff from scene 1); blueprint candidate `kinetic-type-beats` for the line.
**Transition in:** crossfade (same world). **Out:** zoom-through (section boundary into the brand).

### Scene 3: Promise + brand (10.5 to 14.5s)

**VO:** "hyperank shows you what six engines say about your brand."

**On screen:** violet H mark and `hyperank.ai` wordmark; tagline `See what AI says about your brand` (nav tagline, B1).

**Uses:** `kit/scenes/logo-sting`. Logo from the official asset URLs in B6.
**Transition in:** zoom-through.

### Scene 4: See (14.5 to 22.5s)

**VO:** "Every question, every engine, every day. Each answer kept word for word, checked for accuracy, with who got recommended instead."

**On screen:**
- Eyebrow `03 / What you can see`, headline `Every answer, kept word for word` (`word for word` violet italic)
- Answer-archive rows land one per cue, each with an engine chip and a date stamp, flags only, no counts:
  - `Not named` / `Competitor A recommended instead`
  - `Quotes a price you retired` (B3 verbatim)
  - `Named`

**Uses:** site capture, homepage section 03 "Every answer, kept word for word", as the base. Rebuild only the rows component from kit tokens (blueprint candidate `agent-progress-theater`: rows land and flag as the VO names them). The live demo rows show a real competitor name ("Profound") and "x/6 mentioned" mock ratios; both must be masked or rebuilt out. The brief also notes lower sections captured blank because of scroll-triggered animation; if the capture is blank, rebuild that card from kit tokens and the B3 copy.
**Sync:** "word for word" on the first row, "accuracy" on the price row, "recommended instead" on the competitor flag.
**Transition in:** crossfade.

### Scene 5: Change (22.5 to 30.5s)

**VO:** "You can't edit an AI answer. You can edit the sources it's built from. hyperank shows which ones you're missing."

**On screen:**
- Eyebrow `04 / What you can change`, headline `Fix the sources, not the symptoms.` (`not the symptoms` violet italic)
- Split: left `Cited for them` (a comparison page, a forum thread, a review site), right `Cited for you` (shorter list). The difference resolves into rows tagged `Missing`. (Gap analysis, B3; the source types come from "Outranked", B2.)

**Uses:** site capture, homepage section 04 (Source Graph) for reference; blueprint candidate `comparison-split`. Domains shown as source types, not invented real domains.
**Sync:** "can't edit" on a locked answer card, "sources" as the split opens, "missing" as the tags land.
**Transition in:** push-slide LEFT.

### Scene 6: Publish (30.5 to 37.0s)

**VO:** "Then it drafts them from your own material, and a named approver signs off before anything publishes."

**On screen:**
- Eyebrow `05 / What you can publish`, headline `Make the sources you are missing` (`you are missing` violet italic)
- One draft card (type `Comparison`) moves `Draft` to an approver sign-off stamp to `Scheduled`, inside the calendar surface.

**Uses:** site capture, homepage section 05 (Content Engine, Auto-Pilot calendar); blueprint candidate `device-surface-showcase`. Crop out the "Publish automation: Autopilot" label: it fights the "named approver" line even though the site shows it.
**Sync:** "drafts" on the card appearing, "named approver" on the stamp, "publishes" on `Scheduled`.
**Transition in:** push-slide LEFT. **Out:** zoom-through back to the fan-out.

### Scene 7: Honest payoff (37.0 to 40.5s)

**VO:** "The answer follows. Over weeks, not days."

**On screen:** the same question and the same six cards from scene 1. Your brand's citation lights up in violet in one card, then a second. Not all six. Mono label: `Over weeks, not days.`

**Uses:** `kit/scenes/engine-fanout`, second half (violet light-up). Lighting one or two cards rather than six is deliberate: the site says changing answers "takes weeks, not days" and that anyone promising direct control "is overselling" (B3 FAQ). The restraint is the credibility.
**Transition in:** zoom-through.

### Scene 8: CTA (40.5 to 47.0s)

**VO:** "Check your brand free at hyperank.ai. Full report with a free account."

**On screen:** button `Check your brand free`, URL `hyperank.ai`, sub-line `Full report with a free account.` Hold about 2s after the VO ends.

**Uses:** `kit/scenes/cta-endcard`.
**Transition in:** crossfade.

---

## 4. TTS lines (Kokoro)

The brand is written "Hyper-rank" because Kokoro mispronounces "Hyperank"; "AI" is spelled out. Each block is one line for `SCRIPT.md`; the indented text is the only part fed to TTS.

**Voice:** Kokoro, `am_michael` (pipeline default) unless Nikunj picks another.
**Voice direction:** a founder talking to a peer. Unhurried, plain, slightly dry. No announcer lift, no smile on the CTA.

Line 1, Hook (Scene 1)

    Every engine has an answer. None of them is you.

Line 2, Shift (Scene 2)

    Your buyers stopped clicking. They ask A I, and act on the one answer that comes back.

Line 3, Promise (Scene 3)

    Hyper-rank shows you what six engines say about your brand.

Line 4, See (Scene 4)

    Every question, every engine, every day. Each answer kept word for word, checked for accuracy, with who got recommended instead.

Line 5, Change (Scene 5)

    You can't edit an A I answer. You can edit the sources it's built from. Hyper-rank shows which ones you're missing.

Line 6, Publish (Scene 6)

    Then it drafts them from your own material, and a named approver signs off before anything publishes.

Line 7, Payoff (Scene 7)

    The answer follows. Over weeks, not days.

Line 8, CTA (Scene 8)

    Check your brand free, at Hyper-rank dot A I. Full report with a free account.

Listen-test lines 3, 5 and 8 before composing. If "Hyper-rank" still lands as "hyper-ank", try "Hyper rank" (space) next.

---

## 5. CTA

`Check your brand free` at `hyperank.ai`, with `Full report with a free account.`

- The label is the site's primary CTA, verbatim (B1).
- Founder rule (2026-10-05): never say "no signup"; hyperank has signup.
- Not used: the closing-section line "One check, four engines, about twenty seconds". It conflicts with "six engines" everywhere else (flagged in B7). Leave it out until confirmed.
- No price, plan or "free trial" language: plans are custom-quoted (B4).

---

## 6. 9:16 cut notes

- engine-fanout goes from a 3x2 grid to 2x3, with the question card on top. The hook headline sits in the centre-safe area.
- Keep the bottom band and right rail clear for platform UI. Take the current safe-zone and export specs from each platform's own docs at cut time, not from memory.
- Scenes 4 to 6: crop to the single UI card (rows, split, draft card) and drop the eyebrow if space runs out. Keep the headline.
- Captions (stage 5) go above the platform UI band, never over the answer cards' text.

---

## 7. Quality gates (stage 6 must pass all of these)

1. Every on-screen string traces to `brief/product-brief.md` or is marked illustrative here (buyer question, Competitor A/B/C placeholders, which are the site's own convention).
2. No numbers from the homepage dashboard mockups anywhere in frame: no x/6 ratios, percentages, session counts or audit scores.
3. No real competitor names in frame. Mask "Profound" in any capture of section 03.
4. Exactly six engines (ChatGPT, Gemini, Perplexity, Claude, Grok, Google AI Overviews). The site's hero shows a Copilot chip; it must not appear in engine-fanout.
5. No customer names, logos, testimonials, results or prices.
6. The violet light-up in scene 7 covers one or two cards, not six.
7. No em-dashes in on-screen text or captions. No "unlock", "supercharge", "game-changer".
8. Engine marks come from `/media-use` official sources, used as identification only.
9. Mix: voice first, music ducked under it (calm minimal underscore, no drops), loudness normalised to each destination's published target.
10. `design-critic` pass on the contact sheet before any `--quality high` render.

Nothing here publishes. The render goes to review first.
