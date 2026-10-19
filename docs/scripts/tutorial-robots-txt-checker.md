# tutorial-robots-txt-checker: Robots.txt Checker

Status: rendered for review. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: https://github.com/search. Master 16:9 (1920x1080). Project: `tutorials/robots-txt-checker/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Public run (no gate): `premium/capture/try-github.com_search/api.json` (`{"isBlocked": true}`) and the result DOM `result-sec.html` (the fetched robots.txt and the verdict "This URL is BLOCKED by robots.txt.").
- Candidates tried: https://github.com/search (blocked; the file opens with a group for GPTBot, OAI-SearchBot, ClaudeBot, anthropic-ai, PerplexityBot), https://www.airbnb.com/account-settings (blocked, but the file opens with 25 lines of ASCII art), https://www.ikea.com/us/en/ (not blocked, ASCII-art logo first). Picked GitHub.

| Value | Where it shows |
|---|---|
| The robots.txt as GitHub serves it | "robots.txt content:" box |
| The AI crawler group (5 User-agent lines) | first lines of that file |
| Verdict BLOCKED | "Blocked Status: This URL is BLOCKED by robots.txt." |

## Intent

Goal: an SEO lead tests one URL against a live robots.txt before trusting a crawler can reach it | Platform: tool page, social | Length: 30 to 40s | Success: viewer pastes their own page.

One reader: a growth marketer who assumes a public page is crawlable. Belief now: "if I can open it, bots can." Belief after: "one file decides, and I can test any page against it."

## Hook candidates (different categories)

1. Question (picked, from the pattern doc): super "Allowed, or *blocked?*", VO "One small text file decides which pages crawlers may fetch."
2. Pattern-doc VO "Paste any page. See which rule decides." Rejected: the result shows the file and the verdict, not the deciding rule, so the line would promise what the film never shows.
3. Stake: "Your page might be invisible to bots." Rejected: vague and fear-led.

## Script

Runtime 35.87s

| # | VO starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.3 | Allowed, or *blocked?* | One small text file decides which pages crawlers may fetch. |
| 2 name | 4.533 | Robots.txt *Checker* | Meet the Robots.txt Checker, from hyperank. |
| 3 type | 8.276 | Paste any *page.* | Paste a full page address. Here, GitHub's search page. |
| 4 press | 12.104 | One *press.* | It fetches the site's robots.txt and tests your page against it. |
| 5 result | 16.999 | The real *file.* | First, the file itself, exactly as GitHub serves it. |
| 6 read | 20.784 | Rules for AI *bots.* | GitHub opens with a group of rules just for AI crawlers. |
| 7 read | 24.655 | *Blocked.* | Then the verdict. This page is blocked by robots.txt. |
| 8 read | 29.251 | Check before you *ship.* | Test any page before you count on a crawler reaching it. |
| 9 close | close | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    One small text file decides which pages crawlers may fetch.
    Meet the Robots dot t-x-t Checker, from Hyper-rank.
    Paste a full page address. Here, GitHub's search page.
    It fetches the site's robots dot t-x-t, and tests your page against it.
    First, the file itself, exactly as GitHub serves it.
    GitHub opens with a group of rules just for A-I crawlers.
    Then the verdict. This page is blocked by robots dot t-x-t.
    Test any page before you count on a crawler reaching it.
    Free to run. Hyper-rank dot A-I.

Spoken words: 82

## Honesty notes

- The tool page tagline mentions "which rule", but the result only shows the file and the verdict, so the film never names a deciding rule.
- The AI crawler group is called out as text in GitHub's file, not as a per-bot verdict.
- No gate. Sequence shortened from the click to the result (about 4s live).
- Standard close: super "Free to run.", printed "Full report with a free account.", then hyperank.ai. No tool count anywhere.

## Humanizer pass

- Draft read 7 "GitHub blocks search from every crawler" overreached: the verdict is for the User-agent: * group. The VO now reads the UI's own sentence.
- No em dashes, no banned words, no tool count, no signup line.
