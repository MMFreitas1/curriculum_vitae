"""Soft Clay PDFs with vector-only shadows (no blurred box-shadows, which Chrome rasterises
into soft-mask images that some PDF viewers draw as flat squares)."""
import pathlib
from build2 import common_body, links, e, PORTRAIT, ROOT
from content2 import *


def stack(dx, dy, n, rgb, alpha, inset=False):
    pre = "inset " if inset else ""
    return ",".join(f"{pre}{dx * k:.1f}px {dy * k:.1f}px 0 rgba({rgb},{alpha})" for k in range(1, n + 1))


def shadows(P):
    d, l = P["dark"], "255,255,255"
    return {
        "R": stack(1.2, 1.2, 5, d, 0.055) + "," + stack(-1, -1, 4, l, 0.22),
        "RL": stack(1.6, 1.6, 7, d, 0.05) + "," + stack(-1.4, -1.4, 5, l, 0.2),
        "I": stack(1, 1, 3, d, 0.09, True) + "," + stack(-1, -1, 2, l, 0.45, True),
    }


SOFT = dict(name="soft", base="#E6DED5", dark="140,118,98", text="#2F2621", body="#3E332C", muted="#65574C",
            accent="#9C4A2A", punch="#11656B", glow="#11656B", tagbg="#DED5CB", tagfg="#65574C", namefg="#2F2621",
            hlbg=None, hlfg="#11656B", kpi2="#9C4A2A", rule="#D6CABD")
PUNCH = dict(name="punch", base="#F1DFCE", dark="170,118,82", text="#2B1D16", body="#3D2A20", muted="#6B5244",
             accent="#A3361A", punch="#0B7A85", glow="#14B8A6", tagbg="#F7C9A0", tagfg="#5A2A12", namefg="#C94A1C",
             hlbg="#0B7A85", hlfg="#FFFFFF", kpi2="#C94A1C", rule="#E2C6AE")


def clay(P):
    S = shadows(P)
    R, RL, I = S["R"], S["RL"], S["I"]
    contact = "".join(f'<a class="pill" href="{u}"><b>{e(k)}</b>{e(v)}</a>' for k, v, u in CONTACT)
    now = "".join(f'<div class="nowrow"><span>{e(k)}</span>{e(v)}</div>' for k, v in NOW)
    key = "".join(f'<div class="kpi"><b>{e(v)}</b><span>{e(l)}</span></div>' for v, l in KEY)
    cover = f'''<section class="cover">
<div class="disc"><div class="ring"><div class="well"><img src="{PORTRAIT}" alt=""></div></div></div>
<div class="kick">{e(KICKER)}</div>
<h1>{e(NAME_FIRST)} <span>{e(NAME_LAST)}</span></h1>
<p class="tag">{e(TAGLINE)}</p>
<div class="pills">{contact}</div>
<div class="duo"><div class="card nowcard"><h3><i></i>Right now</h3>{now}</div><div class="card"><h3><i></i>Key numbers</h3><div class="kpis">{key}</div></div></div>
</section>'''
    body = common_body('<span class="nowdot">NOW</span>', cover)
    fonts = links(["@fontsource/sora/600.css", "@fontsource/sora/700.css", "@fontsource/sora/800.css",
                   "@fontsource/manrope/400.css", "@fontsource/manrope/500.css", "@fontsource/manrope/600.css", "@fontsource/manrope/700.css",
                   "@fontsource/dm-mono/400.css", "@fontsource/dm-mono/500.css"])
    hl = (f"background:{P['hlbg']};color:{P['hlfg']};" if P["hlbg"] else f"box-shadow:{I};color:{P['hlfg']};")
    nowcard = (f".nowcard{{background:{P['punch']};box-shadow:{RL};color:#FFFFFF}}.nowcard h3 i{{background:#FFD3A8}}.nowcard .nowrow{{color:#FFFFFF}}.nowcard .nowrow span{{color:#FFD3A8}}"
               if P["name"] == "punch" else "")
    ring = (f"background:conic-gradient({P['glow']} 0 72%, {P['rule']} 72% 100%);" if P["name"] == "punch" else "")
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Miguel G.M. Freitas — CV</title>{fonts}<style>
@page{{size:A4;margin:18mm 0 16mm;background:{P['base']};
  @bottom-center{{content:"Miguel G.M. Freitas  ·  " counter(page) " / " counter(pages);font:7pt 'DM Mono',monospace;color:{P['muted']}}}}}
