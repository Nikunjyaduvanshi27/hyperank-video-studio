# tutorial-404-page-checker: 404 Page Checker

Status: prepared for the render queue. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: https://norvig.com/21-days.html (Peter Norvig, "Teach Yourself Programming in Ten Years"). Master 16:9 (1920x1080). Project: `tutorials/404-page-checker/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Public run (no gate): `premium/capture/try-21days/api.json` (POST `/api/tools/404-page-checker`) and `result-sec.html`. The table shows 60 rows: 41 at 200 OK, 2 at 404, 3 at 403, 14 No answer.
- Candidates: norvig.com home (`try-norvig`, 44 links, its one 404 is the last row, below the table's 600px scroll box, so it cannot be shown); joelonsoftware.com (`try-joel`, the Stack Overflow rows return 403 to the checker, a bot block rather than a dead page, and the No answer rows sit below the fold). Picked 21-days.html: its red rows are rows 2, 3 and 5, all inside the visible box.
- "Up to sixty links" and "open the no-answer links yourself before you decide": the tool page's how-it-works copy ("open any 403 or No answer link in your browser before deciding").

| Value | Where it shows |
|---|---|
| We found 60 links on the page | Result header |
| www.ccs.neu.edu/home/matthias/HtDP2e/index.html, "How to Design Programs", 404 | Row 2 |
| abstrusegoose.com/249, "their take", No answer | Row 3 |
| www-pu.informatik.uni-tuebingen.de/.../epigrams.html, "Alan Perlis", No answer | Row 5 |

## Intent

Goal: a site owner sees the status code behind every link on a page, not just a dead list | Platform: tool page, social | Length: 35 to 40s | Success: viewer runs a long-lived page of their own.

One reader: a developer-blog author whose most-read post is ten years old. Belief now: "a broken link is a broken link." Belief after: "a 404 means remove or update it; a no-answer means look first."

## Hook candidates (different categories)

1. Question (picked): super "What did it *return?*", VO "A dead link fails quietly. Its status code tells you why."
2. Contrast: "Green loads. Red tells you why." Rejected: needs the table on screen.
3. Story: "A classic essay, still read, still linking out." Rejected: spends the hook on the demo, not the viewer.

## Script

Runtime 37.53s

| # | Beat start (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.0 | What did it *return?* | A dead link fails quietly. Its status code tells you why. |
| 2 name | 4.19 | 404 Page *Checker* | Meet the 404 Page Checker, from hyperank. |
| 3 type | 7.39 | Any *page.* | Paste a page. Here, Peter Norvig's essay, Teach Yourself Programming in Ten Years. |
| 4 press | 13.08 | One *press.* | It requests up to sixty links, and records what each one returns. |
| 5 result | 17.23 | Sixty *links.* | Sixty links, each with its anchor text. Green ones loaded. |
| 6 read | 21.31 | A real *404.* | The link to How to Design Programs returns a 404. |
| 7 read | 25.33 | No *answer.* | Two more servers never answered at all. |
| 8 read | 28.38 | Fix the *red.* | Update or remove the 404s. Open the no-answer links yourself before you decide. |
| 9 close | 34.34 | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    A dead link fails quietly. Its status code tells you why.
    Meet the four-oh-four Page Checker, from Hyper-rank.
    Paste a page. Here, Peter Norvig's essay, Teach Yourself Programming in Ten Years.
    It requests up to sixty links, and records what each one returns.
    Sixty links, each with its anchor text. Green ones loaded.
    The link to How to Design Programs returns a four-oh-four.
    Two more servers never answered at all.
    Update or remove the four-oh-fours. Open the no-answer links yourself before you decide.
    Free to run. Hyper-rank dot A-I.

Whisper check: vo-02, 03, 06, 08 transcribe as written (Norvig, 404, no answer).

## Honesty notes

- "Two more" refers to the two No answer rows lifted on screen (rows 3 and 5), not to the page total. The VO never states how many rows are red, because the table never prints that count.
- "Sixty links" matches the printed "We found 60 links on the page"; the checker caps at 60.
- No gate. Sequence shortened from the click to the result (about 17s live).
- Distinct from the Broken Link Checker video (CERN, the dead-only list): this one is the per-link status table.
- Standard close. No tool count, no signup line, no em dashes.
