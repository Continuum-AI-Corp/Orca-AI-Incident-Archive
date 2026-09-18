# -*- coding: utf-8 -*-
"""Validate the frontmatter of incidents/**/*.md against SCHEMA.md.

    python scripts/validate.py

Exit code 0 = pass, 1 = errors.  CI runs this on every push.

Beyond the schema this also guards the English-default rule:

  * primary record files must not contain CJK anywhere except the
    ``title_<lang>`` / ``summary_<lang>`` translation fields;
  * generated English pages (README, monthly indexes, topics, regions, docs)
    must not contain CJK either.  The only exception are language switchers,
    which legitimately carry native names (简体中文, 日本語, ...).

SCAN.md and the translation layers (``incidents/i18n/``, ``docs/i18n/``) are
out of scope on purpose.
"""
import os, re, io, sys, glob, datetime
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from orca import (ROOT, INCIDENTS, MIRRORS, load_all, load_mirrors, REQUIRED,
                  KINDS, SEVERITIES, GRADES, AI_VALUES, PRECISIONS, TYPES)
from l10n import LANGS, TRANS_LANGS, REGION_NAME

ERR, WARN = [], []
def err(p, m):  ERR.append(f"{p}: {m}")
def warn(p, m): WARN.append(f"{p}: {m}")

ID_RE = re.compile(r'^\d{4}-\d{2}-\d{2}-[a-z0-9][a-z0-9-]*$')
DATE_RE = re.compile(r'^\d{4}-\d{2}-\d{2}$')
CJK_RE = re.compile('[\u1100-\u11ff\u2e80-\u2eff\u3000-\u303f\u3040-\u30ff'
                    '\u3400-\u4dbf\u4e00-\u9fff\uac00-\ud7af\uff00-\uffef]')

ALLOWED_KEYS = set(REQUIRED) | {"date_end", "date_raw", "scan_month", "scan_ref",
                                "disputed", "landmark"} \
    | {f"{f}_{l}" for l in TRANS_LANGS for f in ("title", "summary")}


def isdate(s):
    if not isinstance(s, str) or not DATE_RE.match(s):
        return False
    try:
        datetime.date.fromisoformat(s)
        return True
    except ValueError:
        return False


rows = load_all()
mirrors = load_mirrors("zh")
if not rows:
    print("no records found - is incidents/ empty?")
    sys.exit(1)

