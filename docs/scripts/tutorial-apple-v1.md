# tutorial-apple-v1: AI Brand Visibility Checker

Status: draft v1. Script, supers and beat plan only. Rendering belongs to the `hyperframes` pipeline.
Tool: https://www.hyperank.ai/tools/ai-visibility/ai-brand-visibility-checker
Master 16:9 (1920x1080), cut 9:16. Target runtime: about 43s (audio decides the final number).

Claim sources:
- `brief/product-brief.md` (B1 to B8 below point to its sections).
- The recorded run: `tutorials/ai-brand-visibility-checker/recording/api.json` (ranAt 2026-10-03T14:20Z) and the crops in `recording/result/*.png` and `recording/fragments/*.png`.
- Live pages re-read on 2026-10-04 (see "Drift found" at the end; it changes the close).

---

## 0. The idea in one line

The product is the hero. Notion is only the input. The viewer watches hyperank's own UI do the work: one field, one press, a report that builds itself. The film sells the experience of using hyperank, and the result is the proof that the experience works.

Values used, all checked against `api.json` and the crops:

| Value | Where it shows |
|---|---|
| Score 60 | `stats.png` ("Overall AI Visibility Score"), `platform.png` |
| ChatGPT named Notion in 3 of 5 | `platform.png`: "ChatGPT, 3 mentions in 5 answers" |
| 6 mentions across 8 answers | `stats.png`: "Total AI Mentions, across 8 answers" (5 buying questions plus 3 that name the brand) |
| Slack leads | `insights.png`: "Slack leads the answers it did not name you in, with 5 mentions". Note: Trello also has 5 (`competitors.png`); Slack is listed first. Say "Slack leads" only because the UI says it. |
| Five buying questions, without the brand name | `howto.png` step 2 and the live page |

---

## 1. Hook options (first 2 to 3 seconds)

Every option opens on hyperank's UI, already moving. No logo sting, no fade from black.

| # | Angle | Super (on screen) | Narration | Frame 1 |
|---|---|---|---|---|
| 1 | Question | Does AI name you? | Your buyers already asked. | Macro on the empty Website field of the tool, cursor blinking, the violet Analyze visibility button soft in the foreground. Slow push in. |
| 2 | Tension | Asked. Not named. | A buyer asked. Your name wasn't in the answer. | Macro on the red mark beside "How can I automate repetitive tasks in my team?" in the report's question list. Brand name cropped out of frame. |
| 3 | Reveal | One domain in. The answer out. | Type a domain. Read what A-I says back. | Match cut: "notion.com" finishes typing, hard cut on the last key to "AI Visibility Report for notion.com" landing. |
| 4 | Outcome | See who AI recommends. | The names A-I gives your buyers, in one report. | The Competitive Landscape list rising into frame, "Your Brand" row pinned on top. |
| 5 | Contrarian | Rank first. Still not named. | You can rank first and still be left out of the answer. | Report question list, slow lateral drift across green checks and red marks. Line adapted from B2: "You can rank first and still not be in the answer". |
| 6 | Product-first | AI Brand Visibility Checker | Meet the A-I Brand Visibility Checker. | The tool title set in hyperank's display type on warm paper, the Analyze visibility button glowing on beneath it. |

### Ranking

1. **Question (recommended).** It works muted: four words, readable in under a second, and the viewer answers it about themselves. The narration adds a stake the super leaves out ("already asked"), so sound and text work together rather than repeating. Frame 1 is hyperank's own input field, so the product is the first thing anyone sees, which is the founder's brief. It also sets up the whole film: the question gets asked at 0s and answered by the report at 20s.
2. **Tension.** Stops the scroll hardest, but it opens on a result, so the film starts by being about one brand's gap rather than the tool. Best as the A/B variant for feed placements.
3. **Reveal.** Calm and very Apple, and it is about the product. It is abstract with the sound off, though, and the viewer's stake comes late.
4. **Outcome.** A strong reason to watch, but it gives away the payoff beat before the walkthrough.
5. **Contrarian.** Sharp, but it needs an SEO frame of reference, which tool-page visitors may not have. It also argues a point the film never shows.
6. **Product-first.** Right for the tool page itself, where the viewer already chose the tool. Too quiet for a cold feed. Use it as the name card in beat 2 instead.

---

## 2. Full script (about 43s)

Register: Apple feature walkthrough. Few words, declarative, unhurried. One idea per beat. The super carries the story with the sound off. The narration adds what the super leaves out.
Voice direction: calm and certain, a little warmth, no announcer lift. A short pause before every number.
Music: one minimal underscore (soft pulse or felt piano), ducked under voice, swelling only in beat 10, where nobody speaks.
Supers: hyperank display serif (Instrument Serif), ink `#1f1e1b` on paper `#f0eee9`. One word per super may go violet italic `#5e4bf6`, never more. Mono eyebrow (JetBrains Mono) only where noted.

