# CLAUDE.md — CV Project Rules

## What this project is

A single-file personal CV website (`index.html`) with inline CSS and JS — the "Soft Clay" neumorphic design. No build tooling. No frameworks. No dependencies beyond Google Fonts. Static, deployed on GitHub Pages. Images, videos and the downloadable PDF live in `assets/`; certificate PDFs in `resources/`.

`design/` holds the source designs (`soft-clay.dc.html`, the alternative `tide.dc.html`) and `HANDOFF.md`. `archive/` holds retired features (the 2D/3D constellation). `tools/pdf/` rebuilds the PDF CVs (`build3.py` → `render.py`); `tools/video/` recuts the lab highlight loops.

---

## Where the content lives

All CV content is in `const` arrays at the top of the `<script>` — edit those, not the rendered markup:

| Array | Feeds |
|---|---|
| `NOW` | "Right now" ticker in the header |
| `CHAPTERS` | The Journey scroll sequence (one chapter per entry; `big` + `cap` fill the side disc) |
| `STACK` | Toolkit cards and the Numbers waffle (counts are computed) |
| `EDUCATION`, `CERTS` | Education and Certificates cards (`pdf` links a file in `resources/`) |
| `PROJECTS` | "Where the work landed" (sector / capability) |
| `YEARLY`, `CURRENT_YEAR`, `HOLT` | Projects-per-year chart and its Holt forecast — each January add the new year and bump `CURRENT_YEAR` |
| `GPA`, `ERAS`, `SUMMERS` | Rigor curve, career split, lifeguard summers |

Static sections (hero, Lab apps, gallery, closing) are plain HTML. Keep the website text consistent with `tools/pdf/content2.py`.

---

## i18n — three languages

Static text in the HTML carries a `data-i18n` key; the English is harvested from the markup into `translations.en` at load, and `pt`/`es` entries go into the `translations` object. Never hardcode display text in HTML without a `data-i18n` attribute (unless it's a proper noun that doesn't change). The data arrays are English-only for now — when translating, give them per-language versions too.

Don't translate until Miguel explicitly confirms the English copy first.

---

## Bullet writing — tone and standards

Miguel's bullets follow a strict pattern. Read the Capgemini and Genesis chapters in `CHAPTERS` before writing anything new.

**Rules:**
- Start with a strong past-tense verb (Built, Deployed, Orchestrated, Designed, Led, Implemented, Architected...)
- One sentence per bullet. If you need a second clause, use an em-dash (—) not a comma
- Numbers and percentages are welcome. Vague superlatives are not
- Never write "leveraged", "utilized", "harnessed", "streamlined", or any word that sounds like it came from a LinkedIn generator
- Technical specifics over generic descriptions — name the model, the DB, the method
- The tone is confident and direct, not corporate. Miguel's background is unusual (shipping → AI) and that makes the writing distinct — don't flatten it

**Good:** `Parallelized concurrent document processing via ThreadPooling, delivering 10–18× faster throughput over manual handling.`

**Bad:** `Leveraged multi-threading capabilities to optimize and streamline document processing workflows.`

---

## Chapter side discs

Each chapter's `big` + `cap` is a single standout result or fact — not a summary. Keep it tight.

---

## What not to do

- Don't split `index.html` into components or introduce a build step
- Don't add new sections without Miguel asking
- Don't modify the print CSS unless specifically asked (the PDF in `assets/cv/` is the printable CV)
- Keep every committed file under 50MB; never commit raw demo recordings
- Don't translate before English copy is approved
- Don't add comments to the HTML/CSS/JS unless the logic is genuinely non-obvious
