# -*- coding: utf-8 -*-
"""Spot-check that outbound source links are still alive.

    python scripts/check_links.py                 # all links (slow)
    python scripts/check_links.py --sample 60     # random sample of 60
    python scripts/check_links.py --timeout 12

Dead links deliberately do **not** fail CI - vendors take primary sources
down all the time.  This script lists what needs attention so a maintainer
can decide whether to replace a source or flag it.

Only public addresses on ports 80/443 are contacted. Redirects are reported
without following them, and HTTPS certificates are verified.
"""
import os, sys, ssl, random, argparse, socket, ipaddress, http.client
from urllib.parse import urlsplit
from concurrent.futures import ThreadPoolExecutor
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from orca import ROOT, load_all

UA = ("Mozilla/5.0 (compatible; OrcaArchiveLinkCheck/1.0; "
      "+https://github.com/Continuum-AI-Corp/Orca-AI-Incident-Archive)")

def public_destination(url):
    """Validate URL and resolve once; connections use these exact addresses."""
    if not isinstance(url, str) or any(ord(c) <= 32 or ord(c) == 127 for c in url) or "\\" in url:
        raise ValueError("invalid URL characters")
    parsed = urlsplit(url)
    if parsed.scheme not in ("http", "https") or not parsed.hostname:
        raise ValueError("only public HTTP(S) URLs are checked")
    if parsed.username is not None or parsed.password is not None:
        raise ValueError("URL credentials are not allowed")
    port = parsed.port if parsed.port is not None else (443 if parsed.scheme == "https" else 80)
    if port not in (80, 443):
        raise ValueError("only web ports are checked")
    addresses = socket.getaddrinfo(parsed.hostname, port, type=socket.SOCK_STREAM)
    if not addresses:
        raise ValueError("host has no addresses")
    for _, _, _, _, address in addresses:
        ip = ipaddress.ip_address(address[0])
        mapped = getattr(ip, "ipv4_mapped", None)
        if (not ip.is_global or ip.is_multicast or ip.is_reserved or
                getattr(ip, "sixtofour", None) is not None or
                getattr(ip, "teredo", None) is not None or
                (mapped is not None and not mapped.is_global)):
            raise ValueError("non-public destination")
    return parsed, addresses


def connect_public(addresses, timeout):
    # Connect directly to validated sockaddr values: resolving the hostname a
    # second time here would reopen DNS-rebinding attacks. Proxies are unused.
    last_error = None
    for family, kind, protocol, _, address in addresses:
        sock = socket.socket(family, kind, protocol)
        try:
            sock.settimeout(timeout)
            sock.connect(address)
            return sock
        except OSError as error:
            sock.close()
            last_error = error
    raise last_error or OSError("no usable address")


class PublicHTTPConnection(http.client.HTTPConnection):
    def connect(self):
        self.sock = connect_public(self.public_addresses, self.timeout)


class PublicHTTPSConnection(http.client.HTTPSConnection):
    def connect(self):
        sock = connect_public(self.public_addresses, self.timeout)
        try:
            # Keep the original DNS name for certificate verification and SNI.
            self.sock = self._context.wrap_socket(sock, server_hostname=self.host)
        except Exception:
            sock.close()
            raise


def check(url, timeout):
    try:
        parsed, addresses = public_destination(url)
    except (ValueError, OSError) as error:
        return 0, type(error).__name__
    target = parsed.path or "/"
    if parsed.query:
        target += "?" + parsed.query
    for method in ("HEAD", "GET"):
        if parsed.scheme == "https":
            conn = PublicHTTPSConnection(parsed.hostname, parsed.port, timeout=timeout,
                                         context=ssl.create_default_context())
        else:
            conn = PublicHTTPConnection(parsed.hostname, parsed.port, timeout=timeout)
        conn.public_addresses = addresses
        try:
            conn.request(method, target, headers={"User-Agent": UA})
            response = conn.getresponse()
            if response.status in (403, 405, 429) and method == "HEAD":
                continue
            # A redirect proves the source responds. Never follow an untrusted
            # Location header into private networks or a different scheme.
            return response.status, response.reason
        except Exception as e:
            if method == "HEAD":
                continue
            return 0, type(e).__name__
        finally:
            conn.close()
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
