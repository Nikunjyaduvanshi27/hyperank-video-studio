# SELF-SLOP: The House Defaults This Org Now Produces Unprompted

Read this **with** `references/aesthetic-directions.md`, before picking a palette or a font, on every
new build.

`references/ai-tells.md` bans the *industry* defaults: Inter, AI-purple, three equal cards, Acme Corp.
This file bans **our own**. Every item below is something this harness reached for without being
asked, repeatedly, until it stopped being taste and became a signature. A house style that fires
automatically is indistinguishable from slop, because the whole failure mode of slop is *convergence*,
not ugliness.

The uncomfortable part: most of these were originally *good* choices, recommended by this very skill
as the escape from a generic default. That is exactly how they became the new generic default.

---

## 1. THE PRIMARY BAN: CREAM, RUST, PLAYFAIR

**Banned as a default, with no override except an explicit brand instruction.**

This is the single confirmed case of the harness reaching for its own house palette unprompted, across
unrelated briefs, for months. It originated as a deliberate rubric palette and metastasized into the
thing the model produces when it is not thinking.

**Banned background family** (warm cream / bone / oat / paper):
`#F5F0E6`, `#FAF6EF`, `#F7F3EA`, `#F4EFE4`, `#EFE9DC`, `#FBF7F0`, `#F2ECE0`
plus everything already banned in `typography-and-color.md` section 2: `#f5f1ea`, `#f7f5f1`, `#fbf8f1`, `#efeae0`, `#ece6db`, `#faf7f1`, `#e8dfcb`.

**Banned accent family** (rust / terracotta / burnt orange / brick):
`#B7410E`, `#C1440E`, `#A8442A`, `#B5533C`, `#C25B3A`, `#9E3D22`, `#AA4A30`
plus the brass and oxblood values already banned: `#b08947`, `#b6553a`, `#9a2436`, `#9c6e2a`, `#bc7c3a`, `#7d5621`.

**Banned type:** `Playfair Display` in any weight, as display or body. Also banned as defaults are its
two nearest substitutes reached for when Playfair is refused: `Cormorant Garamond` and `Libre Baskerville`.
The combinations `Playfair + Inter`, `Playfair + Lato`, and `Playfair + Source Sans` are banned outright.

**Banned as a unit:** the *combination* of a warm off-white canvas, a rust or brass accent, and a
high-contrast display serif. Escaping one axis is not escaping. Swapping Playfair for Fraunces while
keeping cream and rust is the same page. Swapping rust for clay while keeping cream and a display
serif is the same page.

**Override:** only when the brand brief literally names those colors or that typeface, or an existing
brand system already ships them. "The brief is artisan / heritage / warm" is **not** an override.
That reasoning is precisely what produced the problem.

**Note the scope:** cream and rust are banned *for web builds*. They may still be correct inside a
document, deck, or video rubric where they originated. Do not carry them across the media boundary.

---

## 2. THE SECONDARY WATCHLIST

These are lower-confidence than section 1. Verify each against your last three builds before treating
it as a ban. If two of your last three used it, it is a ban for this build.

**Fonts we over-reach for**
* `Bricolage Grotesque` is reserved for LinkedIn carousels, where it is the established house face. Reaching for it on a website makes the site look like the carousels. Do not.
* `Geist` / `Geist Mono`, `Satoshi`, `Cabinet Grotesk`, `Space Grotesk`, `Outfit`, `Sora`, `Manrope`. Every one of these is recommended somewhere in this skill as "not Inter". They have collectively become the new Inter. Pick one per quarter, not one per project.
* `Instrument Serif` and `Fraunces` are already banned in `typography-and-color.md`. Restated here because they are the first two substitutes proposed whenever Playfair is refused.

**Color moves we repeat**
* Zinc or slate near-black canvas plus exactly one electric-blue or emerald accent. This is the literal worked example in this skill's own text and it now ships as a finished design.
* An "escape the purple" accent that lands on emerald `#10B981` or electric blue `#3B82F6` every single time. Those are Tailwind defaults wearing a rebellion costume.
* Any hero gradient at all. Mesh, radial, conic, animated, subtle. If the signature moment is a gradient, there is no signature moment.

