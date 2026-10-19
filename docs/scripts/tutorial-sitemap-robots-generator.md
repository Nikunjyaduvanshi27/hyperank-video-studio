# tutorial-sitemap-robots-generator: Sitemap to Robots.txt Generator

Status: prepared (READY for the render queue). Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: https://www.allbirds.com/sitemap.xml. Neo used: no. Master 16:9 (1920x1080). Project: `tutorials/sitemap-robots-generator/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Public run (no gate): `premium/capture/try-allbirds/result-text.txt` (the generated file: "User-agent: *" and "Sitemap: https://www.allbirds.com/sitemap.xml"). "Leave User agent as * to write rules for every crawler" and "A relative path such as Sitemap: /sitemap.xml does not work for Google" are from the tool page.
- Candidates: Sitemap only (used), and the sitemap plus Allow /collections and Disallow /cart (`capture/run-allbirds`). The second needs typing into four fields, and the pipeline frames all typed fields at once while the lower two sit below the screen, so the camera left the laptop. Kept the one-field run.

| Value | Where it shows |
|---|---|
| User-agent: * | first line of the generated file |
| Sitemap: https://www.allbirds.com/sitemap.xml | last line |
| Copy | file footer |

## Intent

Goal: a site owner wires their sitemap into robots.txt correctly | Platform: tool page, social | Length: 30 to 40s | Success: viewer copies the file for their own site.

One reader: A Shopify store owner whose robots.txt never mentions the sitemap. Belief now: "submitting to Search Console is enough." Belief after: "one Sitemap line in robots.txt reaches every crawler that reads it."

## Hook candidates (different categories)

1. Instruction (picked): super "Point crawlers at your *sitemap.*", VO "One line in robots.txt tells every crawler where your sitemap lives." Sibling of the robots-txt-checker film, which opens on allowed or blocked; this one opens on the Sitemap line.
2. Question: "Does your robots.txt mention your sitemap?" Rejected: a yes ends the video.
3. Contrast: "Search Console reaches Google. robots.txt reaches everyone." Rejected: two claims in one hook, too long for the super.

## Script

Runtime 37.53s

| # | VO starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.3 | Point crawlers at your *sitemap.* | One line in robots.txt tells every crawler where your sitemap lives. |
| 2 name | 5.707 | Sitemap to Robots.txt *Generator* | Meet the Sitemap to Robots.txt Generator, from hyperank. |
| 3 type | 10.431 | Paste the *sitemap.* | Paste the sitemap address. Here, Allbirds'. |
| 4 read | 15.151 | Rules are *optional.* | Allow, disallow and crawl delay are all optional. |
| 5 press | 18.467 | Written for *you.* | One press writes the file. |
| 6 result | 20.417 | The finished *file.* | Here is the finished robots.txt. |
| 7 read | 23.617 | Every *crawler.* | User-agent star means the rules apply to every crawler. |
| 8 read | 27.616 | The full *address.* | The Sitemap line carries the full address, which Google needs. |
| 9 read | 31.508 | Copy, then *upload.* | Copy it, and save it at the root of your domain. |
| 10 close | close | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    One line in robots dot t-x-t tells every crawler where your sitemap lives.
    Meet the Sitemap to Robots dot t-x-t Generator, from Hyper-rank.
    Paste the sitemap address. Here, All-birds.
    Allow, disallow and crawl delay are all optional.
    One press writes the file.
    Here is the finished robots dot t-x-t.
    User agent star means the rules apply to every crawler.
    The Sitemap line carries the full address, which Google needs.
    Copy it, and save it at the root of your domain.
    Free to run. Hyper-rank dot A-I.

Spoken words: 86

## Honesty notes

- The demo file is generated from Allbirds' public sitemap URL; it is not Allbirds' real robots.txt, and the film never says it is.
- Before the press, a beat scrolls the form so the button is in frame and lifts the optional Disallow and Crawl delay fields.
- Sequence shortened from the click to the result.
- Standard close: super "Free to run.", printed "Full report with a free account.", then hyperank.ai. No tool count anywhere.

## Humanizer pass

- No em dashes, no banned words, no tool count, no signup line. Every number on screen and in the VO comes from the captured run.
