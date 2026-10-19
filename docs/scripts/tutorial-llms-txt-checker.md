# tutorial-llms-txt-checker: LLMs.txt Checker

Status: rendered for review. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: cloudflare.com. Master 16:9 (1920x1080). Project: `tutorials/llms-txt-checker/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Public run (no gate): `premium/capture/run-cloudflare.com/api.json` (POST `/api/tools/llms-txt-checker`, input `{"url":"cloudflare.com"}`), Domain Check DOM `result-sec.html`, Content Validator DOM `result-sec-2.html`.
- Candidates tried: vercel.com (its llms-full.txt is served as an HTML page, a confusing demo), supabase.com (both found, small file), cloudflare.com (both found, 186-line file, clean validation). Picked cloudflare.com.

| Value | Where it shows |
|---|---|
| llms.txt found, 16.8 KB; llms-full.txt found, 164.3 KB | Domain Check tab |
| 186 total, 126 content, 14 comment, 46 empty lines | Content Validator tab |
| Validation Successful, no errors, no warnings | Content Validator; `validation.errors` and `warnings` both empty |

## Intent

Goal: a site owner checks in one step whether their llms.txt is there and well formed | Platform: tool page, social | Length: 30 to 40s | Success: viewer checks their own domain.

One reader: a developer who shipped an llms.txt months ago and never looked again. Belief now: "it's probably fine." Belief after: "one run shows it's served, how big it is, and whether it validates."

## Hook candidates (different categories)

1. Question (picked): super "Is your llms.txt *there?*", VO "One plain file can point AI at the pages worth reading."
2. Command: "Check the file AI might read." Rejected: "might read" is honest but weak, and the tool page itself says no provider has confirmed reading it.
3. Proof: "Cloudflare's file, checked." Rejected: leads with the brand.

## Script

Runtime 34.14s

| # | VO starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.3 | Is your llms.txt *there?* | One plain file can point AI at the pages worth reading. |
| 2 name | 4.149 | LLMs.txt *Checker* | Meet the LLMs.txt Checker, from hyperank. |
| 3 type | 8.084 | Type a *domain.* | Enter a domain. Here, cloudflare.com. |
| 4 press | 11.272 | One *press.* | It asks the site's root for both files. |
| 5 result | 13.969 | Both *found.* | Cloudflare serves llms.txt and llms-full.txt. |
| 6 read | 19.461 | Where, and how *big.* | Each one comes with its address and its size. |
| 7 read | 22.511 | Then a line by line *read.* | The Content Validator tab counts every line of the file. |
| 8 read | 27.361 | Ready to *deploy.* | No errors and no warnings, so this file is good to go. |
| 9 close | close | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    One plain file can point A-I at the pages worth reading.
    Meet the L-L-M-s dot t-x-t Checker, from Hyper-rank.
    Enter a domain. Here, Cloudflare dot com.
    It asks the site's root for both files.
    Cloudflare serves L-L-M-s dot t-x-t, and L-L-M-s full dot t-x-t.
    Each one comes with its address and its size.
    The Content Validator tab counts every line of the file.
    No errors and no warnings, so this file is good to go.
    Free to run. Hyper-rank dot A-I.

Spoken words: 72

## Honesty notes

- The film never says AI engines read llms.txt (the tool page: no major provider has confirmed it). The hook says what the file is for.
- No gate: the run returned everything logged out.
- The Content Validator tab is a real tab in the live UI; both tab states come from the same run.
- Sequence shortened from the click to the result (about 4s live).
- Standard close: super "Free to run.", printed "Full report with a free account.", then hyperank.ai. No tool count anywhere.

## Humanizer pass

- Draft hook "AI crawlers look for one file at your root" claimed behaviour nobody has confirmed. Rewritten.
- Draft read 6 "Two files, both healthy" judged files the tool only sized. Now "Each one comes with its address and its size."
- No em dashes, no banned words, no tool count, no signup line.
