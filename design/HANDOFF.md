# Living CV — implementation handoff

**Owner:** Miguel G.M. Freitas · **Repo:** `MMFreitas1/curriculum_vitae` (GitHub Pages) · **Prepared:** 25 Nov 2026

This bundle holds two finished design directions for Miguel's CV website, plus every asset they use and the tools that produced the PDFs and demo videos. Your job is to turn the chosen direction into the live `index.html`.

There is **no server-side backend to build**. The site stays a static GitHub Pages site. Everything below runs in the browser, and the only thing persisted is the visitor's day/night choice, kept in `localStorage`.

---

## 0. Decisions to confirm with Miguel before you start

1. **Which direction goes live:** `soft-clay.dc.html` (neumorphic) or `tide.dc.html` (editorial). Both are finished. Miguel last said he is keeping Soft Clay as the neumorphic direction, but Tide was never dropped. Ask whether it's one of them, or both behind a switch.
2. **Features of the current site that the new designs don't include.** The current `index.html` has the EN/PT/ES language switcher, the "Constellation" modal, `SKILL_TIPS` tooltips on the stack pills, `data-pdf` certificate links and the `data-secret` modal. Ask which of these to carry over.
3. **Translations.** The repo's `CLAUDE.md` says every string needs `en`/`pt`/`es`, but nothing is translated until Miguel approves the English copy. Get that approval, then translate.

## 1. Repo rules that still apply (from `CLAUDE.md`)

- One `index.html` with inline CSS and JS. No build step, no frameworks, no dependencies beyond Google Fonts.
- User-facing text goes through the `translations` object with `data-i18n` (see decision 3).
- Bullets follow Miguel's tone rules: strong past-tense verb, one sentence, em-dash for a second clause, no "leveraged/utilized/streamlined".
- Don't touch the print CSS unless asked.
- Don't add comments unless the logic is non-obvious.

## 2. What's in the bundle

```
design/
  soft-clay.dc.html     Direction B — neumorphic, warm clay
  tide.dc.html          Direction C — editorial, ocean palette
assets/
  img/      portrait, surf, five gallery photos + Andromeda, grain.png
  video/    two 20–25s highlight loops, two full demos (web-compressed), two posters
  cv/       the two downloadable PDF CVs, one per direction
tools/
  pdf/      scripts that generate the PDF CVs
  video/    highlight.py — recuts the highlight loops
```

Every asset path inside the design files already points at `assets/...`. Copy `assets/` to the repo root and the paths resolve as-is.

## 3. How to read the `.dc.html` files

They come from a design canvas and use a small templating runtime. **Port them to plain HTML + vanilla JS; don't ship them as they are.** The format:

- `<x-dc>` wraps the markup. `<helmet><style>` holds the page CSS: copy it into your `<style>`.
- `{{name}}` inserts a value returned by `renderVals()` in the `class Component` at the bottom. That includes inline styles like `width: {{y.doneH}}`.
- `<sc-for list="{{items}}" as="item">` repeats markup. `<sc-if value="{{flag}}">` shows it conditionally.
- `onClick="{{fn}}"`, `onScroll`, `onMouseMove`, `ref="{{setEl}}"` are event bindings and refs.
- `this.state` / `this.setState()` behave like React state. `componentDidMount` starts the clock and restores the saved theme.
- `data-props` on the script tag holds editor-only settings. The default is the real value: `punch` is `#11656B` in Soft Clay and `#FF6B4A` in Tide.
- In the designs the **scroll container is the outer `<div>`** (`height: 100vh; overflow-y: auto`) because they render inside an artboard. On the real site, use the window/document scroll instead and replace `el.getBoundingClientRect()` and `el.scrollTo` with their `window` equivalents.

All the data (chapters, projects, stack, education, certs, yearly counts) sits in `const` arrays at the top of each script. Lift it as-is.

## 4. Page structure (same in both directions)

### Header (sticky)
- **Name / logo.**
- **Story ⇄ Numbers.** In Soft Clay this is a `role="switch"` toggle. In Tide it's two tab buttons with `aria-pressed`. Switching resets the scroll to the top.
- **Night-mode button.** Round moon/sun icon in Soft Clay; "Night"/"Day" button in Tide. The choice is saved to `localStorage` (`cv-theme-clay` / `cv-theme-tide`), wrapped in `try/catch`.
- **Live Porto clock.** Uses `toLocaleTimeString` with `timeZone: "Europe/Lisbon"` and refreshes every 15s.
- **Download CV.** Links to that direction's PDF in `assets/cv/`.
- **"Right now" ticker.** A marquee that pauses on hover. Its content is the `NOW` array, CV facts only; Miguel removed the "Shipping" item on purpose. Stopped under `prefers-reduced-motion`.

