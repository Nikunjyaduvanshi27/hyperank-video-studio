# tutorial-sitemap-index-generator: Sitemap Index Generator

Status: prepared for the render queue. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: three paths from Gymshark's live sitemap index (`/sitemap_products_1.xml`, `/sitemap_collections_1.xml`, `/sitemap_pages_1.xml`) with base URL https://www.gymshark.com. Master 16:9 (1920x1080). Project: `tutorials/sitemap-index-generator/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Logged-in run through BrowserOS neo (Profile 1, tab 36; the anonymous run hit the rate limit): `premium/capture/neo-gymshark2/neo-api.json` (`sitemapsCount: 3`, `estimatedTotalUrls: 3589`, `kbSize: 0.5`, `skipped: []`) and `neo-result-sec.html`.
- The three paths were read from https://www.gymshark.com/sitemap.xml before the run.
- Tool page copy (`premium/capture/page-text.txt`): "Combine several sitemaps into the one index file search engines expect"; base URL "gets prepended to each one"; "fetches each sitemap to count the URLs inside it"; "save the text as a file ... at your site root, and submit that one URL".

| Value | Where it shows |
|---|---|
| "Created index with 3 sitemaps containing ~3589 total URLs" | green banner |
| 3 Sitemaps, 3589 Est. Total URLs, 0.5 KB Index Size | summary cards |
| `<loc>https://www.gymshark.com/sitemap_products_1.xml</loc>` and the other two | sitemap-index.xml box |

## Intent

Goal: a developer or SEO combines split sitemaps into one submittable file | Platform: tool page, social | Length: 40 to 45s | Success: viewer pastes their own sitemap list.

One reader: someone running a store whose platform splits sitemaps by type. Belief now: "I submit each sitemap separately." Belief after: "paste the paths once, get one index, submit one URL."

## Hook candidates (different categories)

1. Question (picked): super "Too many *sitemaps?*", VO "Split your sitemaps, and one index file can list them all."
2. Limit: "Fifty thousand URLs per sitemap." Rejected: a page fact unrelated to this run's size, and a second big number on screen.
3. Instruction: "Submit one URL, not three." Rejected: gives away the payoff before the demo.

## Script

Runtime 44.75s

| # | VO starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.3 | Too many *sitemaps?* | Split your sitemaps, and one index file can list them all. |
| 2 name | 4.107 | Sitemap Index *Generator* | Meet the Sitemap Index Generator, from hyperank. |
| 3 type | 7.423 | One per *line.* | Paste one sitemap per line. Here, Gymshark's products, collections and pages. Paths work if you add the base URL. |
| 4 press | 17.833 | One *press.* | It puts that base URL in front of each path, then counts the URLs inside. |
| 5 result | 23.453 | Index *ready.* | Done. One index for all three sitemaps. |
| 6 read | 26.653 | What it *covers.* | Three sitemaps, about 3,589 URLs, in a half-kilobyte file. |
| 7 read | 33.339 | Full *addresses.* | Each path comes back as a full Gymshark address. |
| 8 read | 36.719 | Copy, save, *submit.* | Copy the XML, save it at your site root, and submit that one URL. |
| 9 close | close | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    Split your sitemaps, and one index file can list them all.
    Meet the Sitemap Index Generator, from Hyper-rank.
    Paste one sitemap per line. Here, Gymshark's products, collections and pages. Paths work if you add the base U-R-L.
    It puts that base U-R-L in front of each path, then counts the U-R-Ls inside.
    Done. One index for all three sitemaps.
    Three sitemaps, about three thousand, five hundred and eighty nine U-R-Ls, in a half kilobyte file.
    Each path comes back as a full Gymshark address.
    Copy the X-M-L, save it at your site root, and submit that one U-R-L.
    Free to run. Hyper-rank dot A-I.

Spoken words: 103

## Honesty notes

- The URL total is the tool's estimate ("~3589", "Est. Total URLs"), so the VO says "about".
- The `<lastmod>` values in the generated XML are the generation time, not Gymshark's own dates; the film never mentions them.
- Logged-in neo run used only because the anonymous run was rate-limited; there is no gate on this tool, so none is shown.
- Sequence shortened from the click to the result. Standard close. No tool count, no signup line.

## Humanizer pass

- Draft hook "Split sitemaps need one index file" overstated the rule; the page says an index is needed past the limits and helps below them. Softened to "can list them all".
- No em dashes, no banned words.
