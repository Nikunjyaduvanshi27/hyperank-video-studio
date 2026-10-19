# VISUAL QA LOOP: Render, Screenshot, Critique, Iterate

Read this **before claiming any UI is done**. Not after. This is the gate that turns a plausible-looking
diff into a verified page.

**The premise:** code review cannot see a page. Contrast math, a hex table, and a passed preflight
checklist all describe intent. They do not tell you that the hero headline wrapped to four lines at
1280px, that the amber pooled in two directions, that the focus ring is invisible on the accent fill,
or that the mobile nav overlays the CTA. Those are only observable in a render.

**The hard rule, stated once:**
> No UI is done until it has been rendered, screenshotted, critiqued against the rubric in section 5,
> and iterated. "Done" without a screenshot path is not a claim, it is a guess.

---

## 1. THE LOOP

```
  BUILD ──> SERVE ──> CAPTURE ──> CRITIQUE ──> [pass?] ──> LEDGER + REPORT
              ^                        |
              |                        v
              └───────── FIX (top 3 findings only) 
```

**Iteration cap: 3 rounds.** Not a suggestion. If the rubric still fails after round 3, stop and report
the surviving findings with evidence. Thrashing past 3 rounds means the problem is the design read or
the chosen direction, not the CSS, and that is a decision to surface, not to grind on.

**One more stopping condition:** if the *same* finding survives two consecutive rounds, stop
immediately. You are not fixing it, you are restating it. Report it.

---

## 2. SERVE: getting a real render

Preference order. Do not skip to a lower rung because a higher one needs setup.

| Rung | How | Use when |
|---|---|---|
| 1 | `preview_start({ name })` with a `.claude/launch.json` entry, then `navigate` | A dev server exists or can be defined. This is the default for Next.js, Vite, Astro. |
| 2 | `preview_start({ url })` | Already-running server, or a deployed preview URL. |
| 3 | Playwright MCP: `browser_navigate` to a `file:///` path | Single self-contained HTML file, no build step. |
| 4 | `mcp__chrome-devtools__navigate_page` | You also need `lighthouse_audit` or a performance trace in the same pass. |

**Windows path note:** use forward slashes in every URL and tool argument. `file:///C:/Users/.../index.html`.

**Never** critique from source code alone and describe it as if seen. Never critique a static mockup
image as a substitute for the built page. If you genuinely cannot serve the page, say
"could not render, unverified" and stop. That sentence is always acceptable. A fabricated visual
assessment never is.

---

## 3. CAPTURE: the evidence matrix

Save every screenshot under the session scratchpad with a stable naming scheme:

```
<scratchpad>/visual-qa/r<round>-<viewport>-<theme>-<state>.png
example: r1-390-dark-hero.png, r1-1280-light-full.png
```

**Viewport matrix (all four, every round):**

| Label | Size | Why this one |
|---|---|---|
| `390` | 390 x 844 | Real iPhone width. Where hero text wrapping and touch targets break. |
| `768` | 768 x 1024 | The tablet dead zone where two-column layouts collapse badly. |
| `1280` | 1280 x 800 | The most common laptop. The default judgment viewport. |
| `1600` | 1600 x 1000 | Where max-width failures and stranded content show up. |

Tools: `resize_window({ preset })` or explicit `width`/`height`; Playwright `browser_resize`;
chrome-devtools `resize_page`. Reload after resizing to 390 so load-time device gates re-run.

**Theme:** both, if the page ships both. `resize_window({ colorScheme: "dark" })` toggles it, or
chrome-devtools `emulate`. The PAGE THEME LOCK is only checkable in a render.

**States to capture, beyond the top of the page:**
1. `full` : full-page screenshot at 1280, light and dark. This is the composition and rhythm evidence.
2. `hero` : first viewport only, every width. Checks the hero-fits rule mechanically.
3. `focus` : press `Tab` to the primary CTA and capture. The focus ring must be visible against the accent fill. This is the single most-skipped check.
4. `hover` : `hover` on the primary CTA.
5. `mid` : one section boundary mid-page, to catch theme flips and layout repetition.
6. `motion` : two frames of the signature moment, before and after. One frame proves nothing moved.
7. `empty` / `error` : any form or data surface, in its empty and error state.

**Also collect, not screenshots but required:**
* `read_console_messages({ onlyErrors: true })` or Playwright `browser_console_messages`. Zero errors is a gate.
* A DOM measurement pass for the things the eye estimates badly. Run via `javascript_tool` / `browser_evaluate` / `evaluate_script`:
  * rendered `font-size` and `line-height` of the display headline and body
  * body measure in characters (`getBoundingClientRect().width` divided by approximate character width)
  * `document.documentElement.scrollWidth > window.innerWidth` (horizontal overflow, a hard blocker)
  * count of elements with `text-transform: uppercase` and small font-size (the mechanical EYEBROW COUNT)
  * every distinct `border-radius` value in use (the SHAPE CONSISTENCY LOCK)

---

## 4. CRITIQUE: how to look

The failure mode here is not missing a bug. It is writing a paragraph of praise about a page you
glanced at. Two mechanics prevent that.

