# tutorial-llms-txt-generator: LLMs.txt Generator

Status: rendered draft for review. Pattern: `scripts/tutorial-apple-v1.md` section 3 (short tool: beats 5 and 6 merged, three read beats, no silent breath beat).
Tool: https://www.hyperank.ai/tools/ai-visibility/llms-txt-generator
Master 16:9 (1920x1080). Runtime: 32.8s (audio decides it). Project: `tutorials/llms-txt-generator/premium/`.

Claim sources:
- The recorded run: `tutorials/llms-txt-generator/premium/capture/api.json` (POST `/api/tools/llms-txt-generator`, ranAt 2026-10-04T13:00:17Z, input `{"name":"Stripe","url":"stripe.com","source":"From my sitemap"}`), and the result page text in `capture/result-main.txt`.
- The live tool page text, "How it works" and FAQ (`capture/page-text.txt`).

Values used, all checked against the run:

| Value | Where it shows |
|---|---|
| `# Stripe` as the first line | `generatedContent`, line 1 |
| `## Legal`, then `- [Legal](https://stripe.com/legal)` | `generatedContent`, lines 3 and 4 |
| 50 links across 6 sections | result card "50 links across 6 sections"; `linkCount: 50`, `sections` (Legal 45, Ssa, Climate, Connect, Connect Account, Atlas: 1 each) |
| 50 is the cap | How it works: "It caps at 50 links." Stripe's run hit it exactly. |
| `https://stripe.com/llms.txt` | Installation Instructions, step 3 |
| Free, no signup | The run returned the full file with no login and no gate (about 7s from click to result, headless browser). |

## Intent

Goal: a site owner sees one llms.txt get written for a real brand, and knows what each part of it is | Platform: tool page and social | Length: 30 to 40s | Success: viewer runs the tool.
One reader: a marketing lead at a SaaS company who has heard of llms.txt and has never opened one.
Belief now: "llms.txt is a technical file somebody else should write." Belief after: "I can draft ours in one click, then edit the titles."

## Hook candidates (different categories)

1. Command: super "Tell AI what to *read*." VO "One plain file that points A-I at the pages worth reading." (picked: works muted, opens on the tool UI on the laptop, the super and the VO say different things.)
2. Example hook from the pattern doc: VO "What to read, what to skip, who to ask. In one file." Rejected for VO: the Stripe run fills neither a skip list nor a contact, so the film would promise what it never shows.
3. Proof: super "Stripe's llms.txt, in one click." Rejected: it leads with the brand, not the tool.

## Script (32.8s)

| # | Time | Visual | Super | Narration (display) |
|---|---|---|---|---|
| 1 Hook | 0.0 to 3.7 | Wide, full laptop on the light stage, the tool page on screen. Engine tiles (ChatGPT, Gemini, Perplexity, Claude, Grok, AI Overviews) float around it, then drift off. Slow push. | Tell AI what to *read*. | One plain file that points AI at the pages worth reading. |
| 2 Name | 3.7 to 7.8 | Settle on the whole laptop. Eyebrow `hyperank / free tool`. | LLMs.txt *Generator* | Meet the LLMs.txt Generator, from hyperank. |
| 3 Input | 7.8 to 10.4 | Push in on the form. Cursor clicks Site name, types "Stripe", clicks Site URL, types "stripe.com". | Name it. Add your *domain*. | Type your site name, then your domain. |
| 4 Action | 10.4 to 13.3 | Pull back to the full laptop, page scrolls, cursor rests on "Pages to list: From my sitemap", then presses Generate LLMs.txt. Fine print `Sequence shortened`. | One *click*. | Leave the pages on your sitemap, and generate. |
| 5 Result | 13.3 to 16.8 | Push in on "Generated LLMs.txt File". The real file writes in line by line: `# Stripe`, `## Legal`, the links. Summary and install cards land under it. | Written line by *line*. | It reads the sitemap and writes the file, line by line. |
| 6 Read 1 | 16.8 to 19.2 | Pull back to the full laptop. `# Stripe` lifts out: "H1: your site name". | Your name on *top*. | Your site name becomes the title. |
| 7 Read 2 | 19.2 to 22.4 | `## Legal` lifts out ("Section: grouped by path"), then `- [Legal](https://stripe.com/legal)` ("Link title: from the URL slug"). | Grouped by *path*. | Every link lands in a section, named after its path. |
| 8 Read 3 | 22.4 to 26.0 | The summary card glows; callout "50 links, 6 sections", label "The tool caps the file at 50". | Capped at *50*. | Stripe hit the cap: fifty links across six sections. |
| 9 Payoff | 26.0 to 29.2 | Page scrolls to Installation Instructions; `https://stripe.com/llms.txt` lifts out: "Upload it to your root". | Edit, then *upload*. | Rewrite the titles, then upload it to your root. |
| 10 Close | 29.3 to 32.8 | End card over the softly blurred laptop: hyperank mark, super, tool name, `hyperank.ai`. Ends 0.6s after the last word. | Free. No *signup*. / LLMs.txt Generator / hyperank.ai | Free, with no signup. hyperank.ai. |

Spoken words: 84. Muted test (supers only): Tell AI what to read. LLMs.txt Generator. Name it. Add your domain. One click. Written line by line. Your name on top. Grouped by path. Capped at 50. Edit, then upload. Free. No signup. hyperank.ai.

### TTS lines (Kokoro, af_heart)

    One plain file that points A-I at the pages worth reading.
    Meet the L-L-M-s dot t-x-t Generator, from Hyper-rank.
    Type your site name, then your domain.
    Leave the pages on your sitemap, and generate.
    It reads the sitemap and writes the file, line by line.
    Your site name becomes the title.
    Every link lands in a section, named after its path.
    Stripe hit the cap: fifty links across six sections.
    Rewrite the titles, then upload it to your root.
    Free, with no signup. Hyper-rank dot A-I.

## Honesty notes

- "Free, with no signup" is what the run did: the file came back with no login. This tool has no gate, unlike the AI Brand Visibility Checker.
- "Rewrite the titles" comes from the tool page itself: "Edit the generated titles before you ship it" and the FAQ "Why are the link titles wrong?".
- The film never says llms.txt gets a site cited. The tool page's own FAQ says "There is no evidence that it does. No major provider has confirmed reading llms.txt." The hook says the file points AI at pages, which is what the file is for, not a result.
- The wait is shortened (about 7s live, under a second on screen), so `Sequence shortened` shows from the click to the result.
- The line-by-line build is a presentation of the real output text; the live UI shows the whole file at once. Every line on screen is verbatim from `api.json`.
- No tool count anywhere.

## Humanizer pass

Draft issues fixed:
- Hook VO draft "What to read, what to skip, who to ask. In one file." was three items, and two of them never appear in the Stripe file. Replaced.
- Beat 5 draft super "Written in seconds." implied a timing the film shortens. Now "Written line by line.", which is what the viewer sees.
- Beat 8 draft "Fifty links, the tool's cap." was a fragment after two fragments. Now a full sentence that names Stripe, which is the one detail only this run has.
Audit: run of short supers is the Apple register on purpose; the narration under them is full sentences of 6 to 11 words. No em dashes, no exclamation marks, no banned words. Nothing added that is not in the run or the page.
