# Handoff: CV "Constellation" — 3D interactive network tab

## Overview
This adds a new **interactive 3D network visualization** to Miguel's CV at
`MMFreitas1/curriculum_vitae`. It renders the career as a rotating wireframe
**globe/planet**: a central "Miguel" core, category hubs distributed on the
sphere surface, and project nodes orbiting their categories — all hyperlinked
back to the relevant CV sections. The same node set re-clusters under four
lenses (Sector / Skill / Domain / Arc), so no part of the career is orphaned
by a single taxonomy.

## ⚠️ This is NOT a "rebuild in another framework" handoff
The repo is a **single self-contained `index.html`** — vanilla HTML/CSS/JS, no
build step, no dependencies, deployed via GitHub Pages. The `index.html` in
this bundle **is the production file**. The task is simply to **replace the
repo's `index.html` with this one and push**. Do not port it to React/Vue —
that would break the project's intentional zero-dependency design.

## What changed (vs. the current repo `index.html`)
Everything that already existed (hero "coin" photo, Journey timeline, Education,
Tech Stack, Certs, EN/PT/ES i18n, lost-cert modal, PDF preview) is **unchanged**.
The additions are fully self-contained and appended:

1. **Nav + entry points** — a new `Network` item in the top `<nav>`, plus a
   fixed gold floating button `.net-fab` ("✦ Constellation") bottom-right
   (so it's reachable on mobile where nav links hide).
2. **Overlay markup** — `<div id="network-view">` (full-screen overlay) added
   right after `</nav>`, containing the top bar (title, lens buttons, close),
   the canvas (`#net-canvas` with `#net-globe`, `#net-grid`, `#net-edges`,
   `#net-legend`, `#net-hint`, `#net-panel`).
3. **CSS** — one block in the main `<style>`, all class-prefixed `.net-*`
   (no collisions with existing styles). Also added `#network-view` / `.net-fab`
   to the existing `@media print { display:none }` rule.
4. **Engine** — one IIFE `<script>` appended before `</body>` (search for
   `/* ════ Network Constellation ════ */`). Vanilla JS, no libraries.
5. **i18n** — network UI strings merged into the existing `translations`
   object for `en`/`pt`/`es`. A `window.__netOnLang` hook is called from the
   existing `applyLang()` so lens labels/legend re-localize on language switch.
   **Node description copy is currently English-only** (PT/ES not yet written —
   see "Open items").

## How to commit & push
From a clone of `MMFreitas1/curriculum_vitae` (default branch `main`):

```bash
# copy the new index.html from this bundle over the repo's index.html
cp design_handoff_constellation/index.html ./index.html

git add index.html
git commit -m "Add 3D Constellation network tab (multi-lens, hyperlinked to CV)"
git push origin main
```

GitHub Pages will redeploy automatically. **No other files need to change** —
the two hero images (`resources/IMG_0589.jpg`, `resources/surf_wow.jpg`) already
exist in the repo and are referenced by relative path; this file does not touch
them. (If a preview tool ever reports those images failing to load, that's an
environment serving quirk — they load fine on GitHub Pages.)

## How the constellation works (for future edits)
- **Data model** lives at the top of the IIFE:
  - `EXP` — the 11 experiences (id → `{co, short, role, kind, years, sum}`).
    `kind` drives dot color: `gold` (milestone), `dim` (self-directed),
    `life` (analog/personal), `green` (current).
  - `TIP` — the short one-line annotation shown on each project's hover card.
  - `LENS` — the four lenses; each is `{ hubs:[ {id,label,tone,exp:[...],desc,stack} ] }`.
    `exp` lists which experience ids belong to that category. A project can
    appear under multiple hubs (e.g. `photo` is under both "Beyond the Desk"
    and "Freelance"). **To re-link a project to a category, edit the `exp`
    arrays** — e.g. Goparity was added to a new `freelance` hub in `LENS.sector`.
  - `UI` — lens names, legend labels, panel button text (en/pt/es).
- **3D rendering** (no library):
  - Nodes hold world coords `x,y,z` (animating toward targets `tx,ty,tz`).
  - `projectVec(x,y,z,m)` rotates by `rotY`/`rotX` and applies perspective
    `s = F/(F+z)` (focal `F=1050`). Depth sets per-element opacity (back of
    globe fades) and `z-index`.
  - Hubs are placed on a sphere via a Fibonacci distribution (radius `RH=m.R`);
    projects sit just above the surface (`RE=m.R*1.06`) in the averaged
    direction of their parent hub(s) + deterministic jitter.
  - `buildGlobe()` builds the lat/long wireframe as ~440 short `<line>`
    segments (so each segment can depth-fade individually).
  - Hub→project links are drawn as **great-circle arcs** (`greatArc()`, slerp)
    so they curve over the globe; center→hub are straight spokes.
  - `frame()` is the rAF loop: gentle auto-rotation (`0.0024 rad/frame`) +
    drag inertia, all damped. It **stops** (`rafId=null`) when settled and
    `paused`, and respects `prefers-reduced-motion` (no auto-spin).
- **Interactions**:
  - Drag empty canvas → rotate the whole globe (pointer events on `#net-canvas`).
  - Hover a **category hub** → its project children inflate + reveal their
    description cards; everything else dims (`setLit()` adds `.lit`/`.dim`/`.expand`).
  - Hover a **project node** → that node inflates + shows its own card.
  - Rotation auto-pauses (`paused=true`) while hovering/selecting so cards
    are readable; resumes on mouse-leave.
  - Click a node → right detail panel (`#net-panel`). Project panels have a
    **Jump to CV** button (`jumpToCV(company)`) that closes the overlay,
    smooth-scrolls to the matching `.tl-item`, and flashes it (`.cv-flash`).
    Skill hubs offer **View in Tech Stack** (`viewStack(name)`).
  - `Esc` or the Close button exits.
- **CV linkage**: `jumpToCV()` matches a `.tl-company` element whose text
  equals `EXP[id].co`. If you rename a company in the timeline, update the
  matching `co` in `EXP` (or vice-versa) so the jump keeps working.

## Design tokens (reuses the CV's existing variables — do not introduce new ones)
- `--gold #c9a84c`, `--gold2 #e8c97a`, `--bg`, `--bg2`, `--cream`, `--muted`,
  `--line` (all already defined in the CV `:root`).
- Dot colors: gold `#c9a84c`, dim `#9a9486`, life `#b07c5a`, green `#4a7c59`.
- Hub tones: pro `#c9a84c`, tech `#e8c97a`, edu `#9a9486`, ops `#6f9e7e`, life `#b07c5a`.
- Fonts: Playfair Display (titles/center label), DM Mono (labels/UI) — both
  already loaded by the CV.
- Motion: gentle, damped, settles to rest (matches the CV's calm fade-up ethos).

## Open items (optional, ask Miguel)
- **PT/ES translations** for the project description copy (`EXP[].sum`, `TIP[]`,
  and hub `desc`). UI chrome is already trilingual; only the body copy is EN-only.
- Whether `photo` (freelance photography) should stay linked to both
  "Beyond the Desk" and the new "Freelance" category, or only one.

## Files in this bundle
- `index.html` — the complete, production-ready CV with the Constellation tab.
- `README.md` — this document.

(Reference versions kept in the design project, not in this bundle:
`index.original.html` = pre-network, `index.v1-2d.html` = flat 2D network,
`index.v2-3d.html` = 3D before the globe/planet treatment.)
