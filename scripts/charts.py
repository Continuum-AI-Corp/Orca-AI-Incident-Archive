# -*- coding: utf-8 -*-
"""assets/*.svg - the three charts used by the README, in light and dark.

Kept in its own file so scripts/build.py can import it; it also runs
standalone:

    python scripts/charts.py
"""
import os, sys, io
from collections import Counter, OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets")

FONT = "ui-sans-serif,-apple-system,'Segoe UI','PingFang SC','Microsoft YaHei',sans-serif"
MONO = "ui-monospace,'SF Mono','Cascadia Mono','Consolas',monospace"

TYPE_EN = {
    "IPI": "Indirect prompt injection", "EXFIL": "Data exfiltration",
    "SUPPLY": "Supply-chain poisoning", "MCP": "MCP & tool-chain",
    "SANDBOX": "Sandbox escape", "ROGUE": "Rogue agent action",
    "WEAPON": "Agent as a weapon", "INFRA": "Infrastructure exposure",
    "CRED": "Credential abuse", "EVAL": "Evaluation-environment breakout",
    "GOV": "Governance & policy", "OTHER": "Other",
}
SEV_EN = {"critical": "Critical", "high": "High", "medium": "Medium",
          "low": "Low", "info": "Info"}
KIND_EN = {"incident": "Incident", "vulnerability": "Vulnerability disclosure",
           "research": "Research demo", "report": "Threat report",
           "policy": "Policy & regulation"}

# Severity is an ordered quantity, so the palette is a single-hue ramp
# (monotonically decreasing lightness) rather than a categorical palette;
# dark mode reverses the direction to fit the dark background.
TH = {
    "light": dict(bg="#FFFFFF", ink="#141A1C", ink2="#48545A", ink3="#7A868C",
                  rule="#D2D8D8", mark="#B08528", markq="#E0CDA0",
                  sev={"critical": "#88091D", "high": "#B23B40", "medium": "#D26F6E",
                       "low": "#E9A4A1", "info": "#9FA6AA"}),
    "dark":  dict(bg="#171E21", ink="#E4E9E9", ink2="#9AA8AD", ink3="#6B787E",
                  rule="#2B383D", mark="#D6A94A", markq="#5C4A24",
                  sev={"critical": "#F88684", "high": "#D66060", "medium": "#AC4244",
                       "low": "#7B3031", "info": "#6B7175"}),
}


def on(hexc):
    """Readable text colour on top of a swatch (relative luminance)."""
    r, g, b = (int(hexc[i:i+2], 16) / 255 for i in (1, 3, 5))
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    lum = 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)
    return "#101617" if lum > 0.36 else "#FFFFFF"


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def tw(s, size=10.5):
    """Rough text width estimate for mixed-case Latin text."""
    return len(str(s)) * size * 0.56


def svg(w, h, body, t):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
            f'width="{w}" height="{h}" role="img" font-family="{FONT}">\n'
            f'<rect width="{w}" height="{h}" fill="{t["bg"]}"/>\n{body}\n</svg>\n')


def write(name, w, h, fn):
    for mode, t in TH.items():
        io.open(os.path.join(OUT, f"{name}-{mode}.svg"), "w", encoding="utf-8",
                newline="\n").write(svg(w, h, fn(t), t))


