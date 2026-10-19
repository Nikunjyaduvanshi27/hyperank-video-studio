# tutorial-brand-audit: Brand Audit Report

Status: READY for the render queue. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: brand Mailchimp, website mailchimp.com. Master 16:9 (1920x1080). Project: `tutorials/brand-audit/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Logged-in run in BrowserOS neo (Profile 1, the hyperank.ai account, verified on chrome://version before the run): `premium/capture/neo-mailchimp/neo-api.json` (POST `/api/tools/brand-audit`, input `{"brand":"Mailchimp","url":"mailchimp.com"}`) and the unlocked result DOM `neo-result-sec.html`.
- `neo-result-sec.settled.html` is that DOM with the six favicons served from local copies (`ico/`), nothing else changed.
- Logged-out run of the same input: `capture/try-mailchimp/` (the real gate card comes from this DOM).
- One candidate run (the site's rate limit was active all session): Mailchimp gave a full report with a ranking and a citation split.

| Value | Where it shows |
|---|---|
| Prompt evaluations 5 / 7 | `promptEvaluations: {scored: 5, total: 7}` |
| ChatGPT 71%, Gemini 57% | Your brand mentions (`brandMentions`) |
| Ranking: Mailchimp 98, ActiveCampaign 80, HubSpot 50, Klaviyo 50 | Competitive ranking |
| Competitors 54%, Your brand 21%, Third party 25% | Citation score breakdown (`topCitations`) |
| Seven buying questions, none naming the brand | tool page "What is the Brand Audit Report?" |

## Intent

Goal: a marketer sees, engine by engine, how often AI names their brand unprompted, and who else it names | Platform: tool page, social | Length: 35 to 45s | Success: viewer audits their own brand.

One reader: the lifecycle marketing lead at an email platform. Belief now: "we're the category leader, AI says our name." Belief after: "it says it most of the time, and competitors still hold most of the cited sources."

## Hook candidates (different categories)

1. Command (picked): super "Ask the *engines.*", VO "Ask ChatGPT and Gemini about your category. Do they name you?" The two engine tiles carry the hook; distinct from the single-engine checker videos. Grok is left out because it returned no number in this run.
2. Number: "Five of seven." Rejected: Mailchimp's number, not the viewer's.
3. Contrast: "Named, but not cited." Rejected for the hook: needs the citation card on screen to land.

## Script

Runtime 40.66s

| # | VO starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.3 | Ask the *engines.* | Ask ChatGPT and Gemini about your category. Do they name you? |
| 2 name | 4.92 | Brand Audit *Report* | Meet the Brand Audit Report, from hyperank. |
| 3 type | 7.89 | Brand, then *site.* | Enter your brand, and your site. Here, Mailchimp. |
| 4 press | 11.93 | Seven *questions.* | It asks seven buying questions that never use your name. |
| 5 gate | 15.67 | *Ready.* | A free account opens the full report. |
| 6 read | 18.41 | Five of *seven.* | Five of the seven questions brought up Mailchimp. |
| 7 read | 21.71 | Engine by *engine.* | ChatGPT named it in seventy-one percent of answers. Gemini, fifty-seven. |
| 8 read | 27.61 | Who else gets *named.* | Next in the ranking: ActiveCampaign, then HubSpot and Klaviyo. |
| 9 read | 32.27 | Whose sources *count.* | Of the sources cited, competitors hold fifty-four percent. Mailchimp, twenty-one. |
| 10 close | close | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    Ask Chat G-P-T and Gemini about your category. Do they name you?
    Meet the Brand Audit Report, from Hyper-rank.
    Enter your brand, and your site. Here, Mailchimp.
    It asks seven buying questions that never use your name.
    A free account opens the full report.
    Five of the seven questions brought up Mailchimp.
    Chat G-P-T named it in seventy-one percent of answers. Gemini, fifty-seven.
    Next in the ranking: Active Campaign, then HubSpot and Klay-vee-oh.
    Of the sources cited, competitors hold fifty-four percent. Mailchimp, twenty-one.
    Free to run. Hyper-rank dot A-I.

Pronunciation: whisper heard "MailChimp", "active campaign", "HubSpot" correctly; "Klaviyo" (spelled Klay-vee-oh) transcribes as "Clavio", which is whisper's spelling of the correct sound.

## Honesty notes

- In this run Grok returned no mention rate; the result lists ChatGPT and Gemini only. The hook, the engine tiles and the VO show only those two engines; the live page subtitle on the laptop still reads the tool's own copy.
- The audit score (98, capped by the tool's formula) is on screen but not narrated, so it never competes with the 5 of 7 and the per-engine rates.
- "Of the sources cited" reads the Citation score breakdown: Competitors 54%, Your brand 21%, Third party 25%.
- The wait is compressed, so `Sequence shortened` shows from the click to the result.
- Standard close. No tool count, no signup line, no em dashes.