| # | Time | Visual (hyperank UI) | Super | Narration (display) | SFX |
|---|---|---|---|---|---|
| 1 | 0.0 to 2.5 | Macro on the empty Website field, cursor blinking. Violet Analyze visibility button soft-focus below. Slow push in. | Does AI name *you*? | Your buyers already asked. | 1s of near silence, then one soft low tone as the super lands. |
| 2 | 2.5 to 6.0 | Pull back from the field to the whole tool card: title "AI Brand Visibility Checker", description, form on its white card with the soft shadow. Camera settles at a slight tilt, like a product shot. | AI Brand Visibility *Checker* (mono eyebrow above: `hyperank / free tool`) | Meet the AI Brand Visibility Checker, from hyperank. | Air move on the pull-back. Underscore enters, quiet. |
| 3 | 6.0 to 9.5 | Dive to the input. "notion.com" types in at a human pace. Helper line under the field stays readable. | Type your *domain*. | All it needs is your domain. | One soft click on the field, then real key taps, quiet (no looped typing bed). |
| 4 | 9.5 to 12.5 | Macro on Analyze visibility. The cursor presses, the button gives a little, the violet glow pulses once, the button enters its running state. | One *press*. | It reads your site and works out your category. | Soft click, tight to the press frame. |
| 5 | 12.5 to 17.0 | The running state, speed-ramped (the real wait is about 22s, `events.json` running 9.99s to ready 31.56s). [GRAPHIC] Above the card, the five real buying questions from this run fade in one at a time as ghost text, then clear. Small mono fine print bottom-left: `Sequence shortened`. | Five buying *questions*. | Then it writes five buying questions without your name, and asks each one. | Low pulse under the ramp. No whoosh. |
| 6 | 17.0 to 20.0 | "Your results are ready" card. The cursor moves to the free signup button and clicks. The blurred report behind it sharpens into focus. | *Ready.* | A free account opens the full report. | Click, then one clean glass tone as the blur clears. |
| 7 | 20.0 to 24.0 | "AI Visibility Report for notion.com" lands. Camera settles on the score card (60), then drifts to the Platform Breakdown card: "ChatGPT, 3 mentions in 5 answers". Numbers appear exactly as the UI renders them, with no count-up. | A score with *receipts*. | Sixty. ChatGPT named Notion in three of five. | Silence under "Sixty", then one soft tick when the platform card arrives. |
| 8 | 24.0 to 27.5 | Industry-Specific Prompts. Slow vertical drift down rows 3 to 5, where the green checks land one by one. | Which answers name *you*. | Green checks count toward the score. | Three tiny ticks, one per check. |
| 9 | 27.5 to 31.0 | Competitive Landscape. "notion.com, Your Brand" pinned on top, Slack and Trello below. Then Key Insights fades in under it with "Slack leads the answers it did not name you in". | Who got recommended *instead*. | In this run, Slack leads. | Underscore steps up one note. |
| 10 | 31.0 to 34.0 | Growth Opportunities. The six cards cascade in, two per row, gently. No narration. | Where to *start*. | (none) | Music swell, the only one in the film. |
| 11 | 34.0 to 38.0 | Long pull back. The whole report drifts up as one tall page and settles, full report in frame, slightly out of focus. | Before your buyer *does*. | Before your next buyer asks AI about you, ask it yourself. | Music drops back. A held breath before the line. |
| 12 | 38.0 to 43.0 | Report fades to paper. hyperank H mark and wordmark. Under it the super, then the small honest line, then `hyperank.ai`. Hold about 2s after the voice ends. | Free to *run*. Small line: `Full report with a free account.` Then: `hyperank.ai` | Free to run. hyperank.ai. | Final soft tone on the URL, then silence. |

Spoken words: 79. That is about 32s of speech at an unhurried pace, plus the silent beat 10 and the end hold, for about 43s.

Beat 11's line is adapted from the homepage closing CTA, which reads in full "Before your next buyer asks AI about you, ask AI about yourself." (B5). Beat 9's super is B3 verbatim ("Who got recommended instead"). Beat 7's super echoes B3, "Not a score with no receipts."

### Why each beat holds attention

