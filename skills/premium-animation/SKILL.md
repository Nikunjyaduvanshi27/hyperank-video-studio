---
name: premium-animation
description: Use when Nikunj asks to build, design, or polish a website/landing/hero with motion. Triggers on "animate", "scroll", "smooth", "premium", "transition", "motion", "parallax", "build [X] website", "build [X] landing". Loads distilled GSAP+Lenis+Motion+View-Transitions recipes that AVOID generic AI-slop output. Pair with frontend-design and ui-ux-pro-max.
---

# premium-animation

Distilled from: GSAP 3.15 (100% free since Webflow's 2025 acquisition, incl. SplitText/ScrollTrigger/MorphSVG — no Club GreenSock license needed), Motion 13 (formerly Framer Motion; import from `motion`, not `framer-motion`), Lenis 1.3, View Transitions API, Awwwards SOTD autopsy (10 sites Apr-May 2026), motionsites.ai 65 prompts, Framer marketplace teardown, Codrops 2025-2026 articles.

## When to fire

ANY website/landing/hero build. Fire ALONGSIDE `frontend-design` and `ui-ux-pro-max` (taste + structure), this skill provides the MOTION layer.

## The anti-slop checklist (READ FIRST)

Before writing a single line, confirm the design avoids:
- [ ] Inter / Roboto / Arial / Space Grotesk as primary type
- [ ] Purple-pink gradient on white background
- [ ] Centered hero with one CTA button
- [ ] Identical "Hero / Features / Pricing / Testimonials / Footer" stack
- [ ] Default Tailwind palette (`blue-500`, `purple-600`)
- [ ] 8px rounded corners on every element
- [ ] Default `ease-in-out 300ms` transitions everywhere

If ANY of these slip in, you have produced slop. Restart.

## The premium-feel checklist (REQUIRED)

Every site MUST have:
- [ ] **Premium type** — PP Neue Montreal · Geist · Bricolage Grotesque · Instrument Serif · Migra · Author · Boldonse (Fontshare free or Pangram trial)
- [ ] **OKLCH palette** (Tailwind v4 default) — low chroma backgrounds (~0.02–0.05), single accent at chroma 0.15–0.25
- [ ] **One signature moment** — pick exactly ONE of: scroll-driven 3D camera · WebGL hero shader · Flip route morph · kinetic SplitText reveal · magnetic cursor + image trail · clip-path scroll reveal · WebGL+HTML merged worlds (akella technique)
- [ ] **Asymmetry or grid-breaking** — no symmetric centered hero
- [ ] **`prefers-reduced-motion` gate** on all motion (WCAG 2.3.3)
- [ ] **Lighthouse target** — 90+ desktop / 70+ mobile

## The 2026 canonical stack

```
Next.js 16 (App Router, RSC, Turbopack default) + React 19 + Tailwind v4 (OKLCH default)
+ GSAP 3.15 + ScrollTrigger + Flip + SplitText + @gsap/react useGSAP()
+ Motion 13 (import from `motion`, not `framer-motion`; `motion/react-client` for RSC) — for layout/spring/gesture UI
+ Lenis 1.3 — smooth scroll, NOT Locomotive
+ Native View Transitions API for route changes
+ Rive for interactive vector icons (NOT Lottie unless AE-authored loop)
```

## Canonical Lenis + GSAP setup (the one snippet to memorize)

```ts
'use client'
import { useEffect } from 'react'
import Lenis from 'lenis'
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

gsap.registerPlugin(ScrollTrigger)

export function SmoothScrollProvider({ children }: { children: React.ReactNode }) {
  useEffect(() => {
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) return
    const lenis = new Lenis({ autoRaf: false })
    lenis.on('scroll', ScrollTrigger.update)
    gsap.ticker.add((t) => lenis.raf(t * 1000))
    gsap.ticker.lagSmoothing(0)
    return () => { lenis.destroy() }
  }, [])
  return <>{children}</>
}
```

Reference cloned at `~/.claude/assets/premium-web/satus/` — the Lenis team's own Next.js starter.

## Motion presets that feel premium (NOT default Motion bouncy)

```ts
// design-system/motion.ts — copy this as the project's motion tokens
export const SPRING = {
  // Linear-feel: snappy, ~250ms settle, no overshoot
  snap:    { type: 'spring', stiffness: 400, damping: 40, mass: 1 } as const,
  // Vercel/Apple-feel: smooth, no overshoot
  smooth:  { type: 'spring', stiffness: 300, damping: 30 } as const,
  // iOS sheet feel
  sheet:   { type: 'spring', stiffness: 500, damping: 50 } as const,
  // Hero entrance, soft
  soft:    { type: 'spring', stiffness: 100, damping: 20, mass: 1 } as const,
} as const

export const EASE = {
  // Framer's universal "easeOutExpo" — used in 80% of premium templates
  outExpo:  [0.16, 1, 0.3, 1] as const,
  // The classic "ease-out-expo" alias
  outExpo2: [0.25, 0.1, 0.25, 1] as const,
} as const

// NEVER ship `ease-in-out 0.3s` defaults. Always one of EASE.* above.
```

## The 5 "signature moment" recipes (pick ONE per page)

### A. Scroll-driven shader uniforms (Codrops Nov 2025 pattern)
Lenis drives normalized scroll progress → uniform → fragment shader uTime/uProgress. Live shader stays sharp at any resolution. See `~/.claude/assets/premium-web/akella-exploding/` for the technique.

### B. GSAP Flip route morph
`Flip.getState('.card, .card img')` → navigate → `Flip.from(state)`. Crossfades hero card → product page seamlessly.

### C. SplitText kinetic typography
```ts
const split = SplitText.create(h1, { type: 'lines,words', mask: 'lines' })
gsap.from(split.lines, { yPercent: 110, stagger: 0.08, ease: 'power4.out' })
```

### D. WebGL+HTML merged worlds (Yuri Artiukh)
DOM elements projected into Three.js via shared transforms. Awwwards Academy course is the canonical reference.

### E. View Transitions cross-document MPA-feel
`view-transition-name: hero` on shared element + `experimental.viewTransition: true` in next.config — Chrome 126+/Safari 18.2+ ship 120fps compositor-thread morphs. Firefox still has no cross-document support as of 2026 (same-document transitions work from Firefox 133+); treat the effect as progressive enhancement, never load-bearing for the flow.

## What to copy from cloned reference repos (NEVER paste full files)

- `voltagent-design-md/` — Pick brand archetype (apple/tesla/linear/stripe). Read its `DESIGN.md` directly (ships in-repo per brand folder now, no proxy fetch needed) → distill type/color/elevation rules → encode as Tailwind v4 `@theme` tokens.
- `motionsites/prompts/` — Read the relevant industry prompt (e.g. `Bionova_Biotech.md`, `AI_Automation_Hero.md`) → extract structural ideas (sections, motion sequence) → REWRITE in your design language. Don't ship a motionsites clone.
- `satus/` — Steal the RAF orchestration pattern, NOT the visual.
- `react-bits/` — Pick ONE animated component pattern → reimplement in the project's own type/color tokens. Don't ship 5 react-bits effects on one page.
- `magicui/` — Same. Pick at most one of {Marquee, Animated Beam, Globe, Border Beam, Meteors}. Stacking them = slop.
- `bruno-room/` — Reference for baked-lighting GLB pipeline.
- `lygia/` — Import the noise/sdf functions you need; don't ship the whole library.

## Output structure for a build

When asked "build [X] website", output in this order:

1. **Brand archetype pick** — which `voltagent-design-md/` file is closest? Or "neither — going [direction] because [reason]".
2. **Aesthetic commitment** — one bold direction (brutalist / editorial / motion-driven / etc.).
3. **Type + color tokens** — premium font pairing + OKLCH palette in Tailwind v4 `@theme`.
4. **Signature moment** — which of the 5 recipes above + WHY it fits the brand.
5. **Page architecture** — sections, NOT the default stack. Asymmetric where possible.
6. **Code** — Next.js 16 + RSC + the canonical Lenis+GSAP setup + chosen signature moment.
7. **Perf gate** — explicit Lighthouse target + `prefers-reduced-motion` fallback.
8. **What I deliberately did NOT include** — note 2-3 obvious-but-cliche moves you skipped.

## Hard rules

- ONE signature moment per page. Two = noise. Three = slop.
- NEVER center a hero with a single CTA button.
- NEVER ship without `prefers-reduced-motion` gate.
- NEVER use `ease-in-out 0.3s` as the default transition.
- NEVER paste a full file from `assets/premium-web/`. Always distill.
- ALWAYS Lighthouse before claiming done.

## Mulch records to consult

- `frontend / decision / GSAP + Lenis over Locomotive`
- `frontend / convention / motion tokens live in design-system/motion.ts`
- `frontend / convention / always gate smooth-scroll on prefers-reduced-motion`
- `frontend / failure / AI-slop animation defaults`

## Sources distilled here

GSAP 3.15 release notes · Motion 13 docs (motion.dev) · Lenis README · Codrops "Cinematic 3D Scroll" Nov 2025 · Awwwards SOTD autopsy 2026-04-22→05-01 (10 sites: Adcker, Studio375, PieterKoopt, Silent House, Detroit Paris, Off Menu, Lando Norris, Bruno Simon, MindMarket) · Framer marketplace 30+ premium template sample · motionsites.ai 65 prompts · React 19 useGSAP pattern · Next.js 16 release notes.

Content refreshed: 2026-08-13