### Story tab, top to bottom
1. **Hero scroll scene** (`data-scene="hero"`, 220–240vh, sticky inner). Progress `heroP` (0–1) drives all the motion:
   - **Soft Clay:** "MIGUEL" sits **above** the portrait disc and must stay fully readable at rest; an earlier version hid letters behind the disc. As you scroll, the name lifts away and fades, the disc moves up-left and shrinks slightly, and a teal ring fills around the disc. The intro copy fades in on the right.
   - **Tide:** at rest, MIGUEL sits above a horizontal line ("AI ENGINEER ● PORTO · EST. 2012") and FREITAS below it. Scrolling opens the line into the full-bleed portrait with `clip-path: inset(h% 0 h% 0)` and ease-in-out timing, while the two words move apart. The intro copy fades in on a left-side gradient. Keep the portrait's `object-position: 50% 26%` so the eye line sits on the slit.
2. **Journey sequence** (`data-scene="seq"`, 700vh, sticky inner). `active = floor(seqP × 10)`:
   - Exactly one chapter is open. Earlier chapters show as pressed/muted, later ones flat.
   - The list scrolls itself so the active row stays visible (`componentDidUpdate`).
   - Clicking a chapter scrolls the page to the middle of that chapter's band.
   - A side panel shows the active chapter's sector, big number and caption.
   - Chapter 08 (Photography) shows the Andromeda photo, with "Gallery ↓" and "Instagram →" buttons. Chapter 10 (MF Concepts) has "See the apps ↓".
   - **Soft Clay bug to avoid:** the list's scroll box needs ~36px padding with a matching negative margin, or the raised card's shadows get clipped into hard squares.
3. **Built in the lab** (`#lab`). Two apps, each with:
   - a highlight loop video: `autoplay loop muted playsinline`, with a poster;
   - a "Watch the full demo · m:ss →" link to the full video;
   - a description, its stack, and a GitHub button.
4. **Through the lens** (`#lens`). A 12-column grid of 5 photos that collapses to one column on phones.
5. **Toolkit.** 57 tools in 6 families.
6. **Education and Certificates.**
7. **Closing.** The surf photo with the manifesto line and contact links.

### Numbers tab
- **Projects per year.** Bars plus a smoothed trend curve plus next year's forecast; full spec in §6.
- **"Where the work landed".** 13 projects grouped by sector or by capability (toggle). The leading group uses the accent colour.
- **The rigor curve.** GPAs 14 → 17 → 18.
- **"Fourteen years, three tides".** Career split into maritime 62% / the pivot 14% / data & AI 24%, with the 10 lifeguard summers shown as dots.
- **Toolkit composition.** A waffle grid, 57 squares coloured by tool family.

## 5. Direction-specific systems

### Soft Clay
- **Theme variables.** All colours are CSS custom properties on `.theme`; `.theme[data-theme="dark"]` overrides them for night mode (charcoal clay, brighter teal `#3FC6BA`). Body text must keep at least 4.5:1 contrast in both themes.
- **Moving light.** Every neumorphic shadow is written as `calc(var(--sx) * Npx) calc(var(--sy) * Npx) blur var(--sh-d), calc(var(--sx) * -Npx) … var(--sh-l)`.
  - On mousemove, the target becomes `0.45 + 0.85 × (offset from centre)`, clamped to [-1, 1.3].
  - The values ease toward the target at 12% per animation frame and return to (1, 1) on mouseleave.
  - Nothing moves under `prefers-reduced-motion`.
  - **Performance:** in the design, `--sx`/`--sy` are set on a `display: contents` wrapper inside `.theme`. On the live site, set them on `document.documentElement` and check that 60+ animated shadows stay smooth. If they don't, throttle the updates or limit the effect to the viewport's sections.
- **Grain.** `assets/img/grain.png` is a 256px tile in a fixed `::after` overlay with `pointer-events: none`. Opacity is `var(--grain-o)`: .55 by day, .3 by night.

### Tide
- **Theme variables.** Same pattern; night mode is deep-sea navy `#0A171A` with brighter teals, and coral stays the accent.
- **Typography.** Archivo is used with `font-stretch` 62–85%, so load the `wdth` axis: `family=Archivo:wdth,wght@62..125,400..900`.

## 6. Projects-per-year chart and forecast (both directions)

