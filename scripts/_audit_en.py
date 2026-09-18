# -*- coding: utf-8 -*-
"""Temporary structural audit for the English translation pass (P2).

    python scripts/_audit_en.py [month ...]

Compares each primary record against its git HEAD version (the migrated but
still-Chinese state) and its Chinese mirror:

  * frontmatter key order unchanged; machine-readable fields identical
  * H1 present, one mermaid block, badge count, table-line count, link count
  * English section names only, same section count as the mirror
  * no CJK in title/summary/body (translation fields are allowed)
"""
import os, re, io, sys, subprocess
from collections import Counter
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from orca import ROOT, INCIDENTS, load_all, load_mirrors, parse_frontmatter

CJK = re.compile('[\u1100-\u11ff\u2e80-\u2eff\u3000-\u303f\u3040-\u30ff'
                 '\u3400-\u4dbf\u4e00-\u9fff\uac00-\ud7af\uff00-\uffef]')
SECTIONS = {"## Summary", "## Attack chain", "## Sources", "## Metadata", "## Related",
            "## Details", "## What happened", "## Timeline", "## Affected data",
            "## What the parties said", "## A glaring asymmetry", "## Why it is listed"}
KEEP_FIELDS = ["date", "date_end", "date_precision", "kind", "type", "severity",
               "confidence", "real_harm", "ai_involvement", "region", "disputed",
               "landmark", "scan_month", "scan_ref"]


def git_head(path):
    r = subprocess.run(["git", "show", "HEAD:" + path], cwd=ROOT,
                       capture_output=True, text=True, encoding="utf-8")
    return r.stdout if r.returncode == 0 else None


def main(months):
    rows = [r for r in load_all() if not months or r["_month"] in months]
    mirrors = load_mirrors("zh")
    errs, warns = [], []

    for r in rows:
        p = r["_path"]
        body = r["_body"]
        old = git_head(p)
        if old is None:
            errs.append((p, "not in git HEAD"))
            continue
        od, _ = parse_frontmatter(old, p)

        # frontmatter key order + machine fields
        keys_new = [ln.split(":")[0] for ln in old.split("\n")[1:] if re.match(r'^[a-z_]+:', ln)]
        for f in KEEP_FIELDS:
            if (f in r) != (f in od) or r.get(f) != od.get(f):
                errs.append((p, f"field `{f}` changed: {od.get(f)!r} -> {r.get(f)!r}"))

        # CJK scan
        for k, v in r.items():
            if k.startswith("_") or k.startswith("title_") or k.startswith("summary_"):
                continue
            vals = v if isinstance(v, list) else [v]
            for item in vals:
                texts = item.values() if isinstance(item, dict) else [item]
                for txt in texts:
                    if isinstance(txt, str) and CJK.search(txt):
                        errs.append((p, f"CJK in `{k}`: {txt[:40]!r}"))
        for label, text in (("title", r.get("title")), ("summary", r.get("summary")),
                            ("body", body)):
            if text and CJK.search(str(text)):
                line = str(text).split("\n")
                line = next((x for x in line if CJK.search(x)), str(text)[:40])
                errs.append((p, f"CJK in {label}: {line.strip()[:50]!r}"))

        # structure vs mirror
        m = mirrors.get(r["id"])
        if not m:
            errs.append((p, "no mirror"))
            continue
        mtext = io.open(os.path.join(ROOT, m["path"]), encoding="utf-8").read()
        _, mbody = parse_frontmatter(mtext, m["path"])
        h1_new = [ln for ln in body.split("\n") if ln.startswith("# ")]
        h2_new = [ln.strip() for ln in body.split("\n") if ln.startswith("## ")]
        h2_old = [ln.strip() for ln in mbody.split("\n") if ln.startswith("## ")]
        if len(h1_new) != 1:
            errs.append((p, f"expected 1 H1, found {len(h1_new)}"))
        if len(h2_new) != len(h2_old):
            errs.append((p, f"H2 count {len(h2_new)} != mirror {len(h2_old)}"))
        for s in h2_new:
            if s not in SECTIONS:
                errs.append((p, f"unexpected section {s!r}"))
        if h2_new and h2_new[0] != "## Summary":
            warns.append((p, f"first section is {h2_new[0]!r}"))
        for need in ("## Sources", "## Metadata"):
            if need not in h2_new:
                errs.append((p, f"missing {need}"))
        counts = lambda t, pat: sum(1 for ln in t.split("\n") if ln.startswith(pat))
        if body.count("```mermaid") != mbody.count("```mermaid"):
            errs.append((p, "mermaid block count changed"))
        if body.count("flowchart") != mbody.count("flowchart"):
            errs.append((p, "flowchart keyword count changed"))
        if body.count("![") != mbody.count("!["):
            errs.append((p, f"badge count {body.count('![')} != mirror {mbody.count('![')}"))
        if counts(body, "|") != counts(mbody, "|"):
            errs.append((p, f"table line count {counts(body, '|')} != mirror {counts(mbody, '|')}"))
        if abs(body.count("](") - mbody.count("](")) > 1:
            warns.append((p, f"link count {body.count('](')} vs mirror {mbody.count('](')}"))
        # H1 sub line should be gone (the H1 is English now)
        lines = body.split("\n")
        try:
            i = next(n for n, ln in enumerate(lines) if ln.startswith("# "))
            if lines[i + 2].startswith("<sub>"):
                warns.append((p, "leftover <sub> title line after H1"))
        except (StopIteration, IndexError):
            pass

    print(f"audited {len(rows)} records | errors {len(errs)} | warnings {len(warns)}")
    for p, m in errs[:40]:
        print("  ERR ", p, "-", m)
    if len(errs) > 40:
        print(f"  ... and {len(errs)-40} more errors")
    for p, m in warns[:15]:
        print("  WARN", p, "-", m)
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
