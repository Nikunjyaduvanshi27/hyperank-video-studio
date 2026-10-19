# NAMED AESTHETIC DIRECTIONS (Palettes + Type Pairings)

Read this **after** the design read (SKILL.md section 0) and **before** the first line of CSS, whenever
the brief needs a visual language and no brand assets dictate one.

This file exists because "pick a palette" is where the model reverts to type. A named direction with
role-mapped hex values and a fixed type pairing is a commitment; "warm neutral with a premium accent"
is a slot the house defaults slide back into.

**Hard rules for using this file**
1. **Pick exactly ONE direction.** Do not blend two. Blending is how every direction becomes the same direction.
2. **Declare it by name** in the design read line: `"...leaning toward Cobalt Brut (light, structural)."`
3. **Check the rotation ledger first** (`references/self-slop.md` section 4). You may not reuse the direction or the display font used in either of the previous two builds.
4. **These are starting points, not skins.** Shift hues, swap the accent, extend the ramp. What you may not do is drift the whole thing back toward warm cream, rust, brass, Playfair, Inter, or a purple gradient. See `references/self-slop.md`.
5. Every contrast ratio below is **computed, not estimated**. If you change a hex, recompute. Do not inherit the AA claim.

**Reading the swatch tables**
* `canvas` = page background. `surface` = raised panel or card. `ink` = headings. `muted` = secondary body and captions. `rule` = hairlines only.
* `accent` is the single accent required by the COLOR CONSISTENCY LOCK (`typography-and-color.md` section 2).
* Where a direction lists `accent-text`, that darker variant is what small text, links, and body-size labels use. The lighter `accent` is for large display type, fills, and graphics only.
* `rule` hairlines sit at roughly 1.4:1 by design. They are decorative separators and are exempt from WCAG 1.4.11. They may **never** be the only boundary of an input, a focus ring, or a control that conveys state.

---

## 1. COBALT BRUT
**Light. Structural, engineered, unsentimental.** For B2B and developer-facing landings where the buyer is technical and the promise is precision. Reads as blueprint, not brochure.

| Role | Hex | Contrast |
|---|---|---|
| canvas | `#EDEFF2` | cool grey, zero warmth |
| surface | `#FAFBFC` | ink on surface 17.67:1 |
| ink | `#0B1524` | on canvas **15.89:1 AAA** |
| muted | `#55606E` | on canvas **5.55:1 AA** |
| rule | `#C9D0D8` | hairline only (1.35:1) |
| accent | `#1B4DFF` | on canvas **5.13:1 AA**, on surface 5.71:1 |
| on-accent | `#F7F9FF` | on accent **5.62:1 AA** |

**Type:** display `Archivo Expanded` (700, tracking -0.02em) / body `Newsreader` (400, 17px, 1.6) / mono `Berkeley Mono`, open substitute `JetBrains Mono`.
A serif body under an expanded-grotesk display is the whole move: it makes long copy feel edited rather than generated. This is the justified-serif case per SERIF DISCIPLINE, and it is body, not display.

**Signature move:** a visible structural grid. Hairline column rules that run the full page height behind content, with sections snapping to them. One diagonal break where the hero ends.
**Do not:** put the cobalt in a gradient. It is a flat ink. Never `#0B1524` text on `#1B4DFF` fill (3.10:1, large display only).

---

## 2. HALIDE
**Dark. Darkroom, analog process, patient.** For creative-technical portfolios, photography, film tools, research labs. Near-black with a green cast plus a single safelight red.

| Role | Hex | Contrast |
|---|---|---|
| base | `#0C0F0D` | green-cast near-black, not `#000` |
| surface | `#141A17` | body on surface 9.70:1 |
| rule | `#27312C` | hairline only (1.43:1) |
| heading | `#EDF3EF` | on base **17.13:1 AAA** |
| body | `#B7C3BC` | on base **10.59:1 AAA** |
| accent | `#F0463C` | on base **5.18:1 AA** |
| on-accent | `#140A09` | on accent **5.24:1 AA** |

**Type:** display `PP Neue Montreal` (500), open substitute `Schibsted Grotesk` (600) / body `Schibsted Grotesk` (400, 16px, 1.65) / mono `Departure Mono` for captions and metadata.
**Signature move:** content that resolves. Images arrive at low contrast and settle to full contrast on entry, once, never on loop. Captions typed in mono at 11px with generous tracking, positioned like a contact-sheet edge notation.
**Do not:** let the red touch more than roughly 5% of any viewport. It is a safelight, not a brand color. No red glow, no red gradient.

---

## 3. CHALK COURT
**Light. Athletic, marked-out, kinetic.** For sport, fitness, consumer apps with streaks and stats, anything measured. Court surface plus painted line.

