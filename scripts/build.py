# -*- coding: utf-8 -*-
"""Rebuild every derived artifact from the frontmatter in incidents/**/*.md.

    python scripts/build.py

Rewrites:
    incidents/YYYY-MM/README.md   between <!-- BEGIN:summary --> and <!-- BEGIN:nav -->
    incidents/README.md           between <!-- BEGIN:index -->
    topics/*.md - regions/*.md    between <!-- BEGIN:incidents -->
    README.md                     the badges / months / critical sections
    docs/i18n/README.*.md         same sections, localized
    dist/incidents.json - .csv - stats.json - sources.txt
    assets/*.svg  and the data block in index.html

Prose outside the BEGIN/END markers is never touched.  To change a record,
edit the source file under incidents/.
"""
import os, re, io, sys, json, csv, glob
from collections import Counter, OrderedDict
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from orca import (ROOT, INCIDENTS, load_all, load_mirrors, localized, badge,
                  SEV_COLOR, SEV_ORDER, KIND_SLOTS, SEV_SLOTS, RECORD_LANGS)
from l10n import LANGS, TYPE_NAME, REGION_NAME, SEV_NAME, KIND_NAME, name, LABELS
import charts
import page_data
from readme_i18n import README_L10N

rows = load_all()
MIRRORS = load_mirrors("zh")
TOTAL = len(rows)
MONTHS = sorted({r["_month"] for r in rows})
BYM = OrderedDict((m, [r for r in rows if r["_month"] == m]) for m in MONTHS)
sev = Counter(r["severity"] for r in rows)
kind = Counter(r["kind"] for r in rows)
tc = Counter(t for r in rows for t in r["type"])
gc = Counter(r["confidence"] for r in rows)
rcnt = Counter(x for r in rows for x in r["region"])
harm = Counter("true" if r["real_harm"] else ("false" if r["real_harm"] is False else "null")
               for r in rows)
ai = Counter(r["ai_involvement"] for r in rows)
URLS = sorted({s["url"] for r in rows for s in r["sources"]})
NLINKS = sum(len(r["sources"]) for r in rows)
CRIT = [r for r in rows if r["severity"] == "critical"]
LAST = max(r["date"] for r in rows)
FIRST = min(r["date"] for r in rows)
BUILD = os.environ.get("ORCA_BUILD_DATE", LAST)

EN = LABELS["en"]
TABLE_HEAD = (f"| {EN['date']} | {EN['record']} | {EN['type']} | {EN['severity']} | "
              f"{EN['confidence']} | {EN['harm']} |\n|---|---|---|---|---|---|")
sev_cell = lambda s: f"**{name(SEV_NAME, s, 'en')}**" if s in ("critical", "high") else name(SEV_NAME, s, "en")
harm_cell = lambda h: "\u2705" if h else ("\u2014" if h is False else "\u00b7")


def en_title(r):
    return str(r.get("title") or "")


def splice(path, marker, new):
    """Replace the content between <!-- BEGIN:marker --> and its END marker."""
    p = os.path.join(ROOT, path)
    t = io.open(p, encoding="utf-8").read()
    a, b = f"<!-- BEGIN:{marker} -->", f"<!-- END:{marker} -->"
    i, j = t.find(a), t.find(b)
    if i < 0 or j < 0:
        raise SystemExit(f"{path}: marker not found: {a} / {b}")
    if t.count("\n", i, j) == 0:          # BEGIN and END on one line -> inline replace
        out = t[:i + len(a)] + new.strip() + t[j:]
    else:
        out = t[:i + len(a)] + "\n" + new.strip("\n") + "\n" + t[j:]
    if out != t:
        io.open(p, "w", encoding="utf-8", newline="\n").write(out)
        return True
    return False


def W(path, text):
    p = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(p) or ".", exist_ok=True)
    io.open(p, "w", encoding="utf-8", newline="\n").write(text.rstrip() + "\n")


changed = []

