# tutorial-gemini-visibility-checker: Gemini Visibility Checker

Status: READY for the render queue. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: asana.com. Master 16:9 (1920x1080). Project: `tutorials/gemini-visibility-checker/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Logged-in run in BrowserOS neo (Profile 1, the hyperank.ai account, verified on chrome://version before the run): `premium/capture/neo-asana.com/neo-api.json` (POST `/api/tools/gemini-visibility-checker`, input `{"url":"asana.com"}`) and the unlocked result DOM `neo-result-sec.html`.
- Logged-out run of the same input: `capture/try-asana/` (the real gate card comes from this DOM).
- Candidates tried: airbnb.com (80%, four of five, the same shape as the ChatGPT video, and already used by favicon-checker), asana.com (60%, two clean misses with named competitors). Picked asana.com.

| Value | Where it shows |
|---|---|
| 60% Citation Score | `citationScore: 60` |
| Named in 3 of 5 answers | Implicit Citation `3` |
| First once, second twice | Position Distribution: Position 1 = 1, Position 2 = 2 |
| Both misses are workflow automation questions | Query 2 "workflow automation tools for human and ai collaboration" and query 5 "workflow automation software integrations list", both No Citation |
| Zapier and Make named in query 5 | query 5 Competitors in Results: Zapier, Make, Workato, Microsoft Power Automate, n8n |

## Intent

Goal: a SaaS marketer sees which buying questions Gemini answers without them, and who it names there | Platform: tool page, social | Length: 35 to 45s | Success: viewer checks their own domain.

One reader: the product marketing lead at a work management SaaS. Belief now: "Gemini knows our category, so it names us." Belief after: "it names us on our core questions and hands the adjacent ones to someone else."

## Hook candidates (different categories)

1. Question about the competitor (picked): super "Who gets named *instead?*", VO "When Gemini leaves you out, who does it name instead?" Distinct from the ChatGPT video ("Does ChatGPT name you?").
2. Number: "Three of five." Rejected: Asana's number, not the viewer's.
3. Stake: "Gemini answers your buyers." Rejected: reads as a copy of the ChatGPT opener.

## Script

Runtime 42.99s

| # | VO starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.3 | Who gets named *instead?* | When Gemini leaves you out, who does it name instead? |
| 2 name | 3.72 | Gemini Visibility *Checker* | Meet the Gemini Visibility Checker, from hyperank. |
| 3 type | 7.29 | Type a *domain.* | Enter your domain. Here, asana.com. |
| 4 press | 10.38 | Your name, *removed.* | It writes five buying questions from your home page, with your name taken out. |
| 5 fan | 15.16 | Asked *cold.* | Then Gemini answers each one, cold. |
| 6 gate | 19.71 | *Ready.* | A free account opens the full report. |
| 7 read | 22.45 | Three of *five.* | Sixty percent. Gemini named Asana in three of the five answers. |
| 8 read | 27.2 | Near the *top.* | When it did, Asana came first once, and second twice. |
| 9 read | 30.92 | Two *misses.* | Both misses were workflow automation questions. |
| 10 read | 35.77 | Named *instead.* | In that answer, Gemini named Zapier and Make. Not Asana. |
| 11 close | close | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    When Gemini leaves you out, who does it name instead?
    Meet the Gemini Visibility Checker, from Hyper-rank.
    Enter your domain. Here, Asana dot com.
    It writes five buying questions from your home page, with your name taken out.
    Then Gemini answers each one, cold.
    A free account opens the full report.
    Sixty percent. Gemini named Asana in three of the five answers.
    When it did, Asana came first once, and second twice.
    Both misses were workflow automation questions.
    In that answer, Gemini named Zapier and Make. Not Asana.
    Free to run. Hyper-rank dot A-I.

Pronunciation: whisper heard "Gemini", "Asana", "Zapier", "Make" correctly. "n8n" was dropped from the line after Kokoro read it as "N A ten".

## Honesty notes

- The five question pills are verbatim from `steps[4].queries`; the tool step itself says "asked Gemini cold".
- "In that answer" is query 5, opened on screen; its competitor list also has Workato, Microsoft Power Automate and n8n, all visible in the lift.
- The result is gated for logged-out users; the film shows the real gate card and says once "A free account opens the full report."
- The wait is compressed, so `Sequence shortened` shows from the click to the result.
- Standard close. No tool count, no signup line, no em dashes.