| Role | Hex | Contrast |
|---|---|---|
| canvas | `#F1F2ED` | cool bone, deliberately not cream |
| surface | `#FBFCF8` | accent on surface 5.16:1 |
| ink | `#10231A` | on canvas **14.61:1 AAA** |
| muted | `#4E5A52` | on canvas **6.42:1 AA** |
| rule | `#D3D8CE` | hairline only |
| accent | `#1F7A4C` | on canvas **4.73:1 AA** |
| on-accent | `#F4FBF6` | on accent **5.06:1 AA** |
| signal | `#E8FF3A` | ink on signal **14.71:1 AAA**, restricted use |

`signal` is a **state color only**: focus rings, active selection, the current value on a chart, a highlighter sweep behind one word. It is not a second brand accent and never appears as a section background. This is the one narrow exception to the one-accent rule and it must be justified in the design rationale.

**Type:** display `Anybody` (variable width, 800, condensed at 85 for stat blocks) / body `Hanken Grotesk` (400, 16px) / numerals `Martian Mono` with `font-variant-numeric: tabular-nums` for every stat.
**Signature move:** painted court lines as layout. 3px `ink` rules that box sections asymmetrically, one arc, numbers set enormous and clipped by the section edge.
**Do not:** use the signal yellow for a CTA fill. Do not center the stats. Tabular numerals are mandatory; proportional digits in a stat row is the tell that nobody looked at the render.

---

## 4. TIDAL SLATE
**Light-mid. Calm, credible, low-adrenaline.** For health, fintech, insurance, anything where the emotion is "this will not surprise me." Cool slate with an oyster surface and one turquoise.

| Role | Hex | Contrast |
|---|---|---|
| canvas | `#E9EDF0` | oyster grey |
| surface | `#F7F9FA` | accent-text on surface 5.69:1 |
| ink | `#16303C` | on canvas **11.72:1 AAA** |
| muted | `#4C6270` | on canvas **5.42:1 AA** |
| rule | `#C3CFD6` | hairline only |
| accent-text | `#0B6E74` | on canvas **5.10:1 AA**, use for links, small labels, CTA fill |
| accent | `#0F9FA6` | 2.73:1 on canvas: **large display and graphics only, never text under 24px** |
| on-accent | `#F2FAFA` | on accent-text **5.67:1 AA** |

**Type:** display `Instrument Sans` (600, tracking -0.01em) / body `Source Serif 4` (400, 18px, 1.7). Note that `Instrument Serif` remains banned; `Instrument Sans` is a different face and is fine.
**Signature move:** a slow horizontal tide. One full-bleed band per page where content moves at 0.85x scroll speed, no more than 40px of travel. Calm is a motion budget, not an absence of motion.
**Do not:** reach for the light turquoise as a text color because it looks nicer. It fails. Two hex values exist for exactly this reason.

---

## 5. SODIUM VAPOR
**Dark. Nocturnal, urban, documentary.** For events, music, nightlife, and developer tools with a late-night personality. Deep blue-black under street-lamp amber.

| Role | Hex | Contrast |
|---|---|---|
| base | `#0A0E14` | blue-black |
| surface | `#121824` | body on surface 9.06:1 |
| rule | `#24303F` | hairline only |
| heading | `#EAF0F8` | on base **16.87:1 AAA** |
| body | `#AFBACB` | on base **9.86:1 AAA** |
| accent | `#FFB020` | on base **10.58:1 AAA** |
| on-accent | `#14100A` | on accent **10.36:1 AAA** |

**Sodium amber is not ochre and not brass.** `#FFB020` is a high-chroma lamp yellow on a blue-black field. The banned `#bc7c3a` / `#b08947` family is a desaturated brown-orange on warm cream. If your build starts drifting the amber toward brown or the base toward warm, you have rebuilt the banned palette and must stop.

**Type:** display `Wix Madefor Display` (800) / body `Wix Madefor Text` (400, 16px, 1.6) / mono `Spline Sans Mono` for timestamps and ticket codes.
**Signature move:** light pooling. A single soft radial of `accent` at very low alpha behind one element per section, cast from a consistent direction, as if from one lamp. Consistent light source or it reads as decoration.
**Do not:** add a second light source. Do not use amber for body text. No neon-outline text.

---

## 6. PORCELAIN AND GRAPHITE
**Light. Swiss, exact, quiet until it is not.** For design studios, agencies, editorial products, anything selling judgment. Achromatic system plus one loud magenta.

| Role | Hex | Contrast |
|---|---|---|
| canvas | `#F2F2F1` | porcelain |
| surface | `#FCFCFB` | |
| ink | `#17181A` | on canvas **15.86:1 AAA** |
| muted | `#5B5E63` | on canvas **5.81:1 AA** |
| rule | `#D6D7D6` | hairline only |
| accent-text | `#C4004F` | on canvas **5.42:1 AA**, links and small labels |
| accent | `#FF2D78` | 3.18:1 on canvas: **display type, fills, and graphics only** |
| on-accent | `#FFF5F9` | on accent-text **5.69:1 AA** |

