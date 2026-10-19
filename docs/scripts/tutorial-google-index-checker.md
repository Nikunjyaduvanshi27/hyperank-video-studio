# tutorial-google-index-checker: Google Index Checker

Status: READY for the render queue. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: https://www.npr.org/. Master 16:9 (1920x1080). Project: `tutorials/google-index-checker/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Gated for logged-out users. Gate card from the anonymous run `premium/capture/try-nasa/result-sec.html` (only the card is used, not that run's result). Unlocked result from the logged-in neo run (Profile 1, tab 38): `premium/capture/neo-npr/neo-api.json` and `neo-result-sec.html`.
- Candidates tried: https://developer.mozilla.org/en-US/docs/Web/CSS (anonymous, "URL is Not Indexed"), https://www.nasa.gov/ (anonymous, Indexed, but nasa.gov is already another video's input), https://www.spotify.com/ (logged in, "URL is Not Indexed"; the URL redirects to open.spotify.com), https://www.who.int/ and https://www.nationalgeographic.com/ (logged in, both "URL is Not Indexed"), https://www.npr.org/ (logged in, Indexed, 6 scanned). Picked npr.org.
- Hook and last read come from the tool page copy: "Googlebot fetching a page is one event, and Google choosing to keep it in the index is a later one", "Start with noindex ... a canonical tag pointing at another URL ... then request indexing in Search Console's URL Inspection tool."

| Value | Where it shows |
|---|---|
| Status: Indexed | `inspectStatus.coverageState` "Indexed" |
| Results scanned: 6 | `inspectStatus.resultsScanned` 6 |
| Checked: Oct 8, 3:05 AM | `inspectStatus.checkedAt`, local time (on the page, not voiced) |

## Intent

Goal: a site owner checks whether Google kept one page, not just crawled it | Platform: tool page, social | Length: 30 to 40s | Success: viewer runs their own URL.

One reader: a content marketer who published a page last week and assumes it is in Google because it returns 200. Belief now: "live means indexed." Belief after: "Google can fetch it and still leave it out, and I can check one page in a single run."

## Hook candidates (different categories)

1. Myth-bust (picked): super "Crawled is not *indexed.*", VO "Google can fetch a page and still leave it out of its index. Is yours in?"
2. Question: "Is your new page in Google?" Rejected: weaker, and it repeats the Bing film's question shape.
3. Proof: "NPR's home page, checked." Rejected: it leads with the demo brand.

## Script

Runtime 33.53s

| # | Beat starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.0 | Crawled is not *indexed.* | Google can fetch a page and still leave it out of its index. Is yours in? |
| 2 name | 4.68 | Google Index *Checker* | Meet the Google Index Checker, from hyperank. |
| 3 type | 7.69 | Paste one *page.* | Paste one page address. Here, NPR's home page. |
| 4 press | 11.67 | One *press.* | It searches Google for that exact address. |
| 5 gate | 14.37 | *Ready.* | A free account opens the result. |
| 6 read | 16.75 | *Indexed.* | NPR's home page came back in Google's results. |
| 7 read | 20.38 | Six results, *read.* | It read six organic results, and found the page among them. |
| 8 read | 24.29 | Missing? Fix, then *request.* | Not there? Clear noindex and stray canonicals, then request indexing in Search Console. |
| 9 close | 30.34 | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    Google can fetch a page and still leave it out of its index. Is yours in?
    Meet the Google Index Checker, from Hyper-rank.
    Paste one page address. Here, N-P-R's home page.
    It searches Google for that exact address.
    A free account opens the result.
    N-P-R's home page came back in Google's results.
    It read six organic results, and found the page among them.
    Not there? Clear no-index and stray canonicals, then request indexing in Search Console.
    Free to run. Hyper-rank dot A-I.

Spoken words: 87. Whisper (small.en) heard "NPR", "noindex" and "Search Console" correctly.

## Honesty notes

- The result is gated for logged-out users. The film shows the real gate card and says once "A free account opens the result."
- "Found the page among them": Indexed means the page came back among the organic results the tool read (tool page definition).
- No engine logos: the build ships only an AI Overviews mark, which is not Google Search.
- The wait is compressed, so `Sequence shortened` shows from the click to the result.
- Standard close. No tool count, no signup line.

## Humanizer pass

- Draft read 7 "It looked through the organic results it got back, and counts them" was vague. Now it names the real number: six.
- No em dashes, no banned words.
