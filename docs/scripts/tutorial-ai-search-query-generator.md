# tutorial-ai-search-query-generator: AI Search Query Generator

Status: READY for the render queue. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: password manager. Master 16:9 (1920x1080). Project: `tutorials/ai-search-query-generator/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Gate card: anonymous run `premium/capture/try-password-manager/result-sec.html` (the logged-out "Your results are ready" card).
- Unlocked result: logged-in run through BrowserOS neo (Profile 1, hyperank.ai), `premium/capture/neo-password-manager/neo-result-sec.html`, `neo-result-text.txt`, `neo-api.json`. Every query and label on screen comes from this run.
- A second candidate (project management software) hit the anonymous rate limit and returned no result.
- "Enter the category, not your brand" follows the field's own hint ("The subject people search for, not your brand name").

| Value | Where it shows |
|---|---|
| password manager free trial / TRY BEFORE BUYING | Query 5 |
| 1password vs bitwarden comparison / COMPARE FEATURES | Query 4 |
| buy lastpass subscription / PURCHASE SOFTWARE | Query 3 |
| purchase nordpass now / IMMEDIATE PURCHASE | Query 10 |
| Ten queries, Copy All | Generated Queries header |

## Intent

Goal: a marketer gets the buying-stage searches for their category, ready to track | Platform: tool page, social | Length: 30 to 40s | Success: viewer runs their own category.

One reader: a growth marketer at a software company who tracks only informational keywords. Belief now: "we know what people search for." Belief after: "the searches closest to a purchase are short, name competitors, and I can list them in one run."

## Hook candidates (different categories)

1. Question (picked): super "What do buyers *type?*", VO "People about to buy type short, pointed searches."
2. Contrast: "Learning searches and buying searches look different." Rejected: abstract until the list is on screen.
3. Named example: "buy lastpass subscription." Rejected for the hook: it belongs to this run, not the viewer's category.

## Script

Runtime 33.26s

| # | VO starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.3 | What do buyers *type?* | People about to buy type short, pointed searches. |
| 2 name | 3.595 | AI Search Query *Generator* | Meet the AI Search Query Generator, from hyperank. |
| 3 type | 7.081 | Name the *category.* | Enter the category, not your brand. Here, password manager. |
| 4 press | 11.187 | One *press.* | It writes ten searches with buying intent. |
| 5 gate | 13.927 | *Ready.* | A free account opens the full result. |
| 6 read | 16.56 | Every intent *named.* | Each search comes with the intent behind it. |
| 7 read | 19.61 | Brands, head to *head.* | Some compare named brands, like 1Password and Bitwarden. |
| 8 read | 23.587 | Ready to *buy.* | Others sit one step from a purchase. |
| 9 read | 26.637 | Track all *ten.* | Copy all ten into your rank tracker. |
| 10 close | 30.287 | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    People about to buy type short, pointed searches.
    Meet the A-I Search Query Generator, from Hyper-rank.
    Enter the category, not your brand. Here, password manager.
    It writes ten searches with buying intent.
    A free account opens the full result.
    Each search comes with the intent behind it.
    Some compare named brands, like one-Password and Bit-warden.
    Others sit one step from a purchase.
    Copy all ten into your rank tracker.
    Free to run. Hyper-rank dot A-I.

Spoken words: 74 (whisper check: "1Password and Bitwarden" heard correctly).

## Honesty notes

- Brand names in the result (LastPass, 1Password, Bitwarden, NordPass, Dashlane) are the model's own output for the category, shown as generated, not endorsements.
- The first query reads "best password manager 2023"; it is the tool's output and is not lifted or narrated.
- The gate card is the real logged-out card; the anonymous run's own list is never shown unblurred, so one list is in play.
- Sequence shortened from the click to the result.
- Standard close: super "Free to run.", printed "Full report with a free account.", then hyperank.ai. No tool count anywhere.

## Humanizer pass

- No em dashes, no banned words, no tool count, no signup line.
