"""Builds the plain, single-column CV for screening systems (ATS / AI parsers) and prints it with headless Chrome.

Usage: python3 build_ats.py  ->  assets/cv/Miguel-Freitas-CV-ATS.pdf
"""
import html
import pathlib
import re
import subprocess

from content2 import CERTS, CONTACT, EDUCATION, KEY, STACK, WORK, BEYOND

ROOT = pathlib.Path(__file__).parent
OUT = ROOT.parent.parent / "assets/cv/Miguel-Freitas-CV-ATS.pdf"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
WEBSITE = ("mmfreitas1.github.io/curriculum_vitae", "https://mmfreitas1.github.io/curriculum_vitae/")
APPS = ("Built and use two apps daily: AI-ML Refresher (SwiftUI, C#/.NET Avalonia, Kotlin Jetpack Compose — macOS, Windows, Android) "
        "and 3D S&P 500 Visualizer (decades of S&P 500 history as an interactive 3D sector cube, with an analyst assistant).")
SUMMARY = ("AI / ML Engineer in Porto, Portugal. From managing Mediterranean shipping lanes to architecting AI systems — "
           "RAG and multi-agent platforms, document-processing pipelines with OCR and VLMs, forecasting at 2,000+ products, "
           "and data engineering on Azure, BigQuery and Oracle.")


def t(s):
    # Hyphenated words are kept on one line: parsers otherwise join "GPT-" + "5.4" into "GPT5.4".
    return re.sub(r"(\S*-\S*)", r'<span class="nw">\1</span>', html.escape(s))


def role(r, extra=None):
    items = []
    if r.get("note"):
        items.append(t(r["note"]))
    for head, body in r["blocks"]:
        items.append((f"<b>{t(head.replace(' · ', ' — '))}:</b> " if head else "") + t(body))
    if extra:
        items.append(t(extra))
    if r.get("highlight") and not extra:
        items.append(t(r["highlight"]))
    lis = "".join(f"<li>{i}</li>" for i in items)
    skills = f'<p class="skills">Skills: {t(", ".join(r["tags"]))}</p>' if r.get("tags") else ""
    title = t(r["role"].replace(" · ", ", "))
    return (f'<section class="job"><h3>{title} — {t(r["org"])}</h3>'
            f'<p class="when">{t(r["when"].replace(" — ", " – ").replace(" · ", ", "))}</p><ul>{lis}</ul>{skills}</section>')


def page():
    contact = CONTACT[:4] + [("Website", *WEBSITE)]
    contact_html = " | ".join(f'<a href="{html.escape(u)}">{t(v if k != "LinkedIn" else "linkedin.com/" + v)}</a>' for k, v, u in contact)
    jobs = "".join(role(r, APPS if r["org"] == "MF Concepts" else None) for r in WORK)
    other = "".join(role(r) for r in BEYOND)
    edu = "".join(
        f'<section class="job"><h3>{t(d)} — {t(s)}</h3><p class="when">{t(w.replace(" — ", " – "))} | Final grade: {g}/20</p><p>{t(txt)}</p></section>'
        for d, s, w, g, txt in EDUCATION)
    skills = "".join(f"<li><b>{t(name)}:</b> {t(', '.join(items))}</li>" for name, items in STACK)
    certs = "".join(f"<li>{t(n)} — {t(by)}, {y}</li>" for n, by, y in CERTS)
    key = "".join(f"<li>{t(v)} {t(l)}</li>" for v, l in KEY)
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Miguel G.M. Freitas — CV</title>
<style>
@page {{ size: A4; margin: 16mm 17mm; }}
body {{ font: 10pt/1.42 Arial, Helvetica, sans-serif; color: #111; margin: 0; }}
h1 {{ font-size: 20pt; margin: 0; }}
.headline {{ margin: 2pt 0 4pt; font-size: 11pt; }}
.contact {{ margin: 0; font-size: 9.5pt; }}
a {{ color: #111; text-decoration: none; }}
h2 {{ font-size: 11.5pt; text-transform: uppercase; letter-spacing: .04em; border-bottom: 1px solid #999; padding-bottom: 2pt; margin: 13pt 0 6pt; }}
h3 {{ font-size: 10.5pt; margin: 0; }}
.job {{ margin: 0 0 9pt; }}
.when {{ margin: 0 0 3pt; color: #333; }}
ul {{ margin: 0; padding-left: 14pt; }}
li {{ margin: 0 0 2.5pt; }}
p {{ margin: 0 0 3pt; }}
.skills {{ color: #333; margin-top: 3pt; }}
.nw {{ white-space: nowrap; }}
h2, h3 {{ break-after: avoid; }}
.when {{ break-after: avoid; }}
</style></head><body>
<header>
<h1>Miguel G.M. Freitas</h1>
<p class="headline">AI / ML Engineer — Porto, Portugal</p>
<p class="contact">{contact_html}</p>
</header>
<h2>Summary</h2>
<p>{t(SUMMARY)}</p>
<ul>{key}</ul>
<h2>Experience</h2>
{jobs}
<h2>Education</h2>
{edu}
<h2>Skills</h2>
<ul>{skills}</ul>
<h2>Certificates</h2>
<ul>{certs}</ul>
<h2>Other experience</h2>
{other}
</body></html>"""


if __name__ == "__main__":
    src = ROOT / "ats.html"
    src.write_text(page(), encoding="utf-8")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--export-tagged-pdf",
                    "--generate-pdf-document-outline", f"--print-to-pdf={OUT}", src.as_uri()],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"Wrote {OUT}")