seen_id, seen_path = {}, {}
for r in rows:
    p = r["_path"]

    for k in REQUIRED:
        if k not in r:
            err(p, f"missing required field `{k}`")
    for k in r:
        if not k.startswith("_") and k not in ALLOWED_KEYS:
            warn(p, f"unknown field `{k}`")

    _id = r.get("id")
    if _id:
        if not ID_RE.match(str(_id)):
            err(p, f"`id` is not a valid slug: {_id!r} (expected YYYY-MM-DD-slug, "
                   f"slug lowercase letters/digits/hyphens only)")
        if r["_file"] != f"{_id}.md":
            err(p, f"`id` does not match the filename: id={_id!r} file={r['_file']!r}")
        if _id in seen_id:
            err(p, f"duplicate `id`, already used by {seen_id[_id]}")
        seen_id[_id] = p

    d = r.get("date")
    if not isdate(d):
        err(p, f"`date` is not a valid ISO date: {d!r}")
    else:
        if _id and not str(_id).startswith(d):
            err(p, f"`id` date prefix does not match `date`: {_id!r} vs {d!r}")
        if r["_month"] != d[:7]:
            err(p, f"directory {r['_month']} does not match `date` {d}")
    de = r.get("date_end")
    if de is not None:
        if not isdate(de):
            err(p, f"`date_end` is not a valid ISO date: {de!r}")
        elif isdate(d) and de <= d:
            err(p, f"`date_end` ({de}) must be later than `date` ({d})")
    if r.get("date_precision") not in PRECISIONS:
        err(p, f"invalid `date_precision`: {r.get('date_precision')!r}, expected {sorted(PRECISIONS)}")

    kind = r.get("kind")
    if kind not in KINDS:
        err(p, f"invalid `kind`: {kind!r}")
    sev = r.get("severity")
    if sev not in SEVERITIES:
        err(p, f"invalid `severity`: {sev!r}")
    if r.get("confidence") not in GRADES:
        err(p, f"invalid `confidence`: {r.get('confidence')!r}")
    if r.get("ai_involvement") not in AI_VALUES:
        err(p, f"invalid `ai_involvement`: {r.get('ai_involvement')!r}")

    ty = r.get("type")
    if not isinstance(ty, list) or not ty:
        err(p, "`type` must be a non-empty list")
    else:
        for t in ty:
            if t not in TYPES:
                err(p, f"unknown `type` value: {t!r}")

    rg = r.get("region")
    if not isinstance(rg, list) or not rg:
        err(p, "`region` must be a non-empty list")
    else:
        for x in rg:
            if not re.match(r'^[A-Z]{2,6}$', str(x)):
                err(p, f"invalid `region` code: {x!r}")
            elif x not in REGION_NAME:
                warn(p, f"`region` {x!r} has no display name, add it to scripts/l10n.py")

    harm = r.get("real_harm", "MISSING")
    if harm not in (True, False, None):
        err(p, f"`real_harm` must be true / false / null, got {harm!r}")
    if kind in ("policy", "report"):
        if harm is not None:
            err(p, f"`kind: {kind}` requires `real_harm: null`")
        if sev != "info":
            err(p, f"`kind: {kind}` requires `severity: info`, got {sev!r}")
    elif harm is None:
        err(p, f"`kind: {kind}` must not have `real_harm: null`")

    title = str(r.get("title") or "").strip()
    if not title:
        err(p, "`title` is empty")
    elif not re.search(r'[A-Za-z]', title):
        err(p, f"`title` contains no Latin letters (English is the source language): {title!r}")

    if not str(r.get("summary") or "").strip():
        err(p, "`summary` is empty")
    elif len(str(r["summary"]).strip()) < 10:
        warn(p, f"`summary` is very short ({len(str(r['summary']).strip())} chars)")

    for l in TRANS_LANGS:
        for f in ("title", "summary"):
            v = str(r.get(f"{f}_{l}") or "").strip()
            if not v:
                err(p, f"missing translation field `{f}_{l}`")
            elif CJK_RE.search(v) and l not in ("zh", "ja", "ko"):
                err(p, f"`{f}_{l}` contains CJK characters")

    src = r.get("sources")
    if not isinstance(src, list) or not src:
        err(p, "`sources` must contain at least one entry - no source, no record")
    else:
        for i, s in enumerate(src, 1):
            if not isinstance(s, dict) or "url" not in s:
                err(p, f"`sources[{i}]` is missing `url`")
                continue
            if not re.match(r'^https?://', str(s["url"])):
                err(p, f"`sources[{i}].url` is not an http(s) link: {s['url']!r}")
            if not str(s.get("label") or "").strip():
                warn(p, f"`sources[{i}]` has no label")
            elif CJK_RE.search(str(s["label"])):
                err(p, f"`sources[{i}].label` contains CJK: {s['label']!r}")

    body = r.get("_body", "")
    for need in ("## Summary", "## Sources"):
        if need not in body:
            err(p, f"body is missing the `{need}` section")
    if CJK_RE.search(body):
        line = next((ln for ln in body.split("\n") if CJK_RE.search(ln)), "")
        err(p, f"body contains CJK outside the translation layer: {line.strip()[:60]!r}")
    if r.get("disputed") and "[!WARNING]" not in body:
        err(p, "`disputed: true` but the body has no warning block")
    if r.get("confidence") in ("C", "D") and "[!WARNING]" not in body:
        err(p, f"`confidence: {r['confidence']}` but the body has no warning block")

    # frontmatter CJK scan (translation fields excluded)
    for k, v in r.items():
            if k.startswith("_") or k.startswith("title_") or k.startswith("summary_"):
                continue
            vals = v if isinstance(v, list) else [v]
            for item in vals:
                texts = item.values() if isinstance(item, dict) else [item]
                for txt in texts:
                    if isinstance(txt, str) and CJK_RE.search(txt):
                        err(p, f"field `{k}` contains CJK: {txt[:50]!r}")

    # internal links
    for m in re.finditer(r'\]\((\.\./[^)#]+|[A-Za-z0-9][^):#]*\.md)\)', body):
        tgt = m.group(1)
        if tgt.startswith("http"):
            continue
        full = os.path.normpath(os.path.join(os.path.dirname(os.path.join(ROOT, p)), tgt))
        if not os.path.exists(full):
            err(p, f"internal link points to a missing file: {tgt}")

