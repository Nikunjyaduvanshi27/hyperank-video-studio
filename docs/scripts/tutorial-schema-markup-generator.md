# tutorial-schema-markup-generator: Schema Markup Generator (JSON-LD)

Status: READY for the render queue. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: Article (default type), values `headline: What is llms.txt?` / `author: Hyperank` / `datePublished: 2026-10-08`. Master 16:9 (1920x1080). Project: `tutorials/schema-markup-generator/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Public run (no gate): `premium/capture/try-article/result-sec.html` (the generated JSON-LD with author nested as a Person, the Usage note, the Required properties list with image missing).
- Candidates tried: this Article run; a second run (Tim Berners-Lee's 1989 web proposal) hit the site's rate limit both anonymously and through neo, so the first run stands.

| Value | Where it shows |
|---|---|
| Generated JSON-LD | dark code box under Generated JSON-LD |
| author nested as Person | "author": { "@type": "Person", "name": "Hyperank" } |
| Script tag usage | blue Usage box |
| image missing | Required properties for Article: image, missing, add a line for it |

## Intent

Goal: a marketer writes schema without hand-typing JSON | Platform: tool page, social | Length: 30 to 40s | Success: viewer generates markup for their own page.

One reader: a marketer who knows schema matters and fears breaking JSON syntax. Belief now: "I need a developer for JSON-LD." Belief after: "I write key, colon, value, and it builds the markup and tells me what is missing."

## Hook candidates (different categories)

1. Contrast (picked): super "Plain lines *in.*", VO "Search engines read JSON-LD. You only write plain lines."
2. Stake: "Rich results need schema." Rejected: the film shows no rich result, and the page itself says markup is no guarantee.
3. Question: "What does your page say it is?" Rejected: too abstract.

## Script

Runtime 33.74s

| # | VO starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.3 | Plain lines *in.* | Search engines read JSON-LD. You only write plain lines. |
| 2 name | 4.704 | Schema Markup *Generator* | Meet the Schema Markup Generator, from hyperank. |
| 3 type | 7.999 | One property per *line.* | Keep Article as the type. Then write key, colon, value, one per line. |
| 4 press | 15.674 | One *press.* | It turns those lines into JSON-LD. |
| 5 result | 18.734 | Ready to *paste.* | Here is the markup. Copy it into a script tag on your page. |
| 6 read | 22.754 | Nested for *you.* | The author line became its own Person object. |
| 7 read | 26.07 | One property *missing.* | The checklist flags image as missing. Add that line and generate again. |
| 8 close | close | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    Search engines read Jay-son L-D. You only write plain lines.
    Meet the Schema Markup Generator, from Hyper-rank.
    Keep Article as the type. Then write key, colon, value, one per line.
    It turns those lines into Jay-son L-D.
    Here is the markup. Copy it into a script tag on your page.
    The author line became its own Person object.
    The checklist flags image as missing. Add that line and generate again.
    Free to run. Hyper-rank dot A-I.

Spoken words: 76

## Honesty notes

- The schema type select stays on Article, its default; the film never shows another type being picked.
- The author value "Hyperank" became a Person because that is how the generator nests author; the film reports it as output.
- No claim that the markup is valid or earns rich results: the film reads the code and the checklist only.
- No gate. Sequence shortened from the click to the result.
- Standard close: super "Free to run.", printed "Full report with a free account.", then hyperank.ai. No tool count anywhere.

## Humanizer pass

- No em dashes in VO, supers or this file's own prose; no banned words, no tool count, no signup line. Dashes inside the live UI (for example the feed count line) stay as the page renders them.
- Pronunciation checked with whisper (small.en): brand names and acronyms transcribe as written.
