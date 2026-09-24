# -*- coding: utf-8 -*-
"""Check that dist/incidents.json still loads in OrcaRouter-O2.

    python scripts/downstream_contract.py              # checks dist/incidents.json
    python scripts/downstream_contract.py other.json   # checks another export

Exit code 0 = compatible, 1 = O2 would break.  CI runs it after every rebuild.

OrcaRouter-O2's /incident-archive page reads ``main``'s dist/incidents.json
twice, and pins neither read to a commit:

  * in the browser, on every visit -- when the file fails O2's validation the
    page silently falls back to an older bundled snapshot;
  * at every O2 build -- a validation failure stops the build, so no O2 release
    of any kind can ship until this repository is fixed.

A merge to ``main`` is therefore a production data release for O2.  This file
ports the two things O2 holds the export to:

  A. the validator O2 runs before accepting the file
     (web/src/pages/IncidentArchive/archiveValidate.js); failing it breaks O2
     in production;
  B. the data assertions in O2's test suite (dataContract.test.js and
     archiveClaims.test.js); failing them turns every O2 pull request red.

Content changes -- new records, corrected facts, extra sources -- pass both.
What does not: another ``schema_version``, a new kind / severity / confidence /
ai_involvement value, a new type code, renamed fields, moved record files.
Land those in O2 first, then here, and update this file to match.

Ported from OrcaRouter-O2 as of 2026-09-24; where Python's URL parsing and the
browser's differ, the port errs on the side of rejecting.
"""
import os, re, sys, json, datetime
from urllib.parse import urlsplit

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, "dist", "incidents.json")

# O2's closed vocabularies (archiveDerive.js).  The page colours, groups and
# filters on these, so O2 rejects an unknown value instead of drawing a blank.
SEVERITIES = ("critical", "high", "medium", "low", "info")
KINDS = ("incident", "vulnerability", "research", "report", "policy")
GRADES = ("A", "B", "C", "D")
AI_INVOLVEMENTS = ("confirmed", "disputed", "unverified", "not-applicable")
# Type codes O2 has a label, a description and an icon for.  Its validator only
# checks the shape of a type code; its test suite needs all three to exist.
O2_TYPES = ("IPI", "EXFIL", "SUPPLY", "MCP", "SANDBOX", "ROGUE", "WEAPON",
            "INFRA", "CRED", "EVAL", "GOV", "OTHER")
TRANS_LANGS = ("zh", "ja", "ko", "de", "fr", "es")
STRING_FIELDS = (["title", "title_en", "summary", "date_raw"]
                 + [f"{f}_{l}" for l in TRANS_LANGS for f in ("title", "summary")])

# fullmatch() throughout: Python's "$" also matches before a trailing newline,
# JavaScript's does not.  [0-9] rather than \d, which matches any Unicode digit.
ID_RE = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}-[a-z0-9][a-z0-9-]*")
DATE_RE = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}")
TYPE_RE = re.compile(r"[A-Z][A-Z0-9_-]*")
REGION_RE = re.compile(r"[A-Z0-9_-]+")
CJK = re.compile("[一-鿿]")               # O2's /[一-鿿]/
SAFE_SCHEME = re.compile(r"\s*https?://", re.I)    # O2's /^\s*https?:\/\//i
CONTROL = re.compile("[\x00-\x1f\x7f]")
# Characters the browser's URL parser refuses in a host but urlsplit() keeps.
BAD_HOST = re.compile(r"[\s<>^|%\\\[\]]")


def valid_date(value):
    if not isinstance(value, str) or not DATE_RE.fullmatch(value):
        return False
    try:
        datetime.date.fromisoformat(value)
    except ValueError:
        return False
    return True


def safe_source_url(value):
    """O2's safeSourceURL: an http(s) URL with a host and no credentials.

    Source URLs end up in an <a href>.  The scheme test is what keeps
    javascript:, data: and the like out; control characters and user:pass@
    are refused outright.  Plain http is fine -- it is a link, not a script."""
    if not isinstance(value, str) or not SAFE_SCHEME.match(value) or CONTROL.search(value):
        return False
    try:
        parts = urlsplit(value.strip(" "))
        parts.port                      # raises ValueError for a malformed port
    except ValueError:
        return False
    host = parts.hostname or ""
    return (parts.scheme in ("http", "https") and bool(host)
            and not BAD_HOST.search(host)
            and not parts.username and not parts.password)


