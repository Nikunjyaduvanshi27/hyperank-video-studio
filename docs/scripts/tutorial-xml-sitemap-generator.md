# tutorial-xml-sitemap-generator: XML Sitemap Generator

Status: prepared (READY for the render queue). Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: htmx.org (default 50 pages). Neo used: no. Master 16:9 (1920x1080). Project: `tutorials/xml-sitemap-generator/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Public run (no gate): `premium/capture/try-htmx/result-text.txt` (Pages found 50, Page limit 50, Crawl time 6.5s, the limit notice, the generated XML).
- Candidates: htmx.org only (a small, link-rich docs site; one run gave a full 50-page crawl).

| Value | Where it shows |
|---|---|
| Pages found 50 / Page limit 50 / Crawl time 6.5s | stat cards |
| "The crawl stopped at your page limit..." | amber notice |
| <url> entry for https://htmx.org/ | first entry of the generated XML |
| Copy / Download | result header |

## Intent

Goal: a site owner with no sitemap gets one from a crawl | Platform: tool page, social | Length: 30 to 40s | Success: viewer runs it on their homepage.

One reader: A founder on a hand-built site with no sitemap. Belief now: "I need a plugin or a dev for that." Belief after: "a crawl writes it for me."

## Hook candidates (different categories)

1. Question (picked): super "No sitemap *yet?*", VO "No sitemap yet? Crawl the site and write one." Names the job in the first line.
2. How-to: "Build a sitemap in seconds." Rejected: speed claim before the run shows it.
3. Contrast: "The sitemap your site should have had." Rejected: too close to the page tagline to stand alone.

## Script

Runtime 34.19s

| # | VO starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.3 | No sitemap *yet?* | No sitemap yet? Crawl the site and write one. |
| 2 name | 3.595 | XML Sitemap *Generator* | Meet the XML Sitemap Generator, from hyperank. |
| 3 type | 7.124 | Start at the *homepage.* | Enter a domain. Here, htmx.org, with the default of 50 pages. |
| 4 press | 12.872 | It follows *links.* | It follows links from the homepage, and never leaves the domain. |
| 5 result | 16.807 | 50 pages *found.* | It found 50 pages in 6.5 seconds. |
| 6 read | 20.485 | Hit the *limit.* | Pages found matches the limit, so the site may have more. |
| 7 read | 24.1 | Real *XML.* | Each page becomes a url entry in the file. |
| 8 read | 27.565 | Copy or *download.* | Copy it, or download it as sitemap.xml. |
| 9 close | close | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    No sitemap yet? Crawl the site and write one.
    Meet the X-M-L Sitemap Generator, from Hyper-rank.
    Enter a domain. Here, h-t-m-x dot org, with the default of fifty pages.
    It follows links from the homepage, and never leaves the domain.
    It found fifty pages, in six point five seconds.
    Pages found matches the limit, so the site may have more.
    Each page becomes a U-R-L entry in the file.
    Copy it, or download it as sitemap dot X-M-L.
    Free to run. Hyper-rank dot A-I.

Spoken words: 84

## Honesty notes

- "Pages found matches the limit, so the site may have more" restates the tool's own notice; the film does not claim htmx.org has more pages.
- The lastmod date inside the lifted XML is what the tool wrote on the run; the VO does not interpret it.
- Pages to crawl stays at the default 50 (the pipeline types text fields only). Sequence shortened from the click to the result.
- Standard close: super "Free to run.", printed "Full report with a free account.", then hyperank.ai. No tool count anywhere.

## Humanizer pass

- No em dashes, no banned words, no tool count, no signup line. Every number on screen and in the VO comes from the captured run.