# ---------------------------------------------------------- translation mirrors
mirror_ids = set()
for mid, m in sorted(mirrors.items()):
    mirror_ids.add(mid)
    if mid not in seen_id:
        err(m["path"], "mirror has no matching primary record")
    else:
        primary = next(r for r in rows if r["id"] == mid)
        if not str(primary.get("title_zh") or "").strip():
            err(m["path"], "primary record is missing `title_zh`")
        elif str(primary["title_zh"]) != m["title"]:
            err(m["path"], "mirror `title` differs from the primary record's `title_zh`")
        if not str(primary.get("summary_zh") or "").strip():
            err(m["path"], "primary record is missing `summary_zh`")
        elif str(primary["summary_zh"]).strip() != m["summary"].strip():
            err(m["path"], "mirror `summary` differs from the primary record's `summary_zh`")
missing_mirrors = [r["_path"] for r in rows if r["id"] not in mirror_ids]
for p in missing_mirrors:
    err(p, "no Chinese mirror under incidents/i18n/zh/")

# ---------------------------------------------------------- monthly directories
for d in sorted(glob.glob(os.path.join(INCIDENTS, "*"))):
    if os.path.isdir(d) and os.path.basename(d) != "i18n" \
            and not os.path.exists(os.path.join(d, "README.md")):
        err(os.path.relpath(d, ROOT).replace("\\", "/"), "missing README.md (run scripts/build.py)")

# regions/ must not keep pages that match no records
REGION_GROUPS = {"us": ["US"], "eu-uk": ["EU", "UK"], "jp": ["JP"], "kr": ["KR"],
                 "cn": ["CN"], "tw-etc": ["TW", "HK", "SG", "SEA", "APAC", "AU"]}
SEEN_REGIONS = {x for r in rows for x in r.get("region", [])}
for f in sorted(glob.glob(os.path.join(ROOT, "regions", "*.md"))):
    slug = os.path.basename(f)[:-3]
    if slug == "README":
        continue
    rel = "regions/" + slug + ".md"
    if not re.match(r'^[a-z0-9-]+$', slug):
        err(rel, "filename contains non-ASCII or illegal characters")
        continue
    codes = REGION_GROUPS.get(slug, [slug.upper()])
    if not (set(codes) & SEEN_REGIONS):
        err(rel, "this region page matches no records (codes " + "/".join(codes) + ") - stale file")

# ---------------------------------------------------------- repo-wide link check
SKIP_DIRS = {".git", "node_modules", "dist", "assets", ".github"}
LINK_RE = re.compile(r'\[[^\]]*\]\(([^)\s]+)\)')
md_files = []
for base, dirs, files in os.walk(ROOT):
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    for f in files:
        if f.endswith(".md"):
            md_files.append(os.path.join(base, f))
for f in sorted(md_files):
    rel = os.path.relpath(f, ROOT).replace("\\", "/")
    if re.match(r'^incidents/[^/]+/[^/]+\.md$', rel) and not rel.endswith("/README.md"):
        continue                                  # checked record by record above
    body = io.open(f, encoding="utf-8").read()
    for m in LINK_RE.finditer(body):
        tgt = m.group(1)
        if tgt.startswith(("http://", "https://", "#", "mailto:")):
            continue
        tgt = tgt.split("#")[0]
        if not tgt:
            continue
        full = os.path.normpath(os.path.join(os.path.dirname(f), tgt))
        if not os.path.exists(full):
            err(rel, f"internal link points to a missing file: {tgt}")

# ---------------------------------------------------------- English-default scan
for f in sorted(md_files):
    rel = os.path.relpath(f, ROOT).replace("\\", "/")
    if rel == "SCAN.md" or rel.startswith("docs/i18n/") or rel.startswith("incidents/i18n/"):
        continue
    if re.match(r'^incidents/[^/]+/[^/]+\.md$', rel):   # primary records: handled above
        continue
    body = io.open(f, encoding="utf-8").read()
    # language switchers legitimately carry native names (简体中文, 日本語, ...)
    lines = [ln for ln in body.split("\n")
             if CJK_RE.search(ln) and not re.search(r'README\.[A-Za-z-]+\.md', ln)]
    if lines:
        err(rel, f"generated English page contains CJK: {lines[0].strip()[:60]!r}")

print(f"validated {len(rows)} records \u00b7 {len(set(r['_month'] for r in rows))} months "
      f"\u00b7 {len(mirrors)} zh mirrors")
if WARN:
    print(f"\n\u26a0\ufe0f  {len(WARN)} warnings")
    for w in WARN[:40]:
        print("   ", w)
    if len(WARN) > 40:
        print(f"    ... and {len(WARN)-40} more")
if ERR:
    print(f"\n\u274c {len(ERR)} errors")
    for e in ERR[:60]:
        print("   ", e)
    if len(ERR) > 60:
        print(f"    ... and {len(ERR)-60} more")
    sys.exit(1)
print("\n\u2705 all checks passed")