@page:first{{margin:0;@bottom-center{{content:none}}}}
*{{box-sizing:border-box}}
html{{background:{P['base']}}}
body{{margin:0;font-family:Manrope,sans-serif;color:{P['text']};font-size:9.6pt;line-height:1.6;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
a{{color:inherit;text-decoration:none}}
p{{margin:0}}
.cover{{height:296mm;padding:20mm 20mm 0;display:flex;flex-direction:column;align-items:center;text-align:center;break-after:page;overflow:hidden}}
.disc{{width:64mm;height:64mm;border-radius:50%;display:flex;align-items:center;justify-content:center;background:{P['base']};box-shadow:{RL}}}
.ring{{width:57mm;height:57mm;border-radius:50%;display:flex;align-items:center;justify-content:center;{ring}}}
.well{{width:54mm;height:54mm;border-radius:50%;padding:2.2mm;background:{P['base']};box-shadow:{I}}}
.well img{{width:100%;height:100%;border-radius:50%;object-fit:cover;object-position:50% 38%;display:block}}
.kick{{margin-top:11mm;font-family:'DM Mono',monospace;font-size:8pt;letter-spacing:.16em;text-transform:uppercase;color:{P['punch']}}}
h1{{margin:4mm 0 0;font-family:Sora,sans-serif;font-weight:800;font-size:34pt;line-height:1.02;letter-spacing:-.035em;color:{P['namefg']}}}
h1 span{{color:{P['accent']}}}
.tag{{margin-top:6mm;max-width:140mm;font-size:11pt;line-height:1.65;color:{P['body']}}}
.pills{{margin-top:8mm;display:flex;flex-wrap:wrap;justify-content:center;gap:3mm;max-width:165mm}}
.pill{{font-size:8pt;padding:2mm 4mm;border-radius:99px;box-shadow:{I};color:{P['body']}}}
.pill b{{color:{P['punch']};margin-right:1.6mm}}
.duo{{margin-top:13mm;width:100%;display:grid;grid-template-columns:1fr 1fr;gap:9mm;text-align:left}}
.card{{border-radius:7mm;padding:7mm;box-shadow:{RL}}}
h3{{margin:0 0 4mm;font-family:Sora,sans-serif;font-weight:700;font-size:12pt;display:flex;align-items:center;gap:2.4mm}}
h3 i{{width:2.6mm;height:2.6mm;border-radius:50%;background:{P['punch']};display:inline-block}}
.nowrow{{padding:2.2mm 0;font-size:9pt;line-height:1.45;color:{P['body']}}}
.nowrow span{{display:block;font-family:'DM Mono',monospace;font-size:7pt;letter-spacing:.12em;text-transform:uppercase;color:{P['accent']}}}
{nowcard}
.kpis{{display:grid;grid-template-columns:1fr 1fr;gap:4mm}}
.kpi{{border-radius:5mm;padding:4mm;box-shadow:{I}}}
.kpi b{{display:block;font-family:Sora,sans-serif;font-weight:800;font-size:17pt;letter-spacing:-.03em;color:{P['kpi2']};line-height:1.1}}
.kpi:nth-child(-n+2) b{{color:{P['punch']}}}
.kpi span{{display:block;margin-top:1.4mm;font-size:7.6pt;line-height:1.4;color:{P['body']}}}
.sec{{padding:0 20mm}}
.pb{{break-before:page}}
.keep{{break-inside:avoid}}
h2{{margin:0 0 8mm;font-family:Sora,sans-serif;font-weight:800;font-size:20pt;letter-spacing:-.03em;display:flex;align-items:baseline;gap:4mm}}
h2 em{{font-style:normal;font-family:'DM Mono',monospace;font-size:9pt;font-weight:500;color:{P['punch']};letter-spacing:.1em}}
.sec+.sec{{margin-top:12mm}}
.job{{border-radius:7mm;padding:7mm 8mm;margin:0 0 9mm;box-shadow:{RL};-webkit-box-decoration-break:clone;box-decoration-break:clone}}
.jh{{display:flex;justify-content:space-between;align-items:flex-start;gap:6mm;break-after:avoid}}
.short{{break-inside:avoid}}
.org{{font-family:Sora,sans-serif;font-weight:700;font-size:14pt;letter-spacing:-.02em;display:flex;align-items:center;gap:3mm}}
.nowdot{{font-family:'DM Mono',monospace;font-size:6.6pt;font-weight:500;letter-spacing:.12em;color:#FFFFFF;background:{P['punch']};border-radius:99px;padding:.6mm 2.2mm}}
.role{{margin-top:1mm;font-weight:700;font-size:9.6pt;color:{P['accent']}}}
.when{{flex:none;font-family:'DM Mono',monospace;font-size:7.6pt;color:{P['muted']};padding:1.6mm 3.4mm;border-radius:99px;box-shadow:{I};white-space:nowrap}}
.note{{margin-top:4mm;font-size:8.6pt;font-style:italic;color:{P['muted']}}}
.blk{{margin-top:5mm;break-inside:avoid}}
.lbl{{display:inline-block;margin-bottom:2mm;font-family:'DM Mono',monospace;font-size:7.2pt;letter-spacing:.08em;text-transform:uppercase;color:{P['punch']};padding:1mm 3mm;border-radius:99px;box-shadow:{I}}}
.blk p{{color:{P['body']}}}
.hl{{margin-top:5mm;padding:3.4mm 5mm;border-radius:4mm;{hl}font-weight:700;font-size:9pt;line-height:1.5;break-inside:avoid}}
.tags{{margin-top:5mm;display:flex;flex-wrap:wrap;gap:2mm}}
.tags span{{font-size:7.4pt;font-weight:600;color:{P['tagfg']};padding:1mm 3mm;border-radius:99px;background:{P['tagbg']}}}
.edu{{display:flex;gap:7mm;align-items:flex-start;border-radius:7mm;padding:6mm 7mm;margin-bottom:7mm;box-shadow:{RL}}}
.gpa{{flex:none;width:19mm;height:19mm;border-radius:50%;box-shadow:{I};display:flex;flex-direction:column;align-items:center;justify-content:center}}
.gpa b{{font-family:Sora,sans-serif;font-weight:800;font-size:15pt;color:{P['accent']};line-height:1}}
.gpa span{{font-family:'DM Mono',monospace;font-size:6pt;color:{P['muted']};letter-spacing:.1em}}
.ew{{font-family:Sora,sans-serif;font-weight:700;font-size:11.5pt}}
.es{{font-size:8.4pt;color:{P['muted']};margin:1mm 0 2.4mm}}
.edu p{{color:{P['body']}}}
.stack{{display:grid;grid-template-columns:1fr 1fr;gap:8mm}}
.grp{{border-radius:7mm;padding:6mm;box-shadow:{RL};break-inside:avoid}}
.gh{{font-family:Sora,sans-serif;font-weight:700;font-size:11pt;display:flex;justify-content:space-between}}
.gh i{{font-style:normal;font-family:'DM Mono',monospace;font-size:8pt;color:{P['muted']}}}
.chips{{margin-top:4mm;display:flex;flex-wrap:wrap;gap:2.4mm}}
.chips span{{font-size:7.8pt;font-weight:600;color:{P['body']};padding:1.4mm 3.2mm;border-radius:99px;box-shadow:{I}}}
.certs{{display:grid;grid-template-columns:1fr 1fr;gap:6mm}}
.cert{{border-radius:5mm;padding:4.5mm 5mm;box-shadow:{R}}}
.cn{{font-weight:700;font-size:9.6pt}}
.cb{{font-family:'DM Mono',monospace;font-size:7.4pt;color:{P['muted']};margin-top:.8mm}}
.closing{{margin-top:14mm !important;text-align:center}}
.closing img{{width:100%;height:78mm;object-fit:cover;border-radius:7mm;box-shadow:{RL};display:block}}
.closing p{{margin:9mm auto 0;max-width:140mm;font-family:Sora,sans-serif;font-weight:600;font-size:11pt;line-height:1.6;color:{P['body']}}}
.sign{{margin-top:5mm;font-family:'DM Mono',monospace;font-size:8pt;letter-spacing:.14em;text-transform:uppercase;color:{P['accent']}}}
</style></head><body>{body}</body></html>'''


if __name__ == "__main__":
    (ROOT / "clay.html").write_text(clay(SOFT), encoding="utf-8")
    print("ok")
