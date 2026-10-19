# tutorial-ssl-tls-checker: SSL/TLS Checker

Status: READY for the render queue. Pattern: `scripts/tutorial-apple-v1.md` section 3, built with `tutorials/_premium/` (tool.json drives the beats, the voice drives the timing).
Demo input: mozilla.org. Master 16:9 (1920x1080). Project: `tutorials/ssl-tls-checker/premium/`, output `out/premium-16x9.mp4`.

## Claim sources

- Public run (no gate): `premium/capture/try-mozilla/result-sec.html` and `result-text.txt` (valid, issued to mozilla.org by Google Trust Services, expires 13/12/2026 with 67 days left, Security Score 100, risk level Low, five headers Enabled, protocol TLSv1.3).
- Port 443: the tool page's What is section.
- Candidates tried: wikipedia.org (Let's Encrypt, 27 days left, three headers missing while Header Hardening still reads PASSED, a conflict on screen), mozilla.org (clean and consistent). Picked Mozilla.

| Value | Where it shows |
|---|---|
| Valid, issuer | SSL Certificate is Valid, Issued to mozilla.org by Google Trust Services |
| Expiry and days left | Expires On 13/12/2026 (67 days left) |
| Score and risk | Security Score 100, Calculated Risk Level: Low |
| Five headers enabled | Security configuration |
| TLSv1.3 | Server & Protocol |

## Intent

Goal: a site owner checks the certificate and its expiry before a browser warning does | Platform: tool page, social | Length: 30 to 40s | Success: viewer checks their own domain.

One reader: a founder who set up HTTPS once and forgot the renewal date. Belief now: "the padlock is there, so it is fine." Belief after: "I can see the issuer, the expiry date and the headers in one check."

## Hook candidates (different categories)

1. Question (picked): super "Trusted, and in *date?*", VO "Before a browser shows your page, it checks your certificate."
2. Stake: "An expired certificate blocks every visitor." Rejected: fear-led, and the demo certificate is healthy.
3. Number: "67 days left." Rejected as a hook, kept as a read beat.

## Script

Runtime 36.85s

| # | VO starts (s) | Super | Narration |
|---|---|---|---|
| 1 hook | 0.3 | Trusted, and in *date?* | Before a browser shows your page, it checks your certificate. |
| 2 name | 4.021 | SSL/TLS *Checker* | Meet the SSL/TLS Checker, from hyperank. |
| 3 type | 7.593 | Any *hostname.* | Enter a domain. Here, mozilla.org. |
| 4 press | 10.675 | Port *443.* | It connects on port 443 and reads the certificate. |
| 5 result | 14.545 | Certificate *valid.* | Mozilla's certificate is valid, issued by Google Trust Services. |
| 6 read | 19.205 | 67 days *left.* | It expires on the thirteenth of December. Sixty-seven days left. |
| 7 read | 23.588 | Score and *risk.* | Security score, one hundred. Risk level, low. |
| 8 read | 26.968 | Headers *on.* | All five security headers come back enabled. |
| 9 read | 30.092 | Down to the *protocol.* | And the connection itself ran on TLS 1.3. |
| 10 close | close | Free to *run.* / Full report with a free account. / hyperank.ai | Free to run. Hyper-rank dot A-I. |

TTS lines (Kokoro, af_heart):

    Before a browser shows your page, it checks your certificate.
    Meet the S-S-L, T-L-S Checker, from Hyper-rank.
    Enter a domain. Here, Mozilla dot org.
    It connects on port four four three, and reads the certificate.
    Mozilla's certificate is valid, issued by Google Trust Services.
    It expires on the thirteenth of December. Sixty-seven days left.
    Security score, one hundred. Risk level, low.
    All five security headers come back enabled.
    And the connection itself ran on T-L-S one point three.
    Free to run. Hyper-rank dot A-I.

Spoken words: 84

## Honesty notes

- Days left (67) is relative to the capture date; the film shows it as the tool printed it.
- No claim that a score of 100 means the site is secure overall; the film reads the score and the risk label only.
- No gate. Sequence shortened from the click to the result.
- Standard close: super "Free to run.", printed "Full report with a free account.", then hyperank.ai. No tool count anywhere.

## Humanizer pass

- No em dashes in VO, supers or this file's own prose; no banned words, no tool count, no signup line. Dashes inside the live UI (for example the feed count line) stay as the page renders them.
- Pronunciation checked with whisper (small.en): brand names and acronyms transcribe as written.
