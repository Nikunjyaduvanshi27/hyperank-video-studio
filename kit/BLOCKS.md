# Registry blocks and components for hyperank videos (v1)

Verified with `npx hyperframes@0.8.113 catalog --json` (`HYPERFRAMES_SKIP_SKILLS=1`, 386 items) and
installed into a scratch project to read each file's tokens. Install into a video project with
`npx hyperframes add <name>`. A registry item is never used at its default skin: re-skin it per the
notes below, then pass `npx hyperframes check` and snapshot it.

Our own scenes (`kit/scenes/`) come first. Registry items fill the gaps.

## Verdict table

| Item                         | Type       | In catalog | Use in                        | Status                                                |
| ---------------------------- | ---------- | ---------- | ----------------------------- | ----------------------------------------------------- |
| `ai-answer-rank`             | -          | **no**     | -                             | Dropped. `hr-engine-fanout` covers the job            |
| `cursor-zoom-follow`         | -          | **no**     | -                             | Dropped. `ui-focus-zoom` + `oversized-cursor` cover it |
| `ui-focus-zoom`              | component  | yes        | tutorials, explainers         | **Use** (camera into an app region)                   |
| `oversized-cursor`           | component  | yes        | tutorials                     | **Use** (substitute for cursor-zoom-follow)           |
| `browser-device-stage`       | component  | yes        | tutorials, promos             | **Use** (app.hyperank.ai inside browser chrome)       |
| `count-up`                   | component  | yes        | explainers, promos            | **Use**, sourced numbers only                         |
| `streaming-text`             | component  | yes        | explainers, promos            | **Use** (an engine's answer streaming in)             |
| `caption-editorial-emphasis` | component  | yes        | all three                     | **Use**, re-skinned to the one-italic-violet rule     |
| `caption-pill-karaoke`       | component  | yes        | shorts / 9:16 cuts            | **Use**, re-skinned                                   |
| `lt-clean-bar`               | block      | yes        | explainers (speaker, source)  | **Use**, re-skinned                                   |
| `data-chart`                 | block      | yes        | explainers                    | **Use**, re-skinned, sourced data only                |
| `ai-chat-reveal`             | block 9:16 | yes        | vertical promos               | **Use with care**, generic chat shell, re-skin end card |
| `logo-sting`                 | component  | yes        | -                             | Superseded by `hr-logo-sting` (slam + white flash is off-brand) |
| `cta-lockup`                 | component  | yes        | -                             | Superseded by `hr-cta-endcard` (overshoot pop is off-brand) |
| `chatgpt-exchange`           | block 9:16 | yes        | -                             | **Do not use.** Reproduces the ChatGPT app shell and OpenAI naming; its contract forbids restyling the shell |
| `claude-exchange`            | block 9:16 | yes        | -                             | **Do not use.** Reproduces the Claude shell, ClaudeSans/ClaudeSerif and the starburst mark |

## Shared re-skin: token-native components

`ui-focus-zoom`, `browser-device-stage`, `oversized-cursor`, `count-up`, `logo-sting` and
`cta-lockup` read inherited CSS custom properties with dark-mode fallbacks. Their `accent` variable
is an enum (`green` rides `--brand`, `blue` rides `--accent`, `violet` rides `--accent-2`). Set all
three to violet on the host root so any enum value lands on brand, and pass `accent: "violet"`
anyway for clarity:

```css
/* index.html, on the host #root */
#root {
  --bg: #f0eee9;
  --fg: #1f1e1b;
  --surface: #ffffff;
  --border: #e7e4dc;
  --muted: #5a564b;
  --brand: #5e4bf6;
  --accent: #5e4bf6;
  --accent-2: #5e4bf6;
  --radius: 14px;
  --font-display: "Instrument Serif", serif;
  --font-body: "Inter", sans-serif;
  --font-mono: "JetBrains Mono", monospace;
}
```

Also add the kit's four `@font-face` rules (see any `kit/scenes/*.html`) to the host, and leave
`--space-*` at component defaults. This mapping is read from the component source; it has not yet
been mounted in a hyperank project, so the first use must pass `check` and a snapshot.

## Per-item notes

### ui-focus-zoom (component)
Camera settles on an app surface, then zooms and pans to an anchor and holds. Variables: `anchor_x`,
`anchor_y` (percent), `zoom` (1-3, keep at or under 1.8), `zoom_at`, `halo`, `accent`, `exit`. Put a
real app.hyperank.ai capture in the surface slot. `halo: "show"` with violet is the only allowed glow
on a product surface. Never zoom on type.

### oversized-cursor (component)
A 3.5x macOS-style arrow lands on one control and clicks. Variables: `cursor_variant`, `target_x`,
`target_y`, `click_label`, `exit`. Pair with `ui-focus-zoom` in the same beat to replace the missing
`cursor-zoom-follow`. Ignite colour comes from `--oc-ignite` driven by the host tokens. One click per
beat.

### browser-device-stage (component)
App surface inside browser, window or phone chrome; screen is a slot. Variables: `chrome`, `title`,
`swap_at`, `accent`, `exit`. Set `title` to the real URL being shown (for example
`app.hyperank.ai/login`). Card radius follows `--radius`; give the stage the e4 shadow from
`frame.md` if it reads flat on the ground.

### count-up (component)
Eases between two values with a restrained pulse. Variables: `start`, `end`, `prefix`, `suffix`
(default `%`, change it), `accent`, `glow`, `exit`. Values must come from `brief/product-brief.md`
("88" free tools, "6" engines, "17%" annual saving). Never count up a dashboard mock value. Override
the display face to Instrument Serif via `--font-display` (already in the host block).

### streaming-text (component)
Words arrive in uneven bursts like a streamed AI answer, grey inking to full colour. Variables:
`size` (18-64px, use 40+ at 1080p), `tone: "dark-on-light"`. Uses `--hf-ui-*` tokens; set on the
host: `--hf-ui-font-sans: "Inter", sans-serif; --hf-ui-text: #1f1e1b; --hf-ui-text-muted: #5a564b;
--hf-ui-canvas: #f0eee9; --hf-ui-surface: #ffffff; --hf-ui-accent: #5e4bf6`. Put it inside an
engine card from the fan-out vocabulary, engine named as text.

### caption-editorial-emphasis (component)
Dual-font captions with large emphasis words. Ships Inter + **Playfair Display** emphasis in cream
`#f5f0d0` with dark text-shadows (built for dark footage). Edit the installed file: emphasis
`font-family` to `"Instrument Serif"` italic, emphasis colour `#5e4bf6`, base words `#1f1e1b`,
remove the text-shadows on our light ground. One emphasis word per caption line, matching the
one-italic-violet rule. Playfair is banned in this kit.

### caption-pill-karaoke (component)
Per-word karaoke highlight inside a pill. Ships **Poppins**, pill `#e7e5e7`, JS constants
`COLOR_INACTIVE = "#A6A6A6"`, `COLOR_ACTIVE = "#1C1E1D"`. Edit: font to `"Inter"` 600, pill
background `#ffffff` with `1px solid #e7e4dc` and the `pill` shadow, `COLOR_INACTIVE = "#767161"`,
`COLOR_ACTIVE = "#1f1e1b"`. Brand keyword ("hyperank") may take `#5e4bf6`. For 9:16 shorts only.

### lt-clean-bar (block, 1920x1080, 4.8s)
White-card lower third with accent tab. Ships Montserrat, tab `#ff5a36`, name `#0f1115`, role
`#5a6170`. Edit: font `"Inter"` (name 600, role 500), tab `#5e4bf6`, name `#1f1e1b`, role
`#5a564b`, card radius 14px, shadow e3. Add the role line in mono uppercase if it is a source credit
("Source · hyperank.ai/about").

### data-chart (block, 1920x1080, 15s)
Bar + line chart with NYT-style typography. Ships Libre Franklin / Libre Baskerville, ground
`#faf9f6`, bars `#5c5c5c` and `#326fa8`. Edit: ground `#f0eee9`, title `"Instrument Serif"`, labels
`"Inter"`, axis and gridlines `#d6d2c7`, default bars `#d6d2c7`, the one highlighted series
`#5e4bf6`. Only chart data with a primary source; the homepage dashboard numbers are mockups.

### ai-chat-reveal (block, 1080x1920, 19.3s)
A question typed on a keyboard, a streamed answer, then a branded end card. Generic chat shell
(system font, neutral greys), so no third-party identity. Variables: `botName`, `userMessage`,
`answer1-3`, `bullet1-3`, `ecHeadline`, `ecSub`, `ecCta`, `ecFooter`, `brandLogo`. Set `botName` to
a neutral label ("AI assistant"), not an engine name, unless the scene is explicitly about that
engine's answer. `brandLogo`: `assets/hyperank-mark.png`; `ecCta`: "Check your brand free";
`ecFooter`: "hyperank.ai". Restyle the end card to the frame tokens (ground, Instrument Serif
headline with its italic violet phrase, violet CTA).

### logo-sting, cta-lockup (components)
Exist and are token-native, but their defaults (a scale slam with a one-frame white flash; an
overshoot pop) break MOTION.md. Use `hr-logo-sting` and `hr-cta-endcard` instead.

### chatgpt-exchange, claude-exchange (blocks)
Exist, but they recreate third-party product UIs (ChatGPT shell and OpenAI naming; Claude's fonts
and starburst mark) and their editing contract protects that shell. That conflicts with the
"engines as text only, no third-party logos" rule. Excluded in v1; use `streaming-text` inside an
engine card instead.
