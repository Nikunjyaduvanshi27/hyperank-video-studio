---
name: taste-skill
description: >-
  Anti-slop design rulebook for NEW landing pages, portfolios, marketing sites
  and webpage UI: "build a website", "design a page", "stop this looking like
  AI slop". Sets VARIANCE/MOTION/DENSITY dials, enforces ~60 hard rules.
  Existing site: use redesign-skill. Not for slide decks or print documents.
---

<!-- Source: https://github.com/Leonxlnx/taste-skill (MIT) — folder skills/taste-skill, upstream install name "design-taste-frontend" (v2 experimental) -->

# tasteskill: Anti-Slop Frontend Skill

> Landing pages, portfolios, and redesigns. Not dashboards, not data tables, not multi-step product UI.
> Every rule below is **contextual**. None of it fires automatically. First read the brief, then pull only what fits.

**This file is the router.** It carries the workflow, the dials, and the non-negotiables. The full rule set lives in `references/` and loads on demand: see the router table in Section 3. Nothing was dropped in the split; every rule still exists, one level down.

---

## 0. BRIEF INFERENCE (Read the Room Before Anything Else)

Before touching code or tweaking dials, **infer what the user actually wants**. Most LLM design output is bad because the model jumps to a default aesthetic instead of reading the room.

### 0.A Read these signals first
1. **Page kind** - landing (SaaS / consumer / agency / event), portfolio (dev / designer / creative studio), redesign (preserve vs overhaul), editorial / blog.
2. **Vibe words** the user used - "minimalist", "calm", "Linear-style", "Awwwards", "brutalist", "premium consumer", "Apple-y", "playful", "serious B2B", "editorial", "agency-y", "glassy", "dark tech".
3. **Reference signals** - URLs they linked, screenshots they pasted, products they named, brands they're competing with.
4. **Audience** - B2B procurement panel vs. design-conscious consumer vs. recruiter scanning a portfolio. The audience picks the aesthetic, not your taste.
5. **Brand assets that already exist** - logo, color, type, photography. For redesigns, these are starting material, not optional input (see `references/redesign-protocol.md`).
6. **Quiet constraints** - accessibility-first audiences, public-sector, regulated industries, trust-first commerce, kids' products. These constraints OVERRIDE aesthetic preference.

### 0.B Output a one-line "Design Read" before generating
Before any code, state in one line: **"Reading this as: \<page kind> for \<audience>, with a \<vibe> language, leaning toward \<design system or aesthetic family>."**

Example reads:
- *"Reading this as: B2B SaaS landing for technical buyers, with a Linear-style minimalist language, leaning toward Tailwind utilities + Geist + restrained motion."*
- *"Reading this as: solo designer portfolio for hiring managers, with an editorial / kinetic-type language, leaning toward native CSS + scroll-driven animation + custom typography."*
- *"Reading this as: redesign of a public-sector service site, with a trust-first language, leaning toward GOV.UK Frontend or USWDS."*

### 0.C If the brief is ambiguous, ask one question, do not guess
Ask exactly **one** clarifying question - never a multi-question dump - and only when the design read genuinely diverges. Example: *"Should this feel closer to Linear-clean or Awwwards-experimental?"*

If you can confidently infer from context, **do not ask**. Just declare the design read and proceed.

### 0.D Anti-Default Discipline
Do not default to: AI-purple gradients, centered hero over dark mesh, three equal feature cards, generic glassmorphism on everything, infinite-loop micro-animations everywhere, Inter + slate-900. These are the LLM defaults. Reach past them deliberately based on the design read.

**And do not default to OUR defaults either.** Cream canvas + rust accent + `Playfair Display` is the house palette this harness now produces unprompted; it is banned as a default. So are the "escapes" this skill itself recommends once they stop being deliberate. Read `references/self-slop.md` alongside `references/aesthetic-directions.md` before the first color or font decision, and declare the direction by name in the design read.

---

## 1. THE THREE DIALS (Core Configuration)

After the design read, set three dials. Every layout, motion, and density decision in the references is gated by these.

