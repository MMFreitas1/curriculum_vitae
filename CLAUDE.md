# CLAUDE.md — CV Project Rules

## What this project is

A single-file personal CV website (`index.html`) with inline CSS and JS. No build tooling. No frameworks. No dependencies beyond Google Fonts. Static, deployed on GitHub Pages.

---

## Adding new timeline entries

Follow the existing `.tl-item` pattern exactly. Dot color conventions:

| Color | Meaning |
|---|---|
| `tl-dot` (gold) | Professional / technical role |
| `tl-dot dim` | Education, self-directed, or transitional |
| `tl-dot life` | Personal / analog (lifeguard, photography, coffee) |
| `tl-dot green` | Current role |

Each entry has: year range → company → role → body paragraphs → tags → optional `.tl-highlight`.

---

## i18n — three languages

All user-facing text lives in the `translations` object at the bottom of `<script>`. Every new string needs a key in all three languages: `en`, `pt`, `es`. Never hardcode display text in HTML without a `data-i18n` attribute (unless it's a proper noun that doesn't change).

Don't translate until Miguel explicitly confirms the English copy first.

---

## Adding tech stack entries

Two places to update simultaneously:
1. A `.skill-pill` div inside `#stack .skills-grid`
2. A matching entry in the `SKILL_TIPS` JS object

Both or neither — never one without the other.

---

## Bullet writing — tone and standards

Miguel's bullets follow a strict pattern. Read the Capgemini and Genesis entries before writing anything new.

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

## Highlight blocks

`.tl-highlight` is for a single standout result or fact per role — not a summary. Keep it tight. It can optionally link a PDF via `data-pdf` or trigger a secret modal via `data-secret`.

---

## What not to do

- Don't split `index.html` into components or introduce a build step
- Don't add new sections without Miguel asking
- Don't modify the print CSS unless specifically asked
- Don't translate before English copy is approved
- Don't add comments to the HTML/CSS/JS unless the logic is genuinely non-obvious
