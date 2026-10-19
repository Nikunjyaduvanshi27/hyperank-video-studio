# tutorial-yandex-index-checker: Yandex Index Checker

Status: READY for the render queue. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: https://www.wikipedia.org/. Master 16:9 (1920x1080). Project: `tutorials/yandex-index-checker/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Gated for logged-out users. Gate card from the anonymous run `premium/capture/try-imdb/result-sec.html`. Unlocked result from the logged-in neo run (Profile 1, tab 38): `premium/capture/neo-wikipedia/neo-api.json` and `neo-result-sec.html`.
- Candidates tried: https://www.imdb.com/chart/top/ (anonymous, "URL is Not Indexed", 14 scanned), https://www.wikipedia.org/ (anonymous run hit the rate limit, then logged in: Indexed). Picked wikipedia.org, the only real "Indexed" result.
- Hook and the last read come from the tool page copy: "Yandex runs its own crawler and its own index, and shares nothing with Google or Bing", and "Only if you have an audience there ... Russian-speaking markets".

| Value | Where it shows |
|---|---|
| Status: Indexed | `inspectStatus.coverageState` "Indexed" |
| Results scanned: 10 | `inspectStatus.resultsScanned` 10 |
| Checked: Oct 8, 2:28 AM | `inspectStatus.checkedAt`, shown in local time |

## Intent

Goal: a site owner with Russian-speaking visitors checks one page against Yandex, separately from Google | Platform: tool page, social | Length: 30 to 40s | Success: viewer runs their own URL.

One reader: an SEO lead who assumes "indexed in Google" covers every engine. Belief now: "if Google has it, everyone has it." Belief after: "Yandex keeps a separate index, and I can check any page against it."

## Hook candidates (different categories)

1. Contrast (picked): super "A separate *index.*", VO "Yandex runs its own crawler and its own index, apart from Google and Bing."
2. Question: "Do you even need Yandex?" Rejected: it opens on a reason to leave.
3. Proof: "Wikipedia, checked in Yandex." Rejected: it leads with the demo brand.

## Script

Runtime 33.93s

| # | Beat starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.0 | A separate *index.* | Yandex runs its own crawler and its own index, apart from Google and Bing. |
| 2 name | 5.23 | Yandex Index *Checker* | Meet the Yandex Index Checker, from hyperank. |
| 3 type | 8.35 | Any public *page.* | Enter any public page, even one you don't own. Here, wikipedia.org. |
| 4 press | 13.74 | One *check.* | It searches Yandex for that exact address. |
| 5 gate | 16.48 | *Ready.* | A free account opens the result. |
| 6 read | 18.86 | *Indexed.* | Wikipedia's front page came back in Yandex's results. |
| 7 read | 22.83 | How many, and *when.* | It scanned ten results to find it, and logs when it checked. |
| 8 read | 26.6 | Only if they search *there.* | Worth checking when your audience searches in Russian-speaking markets. |
| 9 close | 30.75 | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    Yandex runs its own crawler, and its own index, apart from Google and Bing.
    Meet the Yandex Index Checker, from Hyper-rank.
    Enter any public page, even one you don't own. Here, Wikipedia dot org.
    It searches Yandex for that exact address.
    A free account opens the result.
    Wikipedia's front page came back in Yandex's results.
    It scanned ten results to find it, and logs when it checked.
    Worth checking when your audience searches in Russian speaking markets.
    Free to run. Hyper-rank dot A-I.

Spoken words: 82. Whisper (small.en) heard "Yandex" correctly in every line it appears.

## Honesty notes

- The result is gated for logged-out users. The film shows the real gate card and says once "A free account opens the result."
- "Even one you don't own" is the tool page's own claim ("including pages on sites you do not own").
- No engine logos: the build ships none for Yandex.
- The wait is compressed, so `Sequence shortened` shows from the click to the result.
- Standard close. No tool count, no signup line.

## Humanizer pass

- Draft read 7 "It also shows how many results it read" was vague. Now it names the real number: ten.
- No em dashes, no banned words.
