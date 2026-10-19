# tutorial-ai-visibility-report: AI Visibility Report

Status: READY for the render queue. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: shopify.com. Master 16:9 (1920x1080). Project: `tutorials/ai-visibility-report/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Logged-in run in BrowserOS neo (Profile 1, the hyperank.ai account, verified on chrome://version by `neo_capture.py` before the run): `premium/capture/neo-shopify.com/neo-api.json` (POST `/api/tools/ai-visibility-report`, input `shopify.com`) and the unlocked result DOM `neo-result-sec.html`.
- `neo-result-sec.settled.html` is the same DOM with two fixes only: the six hero entrance styles (`opacity:0; blur; translateY`, captured mid-animation in a background tab) set to their end state, and the competitor favicons served from local copies (`ico/`); Magento's favicon, hidden on the live page because it failed to load, is dropped.
- Gate card: the anonymous runs of this tool hit the site's rate limit, so the logged-out gate card comes from the identical site-wide component in `chatgpt-visibility-checker/premium/capture/try-canva.com/result-sec.html`, copied to `capture/gate-card-from-chatgpt-try-canva.html`. Its text ("Your results are ready / Sign up free to see the full report. / Sign up free to unlock") is the same on every gated tool.
- One candidate run: shopify.com gave a clear split (Technical SEO high, AEO low) with concrete fixes, so no second candidate was spent against the rate limit.

| Value | Where it shows |
|---|---|
| 63 out of 100 | score ring, "Analysis for Shopify" |
| Technical SEO 36/40, 11 of 12 checks | Technical SEO pillar card |
| AEO 9/30, 3 of 9 checks | AEO pillar card |
| Knows the brand, confidence: high | "How ChatGPT sees Shopify" card |
| FAQ schema or FAQ pattern, AEO, HIGH, "1 question-style headings" | Improvement Opportunities |
| Image alt-text coverage 80%+, HIGH, "14% of 56 images" | Improvement Opportunities |
| Thirty weighted checks on one page | tool page "What is the AI Visibility Report?" |

## Intent

Goal: a site owner sees that ranking signals and answer-engine signals are scored apart, and what to fix first | Platform: tool page, social | Length: 35 to 45s | Success: viewer runs the report on their own domain.

One reader: the SEO lead at a SaaS company whose technical audit is green. Belief now: "our SEO is clean, so AI engines can use our pages." Belief after: "crawlable and quotable are scored separately, and the report lists the fixes."

## Hook candidates (different categories)

1. Contrast (picked): super "Crawlable. But *quotable?*", VO "Search crawlers can read your site. Can an AI engine lift an answer from it?" Uses the page's own AEO definition ("whether an engine can lift a clean answer out of it").
2. Number: "Sixty-three of 100." Rejected: Shopify's number, not the viewer's.
3. Question about ChatGPT: "Does ChatGPT know your brand?" Rejected: the ChatGPT and brand visibility videos already open on that question.

## Script

Runtime 39.19s

| # | VO starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.3 | Crawlable. But *quotable?* | Search crawlers can read your site. Can an AI engine lift an answer from it? |
| 2 name | 5.02 | AI Visibility *Report* | Meet the AI Visibility Report, from hyperank. |
| 3 type | 8.36 | Any *homepage.* | Enter a domain. Here, shopify.com. |
| 4 press | 11.59 | Thirty *checks.* | It runs thirty weighted checks on the home page. |
| 5 gate | 14.48 | *Ready.* | A free account opens the full report. |
| 6 read | 17.22 | Sixty-three of *100.* | Shopify scores sixty-three out of a hundred. |
| 7 read | 20.49 | SEO high. AEO *low.* | Technical SEO, thirty-six of forty. Answer readiness, nine of thirty. |
| 8 read | 25.54 | ChatGPT knows *Shopify.* | ChatGPT knows the brand, with high confidence. |
| 9 read | 29.26 | What to fix *first.* | First fixes: FAQ markup, and image alt text. Fourteen percent of fifty-six images have it. |
| 10 close | close | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    Search crawlers can read your site. Can an A-I engine lift an answer from it?
    Meet the A-I Visibility Report, from Hyper-rank.
    Enter a domain. Here, Shopify dot com.
    It runs thirty weighted checks on the home page.
    A free account opens the full report.
    Shopify scores sixty-three out of a hundred.
    Technical S-E-O, thirty-six of forty. Answer readiness, nine of thirty.
    Chat G-P-T knows the brand, with high confidence.
    First fixes: F-A-Q markup, and image alt text. Fourteen percent of fifty-six images have it.
    Free to run. Hyper-rank dot A-I.

## Honesty notes

- The result is gated for logged-out users; the film shows the real gate card and says once "A free account opens the full report."
- "Answer readiness" is how the VO says AEO; the tool page defines AEO as whether an engine can lift a clean answer out of the page.
- "ChatGPT knows the brand" is the card's own badge ("Knows the brand", "confidence: high"); the card notes it is generated from public site content.
- The wait is compressed, so `Sequence shortened` shows from the click to the result.
- Standard close. No tool count, no signup line, no em dashes.
