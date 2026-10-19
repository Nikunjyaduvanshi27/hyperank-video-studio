# tutorial-xml-sitemap-validator: XML Sitemap Validator

Status: prepared (READY for the render queue). Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: https://basecamp.com/sitemap.xml. Neo used: no. Master 16:9 (1920x1080). Project: `tutorials/xml-sitemap-validator/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Public run (no gate): `premium/capture/try-basecamp/result-text.txt` (Valid, Score 80/100, 193 URLs, 0 critical errors, metadata coverage, one recommendation). Score rule (priority and changefreq cost 10 points each) and "Google ignores the <priority> and <changefreq> values" are from the tool page text.
- Candidates: https://www.lego.com/sitemap.xml (a sitemap index; Invalid, 40/100 with 0 URLs counted, which would confuse more than teach), https://basecamp.com/sitemap.xml (urlset, valid, 80/100, 193 URLs). Picked Basecamp.

| Value | Where it shows |
|---|---|
| Valid, Score 80/100, 193 URLs | indigo result banner |
| Score: 80/100, URLs: 193, Critical Errors: 0 | summary row |
| Last Modified yes, Priority no, Change Frequency no | Metadata Coverage |
| Add 'priority' and 'changefreq' elements... | Recommendations |

## Intent

Goal: an SEO checks a sitemap is usable and learns where the score comes from | Platform: tool page, social | Length: 30 to 40s | Success: viewer validates their own sitemap.

One reader: An in-house SEO who submits sitemaps but never checks them. Belief now: "if it loads, it is fine." Belief after: "a score and an error count tell me, and I know which deductions matter."

## Hook candidates (different categories)

1. Question (picked): super "Will it *pass?*", VO "Errors in a sitemap decide whether search engines can use it." Built on the page's line that critical errors decide whether search engines can use the file.
2. Stake: "One bad ampersand breaks a sitemap." Rejected: the run has no XML error to show.
3. Number: "80 out of 100." Rejected: a score before the viewer knows the tool means nothing.

## Script

Runtime 35.79s

| # | VO starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.3 | Will it *pass?* | Errors in a sitemap decide whether search engines can use it. |
| 2 name | 4.341 | XML Sitemap *Validator* | Meet the XML Sitemap Validator, from hyperank. |
| 3 type | 7.892 | Paste the *file.* | Paste the sitemap file itself. Here, the one from Basecamp. |
| 4 press | 12.237 | Structure, domains, *tags.* | It checks the structure, the domains and the tags, then scores the file. |
| 5 result | 16.833 | *Valid.* | Basecamp's sitemap is valid, with a score of 80 out of 100. |
| 6 read | 21.088 | Zero critical *errors.* | 193 URLs, and zero critical errors. |
| 7 read | 25.406 | Where the points *went.* | The missing points: no priority or changefreq tags. |
| 8 read | 29.17 | Google ignores *both.* | Worth knowing: Google ignores both of those tags. |
| 9 close | close | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    Errors in a sitemap decide whether search engines can use it.
    Meet the X-M-L Sitemap Validator, from Hyper-rank.
    Paste the sitemap file itself. Here, the one from Basecamp.
    It checks the structure, the domains and the tags, then scores the file.
    Basecamp's sitemap is valid, with a score of eighty out of a hundred.
    One hundred ninety-three U-R-Ls, and zero critical errors.
    The missing points: no priority, or change-freak tags.
    Worth knowing: Google ignores both of those tags.
    Free to run. Hyper-rank dot A-I.

Spoken words: 84

## Honesty notes

- The closing read ("Google ignores both of those tags") comes from the tool page's own FAQ, so the 20 lost points are put in context instead of oversold.
- Score rule from the page: minus 10 each for no priority and no changefreq, which matches 80.
- Sequence shortened from the click to the result.
- Standard close: super "Free to run.", printed "Full report with a free account.", then hyperank.ai. No tool count anywhere.

## Humanizer pass

- No em dashes, no banned words, no tool count, no signup line. Every number on screen and in the VO comes from the captured run.
