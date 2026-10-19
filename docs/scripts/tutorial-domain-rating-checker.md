# tutorial-domain-rating-checker: Domain Rating (DR) Checker

Status: prepared for the render queue. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: khanacademy.org. Master 16:9 (1920x1080). Project: `tutorials/domain-rating-checker/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Public run (no gate): `premium/capture/try-khanacademy/result-sec.html`, `result-text.txt`, `api.json`.
- Tool page copy (`premium/capture/page-text.txt`): Domain Rating is "the 0 to 100 score Ahrefs gives the strength of a site's backlink profile"; "a third-party metric built from Ahrefs' own crawl"; bands "Low Authority up to 25, Good up to 50, Strong up to 75 and Exceptional above that"; "Use DR to compare sites, not to grade one"; "screening link prospects, sizing up competitors".
- One candidate run (anonymous runs are rate-limited).

| Value | Where it shows |
|---|---|
| 90, DR SCORE | score ring |
| Exceptional Authority | band pill next to the domain |
| Domain Rating by Ahrefs | source line under the description |

Only one rating appears on screen: the tool's 90 for khanacademy.org. The VO says "out of a hundred" as the scale, never a second rating.

## Intent

Goal: a link builder sizes up a site before outreach | Platform: tool page, social | Length: 35 to 40s | Success: viewer checks a prospect's domain.

One reader: an SEO freelancer building a link prospect list. Belief now: "a big brand is a good link." Belief after: "one lookup gives me the site's DR and band, for comparing prospects."

## Hook candidates (different categories)

1. Question (picked): super "Is that link *worth it?*", VO "Before you chase a backlink, check the strength of the site behind it." Grounded in the page's "screening link prospects".
2. Myth: "DR is not a Google ranking factor." Rejected as the opener: true per the page, but it argues against the tool before showing it.
3. Number: "Ninety out of a hundred." Rejected: a number before the viewer knows whose it is.

## Script

Runtime 36.12s

| # | VO starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.3 | Is that link *worth it?* | Before you chase a backlink, check the strength of the site behind it. |
| 2 name | 4.384 | Domain Rating *Checker* | Meet the Domain Rating Checker, from hyperank. |
| 3 type | 7.529 | Just the *domain.* | Enter the domain on its own. Here, khanacademy.org. |
| 4 press | 11.805 | One *press.* | It looks up the Domain Rating Ahrefs gives the site, a score for the strength of its backlinks. |
| 5 result | 17.681 | DR *90.* | Khan Academy rates ninety, out of a hundred. |
| 6 read | 20.881 | The top *band.* | That puts it in the top band, Exceptional Authority. |
| 7 read | 24.368 | Straight from *Ahrefs.* | The number is Ahrefs' own, built from its crawl of the web. |
| 8 read | 28.004 | Compare, don't *grade.* | Use it to compare sites, like link prospects or rivals, not to grade one. |
| 9 close | close | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart; "H-refs" and "Kahn" checked with whisper):

    Before you chase a backlink, check the strength of the site behind it.
    Meet the Domain Rating Checker, from Hyper-rank.
    Enter the domain on its own. Here, Kahn Academy dot org.
    It looks up the Domain Rating H-refs gives the site, a score for the strength of its backlinks.
    Kahn Academy rates ninety, out of a hundred.
    That puts it in the top band, Exceptional Authority.
    The number is H-refs' own, built from its crawl of the web.
    Use it to compare sites, like link prospects or rivals, not to grade one.
    Free to run. Hyper-rank dot A-I.

Spoken words: 98

## Honesty notes

- The result's tip and description ("immense ranking power", "rank ... instantly") are never lifted or read; the tool page itself says DR is not a Google ranking factor.
- "Top band" rests on the page's band list (Exceptional is the highest).
- Sequence shortened from the click to the result (the live lookup took about three minutes). No gate.
- Standard close. No tool count, no signup line.

## Humanizer pass

- Draft read 5 "a very strong site" was an adjective on the result; replaced with the number and the UI's band.
- No em dashes, no banned words.