* **`DESIGN_VARIANCE: 8`** - 1 = Perfect Symmetry, 10 = Artsy Chaos
* **`MOTION_INTENSITY: 6`** - 1 = Static, 10 = Cinematic / Physics
* **`VISUAL_DENSITY: 4`** - 1 = Art Gallery / Airy, 10 = Cockpit / Packed Data

**Baseline:** `8 / 6 / 4`. Use these unless the design read overrides them. Do not ask the user to edit this file - overrides happen conversationally.

### 1.A Dial Inference (design read → dial values)
| Signal | VARIANCE | MOTION | DENSITY |
|---|---|---|---|
| "minimalist / clean / calm / editorial / Linear-style" | 5-6 | 3-4 | 2-3 |
| "premium consumer / Apple-y / luxury / brand" | 7-8 | 5-7 | 3-4 |
| "playful / wild / Dribbble / Awwwards / experimental / agency" | 9-10 | 8-10 | 3-4 |
| "landing page / portfolio / marketing site (default)" | 7-9 | 6-8 | 3-5 |
| "trust-first / public-sector / regulated / accessibility-critical" | 3-4 | 2-3 | 4-5 |
| "redesign - preserve" | match existing | +1 | match existing |
| "redesign - overhaul" | +2 | +2 | match existing |

### 1.B Use-Case Presets
| Use case | VARIANCE | MOTION | DENSITY |
|---|---|---|---|
| Landing (SaaS, mainstream) | 7 | 6 | 4 |
| Landing (Agency / creative) | 9 | 8 | 3 |
| Landing (Premium consumer) | 7 | 6 | 3 |
| Portfolio (Designer / studio) | 8 | 7 | 3 |
| Portfolio (Developer) | 6 | 5 | 4 |
| Editorial / Blog | 6 | 4 | 3 |
| Public-sector service | 3 | 2 | 5 |
| Redesign - preserve | match | match+1 | match |
| Redesign - overhaul | +2 | +2 | match |

### 1.C How the Dials Drive Output
Use these (or user-overridden values) as global variables. Cross-references throughout this skill refer to these exact variable names - never invent aliases like `LAYOUT_VARIANCE` or `ANIM_LEVEL`. Technical definition of each band (what level 8 means in CSS) is in `references/stack-conventions.md` section 2.

---

## 2. FOUNDATION CHOICE (Brief → Design System)

Once you have the design read (Section 0) and dials (Section 1), pick the right foundation. Do not invent CSS for things that have an official package. Do not pretend an aesthetic trend is an official system.

**Honesty rule:** if the brief reads as a named vendor system (Fluent, Material, Carbon, Polaris, Atlaskit, Primer, GOV.UK, USWDS, Bootstrap, Radix, shadcn/ui), install and use the **official** package. Do not recreate its CSS by hand. Do not import a system's tokens but then override 90% of them.

**One system per project.** Do not mix Fluent React with Carbon in the same tree. Do not import shadcn/ui components into a Material 3 app.

Default when no vendor system fits: Tailwind v4 utilities + `dark:` variant, per `references/stack-conventions.md`.

Read `references/design-systems.md` for the full brief-to-system map, the aesthetic-vs-system table (glassmorphism, bento, brutalism, Apple Liquid Glass), real install commands, and canonical doc links.

---

## 3. REFERENCE ROUTER

Load a reference file when its condition hits. Do not guess a rule you have not read.