# ---------------------------------------------------------- monthly indexes
for i, m in enumerate(MONTHS):
    rs = sorted(BYM[m], key=lambda r: (r["date"], SEV_ORDER[r["severity"]]))
    s = Counter(r["severity"] for r in rs)
    o = [f"**{len(rs)}** {EN['records']}", ""]
    o.append(f'![{EN["records"]}]({badge(EN["records"], str(len(rs)), "48545A")}) '
             + " ".join(f'![{k}]({badge(name(SEV_NAME, k, "en"), str(s[k]), SEV_COLOR[k])})'
                        for k in SEV_SLOTS if s.get(k)))
    o += ["", "```mermaid", "pie showData", f'    title {m} {EN["by_severity"]}']
    for k in SEV_SLOTS:
        if s.get(k):
            o.append(f'    "{name(SEV_NAME, k, "en")}" : {s[k]}')
    o += ["```", "", f"## {EN['month_records']}", "", TABLE_HEAD]
    for r in rs:
        ty = " ".join(f"`{t}`" for t in r["type"])
        star = "\u2605 " if r["severity"] == "critical" else ""
        warn = " \u26a0\ufe0f" if r.get("disputed") else ""
        o.append(f"| `{r['date'][5:]}` | {star}[{en_title(r)}]({r['_file']}){warn} | {ty} | "
                 f"{sev_cell(r['severity'])} | {r['confidence']} | {harm_cell(r['real_harm'])} |")
    o += ["", f"<sub>{EN['legend']}</sub>"]
    if splice(f"incidents/{m}/README.md", "summary", "\n".join(o)):
        changed.append(f"incidents/{m}/README.md")

    nav = []
    if i > 0:
        nav.append(f"[\u2190 {MONTHS[i-1]}](../{MONTHS[i-1]}/README.md)")
    nav += ["[Archive index](../../README.md)", "[By type](../../taxonomy/types.md)"]
    if i < len(MONTHS) - 1:
        nav.append(f"[{MONTHS[i+1]} \u2192](../{MONTHS[i+1]}/README.md)")
    splice(f"incidents/{m}/README.md", "nav", "---\n\n" + " \u00b7 ".join(nav))

# ---------------------------------------------------------- incidents/README
o = [EN["index_total"].format(n=TOTAL, m=len(MONTHS)), "",
     "| " + " | ".join(EN["index_head"]) + " |", "|---|---|---|---|---|"]
for m in MONTHS:
    rs, s = BYM[m], Counter(r["severity"] for r in BYM[m])
    o.append(f"| [{m}]({m}/README.md) | {len(rs)} | {s.get('critical',0) or '\u00b7'} | "
             f"{s.get('high',0) or '\u00b7'} | {sum(1 for r in rs if r['real_harm'])} |")
o.append(f"| **{EN['index_total_row']}** | **{TOTAL}** | **{sev['critical']}** | **{sev['high']}** | "
         f"**{harm['true']}** |")
if splice("incidents/README.md", "index", "\n".join(o)):
    changed.append("incidents/README.md")

# ---------------------------------------------------------- topics / regions
TOPIC_TYPES = {
    "eval-escapes": ["EVAL", "SANDBOX"], "rogue-agents": ["ROGUE"],
    "zero-click-exfil": ["IPI", "EXFIL"], "agent-supply-chain": ["SUPPLY", "MCP"],
    "offensive-ai": ["WEAPON"], "agent-infra": ["INFRA", "CRED"], "defense": ["GOV"],
}
REGION_MAP = {"us": ["US"], "eu-uk": ["EU", "UK"], "jp": ["JP"], "kr": ["KR"],
              "cn": ["CN"], "tw-etc": ["TW", "HK", "SG", "SEA", "APAC", "AU"]}


def facet_table(rs, depth=1):
    up = "../" * depth
    o = [f"## {EN['all_records']} ({len(rs)})", "", TABLE_HEAD]
    for r in sorted(rs, key=lambda r: r["date"]):
        ty = " ".join(f"`{t}`" for t in r["type"])
        star = "\u2605 " if r["severity"] == "critical" else ""
        warn = " \u26a0\ufe0f" if r.get("disputed") else ""
        o.append(f"| `{r['date']}` | {star}[{en_title(r)}]({up}{r['_path']}){warn} | {ty} | "
                 f"{sev_cell(r['severity'])} | {r['confidence']} | {harm_cell(r['real_harm'])} |")
    return "\n".join(o)


for slug, types in TOPIC_TYPES.items():
    rs = [r for r in rows if set(r["type"]) & set(types)]
    if splice(f"topics/{slug}.md", "incidents", facet_table(rs)):
        changed.append(f"topics/{slug}.md")

