# tutorial-opengraph-viewer: Opengraph Viewer

Status: READY for the render queue. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: https://www.duolingo.com. Master 16:9 (1920x1080). Project: `tutorials/opengraph-viewer/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Public run (no gate): `premium/capture/try-duolingo/api.json`, DOM `result-sec.html`, text `result-text.txt`.
- `result-sec-local.html` is the same DOM with the two card images pointed at local copies (`og.jpg`, `tw.png`, downloaded from the og:image and twitter:image URLs the run returned), so the render needs no network.
- Candidates tried: airbnb.com (rich, but airbnb.com is already the favicon-checker input), figma.com (good card, but its description carries a long dash on screen), duolingo.com (picked: Facebook and X get different titles and different images).

| Value | Where it shows |
|---|---|
| og:title "Learn a language for free" | Facebook card, og:title row |
| twitter:title "Duolingo - Learn a language for free @duolingo" | X card, twitter:title row |
| og:image duo-08523a2.jpg, twitter:image duo200.png | the two card images, image rows |
| title "Duolingo" | Basic Meta Tags column |
| Reads HTML without running JavaScript | tool page, How to use step 2 |
| X reads twitter: tags first, falls back to Open Graph | tool page, "What are Open Graph tags?" |

## Intent

Goal: a marketer sees what a link will look like on Facebook and X before posting it | Platform: tool page, social | Length: 35 to 40s | Success: viewer pastes their own link.

One reader: a content marketer about to share a launch page. Belief now: "the card will just show my page title." Belief after: "each platform can show a different card, and I can see both first."

## Hook candidates (different categories)

1. Question (picked): super "What will your link *show?*", VO "Every link you share turns into a card."
2. Proof: "Duolingo sends two different cards." Rejected: gives the reveal away before the tool appears.
3. Mistake: "Your share card might be wrong." Rejected: a claim the run cannot back for the viewer's own site.

## Script

Runtime 37.49s

| # | Beat starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.0 | What will your link *show?* | Every link you share turns into a card. |
| 2 name | 2.61 | Opengraph *Viewer* | Meet the Opengraph Viewer, from hyperank. |
| 3 type | 5.5 | Paste any *link.* | Paste a page address. Here, Duolingo's home page. |
| 4 press | 9.14 | One *press.* | It reads the page's HTML without running scripts, like a share crawler. |
| 5 result | 13.95 | Two *previews.* | Then it draws the card for Facebook, and the card for X. |
| 6 read | 17.69 | Not the same *card.* | Duolingo sends each one a different title and a different image. |
| 7 read | 21.82 | Two title *tags.* | Facebook reads og:title. X reads its own twitter:title first. |
| 8 read | 26.63 | And a *third.* | The page's own title tag just says Duolingo. |
| 9 read | 30.05 | Every tag, *listed.* | Below, every tag the page serves, so you can check it before you share. |
| 10 close | 34.31 | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    Every link you share turns into a card.
    Meet the Open Graph Viewer, from Hyper-rank.
    Paste a page address. Here, Duolingo's home page.
    It reads the page's H-T-M-L without running scripts, like a share crawler.
    Then it draws the card for Facebook, and the card for X.
    Duolingo sends each one a different title and a different image.
    Facebook reads O-G title. X reads its own Twitter title first.
    The page's own title tag just says Duolingo.
    Below, every tag the page serves, so you can check it before you share.
    Free to run. Hyper-rank dot A-I.

## Honesty notes

- Every title, image and tag value on screen comes from the one recorded run.
- The film does not judge Duolingo's setup; it only shows that the two platforms receive different values.
- twitter:card is "summary" on this page, while the tool's preview draws both cards wide. The film stays off that point so the picture and the words never disagree.
- Sequence shortened from the click to the result.
- Standard close. No tool count, no signup line, no em dashes.
