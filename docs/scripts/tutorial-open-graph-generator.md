# tutorial-open-graph-generator: Open Graph Generator

Status: READY for the render queue. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: Title "Yosemite National Park", Description "Granite cliffs, waterfalls and giant sequoias.", Canonical URL "nps.gov/yose". Master 16:9 (1920x1080). Project: `tutorials/open-graph-generator/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Public run (no gate): `premium/capture/try-yosemite/api.json` (POST `/api/tools/open-graph-generator`, `ok: true`), DOM `result-sec.html`.
- Title and URL are the National Park Service's own (nps.gov/yose, og:title "Yosemite National Park (U.S. National Park Service)", shortened). The description is a short line written for the demo; all three facts in it are true of Yosemite.
- Candidates: MDN's HTML page (worked, but about 200 typed characters, too long to type on screen), Yosemite (picked, 80 characters).

| Value | Where it shows |
|---|---|
| Facebook and Twitter previews, both with an empty "Image Preview" slot | Preview card |
| title, description, og:title, og:description, og:url (https added), og:type, twitter:card summary, twitter:title, twitter:description | Open Graph Meta Tags block |
| Copy Code button | Open Graph Meta Tags header |
| Tags belong in the head of the HTML the server sends | tool page, "Where do Open Graph meta tags go?" |

## Intent

Goal: a site owner writes correct share tags for one page without hand-typing meta markup | Platform: tool page, social | Length: 35 to 40s | Success: viewer fills the form for their own page.

One reader: a small-site owner whose links post as a bare URL. Belief now: "share cards need a developer." Belief after: "three fields give me the tags and a preview."

## Hook candidates (different categories)

1. Command (picked): super "Write your share *card.*", VO "A shared link shows whatever your tags tell it to."
2. Question: "What will your link show?" Rejected: that is the Opengraph Viewer's hook in this batch.
3. Proof: "Three fields, nine tags." Rejected: counts the tags, and the count changes with optional fields.

## Script

Runtime 38.44s

| # | Beat starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.0 | Write your share *card.* | A shared link shows whatever your tags tell it to. |
| 2 name | 3.18 | Open Graph *Generator* | Meet the Open Graph Generator, from hyperank. |
| 3 type | 6.29 | Three *fields.* | A title, one line of description, and the page address. |
| 4 press | 15.95 | One *press.* | It writes the tags from exactly what you typed. |
| 5 result | 18.9 | Both *previews.* | First, the card Facebook would show, and the card for X. |
| 6 read | 22.66 | No image *yet.* | No image address given, so both image slots stay empty. |
| 7 read | 26.62 | Ready to *paste.* | Below, the whole block: title, description, og and twitter tags. |
| 8 read | 31.28 | Copy, then *paste.* | Copy Code takes it all, for the head of your page's HTML. |
| 9 close | 35.26 | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    A shared link shows whatever your tags tell it to.
    Meet the Open Graph Generator, from Hyper-rank.
    A title, one line of description, and the page address.
    It writes the tags from exactly what you typed.
    First, the card Facebook would show, and the card for X.
    No image address given, so both image slots stay empty.
    Below, the whole block. Title, description, O-G and Twitter tags.
    Copy Code takes it all, for the head of your page's H-T-M-L.
    Free to run. Hyper-rank dot A-I.

## Honesty notes

- Every tag on screen is the recorded output for the three typed fields; Image URL, Site name and Type were left at their defaults.
- The film does not claim the tags change how any platform ranks or shows the page beyond the preview the tool draws.
- Sequence shortened from the click to the result.
- Standard close. No tool count, no signup line, no em dashes.
