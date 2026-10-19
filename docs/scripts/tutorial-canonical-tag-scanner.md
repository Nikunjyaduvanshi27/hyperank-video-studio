# tutorial-canonical-tag-scanner: Canonical Tag Scanner

Status: READY for the render queue. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: https://www.wired.com/. Master 16:9 (1920x1080). Project: `tutorials/canonical-tag-scanner/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Public run (no gate): `premium/capture/try-wired/result-sec.html` and `result-text.txt` (Correctly Self-Canonicalized, recommendation "No action needed for this page", SEO Health Score 100 over 21 pages, Duplicate Content Risk 0%, Scanned Pages table: 21 of 21 rows SELF and HTTP 200, counted from the capture).
- Sitemap step: the tool page's How to use text (reads /sitemap.xml, up to 20 more URLs).
- Candidates tried: https://www.python.org/ (missing canonical, 1 page scanned), https://www.wired.com/ (self-canonical, 21 pages). Picked Wired.

| Value | Where it shows |
|---|---|
| Verdict | Correctly Self-Canonicalized, Canonical: https://www.wired.com/ |
| Recommendation | No action needed for this page |
| Site-wide score 100, 21 pages | SEO Health Score card |
| Duplicate risk 0% | Duplicate Content Risk card |
| Every row SELF, 200 | Scanned Pages (21) table |

## Intent

Goal: an SEO lead confirms a page and its sitemap neighbours point canonicals at themselves | Platform: tool page, social | Length: 30 to 40s | Success: viewer scans their own page.

One reader: an SEO who inherited a site and suspects duplicate URLs. Belief now: "I would have to view source page by page." Belief after: "one scan reads the page and the sitemap, row by row."

## Hook candidates (different categories)

1. Question (picked): super "Which URL *counts?*", VO "One page, several addresses. The canonical tag says which one counts."
2. Stake: "Google might index the wrong URL." Rejected: fear-led, and the demo result is clean.
3. Number: "Twenty-one pages, one scan." Rejected as a hook, kept as a read beat.

## Script

Runtime 35.88s

| # | VO starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.3 | Which URL *counts?* | One page, several addresses. The canonical tag says which one counts. |
| 2 name | 5.216 | Canonical Tag *Scanner* | Meet the Canonical Tag Scanner, from hyperank. |
| 3 type | 8.361 | Start from one *URL.* | Paste a page address. Here, the Wired home page. |
| 4 press | 11.891 | Page, then *sitemap.* | It reads that page's canonical, then more pages from the sitemap. |
| 5 result | 16.145 | Points at *itself.* | Wired's home page names itself as the canonical. |
| 6 read | 19.696 | Nothing to *fix.* | The recommendation for this page: no action needed. |
| 7 read | 23.332 | 21 pages *scanned.* | Across twenty-one pages, the health score is one hundred, and duplicate risk is zero. |
| 8 read | 28.995 | Row by *row.* | Every scanned page is marked SELF, next to its status code. |
| 9 close | close | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    One page, several addresses. The canonical tag says which one counts.
    Meet the Canonical Tag Scanner, from Hyper-rank.
    Paste a page address. Here, the Wired home page.
    It reads that page's canonical, then more pages from the sitemap.
    Wired's home page names itself as the canonical.
    The recommendation for this page: no action needed.
    Across twenty-one pages, the health score is one hundred, and duplicate risk is zero.
    Every scanned page is marked SELF, next to its status code.
    Free to run. Hyper-rank dot A-I.

Spoken words: 85

## Honesty notes

- The 100 and 0% are the tool's own site-wide figures for this run; the film compares Wired with no one.
- "Every scanned page is marked SELF" was counted: 21 of 21 rows.
- No gate. Sequence shortened from the click to the result.
- Standard close: super "Free to run.", printed "Full report with a free account.", then hyperank.ai. No tool count anywhere.

## Humanizer pass

- No em dashes in VO, supers or this file's own prose; no banned words, no tool count, no signup line. Dashes inside the live UI (for example the feed count line) stay as the page renders them.
- Pronunciation checked with whisper (small.en): brand names and acronyms transcribe as written.
