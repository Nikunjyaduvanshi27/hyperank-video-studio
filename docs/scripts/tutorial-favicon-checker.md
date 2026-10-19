# tutorial-favicon-checker: Favicon Checker

Status: READY for the render queue. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: airbnb.com. Master 16:9 (1920x1080). Project: `tutorials/favicon-checker/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Public run (no gate): `premium/capture/try-airbnb/result-sec.html` (90/100, the Airbnb icon in Main Preview, five cards). The preview image is saved locally (`premium/assets/airbnb-favicon.png`, referenced by `capture/try-airbnb/result-sec-local.html`) so the render needs no network.
- "Red means missing or not loading" and "requests each file": the tool page's How it works text.
- Candidates tried: spotify.com (60/100), airbnb.com (90/100, three essentials load, two red). Picked Airbnb.

| Value | Where it shows |
|---|---|
| Score 90/100 | Favicon Compatibility Score |
| Icon preview | Main Preview tile |
| Standard, Apple touch, Android load | three cards with View Source |
| SVG favicon and Windows tile red | two cards with red icons, no View Source |

## Intent

Goal: a site owner sees which icon slots their site fills | Platform: tool page, social | Length: 30 to 40s | Success: viewer checks their own domain.

One reader: a founder whose tab icon works and who assumes that covers phones too. Belief now: "one favicon file is enough." Belief after: "each surface asks for its own icon, and I can see which ones load."

## Hook candidates (different categories)

1. Contrast (picked): super "One site, many *icons.*", VO "A home screen asks for a different icon than a browser tab."
2. Question: "Does your icon show on a phone?" Rejected: the result does not test a phone.
3. Number: "Five icon slots." Rejected: weaker without context.

## Script

Runtime 33.99s

| # | VO starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.3 | One site, many *icons.* | A home screen asks for a different icon than a browser tab. |
| 2 name | 4.341 | Favicon *Checker* | Meet the Favicon Checker, from hyperank. |
| 3 type | 7.316 | Just the *domain.* | Enter the homepage domain. Here, airbnb.com. |
| 4 press | 11.549 | One *press.* | It reads the page and requests each icon file. |
| 5 result | 15.057 | 90 out of *100.* | Airbnb scores ninety out of a hundred, with its icon in the preview. |
| 6 read | 19.909 | Essentials *load.* | The standard favicon, the Apple touch icon and the Android icon all load. |
| 7 read | 25.359 | Two cards *red.* | The SVG favicon and the Windows tile show red: missing, or not loading. |
| 8 close | close | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    A home screen asks for a different icon than a browser tab.
    Meet the Fave-icon Checker, from Hyper-rank.
    Enter the homepage domain. Here, Air B-n-B dot com.
    It reads the page and requests each icon file.
    Air B-n-B scores ninety out of a hundred, with its icon in the preview.
    The standard fave-icon, the Apple touch icon, and the Android icon all load.
    The S-V-G fave-icon and the Windows tile show red. Missing, or not loading.
    Free to run. Hyper-rank dot A-I.

Spoken words: 82

## Honesty notes

- "Missing, or not loading" mirrors the page's own definition of a red card; the film does not claim which of the two applies to Airbnb.
- The score is read, not interpreted.
- No gate. Sequence shortened from the click to the result.
- Standard close: super "Free to run.", printed "Full report with a free account.", then hyperank.ai. No tool count anywhere.

## Humanizer pass

- No em dashes in VO, supers or this file's own prose; no banned words, no tool count, no signup line. Dashes inside the live UI (for example the feed count line) stay as the page renders them.
- Pronunciation checked with whisper (small.en): brand names and acronyms transcribe as written.