- Beats 1 to 2: the question is asked, then the product is named. Nobody leaves before the product has been on screen.
- Beats 3 to 6: three actions, each with one super, and the screen changes every 3 to 4 seconds. Beat 6 is the reveal, the moment the answer arrives.
- Beat 7 answers the hook's question with a number the viewer can see.
- Beat 10 is the pattern interrupt: the voice stops and the music lifts, just as attention would start to dip at around 30s.
- Beat 12 ends on one action (the URL) with no thanks and no list.

### TTS lines (Kokoro)

Spoken text only. "AI" is written as "A-I" and the brand as "Hyper-rank". Listen-test lines 2 and 12 first.

Line 1 (beat 1)

    Your buyers already asked.

Line 2 (beat 2)

    Meet the A-I Brand Visibility Checker, from Hyper-rank.

Line 3 (beat 3)

    All it needs is your domain.

Line 4 (beat 4)

    It reads your site and works out your category.

Line 5 (beat 5)

    Then it writes five buying questions without your name, and asks each one.

Line 6 (beat 6)

    A free account opens the full report.

Line 7 (beat 7)

    Sixty. ChatGPT named Notion in three of five.

Line 8 (beat 8)

    Green checks count toward the score.

Line 9 (beat 9)

    In this run, Slack leads.

Line 10 (beat 11)

    Before your next buyer asks A-I about you, ask it yourself.

Line 11 (beat 12)

    Free to run. Hyper-rank dot A-I.

### The close, and why it says what it says

- "Free to run" is true: the recording ran the check with no login (`events.json`: submit at 9.15s, results ready at 31.56s, before any signup).
- The report itself sits behind a free signup (`howto.png` step 3: "The check has already run; a free account reveals it."). Beat 6 says so out loud, and beat 12 prints it on the end card. Without that line, "Free to run" would imply something the UI does not do.
- The film does NOT use "No signup. No email." That line (B3 FAQ) describes the homepage brand check, not this tool page.
- The film carries no tool count. See "Drift found".

### 9:16 cut

- Same 12 beats. Supers go in the upper-middle safe area. Leave the bottom band and the right rail clear for platform UI, and take those safe zones from each platform's current published spec at cut time.
- Beats 7 to 10: crop to the single card (score, rows, list, cards) rather than the full report width.
- Beat 8: crop to rows 3 to 5 only (see gate 4).

### Quality gates the edit must pass

1. Every on-screen number comes from this run's `api.json` and is visible in the UI in the same beat. No count-ups, no mock dashboard numbers from the homepage (B7).
2. The fine print `Sequence shortened` is visible for the whole of beat 5. The real wait is about 22s, and the film must not imply it is instant.
3. The beat 5 ghost questions are the five real `topPrompts.query` strings from `api.json`, verbatim. They are a [GRAPHIC], so they stay clearly separate from the UI card.
4. Keep the row 1 close-up out of frame in beat 8. It shows a red mark beside "Notion is mentioned as a tool with customization and scalability", which reads as a contradiction without the named/described/absent explanation. Rows 3 to 5 are clean.
5. No super longer than 6 words. One violet italic word per super at most.
6. The free signup button keeps its UI label as rendered. It never becomes a super.
7. No em dashes, no exclamation marks, none of the banned words (list in section 3).
8. Voice first in the mix, music ducked under it. Loudness normalised to each destination's published target.
9. `design-critic` pass on a contact sheet before a high-quality render. Nothing publishes. The render goes to review first.

---

## 3. The reusable pattern (every free tool)

### Hook formula

`Frame 1 = the tool's own input, at macro, already moving` + `Super = the viewer's question or stake, 2 to 5 words` + `Narration = one line that adds what the super leaves out`.

The super and the narration never say the same thing. The one exception is the product name card in beat 2, where saying the name while it appears is the point.

### Beat structure (scales from 30s to 45s)

| Beat | Job | Share of runtime |
|---|---|---|
| 1 Hook | Question or stake, on the tool's UI | 0 to 2.5s, fixed |
| 2 Name card | Tool name in hyperank type, pull back to the whole card | about 8% |
| 3 Input | The one thing the user types or pastes | about 8% |
| 4 Action | The button press, macro | about 7% |
| 5 Working | Ramped wait, "Sequence shortened" if compressed | about 10% |
| 6 Reveal | The result lands, or the gate opens | about 7% |
| 7 to 9 Read | Two or three parts of the result, one idea per beat | about 30% |
| 10 Breath | Super only, music lift, no voice | about 7% |
| 11 Payoff | What the viewer now knows or has, said as a benefit | about 9% |
| 12 Close | Accurate free line, then hyperank.ai, hold 2s | about 12% |

Short tools (generators, viewers) merge beats 5 and 6 and keep two read beats. That lands near 30s.

### Super rules

