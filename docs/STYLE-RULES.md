# Style rules (founder feedback)

Cinematic 3D fly-through (Three.js depth, DOF, fog, violet payoff) was "genuinely loved". Kinetic-type title-sequence style (Anton, hard cuts, words slamming) was disliked entirely; do not propose it again. Videos should pull in real elements from hyperank.ai (actual UI, sections, copy, visuals), not only invented abstractions.

Tutorial interview (2026-10-03): one video per free tool (88, list in the live tool list on hyperank.ai); tool #1 gets quick/standard/deep samples, founder picks length for the rest. Voice af_heart. Style: 3-5s cinematic 3D hook built from real site UI, clean kit demo, cinematic outro. Audio: Pixabay SFX layering (what he called "music" in the 3D video was SFX, no music track) + Pixabay Music bed, mood varies by category (AI visibility cinematic, Technical SEO minimal, X/Instagram upbeat). Demo input: a well-known neutral brand. Publish everywhere: YouTube 16:9, Shorts/Reels 9:16, tool pages, LinkedIn/X, captions always on.

Tutorial structure (founder, after v1 was "too BASIC"): 1) open on the tool's real RESULT as the payoff, 2) one sentence on what the tool is, 3) how to use it, 4) the result again, explained with callouts. Results must be hero visuals (cropped, re-staged with depth, real values animated), not a framed screenshot.

Audio: NO background music bed (founder: loud music is unprofessional); only subtle SFX, voice dominant. TTS: write "A-I" (not "A I", which espeak reads "uh-eye"). Videos must be official-social quality: UI readable at phone size (tight zooms), big high-contrast 3-6 word captions, crisp result crops (dsf 2), never two conflicting numbers on screen.

Founder approved (2026-10-03) showing real third-party brands' results (e.g. Notion) in tutorials posted on official socials.

Premium direction (2026-10-04): founder wants Apple/big-SaaS product films. Product UI is the hero (not the example brand). Rebuild UI as crisp HTML from real site CSS (not screen recording), generic silver laptop device (no Apple logo), camera zooms only when needed, BRIGHT Apple-light theme (founder overrode Midnight), hyperank logo + official AI-engine logos as motion graphics around the screen (nominative use, unmodified, sources logged), voice + Apple-style supers + QUIET score (~-26 dB, ducked), brag CC0 SFX. Never cite a tool count: site went from 88 to 54 tools on 2026-10-04 (X/Instagram tools 404); check the live /tools page for the current list.

Premium bright laptop film (the tutorial and intro templates, `templates/tutorial` and `templates/intro`) was "genuinely loved" on 2026-10-04: this is THE template direction. Hard QA gates for every video: no near-empty/white frames (negate+blackdetect pix_th 0.15, ratio 0.97 finds nothing), no voice gap >0.4s (silencedetect -28dB), no music-only tail, dense short end card. The FULL laptop (base, keyboard, hinge) must stay visible in wide shots; v2 at 75% width cropped it and the founder said "the MacBook is missing". "Kill whitespace" meant blank/empty frames and silence, NOT enlarging the device. Apply only the change asked; never re-frame an approved video unasked.

NEVER say "no signup" / "no account needed" in any video (founder, 2026-10-05: hyperank has signup), even if a tool runs anonymously or the site FAQ says it. Standard close: "Free to run." + "Full report with a free account." + hyperank.ai.

**Why:** founder wants each video immersive and interesting, and recognisably his product.
**How to apply:** promos/explainers: immersive/cinematic directions, rotate but stay in that family, always weave captured site elements in. Tutorials/demos use the kit. See `STACK.md`.

Sales promo (2026-10-19): founder rejected a dark cinematic opening for the client-facing promo: "i want it to be bright as i want it to be proffesional". Client-facing films stay bright end to end; borrow 3D depth/focus-pull ideas only in daylight. He also judged v2 of the promo "not premium like Celebal" and "not pitching impactfully": a feature tour with a new visual system per scene, tiny UI and mono label pills reads as AI-generated. Fix = one story idea with a recurring hero object, website graphics as heroes, one lift at a time.
