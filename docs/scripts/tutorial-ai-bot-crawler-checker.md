# tutorial-ai-bot-crawler-checker: AI Bot Crawlability Checker

Status: rendered for review. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: theguardian.com. Master 16:9 (1920x1080). Project: `tutorials/ai-bot-crawler-checker/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Public run (no gate): `premium/capture/try-theguardian.com/api.json` (POST `/api/tools/ai-bot-crawler-checker`, `score: 36`, 14 bots) and `result-sec.html`.
- Candidates tried: medium.com (1 of 14, nearly everything 403), wikipedia.org (11 of 14, but its blocked cards read "defaults to allowed", a confusing read), theguardian.com (5 of 14: the OpenAI bots allowed; ClaudeBot, PerplexityBot and others blocked by `Disallow: /`). Picked the Guardian.

| Value | Where it shows |
|---|---|
| 5 of 14 crawlers can read this page | "Crawler access" line under Crawlability Results |
| GPTBot ALLOWED (200) | GPTBot card |
| ClaudeBot BLOCKED, "Blocked by `Disallow: /` in robots.txt." | ClaudeBot card |
| `Disallow: /` blocks ClaudeBot, anthropic-ai, PerplexityBot and 5 more | Recommendations |

## Intent

Goal: a site owner sees which AI crawlers their site lets in and what to change | Platform: tool page, social | Length: 30 to 40s | Success: viewer checks their own domain.

One reader: a publisher's SEO lead who set robots.txt rules years ago. Belief now: "we allow the bots that matter." Belief after: "I can see per crawler who gets in, and the rule that blocks the rest."

## Hook candidates (different categories)

1. Question (picked, from the pattern doc): super "Which AI bots get *in?*", VO "GPTBot, ClaudeBot and the rest. Which ones can read your site?"
2. Number: "5 of 14." Rejected for the hook: the number belongs to the Guardian, not the viewer.
3. Contrast: "Allowed for one bot, blocked for the next." Rejected: needs the result on screen to land.

## Script

Runtime 32.71s

| # | VO starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.3 | Which AI bots get *in?* | GPTBot, ClaudeBot and the rest. Which ones can read your site? |
| 2 name | 4.832 | AI Bot Crawlability *Checker* | Meet the AI Bot Crawlability Checker, from hyperank. |
| 3 type | 8.511 | Type a *domain.* | Enter a domain. Here, theguardian.com. |
| 4 press | 11.72 | One *press.* | It reads robots.txt, then visits the site as each of fourteen crawlers. |
| 5 result | 17.319 | Five of *fourteen.* | Five of the fourteen crawlers can read the Guardian's home page. |
| 6 read | 21.381 | Allowed, or *blocked.* | GPTBot gets in. ClaudeBot is blocked by a Disallow rule. |
| 7 read | 25.956 | What to *change.* | Then it names the rule to change, and the crawlers it blocks. |
| 8 close | close | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    G-P-T-Bot, Claude-Bot, and the rest. Which ones can read your site?
    Meet the A-I Bot Crawlability Checker, from Hyper-rank.
    Enter a domain. Here, the guardian dot com.
    It reads robots dot t-x-t, then visits the site as each of fourteen crawlers.
    Five of the fourteen crawlers can read the Guardian's home page.
    G-P-T-Bot gets in. Claude-Bot is blocked by a disallow rule.
    Then it names the rule to change, and the crawlers it blocks.
    Free to run. Hyper-rank dot A-I.

Spoken words: 75

## Honesty notes

- "Five of fourteen" is printed in the UI in the same beat (the "Crawler access" line). The VO does not say the 36%, so the film never puts two different counts in play.
- Crawler tiles in the hook use each operator's official mark, labelled with the crawler name the tool tests (nominative use; sources in `tutorials/music/LICENSES.md`).
- No gate. Sequence shortened from the click to the result (about 4s live).
- Standard close: super "Free to run.", printed "Full report with a free account.", then hyperank.ai. No tool count anywhere.

## Humanizer pass

- Draft read 6 "OpenAI is in, Anthropic is out" named companies where the cards name crawlers. Now "GPTBot gets in. ClaudeBot is blocked by a Disallow rule."
- No em dashes, no banned words, no tool count, no signup line.
