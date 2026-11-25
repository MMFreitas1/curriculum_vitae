import html, pathlib
from content2 import *

ROOT = pathlib.Path(__file__).parent
FS = (ROOT / "node_modules").as_uri()
PORTRAIT = (ROOT.parent.parent / "assets/img/portrait.jpg").as_uri()
SURF = (ROOT.parent.parent / "assets/img/surf.jpg").as_uri()
e = html.escape


def links(pkgs):
    return "\n".join(f'<link rel="stylesheet" href="{FS}/{p}">' for p in pkgs)


def job(j, nowtag):
    out = ['<article class="job%s">' % (" short" if len(j["blocks"]) == 1 else "")]
    now = nowtag if j.get("now") else ""
    out.append(f'<header class="jh"><div><div class="org">{e(j["org"])}{now}</div><div class="role">{e(j["role"])}</div></div><div class="when">{e(j["when"])}</div></header>')
    if j.get("note"):
        out.append(f'<div class="note">{e(j["note"])}</div>')
    for lbl, txt in j["blocks"]:
        lab = f'<div class="lbl">{e(lbl)}</div>' if lbl else ""
        out.append(f'<div class="blk">{lab}<p>{e(txt)}</p></div>')
    if j.get("highlight"):
        out.append(f'<div class="hl">{e(j["highlight"])}</div>')
    if j.get("tags"):
        out.append('<div class="tags">' + "".join(f"<span>{e(t)}</span>" for t in j["tags"]) + "</div>")
    out.append("</article>")
    return "".join(out)


def common_body(nowtag, cover):
    work = "".join(job(j, nowtag) for j in WORK)
    beyond = "".join(job(j, nowtag) for j in BEYOND)
    edu = "".join(
        f'<div class="edu"><div class="gpa"><b>{g}</b><span>GPA</span></div><div><div class="ew">{e(w)}</div><div class="es">{e(s)} · {e(d)}</div><p>{e(t)}</p></div></div>'
        for w, s, d, g, t in EDUCATION)
    stack = "".join(
        f'<div class="grp"><div class="gh">{e(n)} <i>{len(items)}</i></div><div class="chips">' + "".join(f"<span>{e(x)}</span>" for x in items) + "</div></div>"
        for n, items in STACK)
    certs = "".join(f'<div class="cert"><div class="cn">{e(n)}</div><div class="cb">{e(b)} · {y}</div></div>' for n, b, y in CERTS)
    return f'''{cover}
<section class="sec"><h2><em>01</em>Experience</h2>{work}</section>
<section class="sec"><h2><em>02</em>Beyond the screen</h2>{beyond}</section>
<section class="sec keep"><h2><em>03</em>Education</h2>{edu}</section>
<section class="sec pb"><h2><em>04</em>Toolkit</h2><div class="stack">{stack}</div></section>
<section class="sec keep"><h2><em>05</em>Certificates</h2><div class="certs">{certs}</div></section>
<section class="sec keep closing"><img src="{SURF}" alt=""><p>{e(MANIFESTO)}</p><div class="sign">Miguel G.M. Freitas</div></section>'''


# ------------------------------------------------------------------ SOFT CLAY
R = "6px 6px 14px #C9BDB0, -6px -6px 14px #FFFFFF"
RL = "10px 10px 24px #C9BDB0, -10px -10px 24px #FFFFFF"
I = "inset 3px 3px 7px #C9BDB0, inset -3px -3px 7px #FFFFFF"


