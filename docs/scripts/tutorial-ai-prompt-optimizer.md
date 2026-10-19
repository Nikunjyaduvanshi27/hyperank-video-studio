# tutorial-ai-prompt-optimizer: AI Prompt Optimizer

Status: prepared for the render queue. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: "write a cold email to a gym owner about our booking app, keep it short", framework APE (the page default). Master 16:9 (1920x1080). Project: `tutorials/ai-prompt-optimizer/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Logged-in run through BrowserOS neo (Profile 1): `premium/capture/neo-gym/neo-api.json` (POST `/api/tools/ai-prompt-optimizer`, input `{"originalPrompt": "...", "framework": "APE"}`), DOM `neo-result-sec.html`.
- Gate card: anonymous run `premium/capture/try-gym2/result-sec.html`.
- One candidate. APE is the page default; the pipeline cannot change a select, so the video shows the framework the run used.

| Value | Where it shows |
|---|---|
| Action: Write a cold email | Optimized Result |
| Purpose: To introduce our booking app to a gym owner | Optimized Result |
| Expectation: The email should be concise and to the point | Optimized Result |
| Open in ChatGPT, Open in Claude buttons | Under the result |

## Intent

Goal: a founder sees their one-line prompt come back with named parts | Platform: tool page, social | Length: 35 to 40s | Success: viewer pastes a prompt they reuse.

One reader: a small SaaS founder who writes outreach with a one-line ChatGPT prompt. Belief now: "a prompt is one sentence." Belief after: "the same request reads better split into parts I can edit."

## Hook candidates (different categories)

1. Transformation (picked): super "Your prompt, *rebuilt.*", VO "Take a prompt you already use, and rebuild it on a framework."
2. Contrast: "Before, and after." Rejected as the hook, kept as the two read beats.
3. Question: "Which framework fits?" Rejected: the video runs one framework, it cannot answer that.

## Script

Runtime 36.86s

| # | Beat starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.0 | Your prompt, *rebuilt.* | Take a prompt you already use, and rebuild it on a framework. |
| 2 name | 3.84 | AI Prompt *Optimizer* | Meet the AI Prompt Optimizer, from hyperank. |
| 3 type | 7.22 | Paste it as *is.* | Paste it the way you use it today. Here, a one-line cold email ask. |
| 4 press | 14.9 | One *press.* | It rewrites the prompt onto the framework you pick. Here, APE. |
| 5 gate | 19.32 | *Ready.* | A free account opens the full rewrite. |
| 6 read | 22.0 | Before: one *line.* | Before, it was one line asking for a short cold email. |
| 7 read | 25.83 | After: three *parts.* | After, it names the action, the purpose and the expectation. |
| 8 read | 29.78 | Run it *anywhere.* | Copy it, or open it straight in ChatGPT or Claude. |
| 9 close | 33.68 | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    Take a prompt you already use, and rebuild it on a framework.
    Meet the A-I Prompt Optimizer, from Hyper-rank.
    Paste it the way you use it today. Here, a one-line cold email ask.
    It rewrites the prompt onto the framework you pick. Here, A-P-E.
    A free account opens the full rewrite.
    Before, it was one line asking for a short cold email.
    After, it names the action, the purpose and the expectation.
    Copy it, or open it straight in Chat G-P-T or Claude.
    Free to run. Hyper-rank dot A-I.

Spoken words: 87

## Honesty notes

- The video does not claim the rewrite performs better; it shows the structure change only.
- The APE rewrite in this run is thin ("concise and to the point" restates "keep it short"). The script describes it plainly and makes no quality claim.
- Gate shown once, printed again on the end card. Sequence shortened from the click to the result.
- No tool count, no signup line, no em dashes.
