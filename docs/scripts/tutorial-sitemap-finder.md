# tutorial-sitemap-finder: Sitemap Checker

Status: prepared (READY for the render queue). Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: apple.com. Neo used: no. Master 16:9 (1920x1080). Project: `tutorials/sitemap-finder/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Public run (no gate): `premium/capture/try-apple/result-text.txt` ("5 sitemap(s) Found", each with type, size and HTTP status). On-screen tool name is "Sitemap Checker" (slug sitemap-finder).
- Candidates: Robots.txt files checked by hand first (apple.com declares five sitemaps, figma.com three, bbc.com dozens). Ran apple.com once: five sitemaps, a mix of indexes and plain sitemaps, all HTTP 200.

| Value | Where it shows |
|---|---|
| 5 sitemap(s) Found | result heading |
| autopush/sitemap/sitemap-index.xml: Index of 293 sitemaps, 25.9KB, HTTP 200 | second entry |
| newsroom/sitemap.xml: 2588 URLs, 822.3KB, HTTP 200 | third entry |
| HTTP 200 on all five | every entry |

## Intent

Goal: a site owner learns where their sitemaps live and that they load | Platform: tool page, social | Length: 30 to 40s | Success: viewer runs their own domain.

One reader: A marketer handed a big site who does not know how many sitemaps it has. Belief now: "there is one sitemap at /sitemap.xml." Belief after: "robots.txt can declare several, and I can confirm each one loads."

## Hook candidates (different categories)

1. Question (picked): super "Where is your *sitemap?*", VO "A sitemap only helps if crawlers can find it."
2. Number: "Apple has five sitemaps." Rejected as an opener: it is the payoff, kept for the result beat.
3. How-to: "Find any site's sitemap." Rejected: flat, names no stake.

## Script

Runtime 34.78s

| # | VO starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.3 | Where is your *sitemap?* | A sitemap only helps if crawlers can find it. |
| 2 name | 3.467 | Sitemap *Checker* | Meet the Sitemap Checker, from hyperank. |
| 3 type | 6.207 | Just the *domain.* | Enter a domain. Here, apple.com. |
| 4 press | 9.224 | Robots.txt *first.* | It reads robots.txt for Sitemap lines, then tries the common paths. |
| 5 result | 14.588 | Five *found.* | Apple declares five sitemaps. |
| 6 read | 17.788 | Maps of *maps.* | Some are indexes. This one lists 293 more sitemaps. |
| 7 read | 22.299 | Every URL *counted.* | The newsroom sitemap holds 2,588 URLs. |
| 8 read | 27.407 | All five *load.* | Each one answers HTTP 200, so crawlers can read it. |
| 9 close | close | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    A sitemap only helps if crawlers can find it.
    Meet the Sitemap Checker, from Hyper-rank.
    Enter a domain. Here, Apple dot com.
    It reads robots dot t-x-t for sitemap lines, then tries the common paths.
    Apple declares five sitemaps.
    Some are indexes. This one lists two hundred ninety-three more sitemaps.
    The newsroom sitemap holds two thousand, five hundred eighty-eight U-R-Ls.
    Each one answers H-T-T-P two hundred, so crawlers can read it.
    Free to run. Hyper-rank dot A-I.

Spoken words: 77

## Honesty notes

- "Apple declares five sitemaps": the five come from apple.com's robots.txt Sitemap: lines (checked by hand), which is the first place the tool looks.
- "Each one answers HTTP 200, so crawlers can read it" covers fetchability only, which is what the status shows.
- Sequence shortened from the click to the result.
- Standard close: super "Free to run.", printed "Full report with a free account.", then hyperank.ai. No tool count anywhere.

## Humanizer pass

- No em dashes, no banned words, no tool count, no signup line. Every number on screen and in the VO comes from the captured run.
