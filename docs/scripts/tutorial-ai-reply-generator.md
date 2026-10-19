# tutorial-ai-reply-generator: AI Reply Generator

Status: READY for the render queue. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: Original message "Could you speak at our design meetup on May 22?", What the reply should say "Decline May, offer June". Where it lands Email, Style Professional, Length Short (the page defaults). Master 16:9 (1920x1080). Project: `tutorials/ai-reply-generator/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Logged-in run through BrowserOS neo (Profile 1, tab 33): `premium/capture/neo-meetup/neo-api.json` (POST `/api/tools/ai-reply-generator`, `ok: true`), DOM `neo-result-sec.html`. The anonymous page puts the result behind "Sign up free to unlock"; anonymous runs were rate-limited during capture, so the film shows the unlocked result with a plain result beat, no gate.
- The input message is a demo invitation written for this film; no real person or event.

| Value | Where it shows |
|---|---|
| Subject "Re: Speaking at Design Meetup", greeting, body declining May 22 and offering June | Generated Reply card |
| Placeholders [Recipient's Name], [Your Name], [Your Position], [Your Contact Information] | Generated Reply card |
| Email, Professional, Short | the form's selects, as sent in the request |

## Intent

Goal: someone who has to say no turns a two-word note into a polite email | Platform: tool page, social | Length: 30 to 40s | Success: viewer drafts their own reply.

One reader: a designer who keeps getting speaking invites and stalls on the polite no. Belief now: "declining well takes ten minutes of wording." Belief after: "a note like 'Decline May, offer June' is enough input."

Sibling films in this batch: AI Answer Generator (a customer question), AI Response Generator (a billing complaint email). This one is the short decline.

## Hook candidates (different categories)

1. Command (picked): super "Say no *nicely.*", VO "An invite you can't accept still needs a reply."
2. Question: "Stuck on a polite no?" Rejected: the Answer Generator film already opens on a question.
3. Proof: "Four words in, one email out." Rejected: counts the note's words, which reads as a gimmick.

## Script

Runtime 35.08s

| # | Beat starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.0 | Say no *nicely.* | An invite you can't accept still needs a reply. |
| 2 name | 3.1 | AI Reply *Generator* | Meet the AI Reply Generator, from hyperank. |
| 3 type | 6.37 | Their message, your *note.* | Paste their message, then a short note of what to say. |
| 4 read | 14.62 | Email, professional, *short.* | It lands in email, professional and short. |
| 5 press | 18.27 | One *press.* | One press, and it drafts the reply. |
| 6 result | 20.8 | A ready *draft.* | Back comes a subject line, a greeting and the reply. |
| 7 read | 24.35 | No to May, yes to *June.* | It turns down May 22, and offers June instead. |
| 8 read | 28.24 | Fill the *brackets.* | Swap in the names in brackets, read it once, then send. |
| 9 close | 31.89 | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    An invite you can't accept still needs a reply.
    Meet the A-I Reply Generator, from Hyper-rank.
    Paste their message, then a short note of what to say.
    It lands in email, professional and short.
    One press, and it drafts the reply.
    Back comes a subject line, a greeting and the reply.
    It turns down May twenty-second, and offers June instead.
    Swap in the names in brackets, read it once, then send.
    Free to run. Hyper-rank dot A-I.

## Honesty notes

- The reply on screen is the model's output from the one recorded run, unedited, placeholders included; the film tells the viewer to fill them in rather than hiding them.
- Zoom 1.15; a settings beat scrolls the form so the Generate reply button is in frame, and the press shot pulls out to the whole laptop.
- Sequence shortened from the click to the result.
- Standard close. No tool count, no signup line, no em dashes.
