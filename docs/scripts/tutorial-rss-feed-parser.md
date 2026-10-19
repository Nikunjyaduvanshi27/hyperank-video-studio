# tutorial-rss-feed-parser: RSS Feed Parser

Status: READY for the render queue. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: https://www.nasa.gov/feed/. Master 16:9 (1920x1080). Project: `tutorials/rss-feed-parser/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Public run (no gate): `premium/capture/try-nasa/result-sec.html` and `result-text.txt` (the feed name NASA and "10 items", each item's URL, title and date, the Copy All URLs button).
- Copy All URLs behaviour ("one per line") and the crawler and spreadsheet use: the tool page's own How to use text (`page-text.txt`).
- Candidates tried: https://www.nasa.gov/feed/ only (10 items, real current headlines, neutral publisher).

| Value | Where it shows |
|---|---|
| Feed name and item count | the feed name NASA and "10 items" under Parsed Feed Items |
| One item: link, title, date | first card, Curiosity, Wednesday, October 7, 2026 at 10:30 PM |
| Artemis II and supernova remnant items | third and fourth cards |
| Copy All URLs | button beside the header |

## Intent

Goal: a content or SEO lead turns a feed into a clean list of URLs | Platform: tool page, social | Length: 30 to 40s | Success: viewer pastes their own feed.

One reader: a marketer who wants every post URL from a blog to run through a checker. Belief now: "I have to copy links one by one." Belief after: "the feed already lists them, and one press lists them for me."

## Hook candidates (different categories)

1. Plain fact (picked): super "Every new *post.*", VO "A feed lists every new post, with its link and its date."
2. Question: "Where is your feed?" Rejected: the film does not show feed discovery.
3. Stake: "Your posts, one copy away." Rejected: vague.

## Script

Runtime 35.03s

| # | VO starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.3 | Every new *post.* | A feed lists every new post, with its link and its date. |
| 2 name | 4.064 | RSS Feed *Parser* | Meet the RSS Feed Parser, from hyperank. |
| 3 type | 7.316 | Paste the *feed.* | Paste the feed's own address. Here, NASA's feed. |
| 4 press | 11.161 | One *press.* | It reads the XML and lists every item. |
| 5 result | 14.349 | Ten *items.* | NASA's feed comes back with ten items. |
| 6 read | 17.549 | Link, title, *date.* | Each item shows its link, its headline and when it went out. |
| 7 read | 21.42 | Real *headlines.* | The Artemis II crew, a supernova remnant. Straight from the feed. |
| 8 read | 25.824 | Every link at *once.* | Copy All URLs copies every link, one per line, ready for a crawler or a spreadsheet. |
| 9 close | close | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    A feed lists every new post, with its link and its date.
    Meet the R-S-S Feed Parser, from Hyper-rank.
    Paste the feed's own address. Here, NASA's feed.
    It reads the X-M-L, and lists every item.
    NASA's feed comes back with ten items.
    Each item shows its link, its headline and when it went out.
    The Artemis two crew, a supernova remnant. Straight from the feed.
    Copy All U-R-L-s copies every link, one per line, ready for a crawler or a spreadsheet.
    Free to run. Hyper-rank dot A-I.

Spoken words: 87

## Honesty notes

- Dates are shown as the tool rendered them during the capture; the film never states a time zone.
- The headlines are NASA's real feed items at capture time, named as they appear.
- "One per line" and the crawler and spreadsheet use come from the tool page's How to use text, not from a demo of pasting.
- No gate. Sequence shortened from the click to the result.
- Standard close: super "Free to run.", printed "Full report with a free account.", then hyperank.ai. No tool count anywhere.

## Humanizer pass

- No em dashes in VO, supers or this file's own prose; no banned words, no tool count, no signup line. Dashes inside the live UI (for example the feed count line) stay as the page renders them.
- Pronunciation checked with whisper (small.en): brand names and acronyms transcribe as written.
