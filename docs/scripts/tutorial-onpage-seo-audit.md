# tutorial-onpage-seo-audit: On-Page SEO Audit

Status: prepared for the render queue. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: https://www.bbc.co.uk/food/recipes, target keyword "recipes". Master 16:9 (1920x1080). Project: `tutorials/onpage-seo-audit/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Public run (no gate): `premium/capture/try-bbcfood/result-sec.html` and `result-text.txt`.
- Tool page copy (`premium/capture/page-text.txt`): "Every on-page issue on one URL ... with the element that caused it"; "The tool fetches the HTML the server sends, the version a crawler receives first".
- One candidate run (anonymous runs are rate-limited).

| Value | Where it shows |
|---|---|
| 73/100; 0 Critical Issues, 3 Warnings, 8 Good Elements | SEO Score card |
| Title tag too short: 18 characters; "Expand it to 30 to 60 characters." | Issues, Title Tag |
| Meta description too short: 50 characters; "Expand toward 120 to 160 characters." | Issues, Meta Tags |
| Images without alt text: "9 of 31 images carry no alt attribute." | Issues, Images |

## Intent

Goal: a site owner gets a ranked fix list for one page | Platform: tool page, social | Length: 35 to 45s | Success: viewer audits their own page.

One reader: an in-house marketer who owns a few landing pages. Belief now: "an audit is a score." Belief after: "each warning shows the element and the fix."

Distinct from the On-Page SEO Checker film: this one leads on the element behind each issue and the recommendation box, and uses the keyword field.

## Hook candidates (different categories)

1. Claim (picked): super "Find the *culprit.*", VO "An audit helps most when it points at the element to fix." Mirrors the page's "with the element that caused it".
2. Question: "What is your page's score?" Rejected: score-first, the angle the sibling checker film takes.
3. Number: "Three warnings on BBC Food." Rejected: a judgment on a brand before the viewer knows the tool.

## Script

Runtime 38.95s

| # | VO starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.3 | Find the *culprit.* | An audit helps most when it points at the element to fix. |
| 2 name | 3.915 | On-Page SEO *Audit* | Meet the On-Page SEO Audit, from hyperank. |
| 3 type | 7.295 | Add a *keyword.* | Paste one page, and a keyword if you have one. Here, BBC Food's recipes page. |
| 4 press | 13.277 | One *press.* | It reads the HTML the server sends, the version a crawler gets first. |
| 5 result | 18.236 | Three *warnings.* | Seventy-three. No critical issues, three warnings, eight good elements. |
| 6 read | 22.917 | Title too *short.* | The title is eighteen characters. It says expand to thirty to sixty. |
| 7 read | 27.577 | Same for the *description.* | The meta description is fifty characters. Aim for one twenty to one sixty. |
| 8 read | 32.515 | Missing *alt* text. | And nine of thirty-one images carry no alt text. |
| 9 close | close | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    An audit helps most when it points at the element to fix.
    Meet the On-Page S-E-O Audit, from Hyper-rank.
    Paste one page, and a keyword if you have one. Here, B-B-C Food's recipes page.
    It reads the H-T-M-L the server sends, the version a crawler gets first.
    Seventy-three. No critical issues, three warnings, eight good elements.
    The title is eighteen characters. It says expand to thirty to sixty.
    The meta description is fifty characters. Aim for one twenty to one sixty.
    And nine of thirty-one images carry no alt text.
    Free to run. Hyper-rank dot A-I.

Spoken words: 96

## Honesty notes

- Every number is read off the run; the three lifted cards are the run's three warnings, in the order the tool lists them.
- The keyword is typed but its two checks (both passed) are not narrated, to keep one idea per line.
- Sequence shortened from the click to the result. No gate.
- Standard close. No tool count, no signup line.

## Humanizer pass

- Draft hook "shows you the exact line to fix" overclaimed: the tool names the element, not a source line. Rewritten.
- No em dashes, no banned words.