def build(rows):
    os.makedirs(OUT, exist_ok=True)
    total = len(rows)

    months = OrderedDict()
    for r in sorted(rows, key=lambda x: x["_month"]):
        months[r["_month"]] = months.get(r["_month"], 0) + 1
    MON = list(months.items())

    def chart_monthly(t):
        W, H = 900, 312
        L, R, T, B = 40, 16, 30, 62
        pw, ph = W - L - R, H - T - B
        mx = max(v for _, v in MON)
        n = len(MON)
        gap = 5
        bw = (pw - gap * (n - 1)) / n
        o = []
        o.append(f'<text x="{L}" y="18" font-size="13" font-weight="700" fill="{t["ink"]}">'
                 f'Records per month \u00b7 {MON[0][0]} \u2192 {MON[-1][0]}</text>')
        o.append(f'<text x="{W-R}" y="18" font-size="11" text-anchor="end" fill="{t["ink3"]}" '
                 f'font-family="{MONO}">n = {sum(v for _,v in MON)}</text>')
        # grid
        for gv in range(0, mx + 1, 10):
            y = T + ph - ph * gv / mx
            o.append(f'<line x1="{L}" y1="{y:.1f}" x2="{W-R}" y2="{y:.1f}" stroke="{t["rule"]}" stroke-width="1"/>')
            o.append(f'<text x="{L-7}" y="{y+3.5:.1f}" font-size="10" text-anchor="end" '
                     f'fill="{t["ink3"]}" font-family="{MONO}">{gv}</text>')
        # year dividers
        for i, (m, _) in enumerate(MON):
            if i and m.endswith("-01"):
                x = L + i * (bw + gap) - gap / 2
                o.append(f'<line x1="{x:.1f}" y1="{T-4}" x2="{x:.1f}" y2="{T+ph+18}" '
                         f'stroke="{t["ink3"]}" stroke-width="1" stroke-dasharray="3 3"/>')
                o.append(f'<text x="{x+6:.1f}" y="{T+ph+29:.1f}" font-size="10.5" font-weight="700" '
                         f'fill="{t["ink2"]}" font-family="{MONO}">{m[:4]}</text>')
        for i, (m, v) in enumerate(MON):
            x = L + i * (bw + gap)
            bh = ph * v / mx
            y = T + ph - bh
            peak = v == mx
            o.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{bh:.1f}" rx="3" '
                     f'fill="{t["mark"] if peak else t["markq"]}"/>')
            if peak or v >= 20 or i in (0, n - 1):
                o.append(f'<text x="{x+bw/2:.1f}" y="{y-5:.1f}" font-size="10" text-anchor="middle" '
                         f'fill="{t["ink"] if peak else t["ink2"]}" font-family="{MONO}" '
                         f'font-weight="{"700" if peak else "500"}">{v}</text>')
            o.append(f'<text x="{x+bw/2:.1f}" y="{T+ph+14:.1f}" font-size="9" text-anchor="middle" '
                     f'fill="{t["ink3"]}" font-family="{MONO}">{m[5:]}</text>')
        o.append(f'<line x1="{L}" y1="{T+ph}" x2="{W-R}" y2="{T+ph}" stroke="{t["ink3"]}" stroke-width="1"/>')
        o.append(f'<text x="{L}" y="{T+ph+29:.1f}" font-size="10.5" font-weight="700" '
                 f'fill="{t["ink3"]}" font-family="{MONO}">{MON[0][0][:4]}</text>')
        years = sorted({m[:4] for m, _ in MON})
        by_year = {y: sum(v for m, v in MON if m.startswith(y)) for y in years}
        parts = []
        for j, y in enumerate(years):
            label = f"{y} ({by_year[y]})" if j == len(years) - 1 else f"{y} full year {by_year[y]}"
            parts.append(label)
        pk = [m for m, v in MON if v == mx][0]
        o.append(f'<text x="{L}" y="{H-10}" font-size="10" fill="{t["ink3"]}">'
                 f'{" \u00b7 ".join(parts)}. Peak {mx} in {pk}</text>')
        return "\n".join(o)

    write("monthly", 900, 312, chart_monthly)

    # ============================================================ 2. by type
    tc = Counter(t for r in rows for t in r["type"])
    TYPES = tc.most_common()

    def chart_types(t):
        W = 900
        rowh, T, B, L = 22, 34, 38, 210
        H = T + rowh * len(TYPES) + B
        pw = W - L - 62
        mx = max(v for _, v in TYPES)
        o = [f'<text x="16" y="18" font-size="13" font-weight="700" fill="{t["ink"]}">'
             f'Distribution by type (a record can carry several, so totals exceed {total})</text>']
        for i, (ty, v) in enumerate(TYPES):
            y = T + i * rowh
            bw = pw * v / mx
            o.append(f'<text x="16" y="{y+13}" font-size="11" '
                     f'fill="{t["ink"]}" font-family="{MONO}" font-weight="600">{ty}</text>')
            o.append(f'<text x="{L-11}" y="{y+13}" font-size="10.5" text-anchor="end" '
                     f'fill="{t["ink3"]}">{esc(TYPE_EN.get(ty, ty))}</text>')
            o.append(f'<rect x="{L}" y="{y+3}" width="{bw:.1f}" height="13" rx="3" fill="{t["mark"]}"/>')
            o.append(f'<text x="{L+bw+7:.1f}" y="{y+13.5}" font-size="10.5" fill="{t["ink2"]}" '
                     f'font-family="{MONO}">{v}</text>')
        top = " \u00b7 ".join(f"{k} {v}" for k, v in TYPES[:3])
        o.append(f'<text x="16" y="{H-13}" font-size="10" fill="{t["ink3"]}">'
                 f'Top three: {top}. GOV runs high because the archive also records regulatory and '
                 f'vendor policy moves (kind=policy, excluded from incident counts)</text>')
        return chr(10).join(o)

    write("by-type", 900, 34 + 22 * len(TYPES) + 38, chart_types)

    # ============================================================ 3. severity + kind
    sev = Counter(r["severity"] for r in rows)
    SEVO = ["critical", "high", "medium", "low", "info"]
    kind = Counter(r["kind"] for r in rows)
    harm = Counter(str(r["real_harm"]) for r in rows)

    def chart_severity(t):
        W, H = 900, 216
        L, R = 16, 16
        pw = W - L - R
        o = [f'<text x="{L}" y="18" font-size="13" font-weight="700" fill="{t["ink"]}">'
             f'{total} records by severity and kind</text>']
        # severity bar
        y = 40
        o.append(f'<text x="{L}" y="{y-6}" font-size="10.5" fill="{t["ink2"]}" font-weight="600">Severity</text>')
        x = L
        for s in SEVO:
            v = sev.get(s, 0)
            if not v:
                continue
            w = pw * v / total
            o.append(f'<rect x="{x:.1f}" y="{y}" width="{max(w-2,1):.1f}" height="26" rx="3" '
                     f'fill="{t["sev"][s]}"/>')
            if w > 54:
                o.append(f'<text x="{x+w/2-1:.1f}" y="{y+17}" font-size="10.5" text-anchor="middle" '
                         f'font-family="{MONO}" font-weight="700" fill="{on(t["sev"][s])}">{v}</text>')
            x += w
        # legend
        y2 = y + 36
        lx = L
        for s in SEVO:
            v = sev.get(s, 0)
            label = f"{SEV_EN[s]} {s} \u00b7 {v}"
            o.append(f'<rect x="{lx}" y="{y2-9}" width="10" height="10" rx="2" fill="{t["sev"][s]}"/>')
            o.append(f'<text x="{lx+15}" y="{y2}" font-size="10.5" fill="{t["ink2"]}">'
                     f'{esc(label)}</text>')
            lx += 15 + tw(label) + 26
        # kind bar
        y3 = y2 + 34
        o.append(f'<text x="{L}" y="{y3-6}" font-size="10.5" fill="{t["ink2"]}" font-weight="600">Kind</text>')
        KO = ["incident", "vulnerability", "research", "report", "policy"]
        ramp = [t["sev"]["critical"], t["sev"]["high"], t["sev"]["medium"], t["sev"]["low"], t["sev"]["info"]]
        x = L
        for i, k in enumerate(KO):
            v = kind.get(k, 0)
            w = pw * v / total
            o.append(f'<rect x="{x:.1f}" y="{y3}" width="{max(w-2,1):.1f}" height="26" rx="3" fill="{ramp[i]}"/>')
            if w > 54:
                o.append(f'<text x="{x+w/2-1:.1f}" y="{y3+17}" font-size="10.5" text-anchor="middle" '
                         f'font-family="{MONO}" font-weight="700" fill="{on(ramp[i])}">{v}</text>')
            x += w
        y4 = y3 + 36
        lx = L
        for i, k in enumerate(KO):
            label = f"{KIND_EN[k]} \u00b7 {kind.get(k,0)}"
            o.append(f'<rect x="{lx}" y="{y4-9}" width="10" height="10" rx="2" fill="{ramp[i]}"/>')
            o.append(f'<text x="{lx+15}" y="{y4}" font-size="10.5" fill="{t["ink2"]}">'
                     f'{esc(label)}</text>')
            lx += 15 + tw(label) + 26
        o.append(f'<text x="{L}" y="{H-10}" font-size="10" fill="{t["ink3"]}">'
                 f'{harm.get("True",0)} with a confirmed victim, {harm.get("False",0)} research demos or '
                 f'no in-the-wild use, {harm.get("None",0)} policy and intelligence reports (not applicable)</text>')
        return "\n".join(o)

    write("severity", 900, 216, chart_severity)

    return sorted(os.listdir(OUT))


if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from orca import load_all
    print(chr(10).join(build(load_all())))
