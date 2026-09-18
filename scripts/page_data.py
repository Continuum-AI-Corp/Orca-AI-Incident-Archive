# -*- coding: utf-8 -*-
"""Inject the incident frontmatter into the <script id="data"> block of index.html.

index.html is hand-written; only the JSON inside <script id="data"> is
generated here.  Re-running is idempotent: any previously injected JSON is
first swapped back for a placeholder.
"""
import os, re, io, sys, json
from collections import Counter, OrderedDict
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from orca import load_all, load_mirrors, localized
from l10n import LANGS, LANG_LABEL, LANG_TAG, TYPE_NAME, REGION_NAME, name

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, "index.html")


def plain(s):
    s = re.sub(r'\[([^\]]+)\]\([^)]+\)', lambda m: m.group(1), str(s))
    s = re.sub(r'\*\*(.+?)\*\*', lambda m: m.group(1), s)
    return s.replace("`", "").strip()


def build(rows=None):
    rows = rows or load_all()
    mirrors = load_mirrors("zh")
    rows.sort(key=lambda r: (r["date"], r["id"]))
    MONTHS = sorted({r["_month"] for r in rows})
    SEVS = ["critical", "high", "medium", "low", "info"]
    TYPES = [t for t, _ in Counter(t for r in rows for t in r["type"]).most_common()]

    # archive number: ORCA-YYYYMM-NNN, in date order within the month
    seq = {}
    out = []
    for r in rows:
        m = r["_month"]
        seq[m] = seq.get(m, 0) + 1
        titles, sums = {"en": plain(r["title"])}, {"en": plain(r["summary"])}
        for lang in LANGS[1:]:
            t, s = localized(r, mirrors, lang)
            # only translations that differ from English are stored; the page
            # falls back to "en" for anything missing.
            if t != str(r["title"]):
                titles[lang] = plain(t)
            if s != str(r["summary"]):
                sums[lang] = plain(s)
        out.append(OrderedDict([
            ("id", r["id"]),
            ("cid", "ORCA-%s-%03d" % (m.replace("-", ""), seq[m])),
            ("date", r["date"]),
            ("dateRaw", r.get("date_raw") or r["date"]),
            ("month", m),
            ("title", OrderedDict((l, titles[l]) for l in LANGS if l in titles)),
            ("summary", OrderedDict((l, sums[l]) for l in LANGS if l in sums)),
            ("types", r["type"]),
            ("regions", r["region"]),
            ("grade", r["confidence"]),
            ("sev", r["severity"]),
            ("kind", r["kind"]),
            ("harm", "yes" if r["real_harm"] else ("no" if r["real_harm"] is False else "na")),
            ("ai", r["ai_involvement"]),
            ("sources", [{"label": s.get("label") or s["url"], "url": s["url"]} for s in r["sources"]]),
            ("flagged", bool(r.get("disputed"))),
            ("landmark", bool(r.get("landmark"))),
            ("path", r["_path"]),
            ("pathZh", mirrors[r["id"]]["path"] if r["id"] in mirrors else None),
        ]))

    months = []
    for m in MONTHS:
        rs = [r for r in rows if r["_month"] == m]
        months.append({
            "m": m, "n": len(rs),
            "sev": {k: v for k, v in Counter(r["severity"] for r in rs).items()},
            "type": {k: v for k, v in Counter(t for r in rs for t in r["type"]).items()},
        })

    harm = Counter("yes" if r["real_harm"] else ("no" if r["real_harm"] is False else "na") for r in rows)
    DATA = OrderedDict([
        ("build", max(r["date"] for r in rows)),
        ("first", min(r["date"] for r in rows)),
        ("last", max(r["date"] for r in rows)),
        ("count", len(rows)),
        ("sourceCount", len({s["url"] for r in rows for s in r["sources"]})),
        ("langs", LANGS),
        ("langLabel", OrderedDict((l, LANG_LABEL[l]) for l in LANGS)),
        ("langTag", OrderedDict((l, LANG_TAG[l]) for l in LANGS)),
        ("bySev", {k: v for k, v in Counter(r["severity"] for r in rows).items()}),
        ("byKind", {k: v for k, v in Counter(r["kind"] for r in rows).items()}),
        ("byGrade", {k: v for k, v in Counter(r["confidence"] for r in rows).items()}),
        ("byHarm", dict(harm)),
        ("byType", OrderedDict((t, sum(1 for r in rows if t in r["type"])) for t in TYPES)),
        ("byRegion", OrderedDict(Counter(x for r in rows for x in r["region"]).most_common())),
        ("typeName", {t: [name(TYPE_NAME, t, l) for l in LANGS] for t in TYPES}),
        # sorted(...) is required: set iteration order varies with PYTHONHASHSEED,
        # which would otherwise make the injected JSON fail CI's "derived files
        # are up to date" check at random.
        ("regionName", OrderedDict(
            (x, [name(REGION_NAME, x, l) for l in LANGS])
            for x in sorted({y for r in rows for y in r["region"]}))),
        ("months", months),
        ("rows", out),
    ])

    t = io.open(P, encoding="utf-8").read()
    t = re.sub(r'(<script id="data" type="application/json">).*?(</script>)',
               lambda m: m.group(1) + "__DATA__" + m.group(2), t, count=1, flags=re.S)
    payload = json.dumps(DATA, ensure_ascii=False, separators=(",", ":"))
    # "<" must be escaped so that a "</script>" sequence inside translated
    # text can never terminate the data block early.
    payload = payload.replace("<", "\\u003c")
    assert "__DATA__" in t, "index.html does not contain the __DATA__ placeholder"
    t = t.replace("__DATA__", payload, 1)
    io.open(P, "w", encoding="utf-8", newline="\n").write(t)
    print(f"injected {len(out)} records \u00b7 {len(months)} months \u00b7 "
          f"{len(payload.encode('utf-8'))//1024} KB payload \u00b7 "
          f"page {len(t.encode('utf-8'))//1024} KB")


if __name__ == "__main__":
    build()
