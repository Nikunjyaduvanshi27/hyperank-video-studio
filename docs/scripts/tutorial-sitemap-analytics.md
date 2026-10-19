# tutorial-sitemap-analytics: Sitemap Analytics & Insights

Status: prepared (READY for the render queue). Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: https://www.figma.com/sitemap.xml. Neo used: no. Master 16:9 (1920x1080). Project: `tutorials/sitemap-analytics/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Public run (no gate): `premium/capture/try-figma/result-text.txt` (Analyzed 9100 URLs, 1 domain, max depth 4, folder split, depth split, 3 recommendations). "Follows a sitemap index into up to 20 of its sitemaps" is from the tool page.
- Candidates: figma.com/sitemap.xml only (a sitemap index; one run gave a rich folder and depth breakdown).

| Value | Where it shows |
|---|---|
| 9100 Total URLs, 1 Domain | Overview |
| /fonts/ 1687 URLs (18.5%), /blog/ 831 URLs (9.1%) | URL Distribution by Directory |
| Depth 2: 4909 (53.9%), Depth 3: 4051 (44.5%) | URL Depth Analysis |
| Consider adding <priority> tags... | Recommendations (3) |

## Intent

Goal: an SEO sees the shape of a site from its sitemap | Platform: tool page, social | Length: 30 to 40s | Success: viewer analyses their own sitemap.

One reader: A content strategist auditing a large site. Belief now: "a sitemap is just a list of URLs." Belief after: "it shows which folders dominate and how deep pages sit."

## Hook candidates (different categories)

1. Question (picked): super "What is your site *made of?*", VO "Your sitemap shows what your site is mostly made of." From the page's own explainer.
2. Surprise: "Figma's biggest folder isn't the blog." Rejected as an opener: it names a brand before the tool.
3. Number: "9,100 URLs, one chart." Rejected: the chart is the read beat, not the hook.

## Script

Runtime 36.28s

| # | VO starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.3 | What is your site *made of?* | Your sitemap shows what your site is mostly made of. |
| 2 name | 3.616 | Sitemap Analytics & *Insights* | Meet Sitemap Analytics and Insights, from hyperank. |
| 3 type | 7.188 | Any *sitemap.* | Paste a sitemap. Here, Figma's. |
| 4 press | 11.633 | Follows the *index.* | It follows the index into up to 20 sitemaps, then counts. |
| 5 result | 15.525 | 9,100 *URLs.* | 9,100 URLs counted, all on one domain. |
| 6 read | 19.95 | Fonts *lead.* | The fonts folder leads with 1,687 URLs, ahead of the blog. |
| 7 read | 26.125 | How *deep.* | Almost every URL sits two or three levels deep. |
| 8 read | 29.548 | What to *fix.* | Then three recommendations, starting with priority tags. |
| 9 close | close | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    Your sitemap shows what your site is mostly made of.
    Meet Sitemap Analytics and Insights, from Hyper-rank.
    Paste a sitemap. Here, Figma's.
    It follows the index into up to twenty sitemaps, then counts.
    Nine thousand one hundred U-R-Ls counted, all on one domain.
    The fonts folder leads, with one thousand six hundred eighty-seven U-R-Ls, ahead of the blog.
    Almost every U-R-L sits two or three levels deep.
    Then three recommendations, starting with priority tags.
    Free to run. Hyper-rank dot A-I.

Spoken words: 80

## Honesty notes

- 9,100 is what the tool counted after following the index into up to 20 sitemaps, so the VO says "counted", not "Figma has".
- "Almost every URL sits two or three levels deep": 53.9% plus 44.5% from the depth panel.
- Sequence shortened from the click to the result.
- Standard close: super "Free to run.", printed "Full report with a free account.", then hyperank.ai. No tool count anywhere.

## Humanizer pass

- No em dashes, no banned words, no tool count, no signup line. Every number on screen and in the VO comes from the captured run.
