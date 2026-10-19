---
version: v1
name: hyperank.ai Frame (video / frame layer)
description: >
  Video-first companion to the hyperank.ai design system (the site's .ds-theme stylesheet). The unit
  is the frame (1920x1080). Atoms are sacred: warm ground #f0eee9, ink #1f1e1b, one violet
  (#5e4bf6) carrying every accent, Instrument Serif display with exactly one italic violet phrase,
  Inter for UI and body, JetBrains Mono for numbered eyebrows. White glass cards with the site's
  violet-tinted elevation, concentric orbit rings, engine names as text-only chips. Composition and
  frame scale rewritten for video. Motion lives in MOTION.md.
unit: the frame, 1920x1080 primary; 9:16 and 1:1 documented
principle: atoms are sacred, composition is free, every number has a source
source: https://www.hyperank.ai compiled CSS (.ds-theme), hero markup, login screen; fetched for this kit

colors:
  ground: "#f0eee9"          # --color-ground, every frame
  surface: "#ffffff"         # --color-surface, cards
  neutral-50: "#faf9f7"      # chip fill
  neutral-100: "#f3f1ec"
  sunken: "#e7e4dc"          # --color-sunken / --color-line
  line: "#e7e4dc"
  line-strong: "#d6d2c7"     # wires, chip borders, rules
  ink: "#1f1e1b"             # headlines, names
  ink-soft: "#2e2c25"        # answer lines, pill labels
  neutral-700: "#434036"     # chip labels, hex codes
  muted: "#5a564b"           # body, microcopy, footers
  faint: "#767161"           # decorative only (4.21:1 on ground, under AA)
  faint-2: "#a8a292"         # decorative only
  violet: "#5e4bf6"          # --color-brand / accent / brand-600: THE accent
  violet-lift: "#7b6bf8"     # brand-500, glow tint, site button fill
  violet-deep: "#4d3eca"     # brand-700, mono eyebrows
  brand-200: "#cfc9fc"       # dots on violet, node halo
  brand-300: "#b7aefb"       # orbit rings
  brand-400: "#968af9"
  violet-pale: "#e7e4fe"     # brand-100, node halo, tints
  violet-tint: "#efedfe"     # brand-50
  brand-800: "#3c309d"
  brand-900: "#2b2371"       # shadow tint inside CTA
  brand-950: "#1c174a"       # rgba(28,23,74,a) is the site's shadow ink
  flag-bad: "#dc5a4b"        # accuracy flags, inline only
  flag-warn: "#e0a32e"
  flag-ok: "#2e9e6b"

radii:
  control-web: "6px"         # site rounded-md buttons
  control: "12px"            # CTA at frame scale (web 6px scaled with 15px -> 34px type)
  chip: "14px"               # engine card outer (site rounded-[14px])
  chip-inner: "13px"
  panel: "14px"              # --radius-panel
  well: "16px"               # --radius-well, question node, large cards
  pill: "999px"              # source chips, engine pills
  circle: "50%"              # index dots, node, rings

shadows:
  e1: "0 1px 2px rgba(28,23,74,0.06), 0 1px 3px rgba(28,23,74,0.05)"
  e2: "0 1px 2px rgba(28,23,74,0.06), 0 10px 22px -10px rgba(28,23,74,0.18)"
  e3: "0 2px 4px rgba(28,23,74,0.06), 0 22px 44px -18px rgba(28,23,74,0.26)"
  e4: "0 4px 8px rgba(28,23,74,0.07), 0 44px 80px -32px rgba(28,23,74,0.36)"
  engine-chip: "0 2px 4px rgba(28,23,74,0.1), 0 24px 48px -22px rgba(28,23,74,0.45), 0 0 44px -18px rgba(94,75,246,0.7)"
  violet-glow: "0 0 90px -8px rgba(94,75,246,0.65)"      # site: 0 0 90px -8px #5e4bf6a6
  pill: "inset 0 1px 0 rgba(255,255,255,0.8), 0 16px 36px -22px rgba(28,23,74,0.55)"
  cta: "inset 0 2px 0 rgba(231,228,254,0.45), inset 0 -20px 36px -24px rgba(43,35,113,0.5), 0 20px 56px -12px rgba(43,35,113,0.55)"  # site CTA, doubled for frame scale

typography:
  # display ramp: Instrument Serif 400 only, -0.02em (site h1/h2)
  display:      { fontFamily: "Instrument Serif", cqw: 7.3, weight: 400, lineHeight: 0.98, tracking: "-0.02em", color: "ink" }
  headline:     { fontFamily: "Instrument Serif", cqw: 5.4, weight: 400, lineHeight: 1.02, tracking: "-0.02em", color: "ink" }
  headline-sm:  { fontFamily: "Instrument Serif", cqw: 4.1, weight: 400, lineHeight: 1.02, tracking: "-0.02em", color: "ink" }
  wordmark:     { fontFamily: "Instrument Serif", cqw: 9.4, weight: 400, lineHeight: 1.05, tracking: "-0.02em", color: "ink" }
  accent-italic:{ fontFamily: "Instrument Serif", italic: true, weight: 400, size: "same as its line", color: "violet" }
  # reading / UI ramp: Inter
  title-ui:     { fontFamily: "Inter", cqw: 1.56, weight: 600, lineHeight: 1.15, tracking: "-0.01em", color: "ink" }
  body:         { fontFamily: "Inter", cqw: 1.3, weight: 400, lineHeight: 1.4, color: "ink-soft" }
  label:        { fontFamily: "Inter", cqw: 1.2, weight: 500, lineHeight: 1.4, color: "ink-soft" }
  pill:         { fontFamily: "Inter", cqw: 1.04, weight: 600, color: "ink-soft" }
  button:       { fontFamily: "Inter", cqw: 1.77, weight: 600, tracking: "-0.01em", color: "surface" }
  # chrome ramp: JetBrains Mono, uppercase
  eyebrow:      { fontFamily: "JetBrains Mono", cqw: 1.04, weight: 500, tracking: "0.22em", upper: true, color: "violet-deep" }
  meta:         { fontFamily: "JetBrains Mono", cqw: 0.94, weight: 500, tracking: "0.14em", upper: true, color: "muted" }
  chip:         { fontFamily: "JetBrains Mono", cqw: 0.83, weight: 500, tracking: "0.12em", upper: true, color: "neutral-700" }

fonts:
  files: "assets/fonts/ (Google Fonts latin woff2, OFL): InstrumentSerif-400, InstrumentSerif-400-italic, Inter-var (100-900), JetBrainsMono-var (100-800)"
  rule: "declare @font-face inside every composition / sub-composition template; never rely on the implicit Google fetch"

spacing:
  pad-edge: "5cqw"           # 96px; also the top/bottom inset is 8.9cqh (96px)
  gap-lg: "2.5cqw"
  gap-md: "1.1cqw"
  gap-sm: "0.6cqw"
  card-gap: "22px"           # between stacked engine cards

components:
  question-node:
    backgroundColor: "{colors.surface}"
    border: "1px solid {colors.line}"
    rounded: "{radii.well}"
    shadow: "{shadows.e4}"
    typography: "{typography.meta} label with a violet dot, then {typography.headline-sm}"
    description: "The buyer's question. Left-anchored, it owns the frame's left third. One per frame."
  engine-card:
    wrapper: "1.5px padding, linear-gradient(145deg, rgba(255,255,255,0.95), rgba(183,174,251,0.6) 44%, rgba(28,23,74,0.18)), rounded {radii.chip}"
    inner: "rgba(255,255,255,0.82), rounded {radii.chip-inner}"
    shadow: "{shadows.engine-chip}"
    typography: "mono index dot (01-06) + {typography.title-ui} engine name + {typography.label} answer line + source chip"
    description: "The site's hero chip at frame scale. Engine name is TEXT ONLY; the logo slot becomes a mono index."
  engine-card-lit:
    border: "2.5px solid {colors.violet}"
    shadow: "{shadows.violet-glow}"
    description: "The cited state. Index dot fills violet, chip becomes violet 'CITED', answer line becomes 'Cites <name>' with the name in accent-italic."
  source-chip:
    backgroundColor: "{colors.neutral-50}"
    border: "1.5px solid {colors.line-strong}"
    rounded: "{radii.pill}"
    typography: "{typography.chip}"
  connector:
    stroke: "2px {colors.line-strong}; lit: 3.5px {colors.violet}, round caps"
    description: "Cubic from the question node to each card's left edge, ending in a white dot. Only connectors that link two real elements."
  orbit-rings:
    stroke: "1.5px {colors.brand-300} at 0.7 / 0.5 / 0.32 opacity"
    description: "The site's concentric rings. Centred on the focal object (question node, mark, CTA orbit)."
  violet-glow:
    background: "radial-gradient(closest-side, rgba(123,107,248,0.22), rgba(123,107,248,0.08) 55%, transparent)"
    description: "One per frame, behind the focal object. The depth layer; a flat ground reads as a template."
  grain:
    background: "feTurbulence noise, ink-tinted, 0.35 opacity, multiply"
    description: "On every full frame. Light grounds need texture."
  cta-button:
    backgroundColor: "{colors.violet}"
    border: "1.5px solid rgba(183,174,251,0.4)"
    rounded: "{radii.control}"
    shadow: "{shadows.cta}"
    typography: "{typography.button}, leading {colors.brand-200} dot"
    description: "The only solid violet block. One per frame, closing frames only. Fill is #5e4bf6 (not the site's #7b6bf8) so white text passes AA."
  engine-pill:
    backgroundColor: "rgba(255,255,255,0.82)"
    border: "1px solid {colors.surface}"
    rounded: "{radii.pill}"
    shadow: "{shadows.pill}"
    typography: "{typography.pill} with a violet dot"
  lockup:
    elements: "assets/hyperank-mark.png + 'hyperank.ai' in Instrument Serif, ink"
    description: "Small lockup bottom-left or top-left on content frames; full lockup only in the sting."
---

# hyperank.ai Frame (video / frame layer)

## Overview

hyperank at frame scale is an **evidence-first editorial system**: a warm paper ground, one ink, and
one violet that only ever means "this is where you appear". The product's whole story is that six
engines answer a buyer's question and the brand is missing; the visual system is built so violet
can be withheld and then spent. Calm, sourced, no hype, the register of the site's own copy ("Every
number on this site has a source").

Three faces in fixed roles: **Instrument Serif** (weight 400 only, tight, -0.02em) for every
statement, with **exactly one italic violet phrase** per frame, the site's signature from "Every
engine has an answer. *None of them is you.*"; **Inter** for engine names, answers and UI;
**JetBrains Mono** uppercase at 0.22em for numbered eyebrows and metadata. Depth is the site's own:
white glass cards with violet-tinted shadows, concentric orbit rings, one radial violet glow.

**Key characteristics at frame scale:**

- **Warm ground #f0eee9** on every frame, with grain and one violet glow. Never white, never dark.
- **One violet** (#5e4bf6) carries the accent: the italic phrase, the lit connector, the cited chip, the CTA.
- **Instrument Serif statements**, one italic violet phrase; Inter for UI; mono eyebrows in violet-deep.
- **Glass engine cards** with the site's gradient hairline border and violet-tinted elevation.
- **Engines are text.** No third-party logos, ever. The logo slot is a mono index dot.
- **Orbit rings** centred on whatever the frame is about.

## The Frame

### Frame Craft Bar

- **Squint:** one serif statement or one lit card dominates at 3-6x its neighbour.
- **Withhold:** violet is spent once per frame. If two things are violet, one of them is wrong (the eyebrow in violet-deep is chrome, not a spend).
- **Evidence:** every figure, name and quote on screen traces to the brief or the live site. Mock UI values are labelled as such or replaced with placeholders.
- **Reference:** aim at the hyperank.ai hero and login screen, an analyst's notebook, a quiet product film. Failure looks like a dark SaaS template with a purple gradient and floating logos.

- **Primary:** 1920x1080 (16:9). Author in `cqw` (`px / 1920 x 100`), vertical metrics in `cqh` where a layout is height-bound.
- **Vertical:** 1080x1920 (9:16). **Square:** 1080x1080 (1:1).
- **Safe area:** 5cqw sides, 8.9cqh top and bottom (96px at 16:9).

**The container law.** Every composition root sets `container-type: size`; frame-relative units are
`cqw`/`cqh`, never `vw`. Card radii and hairlines stay in px.

## Colors

`ground` is the universal background. `ink` sets every headline and engine name; `ink-soft` answer
lines; `muted` body and footers. `violet` is the single accent. `violet-deep` is reserved for mono
eyebrows (the site's own eyebrow colour). `brand-300` draws orbit rings, `violet-lift` tints the
glow. `faint` and `faint-2` are decorative only: at video label sizes they fail AA on the ground.
`flag-bad / warn / ok` appear only inline on accuracy flags, never as fills or accents.

## Typography

Three ramps. **Display** (Instrument Serif 400) carries statements, questions and the wordmark.
**Reading/UI** (Inter 400-600) carries names, answers, pills and the button. **Chrome**
(JetBrains Mono 500 uppercase) carries eyebrows, chips and metadata.

- **Legibility floor:** load-bearing text at or above 1.2cqw (23px). Mono chips at 0.83cqw are chrome.
- **Fit to measure:** 3 words or fewer → `display`; 4-8 → `headline`; 9+ or inside a card → `headline-sm`. Use `text-wrap: balance` on serif blocks so the italic phrase never strands one word.
- **One italic phrase per frame**, always the payoff clause, always violet. Never italic Inter, never a bold serif, never violet roman serif.
- **Eyebrows read like the site:** "Six engines · one question", "01 / The situation". Middle dot separators.

## Depth & Surface

- **Violet glow** behind the focal object, 15-25% at the core.
- **Glass engine cards** (gradient hairline + engine-chip shadow); white **question node** on e4.
- **Orbit rings** in brand-300 hairlines; ambient motion only, never a filled disc.
- **Grain** on every full frame.

**Ceiling:** no hard offset shadows, no dark cards, no gradient text, no glassmorphism blur over busy
content, no neon.

## Shapes

- **999px:** source chips, engine pills. **14px:** engine cards, panels. **16px:** question node, wells.
- **12px:** the CTA. **50%:** index dots, the connector node, rings.

## Components

- **question-node / engine-card / engine-card-lit / source-chip / connector:** the fan-out vocabulary (see `scenes/hr-engine-fanout.html`).
- **orbit-rings / violet-glow / grain:** the atmosphere set, every frame.
- **cta-button / engine-pill / lockup:** the closing vocabulary (see `scenes/hr-cta-endcard.html`, `scenes/hr-logo-sting.html`).

## Frame Treatments

### 1 · Fan-out (signature · left question, right six cards)

**Ground** + glow and rings centred on the question node. **Focal** the question node, then the lit
card. **Chrome** eyebrow top-left, lockup bottom-left. **Fixed** six cards, center-out order, one lit.
**Free** the question, the cited name, which engine lights. **Density** standard-dense.

### 2 · Statement (hook / thesis · left-anchored serif)

**Ground** + glow off the right edge. **Focal** a `display`/`headline` serif block, left, with its
italic violet clause. **Chrome** mono eyebrow above. **Silence** the right 40% holds rings only.

### 3 · Product surface (tutorial · browser or app frame)

**Ground** + glow. **Focal** a captured app screen inside a white well (16px, e4) on the right two
thirds; a `headline-sm` caption left. Zoom and cursor live on the surface, never on the type.

### 4 · Evidence row (explainer · answers as rows)

**Ground**. **Focal** 3-5 engine cards stacked or a table of answers (question, mentioned x/6, flag).
Accuracy flags use `flag-*` text colour only. Values come from the script or stay placeholders.

### 5 · Sting (brand · centred)

Centred lockup inside rings, nav tagline in mono below. The only centred treatment besides the endcard orbit.

### 6 · Endcard (closer · left copy, right orbit)

Closing serif line with italic violet clause, one CTA button, mono microcopy; right side the H mark
in rings with six engine pills orbiting.

## Composition Rules

### Do

- Start every frame on **#f0eee9** with grain and one violet glow.
- Anchor content left (statements, question node); the right side carries evidence or atmosphere.
- Spend violet **once**: the italic clause, the lit card, or the CTA.
- Set engine names as text in Inter 600; index them with mono numerals.
- Use the site's real copy verbatim when it fits ("Every engine has an answer. None of them is you.", "Check your brand free", "Six engines · one question").
- Keep the lockup small and in a corner on content frames.

### Don't

- No third-party logos, glyphs or brand colours for engines (Google's or Claude's logo colours stay off-frame).
- No invented metrics, testimonials, customer names or logos. "Competitor A-D" placeholders are the site's own convention.
- No second accent colour, no gradient on type, no dark mode, no cream + rust, no purple-to-pink gradients.
- No bold or uppercase serif; no italic outside the one violet phrase.
- Don't present dashboard mock numbers (74%, 1,284, +21.4%) as results.
- Don't use `faint` / `faint-2` for anything a viewer must read.

## Aspect-Ratio Behavior

| Treatment       | 16:9                          | 9:16                                              | 1:1                                   |
| --------------- | ----------------------------- | ------------------------------------------------- | ------------------------------------- |
| Fan-out         | question left, 6 cards right  | question top third, 6 cards stacked below, wires drop vertically | question top, 2x3 card grid below |
| Statement       | serif left, rings right       | serif upper half, rings low                        | serif upper two thirds                |
| Product surface | caption left, surface right   | surface top 60%, caption below                     | surface centred, caption above        |
| Evidence row    | 3-5 rows                      | 3-4 rows, chips drop under names                  | 3 rows                                |
| Sting           | horizontal lockup             | stacked lockup (mark over wordmark)               | horizontal, smaller                   |
| Endcard         | copy left, orbit right        | orbit top, copy and CTA below                     | copy top, small orbit bottom-right    |

Keep 5cqw on the short edge; re-step the serif ramp so load-bearing lines stay at or above the
1.2cqw floor measured against the frame's width. The v1 scenes are authored for 16:9; 9:16 and 1:1
are layout guidance until those variants are built.

## Approved Entities

- hyperank.ai mark (`assets/hyperank-mark.png`, official, do not redraw or recolour) and the serif wordmark "hyperank.ai".
- Engine names as text: ChatGPT, Gemini, Perplexity, Claude, Grok, Google AI Overviews (Copilot and Meta AI appear on the site but are not in the tracked six).
- No customers, testimonials or partner logos exist on the site; none appear in video.

## Numerals & Claims (hard rule)

Every number on screen has a source in `brief/product-brief.md` or the live site. Usable as-is:
"six engines", "88 free tools", "Save 17%" (annual billing), "Capture runs daily". Flag before use:
"One check, four engines, about twenty seconds" conflicts with "six engines". Anything else renders
as `{figure}` until the script supplies a sourced value.

## Pre-Render Self-Audit

- **Ground:** #f0eee9 + grain + one glow on every full frame.
- **Violet:** spent once; italic phrase, lit card or CTA.
- **Type:** Instrument Serif 400 at -0.02em, one italic violet phrase, balanced wrap; Inter UI; mono eyebrows 0.22em.
- **Engines:** text only, no logos.
- **Claims:** every numeral and quote traces to the brief.
- **Check:** `npx hyperframes check` at 0 errors, contrast all AA.

## Known Gaps

- 9:16 and 1:1 scene variants are not built in v1 (guidance above).
- The violet CTA uses #5e4bf6 instead of the site's #7b6bf8 fill: white on #7b6bf8 is 3.96:1, under AA for normal text; white on #5e4bf6 is 5.51:1.
- The site ships two token sets; this kit uses the current `.ds-theme` set. The older indigo scale (#6366f1, #4f46e5, Plus Jakarta Sans, Space Grotesk) is legacy and banned here.
