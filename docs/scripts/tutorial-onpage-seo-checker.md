# tutorial-onpage-seo-checker: On-Page SEO Checker

Status: prepared for the render queue. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: https://www.nationalgeographic.com/animals/mammals/facts/african-elephant, keyword "african elephant". Master 16:9 (1920x1080). Project: `tutorials/onpage-seo-checker/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Public run (no gate): `premium/capture/try-natgeo-elephant/api.json` (POST `/api/tools/onpage-seo-checker`) and `result-sec.html`.
- Screened locally before spending a run: lego.com Star Wars (most images lazy-load with no alt, a noisy read), ikea.com desks (few findings), natgeo African elephant (empty meta description). Picked natgeo, one run.
- On screen the field is typed as `www.nationalgeographic.com/...` (the tool page: "The https:// is optional"); the full https URL overflowed the input box onto the keyword field. The result header shows the URL the run used, `https://www.nationalgeographic.com/...`.
- "Ten groups, from the URL to crawlability": the tool page's how-it-works copy.
- Sibling: onpage-seo-audit (prep-H) uses a BBC Food page; this one uses a different site, a keyword, and the fail list.

| Value | Where it shows |
|---|---|
| 82/100 | SEO Score card |
| 2 Fails, 8 Warnings, 24 Passes | SEO Score card |
| Title: "African elephant, facts and photos \| National Geographic", 56 characters | Technical Details, Title Tag |
| No meta description found, 0 characters | Technical Details, Meta Description |
| Inline styles: fail, 46 element(s) with a style attribute | Issues, Code Quality |

## Intent

Goal: a content editor sees one page's on-page fails and which to fix first | Platform: tool page, social | Length: 40s | Success: viewer runs their best-traffic page with its keyword.

One reader: an editor at a publisher who owns hundreds of evergreen articles. Belief now: "a big brand's page must be set up right." Belief after: "one run shows what is missing, and the fails come first."

## Hook candidates (different categories)

1. Question (picked): super "What does a crawler *read?*", VO "Before you rewrite a page, see what a crawler finds in its HTML."
2. Number: "82 out of 100." Rejected for the hook: the score belongs to the demo, not the viewer.
3. Contrast: "Big brand. Empty meta description." Rejected: spends the finding before the tool is named.

## Script

Runtime 41.73s

| # | Beat start (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.0 | What does a crawler *read?* | Before you rewrite a page, see what a crawler finds in its HTML. |
| 2 name | 4.55 | On-Page SEO *Checker* | Meet the On-Page SEO Checker, from hyperank. |
| 3 type | 7.91 | Page, plus a *keyword.* | Paste a page and a target keyword. Here, National Geographic's African elephant page. |
| 4 press | 17.11 | One *press.* | It reads the HTML, and runs checks in ten groups, from the URL to crawlability. |
| 5 result | 23.33 | Two *fails.* | Eighty-two out of a hundred. Two fails, eight warnings, twenty-four passes. |
| 6 read | 28.22 | No meta *description.* | The title is in place, fifty-six characters. The meta description is empty. |
| 7 read | 33.33 | Fix the fails *first.* | The other fail: forty-six elements with inline styles. Fix the fails first. |
| 8 close | 38.55 | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    Before you rewrite a page, see what a crawler finds in its H-T-M-L.
    Meet the On-Page S-E-O Checker, from Hyper-rank.
    Paste a page and a target keyword. Here, National Geographic's African elephant page.
    It reads the H-T-M-L, and runs checks in ten groups, from the U-R-L to crawlability.
    Eighty-two out of a hundred. Two fails, eight warnings, twenty-four passes.
    The title is in place, fifty-six characters. The meta description is empty.
    The other fail: forty-six elements with inline styles. Fix the fails first.
    Free to run. Hyper-rank dot A-I.

Whisper check: vo-01 to vo-05 transcribe as written (National Geographic, HTML, URL).

## Honesty notes

- Every number spoken is printed on screen in the same beat: 82/100, 2, 8, 24, 56 characters, 46 elements.
- Not featured: the "Keyword in URL" warning says "african elephant" is not in the path, though the path ends `african-elephant`. It looks like the check does not treat hyphens as spaces; worth a ticket before anyone demos that row.
- No gate. Sequence shortened from the click to the result.
- Standard close. No tool count, no signup line, no em dashes.