- 2 to 6 words. Sentence case. A period when it is a statement, a question mark when it is a question.
- One idea per super, one super per beat, on screen at least 1.5s.
- Benefit or plain action, never a feature list. "Type your domain", not "Domain input field".
- At most one violet italic word, the word the beat turns on.
- The muted test: read only the supers top to bottom. They must tell the whole story.
- Numbers in a super appear only if the UI shows the same number in that beat.

### Narration rules

- 75 to 95 spoken words for 40s. Every sentence 14 words or fewer.
- Declarative. Present tense. "It writes", not "it will write".
- Vary the rhythm. No more than two fragments in a row. A full sentence between short ones keeps it from sounding like a trailer.
- TTS spelling: "A-I", "Hyper-rank", "dot A-I", file names spelled out ("robots dot t-x-t").
- Banned: unlock, supercharge, seamless, game-changer, revolutionize, elevate, leverage, in today's world, plus exclamation marks and em dashes. Also avoid "powerful", "instantly", "effortless" and "AI-powered".

### Honesty rules per tool (check before scripting)

- Record a real run first. Every number and string comes from that run's API response and crops.
- Check the gate: does the result need an account? If so, say it once in the walkthrough and print it on the end card.
- Check the time: if the wait is ramped, show `Sequence shortened`.
- Do not print a tool count until the live /tools page has been read on the day of the render (see "Drift found").

### Three example hooks

| Tool | Super | Narration | Frame 1 | Source line |
|---|---|---|---|---|
| llms-txt-generator | Tell AI what to *read*. | What to read, what to skip, who to ask. In one file. | Macro on the "Pages to list" field filling with paths. | Live page: "Write an llms.txt for your site: what to read, what to skip, who to ask." |
| robots-txt-checker | Allowed, or *blocked*? | Paste any page. See which rule decides. | A full page URL pasting into "Page or site URL". | Live page: "test one URL against it: allowed, or blocked by which rule." |
| twitter-engagement-rate-calculator | BLOCKED: page returns 404 (checked 2026-10-04). No hook written, because the tool is gone. | | | |
| ai-bot-crawler-checker (replacement) | Which AI bots get *in*? | GPTBot, ClaudeBot and the rest. See which ones your site allows. | Macro on the Website field, a domain typing in. | Live page: "Which AI crawlers your site allows and which it blocks: GPTBot, ClaudeBot and the rest." |

The gate status of the llms.txt and robots.txt tools has not been confirmed with a recorded run yet. Record before scripting the close.

---

## 4. Humanizer pass (draft, audit, final)

Draft issues found and fixed:

- Beat 3's first draft was "One field. Just your homepage.", which made three fragments in a row after beat 2 (pattern 31, staccato drama). It is now one full sentence: "All it needs is your domain."
- The original close repeated "free account" twice in 5 seconds. Now the walkthrough says it (beat 6) and the end card prints it, with no third mention in the narration.
- Beat 9's draft "Here, Slack leads." left "here" unclear. It is now "In this run, Slack leads.", which also scopes the claim to one run.
- Beat 11's draft "Now you know what AI tells your buyers" overclaimed. One run asked one model five questions. Replaced with the homepage's own line.
- Beat 7's draft super "Named in 3 of 5" repeated the narration word for word. Replaced with "A score with receipts", and the UI card carries the 3 of 5 for muted viewers.

Audit questions:

- What still reads as AI-made? The run of one-word supers ("Ready.", "One press.") follows a pattern on purpose, because that is the Apple register. It is capped at two short supers in a row, and the narration under them uses full sentences.
- Was anything added that is not in the sources? No. Every number traces to `api.json` and the crops, and every borrowed line traces to B2, B3 or B5 or to the live tool pages. Em dash check: none. Banned word check: none outside the banned-word list itself.

---

## Drift found (needs a decision before render)

- **Tool count.** The brief (scraped 2026-10-03) says "88 of 88 tools". On 2026-10-04 the live /tools page reads "54 of 54 tools" (AI Visibility 28, Technical SEO 16, Sitemap 7, Indexing 3), and the homepage FAQ reads "Plus fifty-one free tools." The X (Twitter) and Instagram tool pages return 404. The current `tutorial.json` outro ("Explore all eighty-eight free tools") is now wrong, and the 34 X and Instagram rows in `tutorials/tools.csv` point at dead pages. This script carries no count for that reason.
- **Helper text.** The recorded form says "Your domain on its own, such as hyperank.ai. Enter the homepage, not a deeper page." The live page now says "The domain on its own. Any path you add is ignored". The narration ("All it needs is your domain") is true under both versions, but the footage is from the old UI. Re-record if the film should match the live page frame for frame.
