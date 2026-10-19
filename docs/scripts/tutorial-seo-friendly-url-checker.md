# tutorial-seo-friendly-url-checker: SEO Friendly URL Checker

Status: prepared for the render queue. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: https://docs.oracle.com/javase/8/docs/api/java/util/HashMap.html (no keyword). Master 16:9 (1920x1080). Project: `tutorials/seo-friendly-url-checker/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Public run (no gate): `premium/capture/try-oracle/result-sec.html` and `result-text.txt`.
- Tool page copy (`premium/capture/page-text.txt`): "It scores the URL text, so it works on unpublished pages too"; "A person can tell what the page is about before clicking".
- One candidate run (anonymous runs are rate-limited). Picked because it shows all three result states: one fail, two warnings, four passes.

| Value | Where it shows |
|---|---|
| 70/100, "Your URL is Moderate." | score card |
| Fail: "URL contains uppercase characters. Use lowercase." | Lowercase Characters card |
| Warning: "URL is 7 folders deep." | Folder Depth card |
| Warning: "URL ends with a file extension." | Clean URL (No Extension) card |
| Pass: URL Length, Query Parameters, Hyphen Separators, Safe Characters | the other four cards |

## Intent

Goal: a content lead checks a URL slug before publishing | Platform: tool page, social | Length: 35 to 45s | Success: viewer pastes their own URL.

One reader: a marketer who names pages by habit. Belief now: "a URL is just an address." Belief after: "capitals, depth and extensions each cost points, and I can check before the page is live."

## Hook candidates (different categories)

1. Question (picked): super "Clean URL, or *cluttered?*", VO "Can a person tell what your page is about from the URL alone?" Comes straight from the page's own definition.
2. Stake: "Your URL is costing you clicks." Rejected: no click data in the run.
3. Contrast: "/blog/canonical-tags or /index.php?id=4471". Rejected: the example is the page's, not the run's, and it would put a second URL on screen.

## Script

Runtime 40.05s

| # | VO starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.3 | Clean URL, or *cluttered?* | Can a person tell what your page is about from the URL alone? |
| 2 name | 4.576 | SEO Friendly URL *Checker* | Meet the SEO Friendly URL Checker, from hyperank. |
| 3 type | 8.532 | Paste the full *address.* | Paste the full address. Here, a page from Oracle's Java docs. |
| 4 press | 15.677 | One *press.* | It scores the URL text itself, so it works before a page goes live. |
| 5 result | 20.785 | *Moderate.* | Seventy out of a hundred. This URL rates Moderate. |
| 6 read | 24.613 | Capitals in the *path.* | One check fails: the path has capital letters. Use lowercase. |
| 7 read | 28.889 | Two *warnings.* | Two warnings: seven folders deep, and a file extension at the end. |
| 8 read | 33.336 | The rest *passes.* | Length, parameters, hyphens and characters all pass. |
| 9 close | close | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    Can a person tell what your page is about from the U-R-L alone?
    Meet the S-E-O Friendly U-R-L Checker, from Hyper-rank.
    Paste the full address. Here, a page from Oracle's Java docs.
    It scores the U-R-L text itself, so it works before a page goes live.
    Seventy out of a hundred. This U-R-L rates Moderate.
    One check fails: the path has capital letters. Use lowercase.
    Two warnings: seven folders deep, and a file extension at the end.
    Length, parameters, hyphens and characters all pass.
    Free to run. Hyper-rank dot A-I.

Spoken words: 90

## Honesty notes

- The film never says the URL hurts rankings; the tool page calls URL words a light signal, so the VO sticks to the checklist.
- No keyword entered, so the keyword check does not appear and is not mentioned.
- Sequence shortened from the click to the result. No gate.
- Standard close. No tool count, no signup line.

## Humanizer pass

- Draft read 5 "Oracle's URL scores badly" judged the result; replaced with the UI's own grade word, Moderate.
- No em dashes, no banned words.