On a dark inverted band, `#FF2D78` against `#17181A` is 4.99:1 AA, so the loud magenta becomes text-safe when reversed. That reversal is the only place it should carry copy.

**Type:** display `Host Grotesk` (700, tracking -0.03em at display sizes) / body `Host Grotesk` (400, 16px, 1.55) / mono `Fragment Mono`.
Single-family discipline is the point. Weight and size carry the hierarchy, nothing else.
**Signature move:** one intrusion. The entire page is achromatic and rigorously gridded, then exactly one element breaks the grid in magenta at full bleed. One per page. The restraint is what makes the intrusion read.
**Do not:** sprinkle magenta. Two magenta moments equals zero magenta moments.

---

## 7. REACTOR
**Dark. Instrumented, industrial, telemetric.** For infrastructure, observability, robotics, hardware, and dev tooling that wants to look like a readout rather than a brochure.

| Role | Hex | Contrast |
|---|---|---|
| base | `#0F1110` | graphite-black |
| surface | `#171A19` | |
| rule | `#2A2F2D` | hairline only |
| heading | `#F0F4F1` | on base **17.07:1 AAA** |
| body | `#B4BCB7` | on base **9.76:1 AAA** |
| accent | `#C8F31D` | on base **14.71:1 AAA** |
| on-accent | `#101401` | on accent **14.52:1 AAA** |

**Type:** display `Saira Semi Condensed` (700, uppercase permitted here and nowhere else in this file) / body `Figtree` (400, 16px) / mono `Azeret Mono` for every number and readout.
**Signature move:** live-looking instrumentation. One real, data-driven element that actually updates: a sparkline, a throughput counter, a status grid. It must be driven by real or plausibly-shaped data, never a hardcoded animation pretending to be a metric. Fake telemetry is the same lie as a fake product screenshot.
**Do not:** make it a gamer aesthetic. No glow, no scanlines, no monospace body copy. The lime is at 14.71:1 already; it needs no bloom.

---

## 8. NEWSPRINT MONO
**Light. Achromatic, typographic, editorial.** For writing products, publications, documentation, essays, and anything where the text *is* the product. Zero accent color; hierarchy is built from ink weight, scale, and rule weight alone.

| Role | Hex | Contrast |
|---|---|---|
| canvas | `#EDEEEE` | cool newsprint, deliberately not warm paper |
| surface | `#F8F9F9` | |
| ink | `#121314` | on canvas **16.00:1 AAA** |
| muted | `#565A5C` | on canvas **6.00:1 AA** |
| rule | `#C7CACB` | hairline only |
| reversed block | ink fill, canvas text | **16.00:1 AAA** |

The accent is the reversed block. One solid `ink` panel with `canvas` text, used once, is the only high-emphasis device available.

**Type:** display `Bodoni Moda` (600, optical size set for display) / body `Literata` (400, 19px, 1.75, measure 68ch) / mono `Courier Prime` for metadata, bylines, and figure numbers.
This is a genuinely editorial brief, which is the exception SERIF DISCIPLINE allows. State that justification explicitly in the design rationale. `Bodoni Moda` is not `Playfair`, not `Fraunces`, and not `Instrument Serif`; do not substitute any of those in.

**Do not:** add an accent color later because it feels bare. The absence is the direction. If a client needs an accent, this is the wrong direction, not a direction to patch.

---

## 9. CHOOSING BETWEEN THEM

| Brief signal | Direction |
|---|---|
| Technical B2B, API, infra, precision claim | Cobalt Brut, or Reactor if dark |
| Photography, film, craft-technical portfolio | Halide |
| Sport, fitness, measurement, streaks, stats | Chalk Court |
| Health, finance, insurance, trust-first | Tidal Slate |
| Events, music, nightlife, late-night tooling | Sodium Vapor |
| Studio, agency, design-judgment sale | Porcelain and Graphite |
| Observability, hardware, robotics, telemetry | Reactor |
| Writing, publishing, docs, essays | Newsprint Mono |
| Public-sector, regulated, accessibility-critical | None of these. Use GOV.UK Frontend or USWDS per `design-systems.md` |

If two directions both fit, pick the one **not** in the rotation ledger. If the brief fits none of them, invent a ninth: name it, write the role-mapped hex table, compute every contrast ratio, fix the type pairing, and append it to this file. An unnamed palette is a palette that will drift.

## 10. WHAT COUNTS AS DONE

A direction is only real once it survives a render. Contrast math and a hex table prove nothing about
composition, rhythm, or whether the amber actually pooled. Run `references/visual-qa-loop.md` and
attach screenshot evidence before claiming the direction landed.
