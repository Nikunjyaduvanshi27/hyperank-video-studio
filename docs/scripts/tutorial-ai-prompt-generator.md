# tutorial-ai-prompt-generator: AI Prompt Generator

Status: ready for render. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: payroll software for restaurants. Master 16:9 (1920x1080). Project: `tutorials/ai-prompt-generator/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Logged-in run in BrowserOS neo (Profile 1, the hyperank.ai account, verified on chrome://version before the run, tab 30): `premium/capture/neo-payroll/neo-api.json` (`data[]`: ten `{prompt, angle}` pairs) and the unlocked result DOM `neo-result-sec.html`.
- The neo tab was hidden, so the page's entrance animations never played and the capture kept `opacity:0` on the title, intro and form. Those inline styles were settled to the visible state; no text was changed.
- Gate card: the site's logged-out card ("Your results are ready / Sign up free to see the full report. / Sign up free to unlock"), copied from `chatgpt-visibility-checker/premium/capture/try-canva.com/` because both anonymous runs of this tool hit the site's rate limit ("You've run quite a few tools in a short window"). The card text is the same on every gated tool.
- One candidate run (anonymous budget spent on the rate limit). Payroll for restaurants returned ten prompts across five angles with real constraints, named products and a concrete failure, so it was kept.

| Value | Where it shows |
|---|---|
| Ten prompts | `data` has 10 items, "Generated Prompts" list 1 to 10 |
| 50 employees, multiple shifts | prompt 1, angle recommendation |
| Gusto and Paychex | prompt 2, angle comparison |
| Tips not calculated correctly | prompt 8, angle troubleshooting |
| Copy All | button beside "Generated Prompts" |

## Intent

Goal: a SaaS marketer gets the questions buyers actually type into AI, ready to test | Platform: tool page, social | Length: 35 to 45s | Success: viewer types their own category.

One reader: a product marketer at a vertical SaaS who tracks keywords, not questions. Belief now: "buyers search 'payroll software'." Belief after: "buyers ask full sentences with budgets, rivals and problems in them, and I can get ten in one press."

## Hook candidates (different categories)

1. Contrast (picked): super "Ask like a *buyer.*", VO "Buyers ask AI full questions, with their budget and team size left in." Straight from the page's own keyword vs prompt section; super and VO say different things.
2. Question: "What do buyers ask AI?" Rejected: close to the sibling visibility checkers' "Does ChatGPT name you?" opener.
3. Stake: "Keywords miss the question." Rejected: abstract, and the film never shows a keyword.

## Script

Runtime 37.95s

| # | VO starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.3 | Ask like a *buyer.* | Buyers ask AI full questions, with their budget and team size left in. |
| 2 name | 5.301 | AI Prompt *Generator* | Meet the AI Prompt Generator, from hyperank. |
| 3 type | 8.447 | Name your *category.* | Describe what you sell. Here, payroll software for restaurants. |
| 4 press | 12.792 | One *press.* | It writes ten prompts a buyer might type into an AI assistant. |
| 5 gate | 17.174 | *Ready.* | A free account opens the full list. |
| 6 read | 19.658 | Real *constraints.* | Each one carries a real detail, like fifty staff across shifts. |
| 7 read | 23.934 | Named *rivals.* | Some compare products by name, like Gusto and Paychex. |
| 8 read | 27.848 | Real *problems.* | Others start from a problem, like tips that don't add up. |
| 9 read | 31.334 | Run them *yourself.* | Copy all ten, then see which answers name you. |
| 10 close | 34.984 | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    Buyers ask A-I full questions, with their budget and team size left in.
    Meet the A-I Prompt Generator, from Hyper-rank.
    Describe what you sell. Here, payroll software for restaurants.
    It writes ten prompts a buyer might type into an A-I assistant.
    A free account opens the full list.
    Each one carries a real detail, like fifty staff across shifts.
    Some compare products by name, like Gusto and Paychex.
    Others start from a problem, like tips that don't add up.
    Copy all ten, then see which answers name you.
    Free to run. Hyper-rank dot A-I.

Spoken words: 92. Whisper check: "Gusto and Paychex" heard correctly.

## Honesty notes

- Hook engines (ChatGPT, Claude, Perplexity) are the three the tool page names as where buyers type these prompts.
- "Fifty staff across shifts" reads prompt 1 ("50 employees working in multiple shifts"); "tips that don't add up" reads prompt 8 ("not calculating tips correctly").
- The film never claims the tool checks AI answers; the last read tells the viewer to run the prompts themselves, as the page says.
- Wait compressed, so `Sequence shortened` shows from the click to the result.
- Standard close. No tool count, no signup line.

## Humanizer pass

- Draft read 6 "Every prompt is specific" was a claim about all ten; narrowed to "Each one carries a real detail" and named the one on screen.
- No em dashes, no banned words.
