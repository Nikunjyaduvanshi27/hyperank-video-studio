# tutorial-noindex-checker: Noindex Checker

Status: prepared for the render queue. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: https://yoast.com/sitemap_index.xml. Master 16:9 (1920x1080). Project: `tutorials/noindex-checker/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Public run (no gate): `premium/capture/try-yoast-sitemap/api.json` (POST `/api/tools/noindex-checker`: `indexable: false`, `htmlNoindex: false`, `headerNoindex: true`) and `result-sec.html`. Run took 4.6s ("a few seconds later").
- Independent check before the run: `curl -sI https://yoast.com/sitemap_index.xml` returns `X-Robots-Tag: noindex, follow`, and the XML carries no robots meta tag. The result is correct on both lines.
- Rejected: wordpress.org/wp-login.php (`try-wordpress-login`). Its verdict is right, but the tool reports "meta tag: No" while the page carries a second `<meta name="robots" content="noindex,follow">` after a `max-image-preview` one. Featuring it would show the meta line wrong. Worth a bug ticket: the meta check appears to read only the first robots meta tag.
- "Robots meta tag and X-Robots-Tag header", "view-source does not show the header", "told to leave it out of results": the tool page's own copy.

| Value | Where it shows |
|---|---|
| Page is Not Indexable | Verdict line |
| Noindex in HTML meta tag: No | Signal row 1 |
| Noindex in HTTP headers: Yes | Signal row 2 |
| A noindex directive was found in the HTTP headers. | Verdict sentence |

## Intent

Goal: an SEO lead learns a noindex can sit in a header they never see | Platform: tool page, social | Length: 35 to 40s | Success: viewer checks a page that will not index.

One reader: a developer who shipped a site and sees a page missing from Google. Belief now: "view-source shows no noindex, so it is not that." Belief after: "the header can carry it; one check reads both."

## Hook candidates (different categories)

1. Reveal (picked): super "Hidden in the *header.*", VO "A noindex keeps a page out of search. It can live where view-source never shows it."
2. Question: "Why is this page not in Google?" Rejected: noindex is one of several causes; overpromises.
3. Contrast: "Clean HTML. Still not indexed." Rejected: a sitemap has no HTML, so it would mislead about this demo.

## Script

Runtime 37.43s

| # | Beat start (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.0 | Hidden in the *header.* | A noindex keeps a page out of search. It can live where view-source never shows it. |
| 2 name | 5.1 | Noindex *Checker* | Meet the Noindex Checker, from hyperank. |
| 3 type | 7.93 | Paste the exact *URL.* | Paste the exact address. Here, Yoast's sitemap index. |
| 4 press | 12.54 | One *press.* | It fetches the URL and checks both places: the robots meta tag, and the X-Robots-Tag header. |
| 5 result | 19.31 | Both *checked.* | A few seconds later, the verdict. |
| 6 read | 21.67 | Not *indexable.* | Not indexable. Search engines are told to leave it out of results. |
| 7 read | 26.11 | Which *signal?* | Not the meta tag. The noindex sits in the HTTP header. |
| 8 read | 30.43 | Check the *header.* | View-source does not show that header. This check reads it for you. |
| 9 close | 34.24 | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    A no-index keeps a page out of search. It can live where view-source never shows it.
    Meet the No-index Checker, from Hyper-rank.
    Paste the exact address. Here, Yoast's site map index.
    It fetches the U-R-L, and checks both places: the robots meta tag, and the X-Robots-Tag header.
    A few seconds later, the verdict.
    Not indexable. Search engines are told to leave it out of results.
    Not the meta tag. The no-index sits in the H-T-T-P header.
    View-source does not show that header. This check reads it for you.
    Free to run. Hyper-rank dot A-I.

Whisper check: vo-02, 03, 04, 07 transcribe as written (Yoast, X-Robots-Tag, HTTP).

## Honesty notes

- The VO never calls the noindex a mistake: on a sitemap it is a normal choice, so the film only says where it was found.
- No gate. Sequence shortened from the click to the result.
- Standard close. No tool count, no signup line, no em dashes.
