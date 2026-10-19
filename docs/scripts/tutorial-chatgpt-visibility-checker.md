# tutorial-chatgpt-visibility-checker: ChatGPT Visibility Checker

Status: rendered for review. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: canva.com. Master 16:9 (1920x1080). Project: `tutorials/chatgpt-visibility-checker/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Logged-in run in BrowserOS neo (Profile 1, the hyperank.ai account, verified on chrome://version before the run): `premium/capture/neo-canva.com/neo-api.json` (POST `/api/tools/chatgpt-visibility-checker`, input `{"url":"canva.com"}`) and the unlocked result DOM `neo-result-sec.html`.
- Logged-out run of the same input: `capture/try-canva.com/` (the real gate card "Your results are ready / Sign up free to unlock" comes from this DOM).
- Candidates tried: figma.com (100%, every answer named it, so nothing to teach), canva.com (80%, one miss, mixed positions). Picked canva.com.

| Value | Where it shows |
|---|---|
| 80% Citation Score | `citationScore: 80`, top-left card |
| 4 answers named Canva | Implicit Citation `4` |
| 0 answers gave the domain | Explicit Citation `0` |
| First three times | Position Distribution: Position 1 = 3, Position 3 = 1 |
| Query 3 "top user experience design platforms": No Citation | Analysis Steps, 5 Query Generation |

## Intent

Goal: a marketing lead sees how often ChatGPT names their brand, and where it does not | Platform: tool page, social | Length: 30 to 40s | Success: viewer runs the tool.

One reader: the head of marketing at a design SaaS who assumes ChatGPT already recommends them. Belief now: "we are big, so AI names us." Belief after: "it names us, never links us, and misses whole questions."

## Hook candidates (different categories)

1. Question (picked): super "Does ChatGPT name *you?*", VO "Your buyers ask ChatGPT what to buy." Super and VO say different things; works muted.
2. Stake: "Your buyers already asked." Rejected: the approved v3 opens with it, so it would read as a copy.
3. Proof: "Canva, named in 4 of 5." Rejected: leads with the demo brand, not the viewer.

## Script

Runtime 39.64s

| # | VO starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.3 | Does ChatGPT name *you?* | Your buyers ask ChatGPT what to buy. |
| 2 name | 3.168 | ChatGPT Visibility *Checker* | Meet the ChatGPT Visibility Checker, from hyperank. |
| 3 type | 7.017 | Type your *domain.* | Enter your domain. Here, canva.com. |
| 4 press | 10.056 | One *press.* | It reads your home page to learn what you sell. |
| 5 fan | 12.967 | Five buying *questions.* | Then it writes five buying questions without your name, and asks ChatGPT each one. |
| 6 gate | 18.501 | *Ready.* | A free account opens the full report. |
| 7 read | 21.241 | Named in four of *five.* | Eighty percent. Four of the five answers named Canva. |
| 8 read | 24.813 | Named, not *linked.* | But none of them gave canva.com itself. |
| 9 read | 27.863 | Usually *first.* | When ChatGPT named Canva, it was first three times. |
| 10 read | 31.691 | Where you're *missing.* | One question left Canva out: top user experience design platforms. |
| 11 close | close | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    Your buyers ask Chat G-P-T what to buy.
    Meet the Chat G-P-T Visibility Checker, from Hyper-rank.
    Enter your domain. Here, Canva dot com.
    It reads your home page to learn what you sell.
    Then it writes five buying questions without your name, and asks Chat G-P-T each one.
    A free account opens the full report.
    Eighty percent. Four of the five answers named Canva.
    But none of them gave Canva dot com itself.
    When Chat G-P-T named Canva, it was first three times.
    One question left Canva out: top user experience design platforms.
    Free to run. Hyper-rank dot A-I.

Spoken words: 91

## Honesty notes

- The result is gated for logged-out users; the film shows the real gate card and says once "A free account opens the full report."
- "Named, not linked" is the Explicit Citation card (0), which the tool page defines as answers that gave your domain.
- The wait is compressed (about 8s live), so `Sequence shortened` shows from the click to the result.
- The five question pills are verbatim from `steps[4].queries`. ChatGPT is the only engine shown, because this tool asks one GPT model.
- Standard close: super "Free to run.", printed "Full report with a free account.", then hyperank.ai. No tool count anywhere.

## Humanizer pass

- Draft read 7 "Canva scored eighty, a strong result" judged the number. Cut to the fact: "Eighty percent. Four of the five answers named Canva."
- Draft super "Visibility score: 80%" repeated the card. Replaced with "Named in four of *five*."
- No em dashes, no banned words, no tool count, no signup line.