def clay():
    contact = "".join(f'<a class="pill" href="{u}"><b>{e(k)}</b>{e(v)}</a>' for k, v, u in CONTACT)
    now = "".join(f'<div class="nowrow"><span>{e(k)}</span>{e(v)}</div>' for k, v in NOW)
    key = "".join(f'<div class="kpi"><b>{e(v)}</b><span>{e(l)}</span></div>' for v, l in KEY)
    cover = f'''<section class="cover">
<div class="disc"><div class="well"><img src="{PORTRAIT}" alt=""></div></div>
<div class="kick">{e(KICKER)}</div>
<h1>{e(NAME_FIRST)} <span>{e(NAME_LAST)}</span></h1>
<p class="tag">{e(TAGLINE)}</p>
<div class="pills">{contact}</div>
<div class="duo"><div class="card"><h3><i></i>Right now</h3>{now}</div><div class="card"><h3><i></i>Key numbers</h3><div class="kpis">{key}</div></div></div>
</section>'''
    body = common_body('<span class="nowdot">NOW</span>', cover)
    fonts = links(["@fontsource/sora/600.css", "@fontsource/sora/700.css", "@fontsource/sora/800.css",
                   "@fontsource/manrope/400.css", "@fontsource/manrope/500.css", "@fontsource/manrope/600.css", "@fontsource/manrope/700.css",
                   "@fontsource/dm-mono/400.css", "@fontsource/dm-mono/500.css"])
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Miguel G.M. Freitas — CV</title>{fonts}<style>
@page{{size:A4;margin:18mm 0 16mm;background:#E6DED5;
  @bottom-center{{content:"Miguel G.M. Freitas  ·  " counter(page) " / " counter(pages);font:7pt 'DM Mono',monospace;color:#7A6B5F}}}}
@page:first{{margin:0;@bottom-center{{content:none}}}}
*{{box-sizing:border-box}}
html{{background:#E6DED5}}
body{{margin:0;font-family:Manrope,sans-serif;color:#2F2621;font-size:9.6pt;line-height:1.6;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
a{{color:inherit;text-decoration:none}}
p{{margin:0}}
.cover{{height:296mm;padding:20mm 20mm 0;display:flex;flex-direction:column;align-items:center;text-align:center;break-after:page;overflow:hidden}}
.disc{{width:62mm;height:62mm;border-radius:50%;display:flex;align-items:center;justify-content:center;box-shadow:{RL}}}
.well{{width:54mm;height:54mm;border-radius:50%;padding:2.4mm;box-shadow:inset 6px 6px 14px #C9BDB0,inset -6px -6px 14px #FFFFFF}}
.well img{{width:100%;height:100%;border-radius:50%;object-fit:cover;object-position:50% 38%;display:block}}
.kick{{margin-top:11mm;font-family:'DM Mono',monospace;font-size:8pt;letter-spacing:.16em;text-transform:uppercase;color:#11656B}}
h1{{margin:4mm 0 0;font-family:Sora,sans-serif;font-weight:800;font-size:34pt;line-height:1.02;letter-spacing:-.035em}}
h1 span{{color:#9C4A2A}}
.tag{{margin-top:6mm;max-width:140mm;font-size:11pt;line-height:1.65;color:#3E332C}}
.pills{{margin-top:8mm;display:flex;flex-wrap:wrap;justify-content:center;gap:3mm;max-width:160mm}}
.pill{{font-size:8pt;padding:2mm 4mm;border-radius:99px;box-shadow:{I};color:#3E332C}}
.pill b{{color:#11656B;margin-right:1.6mm}}
.duo{{margin-top:13mm;width:100%;display:grid;grid-template-columns:1fr 1fr;gap:9mm;text-align:left}}
.card{{border-radius:7mm;padding:7mm;box-shadow:{RL}}}
h3{{margin:0 0 4mm;font-family:Sora,sans-serif;font-weight:700;font-size:12pt;display:flex;align-items:center;gap:2.4mm}}
h3 i{{width:2.6mm;height:2.6mm;border-radius:50%;background:#11656B;display:inline-block}}
.nowrow{{padding:2.2mm 0;font-size:9pt;line-height:1.45;color:#3E332C}}
.nowrow span{{display:block;font-family:'DM Mono',monospace;font-size:7pt;letter-spacing:.12em;text-transform:uppercase;color:#9C4A2A}}
.kpis{{display:grid;grid-template-columns:1fr 1fr;gap:4mm}}
.kpi{{border-radius:5mm;padding:4mm;box-shadow:{I}}}
.kpi b{{display:block;font-family:Sora,sans-serif;font-weight:800;font-size:17pt;letter-spacing:-.03em;color:#9C4A2A;line-height:1.1}}
.kpi:nth-child(-n+2) b{{color:#11656B}}
.kpi span{{display:block;margin-top:1.4mm;font-size:7.6pt;line-height:1.4;color:#3E332C}}
.sec{{padding:0 20mm}}
.pb{{break-before:page}}
.keep{{break-inside:avoid}}
h2{{margin:0 0 8mm;font-family:Sora,sans-serif;font-weight:800;font-size:20pt;letter-spacing:-.03em;display:flex;align-items:baseline;gap:4mm}}
h2 em{{font-style:normal;font-family:'DM Mono',monospace;font-size:9pt;font-weight:500;color:#11656B;letter-spacing:.1em}}
.sec+.sec{{margin-top:12mm}}
.job{{border-radius:7mm;padding:7mm 8mm;margin:0 0 9mm;box-shadow:{RL};-webkit-box-decoration-break:clone;box-decoration-break:clone}}
.jh{{display:flex;justify-content:space-between;align-items:flex-start;gap:6mm;break-after:avoid}}
.short{{break-inside:avoid}}
.org{{font-family:Sora,sans-serif;font-weight:700;font-size:14pt;letter-spacing:-.02em;display:flex;align-items:center;gap:3mm}}
.nowdot{{font-family:'DM Mono',monospace;font-size:6.6pt;font-weight:500;letter-spacing:.12em;color:#FFFFFF;background:#11656B;border-radius:99px;padding:.6mm 2.2mm}}
.role{{margin-top:1mm;font-weight:700;font-size:9.6pt;color:#9C4A2A}}
.when{{flex:none;font-family:'DM Mono',monospace;font-size:7.6pt;color:#65574C;padding:1.6mm 3.4mm;border-radius:99px;box-shadow:{I};white-space:nowrap}}
.note{{margin-top:4mm;font-size:8.6pt;font-style:italic;color:#65574C}}
.blk{{margin-top:5mm;break-inside:avoid}}
.lbl{{display:inline-block;margin-bottom:2mm;font-family:'DM Mono',monospace;font-size:7.2pt;letter-spacing:.08em;text-transform:uppercase;color:#11656B;padding:1mm 3mm;border-radius:99px;box-shadow:{I}}}
.blk p{{color:#3E332C}}
.hl{{margin-top:5mm;padding:3.4mm 5mm;border-radius:4mm;box-shadow:{I};font-weight:700;font-size:9pt;line-height:1.5;color:#11656B;break-inside:avoid}}
.tags{{margin-top:5mm;display:flex;flex-wrap:wrap;gap:2mm}}
.tags span{{font-size:7.4pt;font-weight:600;color:#65574C;padding:1mm 3mm;border-radius:99px;background:#DED5CB}}
.edu{{display:flex;gap:7mm;align-items:flex-start;border-radius:7mm;padding:6mm 7mm;margin-bottom:7mm;box-shadow:{RL}}}
.gpa{{flex:none;width:19mm;height:19mm;border-radius:50%;box-shadow:{I};display:flex;flex-direction:column;align-items:center;justify-content:center}}
.gpa b{{font-family:Sora,sans-serif;font-weight:800;font-size:15pt;color:#9C4A2A;line-height:1}}
.gpa span{{font-family:'DM Mono',monospace;font-size:6pt;color:#65574C;letter-spacing:.1em}}
.ew{{font-family:Sora,sans-serif;font-weight:700;font-size:11.5pt}}
.es{{font-size:8.4pt;color:#65574C;margin:1mm 0 2.4mm}}
.edu p{{color:#3E332C}}
.stack{{display:grid;grid-template-columns:1fr 1fr;gap:8mm}}
.grp{{border-radius:7mm;padding:6mm;box-shadow:{RL};break-inside:avoid}}
.gh{{font-family:Sora,sans-serif;font-weight:700;font-size:11pt;display:flex;justify-content:space-between}}
.gh i{{font-style:normal;font-family:'DM Mono',monospace;font-size:8pt;color:#65574C}}
.chips{{margin-top:4mm;display:flex;flex-wrap:wrap;gap:2.4mm}}
.chips span{{font-size:7.8pt;font-weight:600;color:#3E332C;padding:1.4mm 3.2mm;border-radius:99px;box-shadow:{I}}}
.certs{{display:grid;grid-template-columns:1fr 1fr;gap:6mm}}
.cert{{border-radius:5mm;padding:4.5mm 5mm;box-shadow:{R}}}
.cn{{font-weight:700;font-size:9.6pt}}
.cb{{font-family:'DM Mono',monospace;font-size:7.4pt;color:#65574C;margin-top:.8mm}}
.closing{{margin-top:14mm !important;text-align:center}}
.closing img{{width:100%;height:78mm;object-fit:cover;border-radius:7mm;box-shadow:{RL};display:block}}
.closing p{{margin:9mm auto 0;max-width:140mm;font-family:Sora,sans-serif;font-weight:600;font-size:11pt;line-height:1.6;color:#3E332C}}
.sign{{margin-top:5mm;font-family:'DM Mono',monospace;font-size:8pt;letter-spacing:.14em;text-transform:uppercase;color:#9C4A2A}}
</style></head><body>{body}</body></html>'''


# ------------------------------------------------------------------ TIDE
def tide():
    contact = "".join(f'<a href="{u}"><span>{e(k)}</span>{e(v)}</a>' for k, v, u in CONTACT)
    now = "".join(f'<div class="nowrow"><span>{e(k)}</span>{e(v)}</div>' for k, v in NOW)
    key = "".join(f'<div class="kpi"><b>{e(v)}</b><span>{e(l)}</span></div>' for v, l in KEY)
    cover = f'''<section class="cover">
<div class="hero"><img src="{PORTRAIT}" alt=""><div class="shade"></div>
<div class="htxt"><div class="tagc">{e(KICKER.upper())}</div><h1>{e(NAME_FIRST)}<br>{e(NAME_LAST)}</h1></div></div>
<div class="cin">
<p class="tag">{e(TAGLINE)}</p>
<div class="contact">{contact}</div>
<div class="duo"><div><h3>Currently</h3>{now}</div><div><h3>Key numbers</h3><div class="kpis">{key}</div></div></div>
</div></section>'''
    body = common_body('<span class="nowtag">NOW</span>', cover)
    fonts = links(["@fontsource-variable/archivo/wdth.css",
                   "@fontsource/instrument-sans/400.css", "@fontsource/instrument-sans/500.css", "@fontsource/instrument-sans/600.css", "@fontsource/instrument-sans/700.css",
                   "@fontsource/ibm-plex-mono/400.css", "@fontsource/ibm-plex-mono/500.css"])
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Miguel G.M. Freitas — CV</title>{fonts}<style>
@page{{size:A4;margin:18mm 0 16mm;
  @bottom-center{{content:"MIGUEL G.M. FREITAS  —  " counter(page) " / " counter(pages);font:7pt 'IBM Plex Mono',monospace;color:#4A6168}}}}
@page:first{{margin:0;@bottom-center{{content:none}}}}
*{{box-sizing:border-box}}
body{{margin:0;font-family:'Instrument Sans',sans-serif;color:#0E2A30;font-size:9.6pt;line-height:1.6;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
a{{color:inherit;text-decoration:none}}
p{{margin:0}}
.cover{{height:296mm;break-after:page;overflow:hidden;position:relative}}
.hero{{position:relative;height:150mm;background:#000;overflow:hidden}}
.hero img{{width:100%;height:100%;object-fit:cover;object-position:50% 28%;display:block}}
.shade{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(6,20,23,0) 35%,rgba(6,20,23,.88) 100%)}}
.htxt{{position:absolute;left:20mm;bottom:12mm;color:#FFFFFF}}
.tagc{{display:inline-block;background:#FF6B4A;color:#2A0E06;font-family:'IBM Plex Mono',monospace;font-size:7.4pt;font-weight:500;letter-spacing:.12em;padding:1.4mm 3mm}}
h1{{margin:4mm 0 0;font-family:'Archivo Variable',sans-serif;font-weight:900;font-stretch:64%;font-size:58pt;line-height:.84;text-transform:uppercase}}
.cin{{padding:11mm 20mm 0}}
.tag{{font-size:12.5pt;line-height:1.55;color:#2C454B;max-width:155mm}}
.contact{{margin-top:7mm;display:flex;flex-wrap:wrap;gap:2mm 8mm;font-size:8.6pt;padding-bottom:7mm;border-bottom:1.6pt solid #0E2A30}}
.contact span{{font-family:'IBM Plex Mono',monospace;font-size:6.8pt;letter-spacing:.1em;text-transform:uppercase;color:#0F5F63;margin-right:2mm}}
.duo{{margin-top:8mm;display:grid;grid-template-columns:1fr 1.25fr;gap:12mm}}
h3{{margin:0 0 3mm;font-family:'Archivo Variable',sans-serif;font-weight:900;font-stretch:72%;font-size:15pt;text-transform:uppercase}}
.nowrow{{padding:2.2mm 0;border-top:1px solid #C9D6D4;font-size:9pt;line-height:1.4}}
.nowrow span{{display:block;font-family:'IBM Plex Mono',monospace;font-size:6.8pt;letter-spacing:.1em;text-transform:uppercase;color:#B93A1C}}
.kpis{{display:grid;grid-template-columns:1fr 1fr;column-gap:8mm}}
.kpi{{padding:2.4mm 0 3mm;border-top:1px solid #C9D6D4}}
.kpi b{{display:block;font-family:'Archivo Variable',sans-serif;font-weight:900;font-stretch:64%;font-size:26pt;line-height:1;color:#0F5F63}}
.kpi:nth-child(-n+2) b{{color:#B93A1C}}
.kpi span{{display:block;margin-top:1.2mm;font-size:7.8pt;line-height:1.4;color:#2C454B}}
.sec{{padding:0 20mm}}
.pb{{break-before:page}}
.keep{{break-inside:avoid}}
.sec+.sec{{margin-top:14mm}}
h2{{margin:0 0 2mm;padding-bottom:3mm;border-bottom:2pt solid #0E2A30;font-family:'Archivo Variable',sans-serif;font-weight:900;font-stretch:66%;font-size:30pt;line-height:.95;text-transform:uppercase;display:flex;align-items:baseline;gap:4mm}}
h2 em{{font-style:normal;font-family:'IBM Plex Mono',monospace;font-size:9pt;font-weight:500;color:#B93A1C}}
.job{{padding:7mm 0 8mm;border-bottom:1px solid #C9D6D4}}
.jh{{display:grid;grid-template-columns:1fr auto;gap:6mm;align-items:baseline;break-after:avoid}}
.short{{break-inside:avoid}}
.org{{font-family:'Archivo Variable',sans-serif;font-weight:800;font-stretch:80%;font-size:17pt;line-height:1.1;display:flex;align-items:center;gap:3mm}}
.nowtag{{font-family:'IBM Plex Mono',monospace;font-size:6.6pt;font-weight:500;letter-spacing:.12em;background:#FF6B4A;color:#2A0E06;padding:.4mm 1.8mm}}
.role{{margin-top:1mm;font-weight:700;font-size:9.8pt;color:#B93A1C}}
.when{{font-family:'IBM Plex Mono',monospace;font-size:8pt;color:#4A6168;white-space:nowrap}}
.note{{margin-top:4mm;padding-left:4mm;border-left:2pt solid #9FD3CF;font-size:8.8pt;font-style:italic;color:#4A6168}}
.blk{{margin-top:5mm;display:grid;grid-template-columns:36mm 1fr;gap:6mm;break-inside:avoid}}
.blk:not(:has(.lbl)){{grid-template-columns:1fr}}
.lbl{{font-family:'IBM Plex Mono',monospace;font-size:7.4pt;letter-spacing:.06em;text-transform:uppercase;color:#0F5F63;line-height:1.45;padding-top:.6mm}}
.blk p{{color:#2C454B}}
.hl{{margin-top:5mm;background:#E6F1EF;border-left:3pt solid #FF6B4A;padding:3.4mm 5mm;font-weight:600;font-size:9.2pt;line-height:1.5;color:#0E2A30;break-inside:avoid}}
.tags{{margin-top:4.5mm;font-family:'IBM Plex Mono',monospace;font-size:7.4pt;color:#4A6168;line-height:1.7}}
.tags span:not(:last-child)::after{{content:"  /  ";color:#9DB3B5}}
.edu{{display:grid;grid-template-columns:22mm 1fr;gap:6mm;padding:6mm 0;border-bottom:1px solid #C9D6D4}}
.gpa b{{display:block;font-family:'Archivo Variable',sans-serif;font-weight:900;font-stretch:62%;font-size:40pt;line-height:.9;color:#0F5F63}}
.gpa span{{font-family:'IBM Plex Mono',monospace;font-size:6.6pt;color:#4A6168;letter-spacing:.12em}}
.ew{{font-family:'Archivo Variable',sans-serif;font-weight:800;font-stretch:82%;font-size:13pt}}
.es{{font-size:8.6pt;color:#4A6168;margin:.6mm 0 2.4mm}}
.edu p{{color:#2C454B}}
.stack{{display:grid;grid-template-columns:1fr 1fr;column-gap:12mm}}
.grp{{padding:5mm 0;border-bottom:1px solid #C9D6D4;break-inside:avoid}}
.gh{{font-family:'Archivo Variable',sans-serif;font-weight:800;font-stretch:82%;font-size:12.5pt;display:flex;justify-content:space-between}}
.gh i{{font-style:normal;font-family:'IBM Plex Mono',monospace;font-size:8pt;color:#B93A1C}}
.chips{{margin-top:2mm;font-size:8.8pt;line-height:1.7;color:#2C454B}}
.chips span:not(:last-child)::after{{content:" · ";color:#9DB3B5}}
.certs{{display:grid;grid-template-columns:1fr 1fr;column-gap:12mm}}
.cert{{padding:4mm 0;border-bottom:1px solid #C9D6D4}}
.cn{{font-weight:700;font-size:10pt}}
.cb{{font-family:'IBM Plex Mono',monospace;font-size:7.6pt;color:#4A6168;margin-top:.6mm}}
.closing{{margin-top:16mm !important}}
.closing img{{width:100%;height:80mm;object-fit:cover;display:block}}
.closing p{{margin-top:7mm;font-family:'Archivo Variable',sans-serif;font-weight:700;font-stretch:85%;font-size:12.5pt;line-height:1.45}}
.sign{{margin-top:5mm;font-family:'IBM Plex Mono',monospace;font-size:8pt;letter-spacing:.14em;text-transform:uppercase;color:#B93A1C}}
</style></head><body>{body}</body></html>'''


if __name__ == "__main__":
    (ROOT / "clay.html").write_text(clay(), encoding="utf-8")
    (ROOT / "tide.html").write_text(tide(), encoding="utf-8")
    print("ok")
