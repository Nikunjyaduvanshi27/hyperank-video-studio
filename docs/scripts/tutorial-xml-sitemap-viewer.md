# tutorial-xml-sitemap-viewer: XML Sitemap Viewer

Status: prepared (READY for the render queue). Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: raycast.com. Neo used: yes (anonymous runs hit the rate limit; logged-in run through BrowserOS neo, Profile 1, tab 37). Master 16:9 (1920x1080). Project: `tutorials/xml-sitemap-viewer/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Logged-in run: `premium/capture/neo-raycast/neo-result-text.txt` ("Pages Found: 98", source file https://www.raycast.com/sitemap.xml, the page list).
- Candidates: duolingo.com (103 pages, clean list, but opengraph-viewer already used duolingo.com), ted.com (anonymous run rate-limited; the neo run for ted.com did not save a result), raycast.com (98 pages, short readable URLs). Picked Raycast.

| Value | Where it shows |
|---|---|
| Pages Found: 98 | count under the title |
| https://www.raycast.com/sitemap.xml | the file the tool read, under the count |
| /pricing, /blog | first entries of the list |
| /blog/the-new-raycast and the community stories | further down the list |

## Intent

Goal: a marketer sees what a sitemap actually lists without reading XML | Platform: tool page, social | Length: 30 to 40s | Success: viewer pastes their own domain.

One reader: A content lead who has never opened their own sitemap. Belief now: "the sitemap is a dev file I can't read." Belief after: "I can read it as a list in one step."

## Hook candidates (different categories)

1. Contrast (picked): super "Read it as a *list.*", VO "A sitemap is XML. This reads it as a plain list of pages." Straight from the tool's own tagline.
2. Question: "Do you know what your sitemap lists?" Rejected: the finder video already opens on a where/what question.
3. Stake: "Old URLs hide in sitemaps." Rejected: the run shows no broken or stale URL, so the film could not pay it off.

## Script

Runtime 32.74s

| # | VO starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.3 | Read it as a *list.* | A sitemap is XML. This reads it as a plain list of pages. |
| 2 name | 4.875 | XML Sitemap *Viewer* | Meet the XML Sitemap Viewer, from hyperank. |
| 3 type | 8.191 | A bare domain *works.* | Give it a bare domain. Here, raycast.com. |
| 4 press | 11.549 | It finds the *file.* | It finds the sitemap through robots.txt, then opens it. |
| 5 result | 15.932 | 98 *pages.* | The Raycast sitemap lists 98 pages. |
| 6 read | 19.132 | The file it *read.* | Under the count, the exact file it read. |
| 7 read | 22.182 | Pages, not *tags.* | Then the pages themselves, like pricing and the blog. |
| 8 read | 25.733 | Open any *page.* | Each one is a link, so you can open it and check that it still loads. |
| 9 close | close | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    A sitemap is X-M-L. This reads it as a plain list of pages.
    Meet the X-M-L Sitemap Viewer, from Hyper-rank.
    Give it a bare domain. Here, Raycast dot com.
    It finds the sitemap through robots dot t-x-t, then opens it.
    The Raycast sitemap lists ninety-eight pages.
    Under the count, the exact file it read.
    Then the pages themselves, like pricing and the blog.
    Each one is a link, so you can open it and check that it still loads.
    Free to run. Hyper-rank dot A-I.

Spoken words: 85

## Honesty notes

- The tool found the sitemap through raycast.com's robots.txt Sitemap: line (checked by hand: robots.txt declares https://www.raycast.com/sitemap.xml). The VO says only that.
- "Check it still loads" is the page's own advice; the film does not claim any link was checked.
- Logged-in result, shown without any account UI. Sequence shortened from the click to the result.
- Standard close: super "Free to run.", printed "Full report with a free account.", then hyperank.ai. No tool count anywhere.

## Humanizer pass

- No em dashes, no banned words, no tool count, no signup line. Every number on screen and in the VO comes from the captured run.