for f in sorted(glob.glob(os.path.join(ROOT, "regions", "*.md"))):
    slug = os.path.basename(f)[:-3]
    if slug == "README":
        continue
    if "<!-- BEGIN:incidents -->" not in io.open(f, encoding="utf-8").read():
        continue                     # hand-written pointer page (region stub), no table
    codes = REGION_MAP.get(slug, [slug.upper()])
    rs = [r for r in rows if set(r["region"]) & set(codes)]
    if splice(f"regions/{slug}.md", "incidents", facet_table(rs)):
        changed.append(f"regions/{slug}.md")

# ---------------------------------------------------------- README x7
CRIT_NR = sum(1 for r in CRIT if not r["real_harm"])
FMT = dict(total=TOTAL, months=len(MONTHS), harm=harm["true"], first=FIRST, last=LAST,
           lastm=LAST[:7], build=BUILD, links=NLINKS, urls=len(URLS),
           ga=gc.get("A", 0), disp=sum(1 for r in rows if r.get("disputed")), cnr=CRIT_NR)

for fname, L in README_L10N.items():
    up = L["up"]
    F = dict(FMT, up=up)
    lang = L["lang"]
    lb = LABELS[lang]
    b = L["badges"]
    splice(fname, "badges", '<p align="center">'
           + f'<img alt="{b[0]}" src="{badge(b[0], str(TOTAL), "48545A")}"> '
           + f'<img alt="{b[1]}" src="{badge(b[1], str(len(MONTHS)), "48545A")}"> '
           + f'<img alt="{b[2]}" src="{badge(b[2], str(sev["critical"]), SEV_COLOR["critical"])}"> '
           + f'<img alt="{b[3]}" src="{badge(b[3], str(harm["true"]), "B23B40")}"> '
           + f'<img alt="{b[4]}" src="{badge(b[4], str(len(URLS)) + " URL", "157A41")}"> '
           + f'<img alt="{b[5]}" src="{badge(b[5], "CC BY 4.0", "2359A8")}">'
           + "</p>")
    splice(fname, "thesis", L["thesis"].format(**F))

    o = []
    for y in sorted({m[:4] for m in MONTHS}):
        ms = [m for m in MONTHS if m.startswith(y)]
        ny = sum(len(BYM[m]) for m in ms)
        o += [L["months_year"].format(y=y, n=ny), "",
              "| " + " | ".join(f"[{m[5:]}]({up}incidents/{m}/README.md)" for m in ms) + " |",
              "|" + "---|" * len(ms),
              "| " + " | ".join(
                  f"`{len(BYM[m])}`"
                  + (lambda c: " \u2605" + str(c) if c else "")(
                      sum(1 for r in BYM[m] if r["severity"] == "critical"))
                  for m in ms) + " |", ""]
    o.append(L["months_foot"])
    splice(fname, "months", chr(10).join(o))

    h = L["crit_head"]
    o = [L["crit_lead"].format(**F), "",
         "| " + " | ".join(h) + " |", "|---|---|---|---|"]
    localize_regions = lang != "en"
    for r in CRIT:
        t, _ = localized(r, MIRRORS, lang)
        sub = f"<br><sub>{en_title(r)}</sub>" if t != en_title(r) else ""
        reg = " ".join((name(REGION_NAME, x, lang) if localize_regions else x) for x in r["region"])
        o.append(f"| `{r['date']}` | [{t}]({up}{r['_path']}){sub} | "
                 + " ".join(f"`{x}`" for x in r["type"]) + f" | {reg} |")
    splice(fname, "critical", chr(10).join(o))

    qh = L["qual_head"]
    o = ["| " + " | ".join(qh) + " |", "|---|---|"]
    for k, v in L["qual"]:
        o.append(f"| {k} | {v.format(**F)} |")
    splice(fname, "quality", chr(10).join(o))
    splice(fname, "cite", chr(10).join(["```bibtex",
        "@misc{orca_ai_incident_archive,",
        "  title  = {Orca AI Incident Archive: An open database of real-world AI agent incidents},",
        "  year   = {2026},",
        "  note   = {" + L["cite"].format(**F) + "},",
        "  url    = {https://github.com/Continuum-AI-Corp/Orca-AI-Incident-Archive}",
        "}",
        "```",
    ]))
    splice(fname, "footer", L["footer"].format(**F))

# ---------------------------------------------------------- dist/
def rec_field(r, field, lang):
    """Localized field exactly as stored (no English fallback), or None."""
    if lang == "zh":
        m = MIRRORS.get(r["id"])
        return (m[field] if m else None)
    return r.get(f"{field}_{lang}")


