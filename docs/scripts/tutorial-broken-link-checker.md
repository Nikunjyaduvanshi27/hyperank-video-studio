# tutorial-broken-link-checker: Broken Link Checker (404 Checker)

Status: prepared for the render queue. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: http://info.cern.ch/hypertext/WWW/TheProject.html (CERN's restored first website). Master 16:9 (1920x1080). Project: `tutorials/broken-link-checker/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Public run (no gate): `premium/capture/try-cern/api.json` (POST `/api/tools/broken-link-checker`, `brokenLinks` holds one URL) and `result-sec.html`.
- Screened before spending a run (local HEAD/GET of each page's first 60 links): info.cern.ch (23 links, 1 dead), spacejam.com/1996 (1 DNS failure, a footer privacy link), norvig.com (kept for the 404 Page Checker), w3.org Berners-Lee page (timeouts, a confusing read). Picked CERN.
- "The first website, still online at CERN": CERN hosts it at info.cern.ch as the home of the first website.
- "Mailing lists": the anchor text of that link in TheProject.html (`<A HREF="Administration/Mailing/Overview.html">Mailing lists</A>`).
- "Up to sixty" and "working links stay off the list": the tool page's own how-it-works copy.

| Value | Where it shows |
|---|---|
| Broken Links Found: 1 | Result heading |
| http://info.cern.ch/hypertext/WWW/Administration/Mailing/Overview.html | The one listed URL |

## Intent

Goal: a site owner sees one page's dead links in one list | Platform: tool page, social | Length: 35s | Success: viewer pastes an old post of their own.

One reader: a content lead with years of blog posts that cite sources. Belief now: "our links were fine when we published." Belief after: "links rot on their own; one paste shows me which ones."

## Hook candidates (different categories)

1. Claim (picked): super "Links *rot.*", VO "The pages you link to move, or vanish. Your links keep pointing at them."
2. Curiosity: "Even the first website has a dead link." Rejected for the hook: spends the result before the tool is named.
3. Question: "When did you last click your own links?" Rejected: generic, fits any link tool.

## Script

Runtime 36.08s

| # | Beat start (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.0 | Links *rot.* | The pages you link to move, or vanish. Your links keep pointing at them. |
| 2 name | 4.74 | Broken Link *Checker* | Meet the Broken Link Checker, from hyperank. |
| 3 type | 7.63 | Paste a *page.* | Paste a page. This one is the first website, still online at CERN. |
| 4 press | 13.47 | One *press.* | It reads every link on the page, up to sixty, and requests each one. |
| 5 result | 17.98 | One *dead.* | One of them no longer resolves. |
| 6 read | 20.38 | Only what *breaks.* | Working links stay off the list, so you only see what needs fixing. |
| 7 read | 24.45 | The exact *address.* | It names the dead address: the link to the project's mailing lists. |
| 8 read | 28.59 | Fix, or *remove.* | Point it at the page's new home, or take the link out. Then check again. |
| 9 close | 32.89 | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    The pages you link to move, or vanish. Your links keep pointing at them.
    Meet the Broken Link Checker, from Hyper-rank.
    Paste a page. This one is the first website, still online at Sern.
    It reads every link on the page, up to sixty, and requests each one.
    One of them no longer resolves.
    Working links stay off the list, so you only see what needs fixing.
    It names the dead address: the link to the project's mailing lists.
    Point it at the page's new home, or take the link out. Then check again.
    Free to run. Hyper-rank dot A-I.

Whisper check: vo-03 transcribes as "...still online at CERN." (an earlier "Here, the first website" read as "Here are the first websites" and was rewritten).

## Honesty notes

- One number on screen and in the VO: one broken link. The VO never says how many links the page has (the tool does not print it).
- No gate. Sequence shortened from the click to the result (about 6s live).
- Distinct from the 404 Page Checker video (norvig.com, status codes per row): this one is the dead-links-only list.
- Standard close. No tool count, no signup line, no em dashes.
