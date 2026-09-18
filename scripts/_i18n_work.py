# -*- coding: utf-8 -*-
"""P3 helpers: extract English record titles/summaries for translation and
apply the translated JSONL back into the frontmatter (temporary script).

    python scripts/_i18n_work.py extract  <workdir>
    python scripts/_i18n_work.py apply    <workdir> <lang> [lang ...]
    python scripts/_i18n_work.py from-zh  <workdir>      # zh fields from mirrors
    python scripts/_i18n_work.py check    <workdir>
"""
import os, io, re, sys, json

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from orca import ROOT, load_all, load_mirrors
from l10n import LANGS, TRANS_LANGS

CJK = re.compile('[\u1100-\u11ff\u2e80-\u2eff\u3000-\u303f\u3040-\u30ff'
                 '\u3400-\u4dbf\u4e00-\u9fff\uac00-\ud7af\uff00-\uffef]')


def q(s):
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"') + '"'


def summary_block(s, indent=2):
    out = []
    for ln in str(s).strip("\n").split("\n"):
        out.append((" " * indent + ln) if ln.strip() else "")
    return "\n".join(out)


def extract(work):
    rows = load_all()
    with io.open(os.path.join(work, "en.jsonl"), "w", encoding="utf-8", newline="\n") as f:
        for r in rows:
            f.write(json.dumps({"id": r["id"], "title": str(r["title"]),
                                "summary": str(r["summary"])}, ensure_ascii=False) + "\n")
    print("extracted", len(rows), "records ->", os.path.join(work, "en.jsonl"))


def insert_frontmatter(text, fields, lang):
    """Insert title_<lang> after title; summary_<lang> after the summary block."""
    lines = text.split("\n")
    # --- title_<lang> right after the `title:` line
    ti = next(i for i, ln in enumerate(lines) if ln.startswith("title:"))
    lines.insert(ti + 1, f"title_{lang}: {q(fields['title'])}")
    # --- summary_<lang> after the `summary: |` block (and its following blank line)
    si = next(i for i, ln in enumerate(lines) if ln.startswith("summary:"))
    j = si + 1
    while j < len(lines) and (lines[j].startswith("  ") or not lines[j].strip()):
        j += 1
    block = [f"summary_{lang}: |"] + summary_block(fields["summary"]).split("\n") + [""]
    lines[j:j] = block
    return "\n".join(lines)


def apply_lang(work, lang):
    path = os.path.join(work, f"{lang}.jsonl")
    data = {}
    with io.open(path, encoding="utf-8") as f:
        for ln in f:
            ln = ln.strip()
            if not ln:
                continue
            d = json.loads(ln)
            data[d["id"]] = d
    rows = load_all()
    n = 0
    for r in rows:
        d = data.get(r["id"])
        if not d:
            print("MISSING", r["id"])
            continue
        p = os.path.join(ROOT, r["_path"])
        t = io.open(p, encoding="utf-8").read()
        if f"title_{lang}:" in t:
            continue
        t2 = insert_frontmatter(t, {"title": d["title"], "summary": d["summary"]}, lang)
        io.open(p, "w", encoding="utf-8", newline="\n").write(t2)
        n += 1
    print(f"applied {lang}: {n} records")
    return n


def from_zh(work):
    """zh fields come straight from the Chinese mirrors (no translation pass)."""
    mirrors = load_mirrors("zh")
    n = 0
    for r in load_all():
        m = mirrors[r["id"]]
        p = os.path.join(ROOT, r["_path"])
        t = io.open(p, encoding="utf-8").read()
        if "title_zh:" in t:
            continue
        t = insert_frontmatter(t, {"title": m["title"], "summary": m["summary"]}, "zh")
        io.open(p, "w", encoding="utf-8", newline="\n").write(t)
        n += 1
    print("applied zh from mirrors:", n)


def canonicalize():
    """Rewrite title_*/summary_* fields in LANGS order (zh, ja, ko, de, fr, es)."""
    import glob
    n = 0
    for p in sorted(glob.glob(os.path.join(ROOT, "incidents", "*", "*.md"))):
        if p.endswith("README.md"):
            continue
        text = io.open(p, encoding="utf-8").read()
        i = text.index("\n---\n", 4)
        head, body = text[4:i], text[i + 5:]
        lines = head.split("\n")
        titles, summaries, keep = {}, {}, []
        k = 0
        while k < len(lines):
            ln = lines[k]
            m = re.match(r'^title_([a-z]{2}):\s*(.*)$', ln)
            if m:
                titles[m.group(1)] = ln
                k += 1
                continue
            m = re.match(r'^summary_([a-z]{2}):\s*\|$', ln)
            if m:
                lang, block = m.group(1), [ln]
                k += 1
                while k < len(lines) and (lines[k].startswith("  ") or not lines[k].strip()):
                    block.append(lines[k])
                    k += 1
                while block and not block[-1].strip():
                    block.pop()
                summaries[lang] = block
                continue
            keep.append(ln)
            k += 1
        out, k = [], 0
        while k < len(keep):
            ln = keep[k]
            out.append(ln)
            if ln.startswith("title:"):
                out += [titles[l] for l in TRANS_LANGS if l in titles]
            elif re.match(r'^summary:\s*\|$', ln):
                k += 1
                while k < len(keep) and (keep[k].startswith("  ") or not keep[k].strip()):
                    out.append(keep[k])
                    k += 1
                for l in TRANS_LANGS:
                    if l in summaries:
                        out.append("")
                        out.extend(summaries[l])
                while k < len(keep) and not keep[k].strip():
                    k += 1
                out.append("")
                continue
            k += 1
        new = "---\n" + "\n".join(out) + "\n---\n" + body
        if new != text:
            io.open(p, "w", encoding="utf-8", newline="\n").write(new)
            n += 1
    print("canonicalized", n, "records")


def check(work):
    rows = load_all()
    problems = []
    for r in rows:
        for lang in TRANS_LANGS:
            t = str(r.get(f"title_{lang}") or "").strip()
            s = str(r.get(f"summary_{lang}") or "").strip()
            if not t or not s:
                problems.append((r["_path"], f"missing {lang}"))
            if lang in ("de", "fr", "es") and (CJK.search(t) or CJK.search(s)):
                problems.append((r["_path"], f"CJK in {lang}"))
    print("check: problems", len(problems))
    for p in problems[:20]:
        print("  ", p[0], p[1])
    return 1 if problems else 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "extract":
        extract(sys.argv[2])
    elif cmd == "apply":
        for l in sys.argv[3:]:
            apply_lang(sys.argv[2], l)
    elif cmd == "from-zh":
        from_zh(sys.argv[2])
    elif cmd == "canon":
        canonicalize()
    elif cmd == "check":
        sys.exit(check(sys.argv[2]))
    else:
        print(__doc__)
