# tutorial-perplexity-prompt-generator: Perplexity Prompt Generator

Status: ready for render. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: task "Find studies on four-day work weeks and productivity", context "Since 2019, peer-reviewed or government sources only". Master 16:9 (1920x1080). Project: `tutorials/perplexity-prompt-generator/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Logged-in run in BrowserOS neo (Profile 1, the hyperank.ai account, verified on chrome://version before the run, tab 30): `premium/capture/neo-workweek/neo-api.json` and the unlocked result DOM `neo-result-sec.html`. Entrance-animation `opacity:0` styles (hidden neo tab) settled to the visible state; no text changed.
- `neo-result-sec-pre.html`: the same DOM with the result's pre-wrap `<p>` retagged as `<pre class="not-prose ...">` (same classes and text; the site CSS has no prose rules) so `spans` can lift single sections.
- Gate card: the site's generic logged-out card, copied from `chatgpt-visibility-checker/premium/capture/try-canva.com/` because the anonymous run hit the rate limit. Same text on every gated tool.

| Value | Where it shows |
|---|---|
| Published in 2019 or later; peer-reviewed or government | "Inclusion criteria", first two bullets |
| News articles, blogs, magazines, think pieces ... excluded | "Exclusion criteria", first bullet |
| Ranked evidence, trials first | "Evidence standards", item 1 "Randomized or quasi-experimental trials" |
| Open in Perplexity | button under the prompt |

## Intent

Goal: a researcher or analyst writes a Perplexity prompt that tells the search what counts as a source | Platform: tool page, social | Length: 35 to 45s | Success: viewer runs their own research question.

One reader: a policy analyst who asks Perplexity a question and gets blog posts back. Belief now: "Perplexity finds good sources on its own." Belief after: "it searches for what my prompt names, so the prompt has to set the source rules; this writes them."

## Hook candidates (different categories)

1. Mechanism (picked): super "Perplexity searches *first.*", VO "Perplexity searches before it answers. Your prompt decides what it finds." From the page: it searches, then writes from what it found, and only the user message drives retrieval.
2. Stake: "Ask badly, cite blogs." Rejected: the film never shows a bad answer.
3. Question: "What counts as a source?" Rejected: abstract without the engine name, and the engine is the point here.

## Script

Runtime 44.64s

| # | VO starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.3 | Perplexity searches *first.* | Perplexity searches before it answers. Your prompt decides what it finds. |
| 2 name | 5.003 | Perplexity Prompt *Generator* | Meet the Perplexity Prompt Generator, from hyperank. |
| 3 type | 8.447 | Name what to *find.* | Name what to find, then your rules. Here, studies on four-day work weeks. |
| 4 press | 19.637 | One *press.* | It turns the task into a research brief, with sources to check. |
| 5 gate | 23.785 | *Ready.* | A free account opens the prompt. |
| 6 read | 26.141 | Your rules, *enforced.* | Your rules become criteria: twenty nineteen or later, peer-reviewed or government. |
| 7 read | 31.889 | Blogs ruled *out.* | News, blogs and think pieces are ruled out by name. |
| 8 read | 35.567 | Trials *first.* | And it ranks the evidence, starting with trials. |
| 9 read | 38.617 | Paste and *search.* | Copy it, or open it straight in Perplexity. |
| 10 close | 41.667 | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    Perplexity searches before it answers. Your prompt decides what it finds.
    Meet the Perplexity Prompt Generator, from Hyper-rank.
    Name what to find, then your rules. Here, studies on four-day work weeks.
    It turns the task into a research brief, with sources to check.
    A free account opens the prompt.
    Your rules become criteria: twenty nineteen or later, peer-reviewed or government.
    News, blogs and think pieces are ruled out by name.
    And it ranks the evidence, starting with trials.
    Copy it, or open it straight in Perplexity.
    Free to run. Hyper-rank dot A-I.

Spoken words: 92. Whisper check: "Perplexity" heard correctly in lines 1 and 2; "twenty nineteen" heard as 2019.

## Honesty notes

- "With sources to check" is the page's own framing ("something with sources to verify"), and the result tells Perplexity to verify each source's type and date.
- "Trials first" reads Evidence standards item 1, "Randomized or quasi-experimental trials".
- The film shows the prompt, not a Perplexity answer; no claim about what Perplexity then returns.
- Wait compressed, so `Sequence shortened` shows from the click to the result. Standard close. No tool count, no signup line.

## Humanizer pass

- Draft read 6 "It follows your rules exactly" judged the output; cut to what the criteria say.
- No em dashes, no banned words.
