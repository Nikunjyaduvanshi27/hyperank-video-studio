# tutorial-ai-response-generator: AI Response Generator

Status: READY for the render queue. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: Message "You billed us for 12 seats in March. We only have 9 people.", Points it must hit "Refund 3 seats this week", Tone Professional, Target length 150 words (the page defaults). Master 16:9 (1920x1080). Project: `tutorials/ai-response-generator/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Logged-in run through BrowserOS neo (Profile 1, tab 33): `premium/capture/neo-invoice/neo-api.json` (POST `/api/tools/ai-response-generator`, `ok: true`, request `responseLength: 150`), DOM `neo-result-sec.html`. Anonymous runs hit the site's rate limit during capture, so there is no gate beat; the film shows the unlocked result.
- The client message is a demo complaint written for this film; no real company or person.

| Value | Where it shows |
|---|---|
| "billing for 12 seats instead of the 9 individuals currently on your team" | Your Generated Reply, first paragraph |
| "we will process a refund for the 3 excess seats this week" | Your Generated Reply, second paragraph |
| Copy text button | Your Generated Reply header |
| Read the draft as the person receiving it before you send | tool page, How to use step 5 |

## Intent

Goal: someone facing an unhappy client gets a complete, polite draft that commits to exactly what they decided | Platform: tool page, social | Length: 30 to 40s | Success: viewer pastes a real message they owe a response to.

One reader: a SaaS founder handling billing email themselves. Belief now: "an AI draft will promise things I didn't agree to." Belief after: "the points field decides what it commits to."

Sibling films in this batch: AI Answer Generator (a customer question), AI Reply Generator (a short decline). This one is the long-form complaint response.

## Hook candidates (different categories)

1. Scene (picked): super "A billing *complaint.*", VO "A client says you billed them for too many seats."
2. Question: "Owe someone a careful reply?" Rejected: the Answer Generator film opens on a question.
3. Mistake: "Most replies answer half the message." Rejected: the tool page says it, but as a hook it lectures before showing anything.

## Script

Runtime 37.65s

| # | Beat starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.0 | A billing *complaint.* | A client says you billed them for too many seats. |
| 2 name | 3.01 | AI Response *Generator* | Meet the AI Response Generator, from hyperank. |
| 3 type | 6.33 | Message, then your *points.* | Paste their message, then the point your response must make. |
| 4 read | 15.69 | Tone and *length.* | Professional tone, about 150 words. |
| 5 press | 19.34 | One *press.* | One press, and it drafts the response. |
| 6 result | 21.98 | A full *draft.* | It names the problem first: 12 seats billed, 9 people on the team. |
| 7 read | 26.85 | Your point, *kept.* | Your point is in: a refund for the 3 extra seats this week. |
| 8 read | 30.98 | Read it as *them.* | Copy it, and read it as the client would before you send. |
| 9 close | 34.46 | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    A client says you billed them for too many seats.
    Meet the A-I Response Generator, from Hyper-rank.
    Paste their message, then the point your response must make.
    Professional tone, about a hundred and fifty words.
    One press, and it drafts the response.
    It names the problem first. Twelve seats billed, nine people on the team.
    Your point is in. A refund for the three extra seats this week.
    Copy it, and read it as the client would before you send.
    Free to run. Hyper-rank dot A-I.

## Honesty notes

- The draft on screen is the model's output from the one recorded run, unedited.
- The numbers 12, 9 and 3 all come from the typed input and the draft; no other figures appear.
- Default zoom; a Tone and length beat scrolls the form so the Generate response button is in frame for the press.
- Sequence shortened from the click to the result.
- Standard close. No tool count, no signup line, no em dashes.
