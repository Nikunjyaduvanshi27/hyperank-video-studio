# tutorial-llms-txt-validator: LLMs.txt Validator

Status: READY for the render queue. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: supabase.com. Master 16:9 (1920x1080). Project: `tutorials/llms-txt-validator/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Result: logged-in run through BrowserOS neo (Profile 1, hyperank.ai), `premium/capture/neo-supabase.com/neo-result-sec.html`, `neo-result-text.txt`, `neo-api.json`. The tool has no gate; neo was used because the three anonymous runs for this tool were spent.
- Anonymous candidates: vercel.com (100/100, a clean pass, too close to the sibling LLMs.txt Checker video), anthropic.com (no file at the root, HTTP 404), shopify.com (99/100 with one dead link; dropped because ai-visibility-report already uses shopify.com).
- Distinct from the sibling `llms-txt-checker` video (cloudflare.com, "is the file there"): this one is about following the format, and ends on a named fix.

| Value | Where it shows |
|---|---|
| llms.txt validation passed with warnings, 85/100 | Verdict bar |
| H1 title "Supabase Docs" present | Validation Summary, 2. H1 Title |
| Missing quote block with project summary | Validation Summary, 3. Quote Block |
| Found 42 links in file lists; All links are accessible | Validation Details |
| Add a blockquote to briefly summarize your project | Improvement Suggestions |

## Intent

Goal: a site owner learns that a live llms.txt can still miss part of the format | Platform: tool page, social | Length: 30 to 40s | Success: viewer validates their own file.

One reader: a developer who shipped an llms.txt last quarter and never looked at it again. Belief now: "the file is live, so it is done." Belief after: "the validator shows which parts of the format are missing, and the fix can be one line."

## Hook candidates (different categories)

1. Question (picked): super "Is it built *right?*", VO "Having an llms.txt is one thing. Following the format is another."
2. Contrast: "Found is not valid." Rejected: this run passes, so the line oversells the failure.
3. Number: "85 out of 100." Rejected for the hook: the score belongs to Supabase, not the viewer.

## Script

Runtime 35.59s

| # | VO starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.3 | Is it built *right?* | Having an llms.txt is one thing. Following the format is another. |
| 2 name | 5.707 | LLMs.txt *Validator* | Meet the LLMs.txt Validator, from hyperank. |
| 3 type | 9.94 | Give it a *site.* | Enter a website, or paste the file. Here, supabase.com. |
| 4 press | 14.301 | One *press.* | It fetches the file, checks the structure, then tests every link. |
| 5 result | 18.364 | Passed, with *warnings.* | It passes with warnings, at 85 out of 100. |
| 6 read | 22.085 | No summary *line.* | The H1 title is there. The summary quote block is not. |
| 7 read | 26.276 | Every link *responds.* | All 42 links in the file respond. |
| 8 read | 29.326 | One line to *add.* | The fix: add a one-line summary as a blockquote. |
| 9 close | 32.621 | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    Having an L-L-M-s dot t-x-t is one thing. Following the format is another.
    Meet the L-L-M-s dot t-x-t Validator, from Hyper-rank.
    Enter a website, or paste the file. Here, Soopa-base dot com.
    It fetches the file, checks the structure, then tests every link.
    It passes with warnings, at eighty-five out of a hundred.
    The H-1 title is there. The summary quote block is not.
    All forty-two links in the file respond.
    The fix: add a one-line summary as a blockquote.
    Free to run. Hyper-rank dot A-I.

Spoken words: 79

## Honesty notes

- The only score on screen is 85/100. The link count (42) is a different unit and is introduced as a count.
- The file checked is the one served at supabase.com/llms.txt, titled "Supabase Docs" in its H1.
- No gate. Sequence shortened from the click to the result.
- Standard close: super "Free to run.", printed "Full report with a free account.", then hyperank.ai. No tool count anywhere.

## Humanizer pass

- Captions keep digits (85, 42); TTS spells them. Whisper heard "supebase.com" for the respelled brand, close enough to Supabase; flag if the founder hears it differently.
- No em dashes, no banned words, no tool count, no signup line.