out = []
for r in rows:
    d = OrderedDict([("id", r["id"]), ("title", r["title"])])
    for lang in LANGS[1:]:
        d[f"title_{lang}"] = rec_field(r, "title", lang)
    d.update([
        ("date", r["date"]),
        ("date_end", r.get("date_end")), ("date_precision", r["date_precision"]),
        ("date_raw", r.get("date_raw")), ("month", r["_month"]), ("kind", r["kind"]),
        ("type", r["type"]), ("severity", r["severity"]), ("confidence", r["confidence"]),
        ("real_harm", r["real_harm"]), ("ai_involvement", r["ai_involvement"]),
        ("region", r["region"]), ("summary", r["summary"]),
    ])
    for lang in LANGS[1:]:
        d[f"summary_{lang}"] = rec_field(r, "summary", lang)
    d.update([
        ("disputed", bool(r.get("disputed"))), ("landmark", bool(r.get("landmark"))),
        ("path", r["_path"]),
        ("path_zh", MIRRORS[r["id"]]["path"] if r["id"] in MIRRORS else None),
        ("sources", r["sources"]),
    ])
    out.append(d)

W("dist/incidents.json", json.dumps(
    {"schema": "https://github.com/Continuum-AI-Corp/Orca-AI-Incident-Archive/blob/main/SCHEMA.md",
     "schema_version": 2, "version": BUILD, "license": "CC-BY-4.0",
     "languages": LANGS, "count": TOTAL, "incidents": out},
    ensure_ascii=False, indent=1))

CSV_LANGS = LANGS[1:]
CSV_COLS = (["id", "date", "date_end", "date_precision", "month", "title"]
            + [f"title_{l}" for l in CSV_LANGS]
            + ["kind", "type", "severity", "confidence", "real_harm", "ai_involvement", "region",
               "disputed", "landmark", "summary"]
            + [f"summary_{l}" for l in CSV_LANGS]
            + ["sources", "path", "path_zh"])
buf = io.StringIO()
w = csv.writer(buf, lineterminator="\n")
w.writerow(CSV_COLS)
for r in rows:
    w.writerow([r["id"], r["date"], r.get("date_end") or "", r["date_precision"], r["_month"],
                r["title"]]
               + [(rec_field(r, "title", l) or "") for l in CSV_LANGS]
               + [r["kind"], ";".join(r["type"]), r["severity"], r["confidence"],
                  "" if r["real_harm"] is None else str(r["real_harm"]).lower(),
                  r["ai_involvement"], ";".join(r["region"]),
                  str(bool(r.get("disputed"))).lower(), str(bool(r.get("landmark"))).lower(),
                  str(r["summary"]).replace("\n", " ")]
               + [str(rec_field(r, "summary", l) or "").replace("\n", " ") for l in CSV_LANGS]
               + [";".join(s["url"] for s in r["sources"]), r["_path"],
                  MIRRORS[r["id"]]["path"] if r["id"] in MIRRORS else ""])
W("dist/incidents.csv", buf.getvalue())

W("dist/stats.json", json.dumps(OrderedDict([
    ("version", BUILD), ("count", TOTAL),
    ("months", OrderedDict((m, len(BYM[m])) for m in MONTHS)),
    ("by_severity", OrderedDict((k, sev.get(k, 0)) for k in SEV_SLOTS)),
    ("by_kind", OrderedDict((k, kind.get(k, 0)) for k in KIND_SLOTS)),
    ("by_type", OrderedDict(tc.most_common())),
    ("by_confidence", OrderedDict((k, gc.get(k, 0)) for k in "ABCD")),
    ("by_region", OrderedDict(rcnt.most_common())),
    ("real_harm", OrderedDict((k, harm.get(k, 0)) for k in ("true", "false", "null"))),
    ("ai_involvement", OrderedDict(ai.most_common())),
    ("sources", {"links": NLINKS, "unique_urls": len(URLS)}),
]), ensure_ascii=False, indent=1))
W("dist/sources.txt", "\n".join(URLS))

# ---------------------------------------------------------- assets/ + index.html
charts.build(rows)
page_data.build(rows)

print(f"built \u00b7 {TOTAL} records \u00b7 {len(MONTHS)} months \u00b7 {len(URLS)} unique URLs \u00b7 "
      f"{sev['critical']} critical")
if changed:
    print(f"updated {len(changed)} index files")