**4.A Describe before you judge.** For each screenshot, write one factual sentence about what is
actually visible, with no evaluative words: "At 390 the headline occupies four lines and the primary
CTA is below the fold." Not "the mobile hero looks a bit tight." Description first forces you to look;
evaluation first lets you pattern-match to what you expected to build.

**4.B Adopt the adversary.** Ask, in order:
1. What would a senior designer point at first, in the first two seconds?
2. Which single element looks most like it was generated rather than designed?
3. Does this render match the **declared aesthetic direction by name**, or did it drift toward the house defaults in `references/self-slop.md`?
4. If I saw this with no context, could I name the product category and the intended audience?
5. What is the signature moment, and is it visible in the evidence I actually captured?

**4.C Banned in a critique**
* "Looks clean", "looks polished", "looks premium", "modern and professional". Empty.
* Any assessment of a viewport or state you did not capture.
* Grading your own intent. The rubric scores the render, not the plan.
* Listing more than the top 3 findings per round for fixing. More than 3 fixes at once means you cannot attribute the next round's change to anything.

---

## 5. THE RUBRIC

Score each row 0 to 3 against the captured evidence.
`0` = broken, `1` = visibly weak, `2` = acceptable, `3` = deliberate and strong.

| # | Category | W | What a 3 looks like |
|---|---|---|---|
| 1 | **Direction fidelity** | 3 | The render is unmistakably the named direction from `aesthetic-directions.md`. Palette and type match the declared table, no drift toward self-slop. |
| 2 | **First viewport** | 3 | Headline 2 lines or fewer at every width, CTA visible without scrolling, 4 or fewer text elements, top padding within `pt-24`. |
| 3 | **Contrast and focus** | 3 | Measured, not assumed. Body and CTA pass AA. Focus ring clearly visible on every interactive element, including on accent fills. |
| 4 | **Responsive integrity** | 3 | No horizontal overflow at 390. No overlap, no stranded content at 1600. Touch targets 44px or more. Nothing collapses into the tablet dead zone. |
| 5 | **Signature moment** | 3 | One distinctive moment, proven by evidence (a frame pair or a captured interaction), not a gradient, glass card, bento grid, or fade-in. |
| 6 | **Type hierarchy** | 2 | Measured display-to-body ratio of 1.5x or greater, measure within 60 to 75ch, no orphan lines in headings, italic descenders uncut. |
| 7 | **Color discipline** | 2 | One accent across every section. One theme, no mid-page inversion. One neutral family. One radius system. |
| 8 | **Layout variance** | 2 | 4 or more distinct layout families across 8 sections. No 3 consecutive splits. Section rhythm visible in the full-page capture. |
| 9 | **Content reality** | 2 | Real images or labeled placeholder slots. No fake div screenshots, no lorem, no Acme, no fabricated metrics. Longest realistic string tested. |
| 10 | **Motion** | 2 | Motion justified in one sentence, visible in the frame pair, `prefers-reduced-motion` honored and verified in a reduced-motion capture. |
| 11 | **Console clean** | 1 | Zero console errors. No hydration warnings, no 404 assets. |

**Hard blockers.** Any of these means fail regardless of total score:
* Horizontal overflow at 390 (row 4 at 0).
* Any text below AA (row 3 at 0).
* Invisible focus indicator (row 3 at 0).
* CTA below the fold at 1280 (row 2 at 0).
* Any console error (row 11 at 0).
* No screenshot evidence for a row you scored.

**Pass bar:** weighted total 80% or higher (score x weight, summed, over 75), **and** no weight-3 row
below 2, **and** no hard blocker. Anything less is another round.

---

## 6. REPORT FORMAT (paste this, filled in)

```
VISUAL QA - round <n> of 3
Direction: <named direction>   Dials: V<n>/M<n>/D<n>
Served via: <rung + url>

Evidence:
  <scratchpad>/visual-qa/r1-390-light-hero.png
  <scratchpad>/visual-qa/r1-1280-light-full.png
  ... (one line per capture, paths must exist)

Measured: display 64px/1.02 · body 17px/1.62 · measure 68ch · scrollWidth==innerWidth OK
Console: 0 errors

Rubric: 1:3 2:3 3:3 4:2 5:3 6:2 7:3 8:2 9:2 10:2 11:1  =  68/75 (91%)
Blockers: none

Top findings this round:
  1. <finding> -> <fix applied>
  2. ...

Verdict: PASS / another round / STOP (finding survived two rounds)
Ledger row appended: yes
```

Every path in that block must be a file that exists. A report citing a screenshot that was never taken
is worse than no report, because it converts an unknown into a false positive.

---

## 7. WHERE THIS SITS

* Run **after** `references/preflight-check.md`. Preflight checks the code you are about to write; this checks the page it produced. Both are mandatory and they are not substitutes.
* `references/performance-a11y.md` owns Core Web Vitals thresholds. If a perf number is needed, use `mcp__chrome-devtools__lighthouse_audit` in this same pass rather than a second serve.
* On the last passing round, append the rotation ledger row (`references/self-slop.md` section 4).
* Related skills, for the deeper versions of individual boxes: `webapp-testing` for the harness, `benchmark` for perf baselines, `accessibility` for a full WCAG audit.
