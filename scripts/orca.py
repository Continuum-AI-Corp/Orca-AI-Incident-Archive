# -*- coding: utf-8 -*-
"""Orca AI Incident Archive - shared library.

Loads records from ``incidents/<month>/<id>.md`` and the Chinese translation
mirrors from ``incidents/i18n/zh/<month>/<id>.md``.

The frontmatter parser is hand-written on purpose: the schema only uses a few
YAML forms, and a small parser beats an extra dependency (it also keeps CI
lightweight).
"""
import os, re, io, sys, glob

from l10n import LANGS, TYPE_NAME, REGION_NAME, SEV_NAME, KIND_NAME, AI_NAME

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INCIDENTS = os.path.join(ROOT, "incidents")
MIRRORS = os.path.join(INCIDENTS, "i18n")

SEV_ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3, "info": 4}
SEV_COLOR = {"critical": "88091D", "high": "B23B40", "medium": "C4615F",
             "low": "8C6A6A", "info": "6B7175"}
GRADE_COLOR = {"A": "157A41", "B": "2359A8", "C": "9A6008", "D": "A82B39"}

KINDS = set(KIND_NAME)
SEVERITIES = set(SEV_NAME)
GRADES = set("ABCD")
AI_VALUES = set(AI_NAME)
PRECISIONS = {"day", "part", "month", "year", "unknown"}
TYPES = set(TYPE_NAME)

SEV_SLOTS = ["critical", "high", "medium", "low", "info"]
KIND_SLOTS = ["incident", "vulnerability", "research", "report", "policy"]

# Fields every record must carry; the per-language fields are optional at
# parse time and enforced by scripts/validate.py.
REQUIRED = ["id", "title", "date", "date_precision", "kind", "type", "severity",
            "confidence", "real_harm", "ai_involvement", "region", "summary", "sources"]


def pct_encode(s):
    """Percent-encode non-ASCII characters (shields.io needs plain URLs)."""
    return "".join(ch if ord(ch) < 128 else b"".join(
        ("%%%02X" % byte).encode() for byte in ch.encode("utf-8")).decode()
        for ch in s)


def badge(label, msg, color):
    enc = lambda s: pct_encode(s.replace("-", "--").replace("_", "__").replace(" ", "_")
                               .replace("/", "%2F").replace("?", "%3F").replace("#", "%23"))
    return f"https://img.shields.io/badge/{enc(label)}-{enc(msg)}-{color}?style=flat-square"


def _unquote(v):
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        return v[1:-1].replace('\\"', '"').replace("\\\\", "\\")
    return v


def _scalar(v):
    v = v.strip()
    if v in ("null", "~", ""):
        return None
    if v == "true":
        return True
    if v == "false":
        return False
    if v.startswith("[") and v.endswith("]"):
        inner = v[1:-1].strip()
        return [_unquote(x) for x in inner.split(",") if x.strip()] if inner else []
    return _unquote(v)


def parse_frontmatter(text, path=""):
    """Return (dict, body). Only the forms used by this repo's schema."""
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing opening '---' for frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError(f"{path}: frontmatter is not closed")
    head, body = text[4:end], text[end + 5:]
    data, lines, i = {}, head.split("\n"), 0
    while i < len(lines):
        ln = lines[i]
        if not ln.strip() or ln.lstrip().startswith("#"):
            i += 1
            continue
        m = re.match(r'^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$', ln)
        if not m:
            raise ValueError(f"{path}: cannot parse line {i+1}: {ln!r}")
        key, val = m.group(1), m.group(2)
        if val.strip() == "|":                       # block scalar
            i += 1
            buf = []
            while i < len(lines) and (lines[i].startswith("  ") or not lines[i].strip()):
                buf.append(lines[i][2:] if lines[i].startswith("  ") else "")
                i += 1
            data[key] = "\n".join(buf).strip("\n")
            continue
        if val.strip() == "":                        # list
            i += 1
            items, cur = [], None
            while i < len(lines) and lines[i].startswith("  "):
                s = lines[i][2:]
                if s.startswith("- "):
                    if cur is not None:
                        items.append(cur)
                    rest = s[2:]
                    mm = re.match(r'^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$', rest)
                    cur = {mm.group(1): _scalar(mm.group(2))} if mm else rest.strip()
                elif s.startswith("  ") and isinstance(cur, dict):
                    mm = re.match(r'^\s*([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$', s)
                    if mm:
                        cur[mm.group(1)] = _scalar(mm.group(2))
                elif s.strip() == "[]":
                    pass
                i += 1
            if cur is not None:
                items.append(cur)
            data[key] = items
            continue
        data[key] = _scalar(val)
        i += 1
    return data, body


def _load_dir(pattern, verbose_tag=""):
    out = []
    for p in sorted(glob.glob(pattern)):
        name = os.path.basename(p)
        if name == "README.md":
            continue
        t = io.open(p, encoding="utf-8").read()
        d, body = parse_frontmatter(t, os.path.relpath(p, ROOT).replace("\\", "/"))
        d["_path"] = os.path.relpath(p, ROOT).replace("\\", "/")
        d["_month"] = os.path.basename(os.path.dirname(p))
        d["_file"] = name
        d["_body"] = body
        out.append(d)
    return out


def load_all(verbose=False):
    """Load every record, sorted by date then id."""
    out = _load_dir(os.path.join(INCIDENTS, "*", "*.md"))
    out.sort(key=lambda r: (str(r.get("date")), r.get("id", "")))
    if verbose:
        print(f"loaded {len(out)} incidents from {len(set(r['_month'] for r in out))} months")
    return out


def load_mirrors(lang="zh"):
    """Load translation mirrors -> {id: {title, summary, path, month}}."""
    out = {}
    for p in sorted(glob.glob(os.path.join(MIRRORS, lang, "*", "*.md"))):
        t = io.open(p, encoding="utf-8").read()
        d, _ = parse_frontmatter(t, os.path.relpath(p, ROOT).replace("\\", "/"))
        out[d["id"]] = {
            "title": str(d.get("title") or ""),
            "summary": str(d.get("summary") or ""),
            "path": os.path.relpath(p, ROOT).replace("\\", "/"),
            "month": os.path.basename(os.path.dirname(p)),
        }
    return out


def localized(record, mirrors, lang):
    """Return (title, summary) for a language, falling back to English.

    Chinese prefers the mirror files (single source of truth for zh), every
    other language reads the inline ``title_<lang>`` / ``summary_<lang>``
    fields.
    """
    if lang == "en":
        return str(record.get("title") or ""), str(record.get("summary") or "")
    if lang == "zh" and record.get("id") in mirrors:
        m = mirrors[record["id"]]
        return m["title"], m["summary"]
    t = record.get("title_" + lang) or record.get("title")
    s = record.get("summary_" + lang) or record.get("summary")
    return str(t or ""), str(s or "")


# Languages that ship translated record titles/summaries:
# en (source) + zh (mirror) + the inline translation fields = all LANGS.
RECORD_LANGS = list(LANGS)
