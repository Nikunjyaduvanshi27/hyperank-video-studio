# tutorial-ai-query-fan-out: AI Query Fan Out Analysis

Status: rendered for review. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: prompt "best running shoes for flat feet", engines ChatGPT Search and Perplexity Pro. Master 16:9 (1920x1080). Project: `tutorials/ai-query-fan-out/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Logged-in run in BrowserOS neo (Profile 1, verified before the run): `premium/capture/neo-best-running-shoes-for-flat-feet/neo-api.json` (input `{"query":"best running shoes for flat feet","modes":["ChatGPT Search","Perplexity Pro"]}`) and `neo-result-sec.html`.
- Gate card from the logged-out run `capture/try-p1/`.
- Candidates tried: "best project management tool for a small team" (ChatGPT only), "best CRM for a small business" and "best running shoes for flat feet" (two engines each). Every ChatGPT expansion carries a stale "2023" in at least one sub-query; the running-shoes run has only one such line and the richest Perplexity reasons, so it won. No callout points at the 2023 line.

| Value | Where it shows |
|---|---|
| Four searches per engine | 4 items under each "Expansion" |
| ChatGPT row "best arch support running shoes for flat feet", Primary Source Retrieval | ChatGPT Search Expansion, row 4 |
| Perplexity rows: Academic Sourcing (clinical trials and systematic reviews), Fact Checking | Perplexity Pro Expansion, rows 1 and 4 |
| Export to CSV | Results header button |

## Intent

Goal: a content lead sees the hidden searches behind one prompt and knows to cover them | Platform: tool page, social | Length: 30 to 40s | Success: viewer runs a prompt of their own.

One reader: an SEO writer who still briefs pages from one keyword. Belief now: "one prompt, one query." Belief after: "each engine runs its own set of searches, and my page has to answer them."

## Hook candidates (different categories)

1. Question (picked): super "What does AI actually *search?*", VO "One question to AI turns into searches you never see." (the live page: "One prompt becomes several hidden searches.")
2. Number: "Four searches per engine." Rejected as a hook: the number lands better once the result is on screen.
3. Contrast: "You typed one thing. AI searched eight." Rejected: eight is only true for two engines, and it states a number before showing it.

## Script

Runtime 36.75s

| # | VO starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.3 | What does AI actually *search?* | One question to AI turns into searches you never see. |
| 2 name | 4.064 | AI Query Fan Out *Analysis* | Meet the AI Query Fan Out Analysis, from hyperank. |
| 3 type | 7.871 | Ask it like a *person.* | Type a prompt the way a person would ask it, then pick your engines. |
| 4 press | 13.016 | One *press.* | Press analyze, and it simulates each engine's searches. |
| 5 fan | 16.694 | One prompt, two *engines.* | Each engine splits your prompt into four searches. |
| 6 gate | 19.904 | *Ready.* | A free account opens the full result. |
| 7 read | 22.537 | Every search, *explained.* | Each search comes with its intent, and why it was run. |
| 8 read | 25.96 | Perplexity digs *deeper.* | The Perplexity searches go to clinical studies, then a fact check. |
| 9 read | 30.129 | Cover every *search.* | Export the list, and make sure your page answers each one. |
| 10 close | close | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    One question to A-I turns into searches you never see.
    Meet the A-I Query Fan Out Analysis, from Hyper-rank.
    Type a prompt the way a person would ask it, then pick your engines.
    Press analyze, and it simulates each engine's searches.
    Each engine splits your prompt into four searches.
    A free account opens the full result.
    Each search comes with its intent, and why it was run.
    The Perplexity searches go to clinical studies, then a fact check.
    Export the list, and make sure your page answers each one.
    Free to run. Hyper-rank dot A-I.

Spoken words: 95

## Honesty notes

- The tool simulates the searches (live page: "simulates the background searches an AI answer engine might run"). The film says "simulates" in the press beat and never presents them as real engine logs.
- Gated for logged-out users: shown once, said once.
- The fan beat shows the prompt going to the two engines that were picked; Google AI-Mode was not run, so it gets no logo.
- Sequence shortened from the click to the result (about 19s live).
- Standard close: super "Free to run.", printed "Full report with a free account.", then hyperank.ai. No tool count anywhere.

## Humanizer pass

- Draft read 8 "Perplexity reaches for clinical studies" implied the real Perplexity did it. Now "The Perplexity searches go to clinical studies, then a fact check."
- Draft payoff "Now you know what to write" overclaimed. Replaced with the page's own use: "make sure your page answers each one."
- No em dashes, no banned words, no tool count, no signup line.
