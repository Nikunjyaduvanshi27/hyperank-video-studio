# tutorial-ai-readiness-audit: AI Readiness Audit

Status: READY for the render queue. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: https://www.nasa.gov. Master 16:9 (1920x1080). Project: `tutorials/ai-readiness-audit/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Public run (no gate): `premium/capture/try-nasa.gov/api.json` and `result-sec.html`, `result-text.txt`.
- Candidates tried: allrecipes.com (rejected: the audit read a 35-word page with no H1 and no meta tags, so the fetch did not see the real site and the result would misrepresent it), nasa.gov (picked: a full page read, a clear mix of strong and weak checks).
- "Thirteen weighted checks" is from the tool page's own How it works copy.

| Value | Where it shows |
|---|---|
| 75 overall, AI Optimization Level 75/100 | Overall AI Readiness Score card |
| 8 of 8 major AI crawlers can read this site | AI Bot Accessibility card, 100/100 |
| No llms.txt at the site root | LLMs.txt Implementation card, 0/100, and Critical Issues |
| 0 H1, 98 headings total | Heading Structure card, 60/100 |
| Fixes listed with the check and score each belongs to | Recommendations, Basic Improvements |

## Intent

Goal: a site owner sees how one page scores for answer engines and which gaps cost it | Platform: tool page, social | Length: 35 to 45s | Success: viewer audits one of their own pages.

One reader: a content lead at a large organisation whose site already ranks. Belief now: "a big, well-built site is ready for AI search." Belief after: "even a strong page can miss the basics answer engines look for, and the audit names them."

## Hook candidates (different categories)

1. Question (picked): super "Ready for answer *engines?*", VO "Before an answer engine quotes a page, it has to reach it and read it."
2. Number: "75 out of 100." Rejected for the hook: the number belongs to NASA, not the viewer.
3. Contrast: "Every crawler allowed. Still not ready." Rejected: needs the result on screen to land.

## Script

Runtime 39.23s

| # | VO starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.3 | Ready for answer *engines?* | Before an answer engine quotes a page, it has to reach it and read it. |
| 2 name | 4.811 | AI Readiness *Audit* | Meet the AI Readiness Audit, from hyperank. |
| 3 type | 7.913 | Paste one *page.* | Enter one page. Here, the NASA home page. |
| 4 press | 11.213 | One *press.* | It fetches the page, then robots.txt, llms.txt and the sitemap. |
| 5 result | 17.665 | Thirteen checks, one *score.* | Thirteen weighted checks. NASA scores 75. |
| 6 read | 21.451 | Every AI crawler *allowed.* | All eight major AI crawlers can read the site. |
| 7 read | 24.809 | But no *llms.txt.* | But there is no llms.txt at the site root. |
| 8 read | 28.552 | Zero *H1s.* | And 98 headings, without one H1 naming the page. |
| 9 read | 32.615 | Work down the *list.* | Then every fix, next to the check it would raise. |
| 10 close | 36.265 | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    Before an answer engine quotes a page, it has to reach it and read it.
    Meet the A-I Readiness Audit, from Hyper-rank.
    Enter one page. Here, the NASA home page.
    It fetches the page, then robots dot t-x-t, L-L-M-s dot t-x-t, and the sitemap.
    Thirteen weighted checks. NASA scores seventy-five.
    All eight major A-I crawlers can read the site.
    But there is no L-L-M-s dot t-x-t at the site root.
    And ninety-eight headings, without one H-1 naming the page.
    Then every fix, next to the check it would raise.
    Free to run. Hyper-rank dot A-I.

Spoken words: 92

## Honesty notes

- The overall score (75) and the optimization bar (75/100) are the same number, so only one score is ever in play.
- "Every AI crawler allowed" means the eight major crawlers the audit tests, which the VO states.
- No gate. Sequence shortened from the click to the result.
- Engine tiles in the hook use each operator's official mark (nominative use; sources in `tutorials/music/LICENSES.md`).
- Standard close: super "Free to run.", printed "Full report with a free account.", then hyperank.ai. No tool count anywhere.

## Humanizer pass

- Draft hook super "Can answer engines quote you?" carried a two-word accent. Now "Ready for answer engines?" with one accent word.
- Captions keep digits (75, 98); TTS spells them.
- No em dashes, no banned words, no tool count, no signup line.
