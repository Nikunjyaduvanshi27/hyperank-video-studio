# tutorial-gemini-prompt-generator: Gemini Prompt Generator

Status: ready for render. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: task "Review a vendor contract and flag risky clauses", context "Auto-renewal, termination and liability, in plain English". Master 16:9 (1920x1080). Project: `tutorials/gemini-prompt-generator/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Logged-in run in BrowserOS neo (Profile 1, the hyperank.ai account, verified on chrome://version by `_premium/neo_capture.py`, tab 30): `premium/capture/neo-contract/neo-api.json` and the unlocked result DOM `neo-result-sec.html`. Earlier attempts hit the site limits ("You've run quite a few tools in a short window", then "This tool runs 2 times an hour").
- `neo-result-sec-pre.html`: the same DOM with the result's pre-wrap `<p>` retagged as `<pre class="not-prose ...">` (same classes and text; the site CSS has no prose rules) so `spans` can lift single items.
- Gate card: the site's generic logged-out card, copied from `chatgpt-visibility-checker/premium/capture/try-canva.com/` because the anonymous run hit the rate limit. Same text on every gated tool.

| Value | Where it shows |
|---|---|
| Persona, Focus Areas, Instructions, Constraints | sections of "Your Optimized Prompt" |
| Auto-Renewal, Termination as focus areas | Focus Areas items 1 and 2 |
| Exact quote, Plain English translation, specific risk | Instructions item 3 "Draft" |
| No Assumptions rule | "Constraints to Prevent Hallucination", first bullet |
| Open in Gemini | button under the prompt |

## Intent

Goal: an ops or legal lead turns a loose request into a Gemini prompt with standing rules kept apart from the task | Platform: tool page, social | Length: 35 to 45s | Success: viewer runs their own task.

One reader: an operations manager who pastes vendor contracts into Gemini and asks "anything risky?". Belief now: "Gemini will spot what matters." Belief after: "name the risks and the rules once, and the prompt does the rest; this writes it."

## Hook candidates (different categories)

1. Mechanism (picked): super "Rules first, task *second.*", VO "Gemini keeps standing rules apart from the chat. Your prompt should too." From the page: systemInstruction sits apart from the chat turns, rules up top, task below.
2. Question: "Where does the question go?" Rejected: the page's long-context tip (question after the material) is not what the result demonstrates.
3. Stake: "One missed auto-renewal costs a year." Rejected: an invented stake, nothing in the run supports it.

## Script

Runtime 44.75s

| # | VO starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.3 | Rules first, task *second.* | Gemini keeps standing rules apart from the chat. Your prompt should too. |
| 2 name | 4.939 | Gemini Prompt *Generator* | Meet the Gemini Prompt Generator, from hyperank. |
| 3 type | 8.34 | Describe the *job.* | Describe the job, then what to watch for. Here, a vendor contract. |
| 4 press | 19.575 | One *press.* | It writes a persona, focus areas, steps and limits. |
| 5 gate | 23.296 | *Ready.* | A free account opens the prompt. |
| 6 read | 25.652 | Your risks, *named.* | Your risks become focus areas: auto-renewal, then termination. |
| 7 read | 30.163 | Quote, then *translate.* | For each clause: the exact quote, a plain English version, and the risk. |
| 8 read | 34.802 | No *guessing.* | And a rule against assuming terms the contract never states. |
| 9 read | 38.736 | Straight into *Gemini.* | Copy it, or open it straight in Gemini. |
| 10 close | 41.786 | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    Gemini keeps standing rules apart from the chat. Your prompt should too.
    Meet the Gemini Prompt Generator, from Hyper-rank.
    Describe the job, then what to watch for. Here, a vendor contract.
    It writes a persona, focus areas, steps and limits.
    A free account opens the prompt.
    Your risks become focus areas: auto-renewal, then termination.
    For each clause: the exact quote, a plain English version, and the risk.
    And a rule against assuming terms the contract never states.
    Copy it, or open it straight in Gemini.
    Free to run. Hyper-rank dot A-I.

Spoken words: 89. Whisper check: "Gemini" heard correctly in lines 1, 2 and 9.

## Honesty notes

- The hook states how Gemini separates system instructions from chat turns, as the tool page explains; the film does not claim the generator splits the output into two blocks (it returns one block, and the page says so).
- Liability, the third risk typed, is also a focus area in the result; the film names the first two to keep the line short.
- "Never states" reads the No Assumptions rule: "Do not assume terms exist if they are not explicitly written."
- Wait compressed, so `Sequence shortened` shows from the click to the result. Standard close. No tool count, no signup line.

## Humanizer pass

- Draft read 7 "It reads the contract like a lawyer" overclaimed; the prompt only sets a persona. Cut to the three outputs the prompt asks for.
- No em dashes, no banned words.
