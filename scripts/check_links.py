# -*- coding: utf-8 -*-
"""Spot-check that outbound source links are still alive.

    python scripts/check_links.py                 # all links (slow)
    python scripts/check_links.py --sample 60     # random sample of 60
    python scripts/check_links.py --timeout 12

Dead links deliberately do **not** fail CI - vendors take primary sources
down all the time.  This script lists what needs attention so a maintainer
can decide whether to replace a source or flag it.
"""
import os, sys, ssl, json, random, argparse, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from orca import ROOT, load_all

UA = ("Mozilla/5.0 (compatible; OrcaArchiveLinkCheck/1.0; "
      "+https://github.com/Continuum-AI-Corp/Orca-AI-Incident-Archive)")

def check(url, timeout):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
                return r.status, ""
        except urllib.error.HTTPError as e:
            if e.code in (403, 405, 429) and method == "HEAD":
                continue
            return e.code, e.reason
        except Exception as e:
            if method == "HEAD":
                continue
            return 0, type(e).__name__
    return 0, "unreachable"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sample", type=int, default=0, help="random sample size, 0 = check all")
    ap.add_argument("--timeout", type=int, default=15)
    ap.add_argument("--workers", type=int, default=8)
    a = ap.parse_args()

    rows = load_all()
    pairs = sorted({(s["url"], r["id"]) for r in rows for s in r["sources"]})
    by_url = {}
    for u, i in pairs:
        by_url.setdefault(u, []).append(i)
    urls = sorted(by_url)
    if a.sample and a.sample < len(urls):
        random.seed(20260916)
        urls = random.sample(urls, a.sample)

    print(f"checking {len(urls)} URLs ({len(by_url)} unique URLs in the archive)\n")
    bad = []
    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        for u, (code, msg) in zip(urls, ex.map(lambda x: check(x, a.timeout), urls)):
            ok = 200 <= code < 400
            if not ok:
                bad.append((u, code, msg, by_url[u]))
                print(f"  x {code or '-'} {u}\n      cited by: {', '.join(by_url[u][:3])}"
                      + (f" and {len(by_url[u])} more" if len(by_url[u]) > 3 else ""))
    print(f"\n{len(urls) - len(bad)}/{len(urls)} reachable")
    if bad:
        print(f"{len(bad)} need attention. 403/429 is usually bot protection, not a dead "
              f"link - confirm by hand before changing anything.")
    # deliberately no exit(1): outbound link rot is normal and must not block contributors

if __name__ == "__main__":
    main()