| Read this | When |
|---|---|
| `references/design-systems.md` | Choosing the foundation, or the brief names a vendor system / an aesthetic family (Section 2) |
| `references/aesthetic-directions.md` | **Before the first color or font decision** whenever no brand assets dictate one. 8 named directions with role-mapped hex (contrast pre-computed) + fixed type pairings. Pick ONE by name. |
| `references/self-slop.md` | **Same moment as `aesthetic-directions.md`**, and any time a palette / font / layout choice feels like the obvious one. Bans this org's OWN convergent defaults (cream + rust + Playfair first). Carries the rotation ledger. |
| `references/visual-qa-loop.md` | **Mandatory after the code runs, before claiming done.** Render, screenshot, critique against the rubric, iterate (max 3 rounds). |
| `references/stack-conventions.md` | Before the first component: framework, Tailwind version, Motion import, state rules, icon libraries, breakpoints, dial band definitions |
| `references/typography-and-color.md` | Choosing fonts or a palette; any premium-consumer / editorial / luxury brief; before shipping dark mode |
| `references/layout-rules.md` | Composing the page skeleton, the hero, nav, bento grids, sections, buttons, forms |
| `references/content-and-assets.md` | Filling sections: images, logo walls, content density, long lists, spec sheets, quotes, copy self-audit |
| `references/motion.md` | `MOTION_INTENSITY > 3`, or any scroll animation, sticky-stack, horizontal pan, marquee (canonical GSAP skeletons live here) |
| `references/performance-a11y.md` | Before shipping motion, filters, or heavy assets; any Core Web Vitals or reduced-motion question |
| `references/ai-tells.md` | Before writing any visible string, eyebrow, pill, caption, footer; during the copy self-audit |
| `references/pattern-library.md` | Naming a layout move, picking a hero paradigm or scroll device, authoring a new block file |
| `references/redesign-protocol.md` | The brief touches an existing site (detect mode FIRST, audit before proposing) |
| `references/preflight-check.md` | **Mandatory before outputting code.** The full ~60-box final gate |

---

## 4. NON-NEGOTIABLES (apply without a lookup)

### 4.A EM-DASH BAN (the single most-violated Tell)

**Em-dash (`—`) is COMPLETELY banned.** It is the LLM's signature stylistic crutch and it is the #1 visual Tell in production tests. There is no "limited use" allowance, no "natural language frequency" allowance, no "in body copy is fine" allowance. None.

* **Banned in headlines.** Use a period or a comma.
* **Banned in eyebrows / labels / pills / button text / image captions / nav items.** Replace with line breaks, columns, or hairlines.
* **Banned in body copy.** Restructure the sentence: two sentences with a period, OR a comma, OR parentheses, OR a colon.
* **Banned in quote attribution.** Use a normal hyphen with spaces (` - `) or a line break + smaller-weight name.
* **Banned in en-dash form too (`–`) when used as a separator.** Date ranges (`2018-2026`) use a hyphen. Number ranges (`€40-80k`) use a hyphen.

The ONLY permitted dash characters on the page are:
* Regular hyphen `-` (for compound words, ranges, line dividers in markup)
* Minus sign in math (`-5°C`)

If your output contains a single `—` or `–` anywhere visible to the user, the output fails the Pre-Flight Check and must be rewritten.

This rule is non-negotiable. The agent has historically ignored em-dash limits when phrased as "use sparingly." The phrasing here is binary: zero em-dashes.

### 4.B The mandatory locks (full text in the referenced file)

LLMs default to clichés. Override these defaults proactively. Each rule has a context-aware override path. These are the battle-tested rules that fail production tests most often. Treat each as a hard gate; open the file for the full wording before you rely on an edge case.

