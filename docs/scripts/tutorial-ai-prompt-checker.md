# tutorial-ai-prompt-checker: AI Prompt Checker

Status: prepared for the render queue. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: "Write a blog post about electric cars. Make it SEO friendly etc." (use case General). Master 16:9 (1920x1080). Project: `tutorials/ai-prompt-checker/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Logged-in run through BrowserOS neo (Profile 1): `premium/capture/neo-evblog/neo-api.json` (POST `/api/tools/ai-prompt-checker`, input `{"prompt": "...", "useCase": "General"}`), DOM `neo-result-sec.html`. The neo DOM was captured before the page's entrance fade finished; `neo-result-sec-settled.html` only swaps those six inline styles for the page's settled state (opacity 1, no blur). No text changed.
- Gate card: anonymous run `premium/capture/try-evblog2/result-sec.html` ("Your results are ready", "Sign up free to see the full report.").
- One candidate only. The prompt was written to carry the defects the tool page lists by name (no audience, no length, no format, an "etc."), so the review has something real to find.

| Value | Where it shows |
|---|---|
| Rating: 3/10 | Rating card |
| "The use of 'etc.' is ambiguous and invites hallucination" | Rating card reasoning |
| 9 techniques under Missing / Recommended (Context, Role, Instructions, Steps, Persona, Examples, Few-shot examples, Chain-of-thought, Output formatting) | Technique Evaluation |
| Enhanced Version (full rewritten prompt) | Enhanced Version card |

## Intent

Goal: a marketer sees what a checker finds in a prompt that looks fine | Platform: tool page, social | Length: 35 to 45s | Success: viewer pastes their own prompt.

One reader: a content marketer who reuses a one-line blog prompt every week. Belief now: "my prompt is fine, the model is the problem." Belief after: "the prompt left out the audience, the format and the length, and a checker names each gap."

## Hook candidates (different categories)

1. Question (picked): super "What's wrong with this *prompt?*", VO "A prompt can read fine to you, and still leave the model guessing."
2. Proof: "Three out of ten." Rejected: spends the reveal in second one.
3. Contrast: "Looks done. Isn't." Rejected: judges the viewer's prompt before the tool has.

## Script

Runtime 39.14s

| # | Beat starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.0 | What's wrong with this *prompt?* | A prompt can read fine to you, and still leave the model guessing. |
| 2 name | 3.95 | AI Prompt *Checker* | Meet the AI Prompt Checker, from hyperank. |
| 3 type | 6.9 | Paste your *prompt.* | Paste the prompt you'd send. Here, a quick blog brief about electric cars. |
| 4 press | 14.05 | One *press.* | It rates the prompt for its use case, and explains the score. |
| 5 gate | 17.86 | *Ready.* | A free account opens the full review. |
| 6 read | 20.55 | Three out of *ten.* | Three out of ten. Too vague, with too little context. |
| 7 read | 24.08 | Even the *etc.* | It flags the etc. as room for the model to invent. |
| 8 read | 27.93 | Nine techniques *missing.* | Nine techniques are missing, from a role to an output format. |
| 9 read | 31.93 | A stronger *version.* | Then it writes an enhanced version to test against your original. |
| 10 close | 35.95 | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    A prompt can read fine to you, and still leave the model guessing.
    Meet the A-I Prompt Checker, from Hyper-rank.
    Paste the prompt you'd send. Here, a quick blog brief about electric cars.
    It rates the prompt for its use case, and explains the score.
    A free account opens the full review.
    Three out of ten. Too vague, with too little context.
    It flags the et cetera, as room for the model to invent.
    Nine techniques are missing, from a role to an output format.
    Then it writes an enhanced version to test against your original.
    Free to run. Hyper-rank dot A-I.

Spoken words: 98

## Honesty notes

- "Three out of ten" and "too vague, with too little context" paraphrase the run's own reasoning ("vague and lacks detailed instructions", "doesn't provide enough context").
- "Room for the model to invent" paraphrases "invites hallucination".
- Nine is counted from the Missing / Recommended list in this run.
- The video never says the enhanced version scores higher; the tool page itself says to run it beside the original, and the VO says the same.
- Gate shown once, printed again on the end card. Sequence shortened from the click to the result.
- No tool count, no signup line, no em dashes.
