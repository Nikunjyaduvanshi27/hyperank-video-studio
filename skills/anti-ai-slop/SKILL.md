---
name: anti-ai-slop
description: >-
  Nikunj's signature-taste layer for NEW web UI, fires WITH taste-skill (the primary mechanical rulebook). Adds the three things taste-skill doesn't cover: declare ONE explicit aesthetic stance before coding, enforce the one-signature-moment principle (named reference sites), and ban slop copy phrases. Fires on "build website", "design landing", "create UI", "make a page" alongside taste-skill → frontend-design → ui-ux-pro-max → premium-animation.
---

# anti-ai-slop

The stance + signature + copy layer. `taste-skill` owns the mechanical rules (banned hex palettes, font/eyebrow/CTA rules, motion skeletons — ~60 hard rules); THIS skill adds what it lacks. Demoted from primary rulebook to companion layer 2026-07-07 (superseded sections now live in taste-skill with more mechanical enforcement).

## When to fire

On any new-build design brief, WITH `taste-skill` (which fires first). For existing sites, neither fires — that's `redesign-skill`.

## Required moves (pick a stance, commit)

Before writing a line, declare the aesthetic direction explicitly, **by name**.

The named directions with real palettes (role-mapped hex, contrast pre-computed) and fixed type pairings
live in `taste-skill/references/aesthetic-directions.md`: Cobalt Brut, Halide, Chalk Court, Tidal Slate,
Sodium Vapor, Porcelain and Graphite, Reactor, Newsprint Mono. Read that file and pick one.

Broader stances, if none of the eight fits and you are authoring a ninth:

```
[ ] Brutalist / raw HTML aesthetic (heavy borders, mono type, asymmetric)
[ ] Motion-driven (GSAP scroll narrative as primary content)
[ ] 3D-hyperrealist (R3F hero scene as signature moment)
[ ] Retro-futurist (CRT scanlines, chromatic aberration, neon, pixel grid)
[ ] Swiss Modernism 2.0 (precision grid, single accent, weight-only hierarchy)
[ ] Anti-design / vaporwave (broken layouts, stock-imagery-as-irony)
```

Authoring a ninth means writing the full hex table and computing every contrast ratio, not naming a mood.

PICK ONE. Don't blend three. Don't pick "minimalist", that's a slop fallback. And check
`taste-skill/references/self-slop.md` first: the direction and display font may not repeat either of
the previous two builds, and cream + rust + Playfair is banned outright.

## Banned phrases in copy

- "Welcome to [product]"
- "Made with ❤️"
- "Your [thing] reimagined"
- "Built for the future of [industry]"
- "Empowering [vague verb]"
- "Seamless / Effortless / Intuitive" (one is OK if specific, three = slop)
- "Game-changer / Revolutionary / Disruptive"

Replace with concrete, specific, voiced copy.

## The signature-moment principle

Every premium site has exactly ONE thing it's known for. Pick from:
- Apple's scroll-driven product video scrub
- Linear's gradient-mesh hero + perfect type
- Stripe's animated WebGL gradient
- Bruno Simon's drivable 3D world
- Active Theory's WebGL+DOM merged interactions
- Lusion's photoreal product shaders
- Igloo Inc's full-bleed creative coding
- Lando Norris's Rive helmet gallery

Steal the PRINCIPLE (one signature interaction), not the asset.

## Self-audit before claiming done

Run this against **screenshots**, not against the source. You cannot audit a look you have not seen.

```
1. Could a competitor's "$50 fiverr Tailwind site" look identical? → restart
2. Is there one distinctive thing I'd point to as the signature? → name it
3. Does it look like a v0.app or Lovable default? → restart
4. Did taste-skill's hard rules all pass? → if unsure, re-run its checklist
5. Is there a declared stance and exactly one signature moment? → if not, restart
6. Could I paste this palette + type pairing onto the LAST site I built and have nobody notice?
   → if yes, I built the same site twice (taste-skill/references/self-slop.md)
7. Do I have screenshot paths proving 1-6, or am I describing what I intended to build?
   → no evidence means not done (taste-skill/references/visual-qa-loop.md)
```

## Workflow

1. User says "build [X] website"
2. `taste-skill` fires FIRST: dials, design-system routing, the ~60 mechanical hard rules, plus `aesthetic-directions.md` + `self-slop.md` before any color or font decision
3. THIS skill: declare the named stance, pick the ONE signature moment, scrub copy
4. `voltagent-design-md` picks brand archetype OR you go off-script
5. `frontend-design` enforces production taste
6. `ui-ux-pro-max` provides type/color/structure lookups (verify hexes against taste-skill's bans — parts of its colors.csv predate them)
7. `premium-animation` provides motion layer
8. `interactive-3d` if signature moment is 3D
9. `taste-skill/references/visual-qa-loop.md` gates "done": render, screenshot, critique, iterate. No screenshot evidence means not done.
10. `verification-loop` gates the final ship (build + type + lint + test + security; Lighthouse targets live in `performance-a11y.md`)

## Mulch records this skill enforces

- `feedback / no-ai-slop` (anchor)
- `frontend / failure / AI-slop animation defaults`
- `frontend / convention / forbidden defaults list` (mechanical lists now enforced by taste-skill)