* **EYEBROW RESTRAINT** - max 1 eyebrow per 3 sections, hero counts as 1. Mechanical check: count `uppercase tracking` micro-labels; fail if count > ceil(sectionCount / 3). (`layout-rules.md`)
* **Hero fits the viewport** - headline max 2 lines, subtext max 20 words and max 3-4 lines, CTAs visible without scroll, top padding max `pt-24`, max 4 text elements total. (`layout-rules.md`)
* **BUTTON CONTRAST + CTA WRAP + NO DUPLICATE CTA INTENT + FORM CONTRAST** - WCAG AA on every CTA and form, no CTA label wrapping at desktop, one label per intent. (`layout-rules.md`)
* **SECTION-LAYOUT-REPETITION BAN + ZIGZAG CAP + SPLIT-HEADER BAN + BENTO CELL COUNT** - at least 4 layout families across 8 sections, max 2 consecutive image+text splits, no headline-plus-corner-paragraph headers, N items means N cells. (`layout-rules.md`)
* **SERIF DISCIPLINE** - serif is very discouraged as default; `Fraunces` and `Instrument_Serif` are banned as defaults; italic descenders need `leading-[1.1]` + `pb-1`. (`typography-and-color.md`)
* **THE LILA RULE + PREMIUM-CONSUMER PALETTE BAN** - no AI-purple default; the beige/cream + brass/clay/oxblood + espresso hex families are banned as the default reach for premium-consumer briefs, rotate palettes instead. (`typography-and-color.md`)
* **SELF-SLOP BAN** - the org's OWN convergent defaults are banned as defaults, not just the industry's. Cream canvas + rust/brass accent + `Playfair Display` is banned as a unit and on each axis separately; escaping one axis is not escaping. Also on the watchlist: `Bricolage Grotesque` on a website (carousel-only face), zinc-black + electric-blue/emerald, hero gradients as the signature moment, bento-as-every-features-section. (`self-slop.md`)
* **NAMED DIRECTION + ROTATION LEDGER** - state the aesthetic direction by name before the first color or font decision, and read the rotation ledger first. No reusing the direction or display font from either of the previous two builds. (`aesthetic-directions.md`, `self-slop.md`)
* **VISUAL QA GATE** - no UI is done until it has been rendered, screenshotted across the 4-viewport matrix in both themes, critiqued against the rubric, and iterated (max 3 rounds). A "done" claim with no screenshot path is a guess, not a claim. (`visual-qa-loop.md`)
* **COLOR CONSISTENCY LOCK + SHAPE CONSISTENCY LOCK + PAGE THEME LOCK** - one accent, one radius system, one theme for the whole page. (`typography-and-color.md`, `layout-rules.md`)
* **REAL IMAGES, NO FAKE SCREENSHOTS** - gen tool first, then Picsum seeds, then labeled placeholder slots. Div-based fake product UI and hand-rolled decorative SVGs are banned. Logo walls use real SVG marks, logos only, under the hero. (`content-and-assets.md`)
* **COPY SELF-AUDIT** - re-read every visible string before shipping; rewrite anything broken, cute-but-wrong, or fake-precise. (`content-and-assets.md`)
* **MOTION MUST BE MOTIVATED + MARQUEE MAX-ONE-PER-PAGE + no `window.addEventListener('scroll')`** - every animation justified in one sentence; reduced motion mandatory above `MOTION_INTENSITY 3`. (`motion.md`, `performance-a11y.md`)
* **Viewport stability** - `min-h-[100dvh]`, never `h-screen`. Grid over flexbox percentage math. (`stack-conventions.md`)

---

## 5. OUT OF SCOPE

This skill is NOT for:
* Dashboards / dense product UI / admin panels (use Fluent, Carbon, Atlassian, or Polaris from `references/design-systems.md`).
* Data tables (use TanStack Table or AG Grid).
* Multi-step forms / wizards (use Form-specific patterns; this skill won't make them better).
* Code editors (use Monaco / CodeMirror with their official skinning).
* Native mobile (use Apple HIG / Material directly).
* Realtime collab UIs (presence, cursors, OT-aware - different problem class).

If the brief is one of the above, **say so explicitly**, point to the right tool, and only apply this skill's marketing-page / about-page / landing-page parts to the surfaces where they apply.

---

## 6. THE TWO GATES

### 6.A Pre-flight (before outputting code)
Read `references/preflight-check.md` and run every box. **THIS IS NOT OPTIONAL.** If a single checkbox cannot be honestly ticked, the page is not done. Fix it before delivering.

### 6.B Visual QA (after the code runs, before saying done)
Pre-flight checks the code you are about to write. It cannot see the page that code produced. Run `references/visual-qa-loop.md`: serve the page, capture the 4-viewport matrix in both themes plus the focus / hover / motion / empty states, critique against the rubric, fix the top 3 findings, repeat up to 3 rounds. Then append the rotation ledger row.

**Both gates are mandatory and neither substitutes for the other.** A passed pre-flight with no render is an untested page. If the page genuinely cannot be served, say "could not render, unverified" and stop; never describe a render you did not capture.
