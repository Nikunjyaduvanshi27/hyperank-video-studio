# tutorial-chatgpt-prompt-generator: ChatGPT Prompt Generator

Status: ready for render. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: task "Turn a week of support tickets into a bug summary", context "For the engineering team, top five issues only". Master 16:9 (1920x1080). Project: `tutorials/chatgpt-prompt-generator/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Logged-in run in BrowserOS neo (Profile 1, the hyperank.ai account, verified on chrome://version before the run, tab 30): `premium/capture/neo-tickets/neo-api.json` and the unlocked result DOM `neo-result-sec.html`. Entrance-animation `opacity:0` styles (hidden neo tab) settled to the visible state; no text changed.
- `neo-result-sec-pre.html` is the same DOM with the result's `<p class="font-mono ... whitespace-pre-wrap">` retagged as `<pre class="not-prose ...">` (same classes, same text; the site CSS has no prose rules, so it renders the same). This lets the `spans` key lift single lines. Side effect: the blank line after the Persona line and after Issue #1 is dropped by the span split.
- Gate card: the site's generic logged-out card, copied from `chatgpt-visibility-checker/premium/capture/try-canva.com/` because the anonymous run hit the rate limit. Same text on every gated tool.
- The first logged-in run also hit the rate limit; the second returned the prompt.

| Value | Where it shows |
|---|---|
| Persona: Technical Support Analyst | first line of "Your Optimized Prompt" |
| Issue block: Description, Frequency, Context | Formatting, Issue #1 to #5 |
| "the top five issues only" | Constraints line, and the context field |
| Open in ChatGPT | button under the prompt |

## Intent

Goal: someone who pastes loose requests into ChatGPT gets a prompt with a role, rules, a shown format and limits | Platform: tool page, social | Length: 35 to 45s | Success: viewer runs their own task.

One reader: a support lead who asks ChatGPT for a weekly summary and gets a different shape every time. Belief now: "ChatGPT just needs the request." Belief after: "show it the format and it copies it; this writes that for me."

## Hook candidates (different categories)

1. Contrast (picked): super "Show it, don't *describe.*", VO "ChatGPT copies a format you show it, and guesses one you only describe." From the page: "A described format gets approximated; a shown format gets copied."
2. Stake: "Same prompt, new shape every week." Rejected: the film never runs the prompt twice.
3. Question: "Where does the persona go?" Rejected: true to the page, too inside-baseball for a cold open.

## Script

Runtime 43.33s

| # | VO starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.3 | Show it, don't *describe.* | ChatGPT copies a format you show it, and guesses one you only describe. |
| 2 name | 5.579 | ChatGPT Prompt *Generator* | Meet the ChatGPT Prompt Generator, from hyperank. |
| 3 type | 9.321 | Describe the *task.* | Describe the task, then the context. Here, a week of support tickets. |
| 4 press | 19.761 | One *press.* | It writes a role, instructions, a format and limits. |
| 5 gate | 23.248 | *Ready.* | A free account opens the prompt. |
| 6 read | 25.604 | A clear *role.* | First, a role: technical support analyst. |
| 7 read | 28.856 | A format to *copy.* | Then a shape for every issue: description, frequency, context. |
| 8 read | 33.217 | Your limit, *kept.* | And your limit, word for word: the top five issues only. |
| 9 read | 37.131 | Paste and *go.* | Copy it, or open it straight in ChatGPT. |
| 10 close | 40.361 | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    Chat G-P-T copies a format you show it, and guesses one you only describe.
    Meet the Chat G-P-T Prompt Generator, from Hyper-rank.
    Describe the task, then the context. Here, a week of support tickets.
    It writes a role, instructions, a format and limits.
    A free account opens the prompt.
    First, a role: technical support analyst.
    Then a shape for every issue: description, frequency, context.
    And your limit, word for word: the top five issues only.
    Copy it, or open it straight in Chat G-P-T.
    Free to run. Hyper-rank dot A-I.

Spoken words: 86

## Honesty notes

- "Role, instructions, a format and limits" are the four labelled parts of the result (Persona, Instructions, Formatting, Constraints); the page names the same four.
- "Word for word" holds: the Constraints line contains "the top five issues only", the exact phrase typed in Context.
- Hook is the page's own claim about how ChatGPT reads prompts, not a measured result.
- Wait compressed, so `Sequence shortened` shows from the click to the result. Standard close. No tool count, no signup line.

## Humanizer pass

- Draft read 7 "A perfect template for every issue" was a superlative; cut to what is on screen.
- No em dashes, no banned words.