```js
const YEARLY = [
  { y: 2023, items: ["BNA", "IPQ", "Automotive"] },
  { y: 2024, items: ["Generis · phase I", "News NLP research"] },
  { y: 2025, items: ["Generis · phase II", "Goparity"] },
  { y: 2026, items: ["MoneyFlix", "Havas", "ProcurifAI", "Dell · Pombal & Leiria", "Shift Global", "Transfim", "MF Concepts app 1", "MF Concepts app 2"] }
];
const CURRENT_YEAR = 2026;
const HOLT = { alpha: 0.9, beta: 0.5 };
```

- **Current year.** It's shown as a solid bar for projects done so far, plus a faded, dashed block on top for the projection to 31 December. The projection is the count divided by the share of the year elapsed.
- **Forecast.** Next year comes from Holt's linear trend (double exponential smoothing), fitted on annualised counts. It's drawn as a faded, dashed bar, with an 80% interval whisker (±1.28σ of the one-step errors). The trend curve is a Catmull-Rom spline through the smoothed levels, turning dashed for the forecast segment.
- **Tooltip.** The forecast bar's `title` names the method and its parameters. Miguel asked for a tooltip only, not a clickable easter egg. Bars and labels must be centred in equal columns so the trend dots line up with them.
- **Yearly update (January).** Add the new year to `YEARLY` and bump `CURRENT_YEAR`; everything else recomputes. Item names must stay real: Generis really was two phases in 2024 and 2025.

## 7. Assets

| File | Used for | Notes |
|---|---|---|
| `img/portrait.jpg` | Hero | 1400px; dark background |
| `img/surf.jpg` | Closing | |
| `img/falls.jpg` | Gallery — "Basalt & water" | Caption is a placeholder |
| `img/street.jpg` | Gallery — "Old-town light" | Placeholder caption; portrait orientation |
| `img/veil.jpg` | Gallery — Western & Eastern Veil Nebulae | |
| `img/doorway.jpg` | Gallery — "Doorway, with company" | Identifiable person: confirm consent |
| `img/plane.jpg` | Gallery — "Inverted pass" | Developed from RAW (IMG_2123), +saturation |
| `img/andromeda.jpg` | Chapter 08 | Dehazed and sharpened |
| `img/grain.png` | Soft Clay overlay | |
| `video/*-highlight.mp4` | Lab autoplay loops | 2–4MB, no audio, crossfades, fade from/to black |
| `video/*-demo.mp4` | "Watch the full demo" | 1440×900, 30fps, no audio |
| `video/*-poster.jpg` | Video posters | |
| `cv/*.pdf` | Download CV | One per direction, A4 |

Keep every file under 50MB: GitHub hard-rejects anything over 100MB. Never commit the original demo recordings (163MB). Consider adding WebP/AVIF versions of the images with `srcset`.

## 8. PDFs

`tools/pdf` builds both CVs from HTML with headless Chromium:

- Fonts come from `@fontsource` packages: run `npm i` with the `package.json`.
- Run `python3 build2.py` for Tide and `python3 build3.py` for Soft Clay, then `python3 render.py`. `render.py` still includes `clay_punch` in its list; remove it.
- Content is in `content2.py`. It must stay consistent with the website's chapter text.
- **Soft Clay must use vector-only shadows.** These are stacked, unblurred `box-shadow` layers, as in `build3.py`. Blurred shadows get rasterised into soft-mask images that some viewers (Preview, for one) draw as flat white/beige squares. Check with `pdfimages -list`: it should list only the two photos.
- Paths in the scripts point at the original build workspace (`/home/claude/...`). Repoint them at `assets/img/`.

## 9. Accessibility and quality checklist

- Real `<button>`/`<a>` elements, `aria-pressed`/`aria-checked`/`aria-expanded` as in the designs, and visible focus outlines.
- Under `prefers-reduced-motion`: no marquee, no rise animations, no light motion. Scroll scenes may still progress, but there's nothing extra.
- At phone width (≤820px): the side panels hide, the hero type scales down, the gallery goes to one column and the header wraps.
- **Neither design has been play-tested in a real browser yet.** Test the scroll scenes, the light motion, night mode and video autoplay in Safari, Chrome and Firefox, and on iOS.

## 10. Open items for Miguel

- **3D S&P 500 repo.** `MMFreitas1/3d-sp500-historical-visualizer` couldn't be read; it's probably private. If it is, its GitHub button will show visitors a 404. Its stack line is also missing from the Lab section.
- **Gallery captions.** Swap the placeholders for real titles or places.
- **Doorway portrait.** Confirm consent from the person photographed.
- **The two apps in `YEARLY`.** Replace "MF Concepts app 1/2" with "AI-ML Refresher" and "3D S&P 500 Visualizer" if Miguel agrees.
- **PDFs.** The PDFs don't name the two apps yet, only "2 working apps". Add them if Miguel wants.
