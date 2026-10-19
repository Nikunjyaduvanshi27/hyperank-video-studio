# tutorial-ai-answer-generator: AI Answer Generator

Status: READY for the render queue. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: Question "Is it safe to charge my phone overnight?", Tone Professional, Language empty (English). Master 16:9 (1920x1080). Project: `tutorials/ai-answer-generator/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Logged-in run through BrowserOS neo (Profile 1, tab 33): `premium/capture/neo-phone/neo-api.json` (POST `/api/tools/ai-answer-generator`, `ok: true`), DOM `neo-result-sec.html`. Anonymous runs hit the site's rate limit during capture, so there is no gate beat; the film shows the unlocked result.
- "Tone changes the register, not the facts" is the tool's own field help.

| Value | Where it shows |
|---|---|
| Opening: "generally considered safe for most modern smartphones" | Generated Answer, first paragraph |
| Four numbered tips: original charger, overheating, battery management settings, updates | Generated Answer, list |
| Copy button | Generated Answer header |

## Intent

Goal: a support or content person turns a customer question into a usable first answer | Platform: tool page, social | Length: 30 to 40s | Success: viewer types their own customers' question.

One reader: a small shop owner answering the same product questions in DMs. Belief now: "I write every answer from scratch." Belief after: "one question in, a structured answer I can edit."

Sibling films in this batch: AI Response Generator (a billing complaint email), AI Reply Generator (a short decline). This one is the customer question.

## Hook candidates (different categories)

1. Question (picked): super "Got a customer *question?*", VO "A customer asks if they can charge their phone overnight."
2. Scene: "Same question, fifth time today." Rejected: implies a frequency nobody measured.
3. Command: "Answer it once, well." Rejected: says nothing about the tool.

## Script

Runtime 31.98s

| # | Beat starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.0 | Got a customer *question?* | A customer asks if they can charge their phone overnight. |
| 2 name | 3.63 | AI Answer *Generator* | Meet the AI Answer Generator, from hyperank. |
| 3 type | 6.8 | Type the *question.* | Type the question the way they asked it. |
| 4 read | 11.85 | Pick a *tone.* | Tone changes the register, not the facts. |
| 5 press | 15.5 | One *press.* | One press, and it writes the answer. |
| 6 result | 17.96 | Answer *first.* | It opens with the answer: generally safe for most modern phones. |
| 7 read | 22.24 | Then the *tips.* | Then four tips, from the charger to the battery settings. |
| 8 read | 25.74 | Copy, then *edit.* | Copy it, then add the details only you know. |
| 9 close | 28.79 | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    A customer asks if they can charge their phone overnight.
    Meet the A-I Answer Generator, from Hyper-rank.
    Type the question the way they asked it.
    Tone changes the register, not the facts.
    One press, and it writes the answer.
    It opens with the answer: generally safe for most modern phones.
    Then four tips, from the charger to the battery settings.
    Copy it, then add the details only you know.
    Free to run. Hyper-rank dot A-I.

## Honesty notes

- The answer on screen is the model's output from the one recorded run, unedited. It shows raw markdown asterisks (`**Use the Original Charger**`) because the page prints them; the film leaves them as they are.
- The film does not vouch for the battery advice; it describes what the answer contains.
- Default zoom; a Pick a tone beat scrolls the form so the Generate answer button is in frame for the press.
- Sequence shortened from the click to the result.
- Standard close. No tool count, no signup line, no em dashes.
