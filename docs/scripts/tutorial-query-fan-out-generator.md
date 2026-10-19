# tutorial-query-fan-out-generator: Query Fan Out Generator

Status: READY for the render queue. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: standing desk (Keyword; Country left empty). Master 16:9 (1920x1080). Project: `tutorials/query-fan-out-generator/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Gate card: anonymous run `premium/capture/try-standing-desk/result-sec.html` (the logged-out "Your results are ready" card).
- Unlocked result: logged-in run through BrowserOS neo (Profile 1, hyperank.ai), `premium/capture/neo-standing-desk/neo-result-sec.html`, `neo-result-text.txt`, `neo-api.json`. Every number on screen and in the VO comes from this run.
- A second candidate (espresso machine, United Kingdom) hit the anonymous rate limit and returned no result.
- Distinct from the sibling `ai-query-fan-out` video (a full prompt, simulated ChatGPT and Perplexity searches): this one starts from a short keyword and reads a scored table of variants.

| Value | Where it shows |
|---|---|
| Showing 18 variants; Tier 1: 4, Tier 2: 7, Tier 3: 7 | Strip above the table |
| buy standing desk online: Exact, Transactional | Table row |
| best standing desk: popularity 0.80, the highest in the table | Table row |
| Download CSV | Strip button |

## Intent

Goal: a content marketer sees the queries around one keyword, labelled and scored, before planning pages | Platform: tool page, social | Length: 30 to 40s | Success: viewer runs their own seed keyword.

One reader: an SEO writer handed one target keyword per article. Belief now: "I write for the keyword." Belief after: "one keyword has a cluster of variants with different intents, and I can see and export them."

## Hook candidates (different categories)

1. Claim (picked): super "Beyond one *keyword.*", VO "One keyword grows into a whole cluster of searches."
2. Question: "What else do people search?" Rejected: generic, fits any keyword tool.
3. Number: "18 variants from two words." Rejected for the hook: the count belongs to this run, not the viewer.

## Script

Runtime 34.57s

| # | VO starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.3 | Beyond one *keyword.* | One keyword grows into a whole cluster of searches. |
| 2 name | 3.765 | Query Fan Out *Generator* | Meet the Query Fan Out Generator, from hyperank. |
| 3 type | 7.06 | Type a *seed.* | Type one seed phrase. Here, standing desk. |
| 4 press | 10.333 | One *press.* | It expands the seed into the queries around it. |
| 5 gate | 13.265 | *Ready.* | A free account opens the full result. |
| 6 read | 15.899 | Eighteen variants, three *tiers.* | Eighteen variants, sorted into three tiers. |
| 7 read | 18.949 | Every one *labelled.* | Each one gets an intent. Buy standing desk online is transactional. |
| 8 read | 23.63 | Scored from zero to *one.* | Each has three scores. Best standing desk leads on popularity. |
| 9 read | 27.949 | Take it to a *sheet.* | Download the CSV to sort and filter the list. |
| 10 close | 31.599 | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    One keyword grows into a whole cluster of searches.
    Meet the Query Fan Out Generator, from Hyper-rank.
    Type one seed phrase. Here, standing desk.
    It expands the seed into the queries around it.
    A free account opens the full result.
    Eighteen variants, sorted into three tiers.
    Each one gets an intent. Buy standing desk online is transactional.
    Each has three scores. Best standing desk leads on popularity.
    Download the C-S-V to sort and filter the list.
    Free to run. Hyper-rank dot A-I.

Spoken words: 82

## Honesty notes

- The gate card is the real logged-out card; the report under it and after "unlock" is the logged-in run of the same input. The anonymous run's own table (18 variants, different tier split) is never shown unblurred, so only one tier split is ever readable.
- "Leads on popularity": 0.80 is the highest popularity value in the 18 rows.
- Scores are labelled as the tool's own 0 to 1 scores, not search volumes.
- Sequence shortened from the click to the result.
- Standard close: super "Free to run.", printed "Full report with a free account.", then hyperank.ai. No tool count anywhere.

## Humanizer pass

- Draft beat 7 said "a type and an intent" while only the intent was lifted; trimmed to what is on screen.
- No em dashes, no banned words, no tool count, no signup line.
