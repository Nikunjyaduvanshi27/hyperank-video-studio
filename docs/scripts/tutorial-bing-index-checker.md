# tutorial-bing-index-checker: Bing Index Checker

Status: READY for the render queue. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: https://www.w3.org/. Master 16:9 (1920x1080). Project: `tutorials/bing-index-checker/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Gated for logged-out users. Gate card from the anonymous run `premium/capture/try-python/result-sec.html`. Unlocked result from the logged-in neo run (Profile 1, tab 38): `premium/capture/neo-w3c/neo-api.json` and `neo-result-sec.html`.
- Candidates tried: https://www.python.org/downloads/ (anonymous, "URL is Not Indexed", 7 scanned), https://www.python.org/ (anonymous, "URL is Not Indexed", 10 scanned), https://www.ikea.com (logged in, "URL is Not Indexed", 0 scanned), https://www.w3.org/ (logged in, Indexed, 10 scanned). Picked w3.org. The first three look like false negatives from the tool, so none of them is shown.
- Hook, the Copilot line and the IndexNow line come from the tool page copy: "a page can rank in Google while Bing has never fetched it", "Microsoft Copilot answers from Bing", "verify the site in Bing Webmaster Tools ... Bing also supports IndexNow".

| Value | Where it shows |
|---|---|
| Status: Indexed | `inspectStatus.coverageState` "Indexed" |
| Results scanned: 10 | `inspectStatus.resultsScanned` 10 (shown in the lifted card, not voiced) |
| Checked: Oct 8, 2:49 AM | `inspectStatus.checkedAt`, local time |

## Intent

Goal: a site owner who only watches Google checks one page against Bing | Platform: tool page, social | Length: 30 to 40s | Success: viewer runs their own URL.

One reader: a marketer who has Search Console open daily and has never opened Bing Webmaster Tools. Belief now: "if Google has it, Bing does too." Belief after: "Bing keeps its own index, it feeds Copilot, and I can check a page in one run."

## Hook candidates (different categories)

1. Contrast (picked): super "In Google. In *Bing?*", VO "A page can rank in Google while Bing has never fetched it."
2. Stake: "Copilot can't cite what Bing never saw." Rejected: it goes past what the page claims.
3. Question: "When did you last check Bing?" Rejected: a generic hook that could sit on any Bing tool.

## Script

Runtime 33.15s

| # | Beat starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.0 | In Google. In *Bing?* | A page can rank in Google while Bing has never fetched it. |
| 2 name | 3.8 | Bing Index *Checker* | Meet the Bing Index Checker, from hyperank. |
| 3 type | 6.71 | Drop in a *URL.* | Drop in one page address. Here, the W3C home page. |
| 4 press | 11.44 | One *search.* | It searches Bing for that exact page. |
| 5 gate | 14.03 | *Unlocked.* | A free account unlocks the result. |
| 6 read | 16.55 | *Indexed.* | The W3C home page is in Bing's results. |
| 7 read | 20.19 | Bing feeds *Copilot.* | That matters past Bing. Microsoft Copilot answers from Bing's index. |
| 8 read | 25.19 | Not there? *Submit.* | Not there? Submit it in Bing Webmaster Tools, or ping it with IndexNow. |
| 9 close | 29.96 | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    A page can rank in Google while Bing has never fetched it.
    Meet the Bing Index Checker, from Hyper-rank.
    Drop in one page address. Here, the W-3-C home page.
    It searches Bing for that exact page.
    A free account unlocks the result.
    The W-3-C home page is in Bing's results.
    That matters past Bing. Microsoft Copilot answers from Bing's index.
    Not there? Submit it in Bing Webmaster Tools, or ping it with Index Now.
    Free to run. Hyper-rank dot A-I.

Spoken words: 80. Whisper (small.en) heard "Bing", "W3C", "Copilot" and "IndexNow" correctly.

## Honesty notes

- The result is gated for logged-out users. The film shows the real gate card and says once "A free account unlocks the result."
- The Copilot claim is the tool page's own; the film does not claim ChatGPT uses Bing (the page hedges that one).
- No engine logos: the build ships none for Bing.
- The wait is compressed, so `Sequence shortened` shows from the click to the result.
- Standard close. No tool count, no signup line.

## Humanizer pass

- Draft gate line "Sign in free, and the result opens" did not match the card ("Sign up free to unlock"). Now "A free account unlocks the result."
- Draft super "Missing? *Submit it.*" put two words in the accent. Now "Not there? *Submit.*"
- No em dashes, no banned words.
