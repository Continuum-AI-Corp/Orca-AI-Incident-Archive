# -*- coding: utf-8 -*-
"""One-off migration to schema v2 (temporary; delete after use).

For every record in incidents/<month>/<id>.md:
  1. create a full Chinese mirror at incidents/i18n/zh/<month>/<id>.md
     (frontmatter: id / lang / source / title / summary; body kept in Chinese,
      every relative link shifted down two directories, footer rewritten);
  2. rewrite the primary file frontmatter: `title` <- old `title_en`,
     drop the `title_en` line (body stays Chinese until the translation pass).

Usage:
    python scripts/_migrate_v2.py --dry-run   # report only
    python scripts/_migrate_v2.py             # write files
"""
import os, re, io, sys, argparse
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from orca import ROOT, INCIDENTS, load_all

MIRROR_ROOT = os.path.join(INCIDENTS, "i18n", "zh")
NAV_RE = re.compile(r'^\[\u2190[^\n]*\]\([^)]*README\.md\)[^\n]*$', re.M)
LINK_RE = re.compile(r'(!?\[[^\]]*\]\()([^)\s]+)(\))')


def quote(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def shift_target(t, month):
    """Return (new_target, handled). Mirror sits two directories deeper."""
    if t.startswith(("http://", "https://", "#", "mailto:")):
        return t, True
    body, frag = (t.split("#", 1) + [""])[:2]
    frag = ("#" + frag) if frag else ""
    if body.startswith("../"):
        return "../../" + body + frag, True
    if re.match(r'^[A-Za-z0-9][^/]*\.md$', body):
        # bare link inside the month directory (sibling record or month README)
        return "../../../%s/%s%s" % (month, body, frag), True
    return t, False


def migrate(rows, dry):
    os.makedirs(MIRROR_ROOT, exist_ok=True)
    written, anomalies, unchecked = 0, [], []
    for r in rows:
        month, fname, rid = r["_month"], r["_file"], r["id"]
        src = os.path.join(ROOT, r["_path"])
        text = io.open(src, encoding="utf-8").read()
        i = text.find("\n---\n", 4)
        head, body = text[:i], text[i + 5:]

        # --- mirror body: shift relative links, rewrite nav line -------------
        def repl(m):
            new, ok = shift_target(m.group(2), month)
            if not ok:
                unchecked.append((r["_path"], m.group(2)))
            return m.group(1) + new + m.group(3)
        mbody = LINK_RE.sub(repl, body)
        nav = ("[\u2190 English original](../../../%s/%s.md) \u00b7 "
               "[%s index](../../../%s/README.md) \u00b7 "
               "[All records](../../../README.md) \u00b7 "
               "[Home](../../../../README.md)" % (month, rid, month, month))
        mbody, n = NAV_RE.subn(nav, mbody, count=1)
        if n != 1:
            anomalies.append((r["_path"], "nav line not found"))

        # --- mirror frontmatter --------------------------------------------
        summary = str(r["summary"]).strip("\n")
        summ_lines = "\n".join(("  " + ln) if ln.strip() else "" for ln in summary.split("\n"))
        mirror = (
            "---\n"
            "id: %s\n"
            "lang: zh\n"
            "source: %s\n"
            "title: %s\n"
            "summary: |\n"
            "%s\n"
            "---\n"
            "%s" % (rid, r["_path"], quote(str(r["title"])), summ_lines, mbody))

        # --- primary frontmatter: title <- title_en, drop title_en ----------
        if "title_en" in head:
            en = str(r.get("title_en") or "").strip()
            if not en:
                anomalies.append((r["_path"], "empty title_en"))
                continue
            new_head = re.sub(r'^title: .*$', "title: " + quote(en), head, count=1, flags=re.M)
            new_head = re.sub(r'^title_en: .*$\n?', "", new_head, count=1, flags=re.M)
            ptext = new_head + "\n---\n" + body
        else:
            ptext = text  # already migrated

        if not dry:
            mp = os.path.join(MIRROR_ROOT, month, fname)
            os.makedirs(os.path.dirname(mp), exist_ok=True)
            io.open(mp, "w", encoding="utf-8", newline="\n").write(mirror)
            io.open(src, "w", encoding="utf-8", newline="\n").write(ptext)
        written += 1

    print("records: %d | mirrors written: %d | dry-run: %s" % (len(rows), written, dry))
    if unchecked:
        print("UNHANDLED link forms (%d):" % len(unchecked))
        for p, t in unchecked[:20]:
            print("   ", p, "->", t)
    if anomalies:
        print("ANOMALIES (%d):" % len(anomalies))
        for p, m in anomalies[:20]:
            print("   ", p, ":", m)
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    sys.exit(migrate(load_all(), a.dry_run))