def _is_number(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def check_archive(doc):
    """Part A -- port of archiveValidate(): every problem O2's validator would
    report, in its wording.  Any problem at all makes O2 reject the whole file."""
    if not isinstance(doc, dict):
        return ["payload is not a JSON object"]
    p = []
    rows = doc.get("incidents")
    if doc.get("version") is not None and not valid_date(doc["version"]):
        p.append("version must be an ISO date string")
    sv = doc.get("schema_version")
    if sv is not None and not (_is_number(sv) and sv == 2):
        p.append(f"unsupported schema_version: {sv}")
    if not isinstance(rows, list):
        return p + ["payload has no `incidents` array"]
    count = doc.get("count")
    if count is not None and not (_is_number(count) and float(count).is_integer()
                                  and count == len(rows)):
        p.append(f"count={count} but incidents[] has {len(rows)} entries")
    if not rows:
        return p + ["incidents[] is empty"]

    ids = set()
    for r in rows:
        at = r.get("id") if isinstance(r, dict) and r.get("id") else "(record with no id)"
        if not isinstance(r, dict):
            p.append(f"{at}: not an object")
            continue
        rid, date = r.get("id"), r.get("date")
        if not isinstance(rid, str) or not ID_RE.fullmatch(rid) or not valid_date(date):
            p.append(f"{at}: missing id or date")
            continue
        if rid in ids:
            p.append(f"{at}: duplicate id")
        ids.add(rid)
        if r.get("real_harm") is not None and not isinstance(r["real_harm"], bool):
            p.append(f"{at}: real_harm must be boolean or null")
        for field in ("disputed", "landmark"):
            if field in r and not isinstance(r[field], bool):
                p.append(f"{at}: {field} must be boolean")
        month = date[:7]
        if r.get("month") is not None and r["month"] != month:
            p.append(f"{at}: inconsistent month")
        for field in STRING_FIELDS:
            if r.get(field) is not None and not isinstance(r[field], str):
                p.append(f"{at}: {field} must be a string")

        # every "open the record" link on the page is built from `path`
        want = f"incidents/{month}/{rid}.md"
        if r.get("path") != want:
            p.append(f'{at}: path="{r.get("path")}" expected "{want}"')
        if r.get("path_zh") is not None and r["path_zh"] != f"incidents/i18n/zh/{month}/{rid}.md":
            p.append(f"{at}: invalid Chinese record path")

        # the whole English view of the page rests on this one field
        en = r.get("title_en") or r.get("title")
        if not en or not str(en).strip():
            p.append(f"{at}: no English title (neither title_en nor title)")
        elif CJK.search(str(en)):
            p.append(f'{at}: the English title contains Chinese — "{str(en)[:40]}"')

        sources = r.get("sources")
        if not isinstance(sources, list) or not sources:
            p.append(f"{at}: no sources — the archive's own rule is that a record needs one")
        else:
            for s in sources:
                label = s.get("label") if isinstance(s, dict) else None
                url = s.get("url") if isinstance(s, dict) else None
                if label is not None and not isinstance(label, str):
                    p.append(f"{at}: source label must be a string")
                if not s or not safe_source_url(url):
                    p.append(f'{at}: source url is not http(s) — "{str(url)[:60]}"')

        if r.get("severity") not in SEVERITIES:
            p.append(f'{at}: unknown severity "{r.get("severity")}"')
        if r.get("kind") not in KINDS:
            p.append(f'{at}: unknown kind "{r.get("kind")}"')
        if r.get("confidence") not in GRADES:
            p.append(f'{at}: unknown confidence "{r.get("confidence")}"')
        if r.get("ai_involvement") not in AI_INVOLVEMENTS:
            p.append(f'{at}: unknown ai_involvement "{r.get("ai_involvement")}"')
        ty = r.get("type")
        if (not isinstance(ty, list) or not ty
                or any(not isinstance(v, str) or not TYPE_RE.fullmatch(v) for v in ty)):
            p.append(f"{at}: type[] is empty")
        rg = r.get("region")
        if (not isinstance(rg, list) or not rg
                or any(not isinstance(v, str) or not REGION_RE.fullmatch(v) for v in rg)):
            p.append(f"{at}: region[] is empty")
    return p


def _newest_first(rows):
    # O2 sorts on date descending, then id ascending; two stable passes.
    return sorted(sorted(rows, key=lambda r: r["id"]), key=lambda r: r["date"], reverse=True)


def pick_landmarks(rows):
    """Port of archiveDerive.js pickLandmarks(): the three cards O2 features --
    critical records with confirmed harm, landmark ones first, newest first,
    preferring three different first types."""
    def take(pool, out, distinct):
        seen = {r["type"][0] for r in out}
        taken = {r["id"] for r in out}
        for r in pool:
            if len(out) >= 3:
                break
            if r["id"] in taken or (distinct and r["type"][0] in seen):
                continue
            out.append(r)
            seen.add(r["type"][0])
            taken.add(r["id"])
        return out

    harmful = [r for r in rows if r["severity"] == "critical" and r.get("real_harm") is True]
    primary = _newest_first([r for r in harmful if r.get("landmark")])
    backfill = _newest_first(harmful)
    out = take(primary, [], True)
    if len(out) < 3:
        out = take(backfill, out, True)
    if len(out) < 3:
        out = take(primary, out, False)
    if len(out) < 3:
        out = take(backfill, out, False)
    return _newest_first(out)


def check_o2_tests(doc):
    """Part B -- data assertions in O2's test suite.  Assumes part A passed."""
    rows = doc["incidents"]
    p = []
    unknown = sorted({t for r in rows for t in r["type"]} - set(O2_TYPES))
    if unknown:
        p.append(f"type code(s) {', '.join(unknown)} have no label, description or icon in "
                 "O2 (taxonomy.js, icons.jsx) — add them there first")

    featured = pick_landmarks(rows)
    if not featured:
        p.append("no critical record with real_harm: true — O2's featured cards would be empty")
    below_a = [r["id"] for r in featured if r["confidence"] != "A"]
    if below_a:
        p.append("O2 would feature records below grade A: " + ", ".join(below_a)
                 + " — its copy promises the featured cards a primary source")
    firsts = [r["type"][0] for r in featured]
    if len(set(firsts)) != len(firsts):
        p.append("O2's featured cards would repeat a type description: first types "
                 + ", ".join(firsts))

    kinds = {r["kind"] for r in rows}
    if len(kinds) < 2:
        p.append("every record has the same kind — O2's methodology checks need more than one")
    incidents = sum(1 for r in rows if r["kind"] == "incident")
    if incidents == 0:
        p.append("no record has kind incident — O2's counting-rule check expects some")
    elif incidents >= len(rows):
        p.append("every record is an incident — O2's counting-rule check no longer applies")
    if all(r["confidence"] == "A" for r in rows):
        p.append("every record is grade A — O2's primary-source check no longer applies")

    # the landing-page band ships inside the page's first chunk; O2 caps it at 2,000 bytes
    strip = {"build": doc.get("version") or "", "count": len(rows),
             "harm": sum(1 for r in rows if r.get("real_harm") is True),
             "sources": len({s["url"] for r in rows for s in r["sources"]}),
             "m": [n for _, n in sorted(_month_counts(rows).items())]}
    size = len(json.dumps(strip, separators=(",", ":"), ensure_ascii=False))
    if size >= 2000:
        p.append(f"O2's landing-band data would be {size} bytes (limit 2,000)")
    return p


def _month_counts(rows):
    out = {}
    for r in rows:
        out[r["date"][:7]] = out.get(r["date"][:7], 0) + 1
    return out


def check(doc):
    """(part A problems, part B problems).  B is only evaluated once A is clean."""
    a = check_archive(doc)
    return a, ([] if a else check_o2_tests(doc))


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8")
    path = argv[1] if len(argv) > 1 else DIST
    rel = os.path.relpath(path, ROOT).replace("\\", "/")
    try:
        with open(path, encoding="utf-8") as f:
            doc = json.load(f)
    except (OSError, ValueError) as e:
        print(f"❌ {rel}: cannot read it as JSON ({e})")
        return 1
    a, b = check(doc)
    n = len(doc.get("incidents") or []) if isinstance(doc, dict) else 0
    print(f"downstream contract · OrcaRouter-O2 · {rel} · {n} records")
    if a:
        print(f"\n❌ A. O2's validator would reject the whole file ({len(a)} problems):")
        for x in a[:40]:
            print("   ", x)
        if len(a) > 40:
            print(f"    ... and {len(a) - 40} more")
        print("\n   Effect: O2's page silently falls back to an older snapshot, and every O2 build"
              "\n   fails until this is fixed. Fix the data, or change O2 first (see SCHEMA.md).")
        return 1
    print("   A. O2 validator (production)       ✅")
    if b:
        print(f"\n❌ B. O2's test suite would fail ({len(b)} problems):")
        for x in b:
            print("   ", x)
        print("\n   Effect: O2 still loads the file, but every O2 pull request turns red."
              "\n   Coordinate with O2 before merging.")
        return 1
    print("   B. O2 test-suite data checks       ✅")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