**Layout moves we repeat**
* Bento grid as the answer to every features section. Bento is one layout family out of the four-plus required by SECTION-LAYOUT-REPETITION. It is not the features pattern.
* The fixed page skeleton: hero, logo wall, three-up features, bento, numbered three-step how-it-works, testimonial, FAQ accordion, centered CTA band, footer. Shipping that exact order is shipping a template.
* Glass card on a dark page with a faint dot or line grid behind it.
* A centered hero with the CTA pair directly under a two-line headline, at every single VARIANCE setting. High variance that produces a centered hero is not high variance.

**Code-level tells**
* Pasting this skill's own example utility strings verbatim: `text-4xl md:text-6xl tracking-tighter leading-none` and `text-base text-gray-600 leading-relaxed max-w-[65ch]`. Those are illustrations of a shape, not a type scale. Derive real values from the chosen direction and state them.
* `text-gray-600` on a page whose neutral ramp is zinc, stone, or a custom scale. Mixed neutral families is the fastest way to look assembled rather than designed.
* Lucide icons at 24px, 1.5 stroke, everywhere, unexamined.
* Emoji standing in for icons, and any emoji inside a heading.

---

## 3. THE FIVE-QUESTION SELF-SLOP AUDIT

Run before writing code. Any "yes" is a restart of that decision, not a note for later.

1. Did I pick this palette because the brief demanded it, or because it is what I always produce for briefs that *feel* like this one?
2. Is the canvas warm off-white and the accent somewhere between orange and brown? (If yes: section 1, stop.)
3. Is the display face a high-contrast serif, and can I name the specific brand reason it is that face rather than a sans? (No reason means SERIF DISCIPLINE fails.)
4. Could I paste this page's palette and type pairing onto the last site I built and have nobody notice? (If yes, I built the same site twice.)
5. Is my "signature moment" a gradient, a glass card, a bento grid, or a scroll-triggered fade-in? (All four are defaults, not signatures. See `anti-ai-slop`.)

---

## 4. THE ROTATION LEDGER (mechanical enforcement)

Taste rules that depend on the model remembering its last three projects do not work, because it does
not remember. Write it down.

**Ledger path:** `~/.claude/memory/design-rotation-ledger.md`

If the file does not exist, create it with this header, then append. One line per shipped build:

```
| date | project | direction | canvas hex | accent hex | display font |
|---|---|---|---|---|---|
| 2026-08-13 | acme-landing | Cobalt Brut | #EDEFF2 | #1B4DFF | Archivo Expanded |
```

**Rules**
* **Read the ledger before choosing.** This is a one-file read, not an exploration.
* You may not reuse the **direction** used in either of the previous two entries.
* You may not reuse the **display font** used in either of the previous two entries.
* You may not reuse an **accent within the same hue family** as the previous entry.
* Append the new row **before** you claim the build is done, in the same pass as the visual QA evidence.

If the ledger is empty or missing, say so explicitly in the design rationale rather than silently
assuming the slate is clean. An unverifiable claim of freshness is what got us here.

---

## TIER VIEW (P0/P1/P2) — for consumers that triage by severity

`document-design` and the visual-qa loop run this file as a tiered checklist. Mapping:

* **P0 — restart the visual layer** if present: everything in section 1 (cream/rust/Playfair cluster, banned as a unit), plus any entry later promoted by the Convergence rule below. For documents, the near-black canvas with a single warm clay or gold pop is also P0 (it is the carousel generator's old default).
* **P1 — rewrite the offending components**: section 2 watchlist items that appear in 2 of your last 3 builds (fonts over-reached, repeated color moves, repeated layout moves, hero gradients, decorative bars/stripes, left accent rails, uniform sheen-plus-glow elevation).
* **P2 — polish before ship**: section 2 code-level tells (verbatim utility strings, mixed neutral families, unexamined Lucide defaults, emoji-as-icons), more than 3 distinct border radii, type sizes off the modular scale.

**Convergence rule:** any palette or type pairing the model reaches for unprompted more than twice in a month is promoted to P0 by definition. That is the mechanism that caught cream plus rust; it stays live via the rotation ledger in section 4.

---

## 5. WHY THIS FILE EXISTS

A design rulebook that only bans other people's defaults will always be one cycle behind its own
output. The failure mode is not that the model has bad taste; it is that the model has *consistent*
taste and consistency at this scale reads as automation. Every genuinely good choice this skill
recommends is on a clock. When a recommendation starts appearing in builds that did not ask for it,
it belongs in this file.

**Maintenance rule:** when a reviewer or Nikunj flags "this looks like the last one", the fix is not
only to change the current build. Add the offending choice to section 2 in the same pass.
