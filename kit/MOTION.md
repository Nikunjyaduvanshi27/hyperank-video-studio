# hyperank motion grammar (v1)

Motion follows the brand's tone: calm, sourced, deliberate. Things settle; nothing bounces. Violet
moves once per scene, and when it moves it travels a path, because the product is about tracing an
answer back to its source. Every rule below is seek-safe for HyperFrames (one paused GSAP timeline,
deterministic, scrubbable to any frame).

## Named easings

| Name         | GSAP           | Web origin                                           | Use for                                                       |
| ------------ | -------------- | ---------------------------------------------------- | ------------------------------------------------------------- |
| `hr-settle`  | `power4.out`   | site `cubic-bezier(.22,1,.36,1)` (closest built-in)  | Every entrance and landing: type, cards, chips, the mark      |
| `hr-trace`   | `power2.inOut` | none; video-only                                     | Anything travelling a path: connector draws, the violet trace, camera moves |
| `hr-recede`  | `power2.in`    | none; video-only                                     | Exits and swaps out. Accelerates away, never lingers          |

Ambient only: `sine.inOut` (glow, ring breathe, dims) and `none` (orbit rotation). Banned: `back`,
`elastic`, `bounce`, overshoot springs. Built-ins are used instead of CustomEase so scenes load with
plain GSAP.

In code, declare them once per composition:

```js
var SETTLE = "power4.out", TRACE = "power2.inOut", RECEDE = "power2.in";
```

## Duration scale

| Token   | Seconds   | Use                                                    |
| ------- | --------- | ------------------------------------------------------ |
| micro   | 0.12-0.18 | Chip label swap, connector end dots                    |
| quick   | 0.25-0.36 | Swap-outs, node pop, CTA chip ignite                   |
| base    | 0.5-0.6   | Cards, buttons, chrome, the violet trace (0.45)        |
| slow    | 0.7-0.9   | Serif statements through masks, the mark               |
| atmos   | 1.0-1.4   | Glow fade, ring ping, ring entrance                    |
| ambient | scene     | Orbit rotation, ring breathe (linear or sine)          |

Exits are faster than entrances (swap-out 0.25s against swap-in 0.5s). The slowest move in a scene
should be about 3x the fastest.

## Stagger

| What                     | Each   | Order                                   |
| ------------------------ | ------ | --------------------------------------- |
| Letters (wordmark)       | 0.03   | reading order                           |
| Words (serif statements) | 0.035-0.04 | reading order                       |
| Engine pills             | 0.06   | clockwise from top-left                 |
| Engine cards and wires   | 0.07   | centre-out: rows 3,4,2,5,1,6            |
| Rings                    | 0.08   | inner to outer                          |
| Palette tiles            | 0.04   | grid from start                         |

Keep any one stagger sequence under 0.5s total.

## Entrance grammar

1. **Nothing starts at 0.** First tween at 0.1s. Atmosphere (glow, rings) leads, the statement follows at 0.15-0.3s.
2. **Order by importance, not DOM order.** Eyebrow, statement, focal object, secondary, microcopy.
3. **Serif type rises through masks.** Each word (or letter for the wordmark) sits in an `overflow:hidden` span and rises `yPercent 110 → 0` on `hr-settle`. Masks carry `data-layout-allow-overflow` and `padding-bottom: 0.12em` so descenders survive.
4. **Cards arrive from the side they connect to.** Engine cards: `x +64, scale .96 → 1`, starting when their wire is about 70% drawn.
5. **Chrome slides in short.** Eyebrows and lockups: `opacity 0, x -16..-24 → 0`.
6. **Pills and chips pop small.** `scale .6-.8 → 1`, opacity with it.
7. **Wires draw, they do not fade.** `strokeDashoffset length → 0` on `hr-trace`.
8. **Never tween `letterSpacing`, `width`, `top`, `left`.** Lint rejects letterSpacing; layout props stutter.

