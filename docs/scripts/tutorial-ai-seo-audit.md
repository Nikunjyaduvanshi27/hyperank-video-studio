# tutorial-ai-seo-audit: AI SEO Audit

Status: READY for the render queue. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: https://www.rottentomatoes.com. Master 16:9 (1920x1080). Project: `tutorials/ai-seo-audit/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Gate card: anonymous run `premium/capture/try-patagonia.com/result-sec.html` (only the logged-out "Your results are ready" card is used; that run's report is never shown).
- Unlocked result: logged-in run through BrowserOS neo (Profile 1, hyperank.ai), `premium/capture/neo-rottentomatoes.com/neo-result-sec.html`, `neo-result-text.txt`, `neo-api.json`. Every number on screen and in the VO comes from this run.
- Candidates: patagonia.com (rejected: the audit saw no H1, no meta description and no internal links, so the fetch did not see the real page), python.org (anonymous run rate-limited), wikipedia.org and w3.org (taken by sibling videos), rottentomatoes.com (picked: a full read with a clear pass and fail mix).
- "Sixteen signals" and "measures first, then grades" are from the tool page's own How it works copy.

| Value | Where it shows |
|---|---|
| Overall Rating: C (70/100) | Report header |
| Content Structure 50, the lowest of the four sub-scores (100, 75, 80, 50) | Sub-score dials |
| There are no H1 tags on the page. | H1 Tag check |
| JSON-LD structured data is not implemented. | Structured Data (JSON-LD) check |
| Only 13 out of 31 images have alt text. | Image Alt Text check |
| Four recommendations | Recommendations to Improve Your Score |

## Intent

Goal: a site owner sees a measured, graded technical read of one page | Platform: tool page, social | Length: 30 to 40s | Success: viewer audits one of their own pages.

One reader: a marketing lead at a media brand who assumes the dev team covered the SEO basics. Belief now: "a big site has the basics." Belief after: "a measured audit shows which basics a real page is missing, and what to fix."

## Hook candidates (different categories)

1. Contrast (picked): super "Measured, not *guessed.*", VO "This audit measures the page first, then grades it."
2. Question: "Can answer engines parse your page?" Rejected: too close to the sibling AI Readiness Audit hook.
3. Number: "Graded C." Rejected for the hook: the grade belongs to Rotten Tomatoes, not the viewer.

## Script

Runtime 35.91s

| # | VO starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.3 | Measured, not *guessed.* | This audit measures the page first, then grades it. |
| 2 name | 3.595 | AI SEO *Audit* | Meet the AI SEO Audit, from hyperank. |
| 3 type | 7.039 | Point it at a *page.* | Enter one page. Here, the Rotten Tomatoes home page. |
| 4 press | 11.214 | One *press.* | It fetches the page, times it, and checks sixteen signals. |
| 5 gate | 14.999 | *Ready.* | A free account opens the full report. |
| 6 read | 17.739 | Graded *C.* | A C, at 70 out of 100. Content structure scores lowest. |
| 7 read | 22.378 | Two basics *missing.* | No H1 on the page, and no JSON-LD. |
| 8 read | 25.886 | Alt text *gaps.* | Only 13 of 31 images have alt text. |
| 9 read | 29.287 | Four fixes to *make.* | Then four fixes to raise the score. |
| 10 close | 32.937 | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    This audit measures the page first, then grades it.
    Meet the A-I, S. E. O. Audit, from Hyper-rank.
    Enter one page. Here, the Rotten Tomatoes home page.
    It fetches the page, times it, and checks sixteen signals.
    A free account opens the full report.
    A C, at seventy out of a hundred. Content structure scores lowest.
    No H-1 on the page, and no J-SON L-D.
    Only thirteen of thirty-one images have alt text.
    Then four fixes to raise the score.
    Free to run. Hyper-rank dot A-I.

Spoken words: 78 (whisper check: "AI SEO audit" and "JSON-LD" heard correctly after respelling).

## Honesty notes

- One overall score in play (70/100, grade C); sub-scores are introduced as sub-scores and only the lowest is named.
- The audit reads one page; the VO says "the Rotten Tomatoes home page", never "the site".
- The gate card is the real logged-out card from another input; the report under it and after "unlock" is the Rotten Tomatoes run.
- Sequence shortened from the click to the result.
- Standard close: super "Free to run.", printed "Full report with a free account.", then hyperank.ai. No tool count anywhere.

## Humanizer pass

- First cut lifted whole check rows; the text was too small at phone size, so the lifts now carry just the check name and its sentence.
- No em dashes, no banned words, no tool count, no signup line.
