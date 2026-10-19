# tutorial-best-ai-prompt-generator: Best AI Prompt Generator

Status: ready for render. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: Goal "Write a returns policy page for an online furniture store", Context "Friendly tone, under 300 words, no legal advice", Framework APE (the page default). Master 16:9 (1920x1080). Project: `tutorials/best-ai-prompt-generator/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Logged-in run in BrowserOS neo (Profile 1, the hyperank.ai account, verified on chrome://version before the run, tab 30): `premium/capture/neo-returns/neo-api.json` and the unlocked result DOM `neo-result-sec.html`. The hidden neo tab never played the page's entrance animations, so the `opacity:0` inline styles on the title and form were settled to the visible state; no text changed.
- Gate card: the site's generic logged-out card, copied from `chatgpt-visibility-checker/premium/capture/try-canva.com/` because the anonymous run hit the rate limit. Same text on every gated tool.
- `zoom` 0.85 in tool.json: the form is tall (framework help, goal, context), and at the default zoom the context field and the button sat below the screen, so the typing and the press happened off camera.

| Value | Where it shows |
|---|---|
| APE = Action, Purpose, Expectation | framework help text on the page, and the three labels in the result |
| Action / Purpose / Expectation labels | "Your Optimized Prompt" box, three lines |
| Under 300 words, welcoming tone | the Expectation line |
| Open in ChatGPT, Open in Claude | buttons under the prompt |

## Intent

Goal: a marketer who writes prompts freehand sees a framework fill each part for them | Platform: tool page, social | Length: 35 to 45s | Success: viewer picks a framework and runs their own goal.

One reader: an e-commerce content lead who rewrites the same prompt every week. Belief now: "prompting is about finding the magic phrasing." Belief after: "a framework names the parts, and this fills them from my goal."

## Hook candidates (different categories)

1. Command (picked): super "Stop guessing at *wording.*", VO "A framework names the parts a good prompt has to carry." Echoes the page tagline ("instead of guessing at wording"); super and VO split the idea.
2. Question: "Which parts is your prompt missing?" Rejected: promises a diagnosis the tool does not run.
3. List: "APE, RACE, CREATE, SPARK." Rejected: four acronyms in two seconds says nothing to a new viewer.

## Script

Runtime 41.83s

| # | VO starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.3 | Stop guessing at *wording.* | A framework names the parts a good prompt has to carry. |
| 2 name | 3.744 | Best AI Prompt *Generator* | Meet the Best AI Prompt Generator, from hyperank. |
| 3 type | 7.252 | Write your *goal.* | Write the goal, then the context. Here, a returns page for a furniture store. |
| 4 press | 18.487 | One *press.* | It builds the prompt on APE: action, purpose, expectation. |
| 5 gate | 23.19 | *Ready.* | A free account opens the prompt. |
| 6 read | 25.546 | Every part, *labelled.* | Each part gets its own label, so a missing one stands out. |
| 7 read | 29.288 | Your limits, *kept.* | Your context lands in the expectation: under three hundred words, a welcoming tone. |
| 8 read | 34.972 | Paste it *anywhere.* | Copy it, or open it straight in ChatGPT or Claude. |
| 9 close | 38.864 | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    A framework names the parts a good prompt has to carry.
    Meet the Best A-I Prompt Generator, from Hyper-rank.
    Write the goal, then the context. Here, a returns page for a furniture store.
    It builds the prompt on A-P-E. Action, purpose, expectation.
    A free account opens the prompt.
    Each part gets its own label, so a missing one stands out.
    Your context lands in the expectation: under three hundred words, a welcoming tone.
    Copy it, or open it straight in Chat G-P-T or Claude.
    Free to run. Hyper-rank dot A-I.

Spoken words: 86. Whisper check: "APE. Action, purpose, expectation" and "ChatGPT or Claude" heard correctly.

## Honesty notes

- The framework stays on APE, the page default (the pipeline does not change a select). The film says APE because the result is built on it.
- The context asked for "no legal advice"; the result says "avoid any legal jargon", which is not the same thing, so the film does not claim that part was kept. It names only the two parts that did carry over: under 300 words, and a welcoming tone (the context said "friendly").
- The typing beat is long (about 11s) because both fields are typed in full as they were run.
- Wait compressed, so `Sequence shortened` shows from the click to the result. Standard close. No tool count, no signup line.

## Humanizer pass

- Draft read 7 "It keeps every rule you set" overclaimed (see the legal-advice note). Cut to the two rules that are on screen.
- No em dashes, no banned words.