## Exit grammar

- **Scenes do not exit themselves.** Kit scenes end on a held final state; the host cuts.
- **Default transition is a hard cut.** Every scene shares the #f0eee9 ground, so a cut reads as continuity. Use a 0.3s crossfade only between two content scenes in an explainer; never a wipe, push or zoom transition.
- **Recede, do not remove.** De-emphasis is `opacity 1 → 0.78, scale 1 → 0.985` over 0.5s `sine.inOut`. Not lower: 0.78 keeps every receded label AA.
- **Swap = out up, in from below.** Old line `yPercent 0 → -110, opacity → 0`, 0.25s `hr-recede`; new line `yPercent 110 → 0, opacity → 1`, 0.5s `hr-settle`, 0.12s later.
- **Colour state flips are sets, not tweens,** when text sits on the colour (index dot turning violet). A mid-tween blend fails contrast for several frames.

## Signature move: the Fan-out

**One buyer question fans out along six hairline connectors to six engine answer cards; a violet
trace runs one connector and the brand's citation ignites in violet italic serif while the other
five answers recede.** Scene: `scenes/hr-engine-fanout.html` (4.0s). Variables: `question`, `cited`.

| t (s)      | Beat                                                                                           | Ease       |
| ---------- | ---------------------------------------------------------------------------------------------- | ---------- |
| 0.10-1.50  | Rings open `scale .9 → 1`                                                                      | settle     |
| 0.15       | Eyebrow "Six engines · one question" slides in                                                 | settle     |
| 0.20-0.32  | Question node slides from `x -48`; question text rises through its mask                        | settle     |
| 0.70       | Connector node pops at the node's right edge                                                   | settle     |
| 0.80-1.65  | Six wires draw, centre-out, 0.07 stagger                                                       | trace      |
| 1.14-2.05  | Six cards land from `x +64`, same order                                                        | settle     |
| 2.10-2.55  | **The trace:** a violet copy of the hero wire draws node to card; node halo widens             | trace      |
| 2.52       | Hero card lifts `x -14, scale 1.035`; violet border and glow fade in                           | settle     |
| 2.56       | Index dot flips violet (set)                                                                   | set        |
| 2.52-3.14  | "Recommends Competitor A" swaps out; "Cites *hyperank.ai*" swaps in (italic serif, violet)    | recede / settle |
| 2.60       | Source chip ignites to violet "CITED"                                                          | settle     |
| 2.64-3.14  | Other five cards and wires recede (0.78 / 0.35)                                                | sine       |
| 1.50-4.00  | Rings breathe `scale 1 → 1.035`                                                                | sine       |
| 3.14-4.00  | Hold                                                                                           |            |

Rules of the move: one hero only; the hero is a middle row; the trace always runs before the
ignition; the cited name is always the accent-italic style. Cut it down by trimming the hold, never
by compressing the trace.

## Seek-safety checklist (hyperframes-animation + lint, learned on this kit)

- One `gsap.timeline({ paused: true })` per composition, registered last: `window.__timelines[ID] = tl`.
- `fromTo` only, never `from`. The **first** `fromTo` on an element owns its baseline; every later `fromTo` on the same element gets `immediateRender: false`, or its from-values leak to t=0 (lint: `gsap_repeated_fromto_without_baseline`).
- Layout constants are pre-calculated in the script (row y, arc offsets, ring radii); nothing measures the DOM at tween time. `getTotalLength()` runs once at setup.
- No `Math.random`, `Date.now`, `repeat: -1`. Orbits are a finite linear rotation across the scene.
- Animate transforms, opacity, `strokeDashoffset`, `boxShadow`; never a `.clip` element's visibility.
- Prefix every id and class per scene (`hr-engine-fanout-*`, `.hrf-*`, `.hrs-*`, `.hre-*`): template styles are global once mounted.
- Gate: `npx hyperframes check` at 0 errors and 0 warnings, then `snapshot` and look.
