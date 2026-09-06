"""Near-duplicate detector for templated page sets - city pages above all.

    python3 code/check_page_similarity.py --base http://localhost:3000
    python3 code/check_page_similarity.py --base https://theirsite.com --pattern /services/

Answers one question: are these pages genuinely different, or is this the same
page with the city name swapped? Full method and provenance in
references/doorway-pages.md.

The method (order matters - skip step 2 and every number is garbage):
  1. Extract main content, dropping nav/footer/template chrome.
  2. Drop shingles that appear on >30% of pages - the site's own boilerplate.
     THIS is what turns "all my pages are 95% similar" into a real signal.
  3. Compare what's left, by containment as well as Jaccard. A template clone
     is not "resembling" the master, it is CONTAINED in it.

Thresholds and where they come from:
  Jaccard >= 0.50   near-duplicate    Broder et al., WWW 1997 (AltaVista, web-scale)
  Containment >= 0.80  template clone  the right measure for templated sets
  Jaccard >= 0.85   duplicate, consolidate
  unique shingles   the most actionable number here - "how many distinct 5-word
                    phrases does this page own". 12 is a doorway page.

NO WORD-COUNT GATE, deliberately. Mueller: word count is not a ranking factor
and not a sign of thin content. Word count is reported as context only.
"""

import argparse
import re
import sys
import urllib.request
from collections import Counter
from html.parser import HTMLParser

SHINGLE_WIDTH = 5           # 5-word windows; Broder used 10, 5 suits short web copy
BOILERPLATE_DF = 0.30       # drop shingles on >30% of pages
JACCARD_NEAR = 0.50         # Broder 1997
JACCARD_DUPE = 0.85
CONTAINMENT_CLONE = 0.80
UNIQUE_SHINGLE_FLOOR = 50   # below this, the page owns almost nothing
TIMEOUT = 20

# Tags whose contents are never main content.
_SKIP_TAGS = {"script", "style", "nav", "header", "footer", "noscript", "svg", "form"}


class MainText(HTMLParser):
    """Minimal main-content extractor - no dependency needed.

    trafilatura does this better (best performer in the 2023 ACM SIGIR
    comparison). If it is installed we use it; this is the fallback so the
    check always runs.
    """

    def __init__(self):
        super().__init__()
        self.chunks = []
        self._skip_depth = 0

    def handle_starttag(self, tag, attrs):
        if tag in _SKIP_TAGS:
            self._skip_depth += 1

    def handle_endtag(self, tag):
        if tag in _SKIP_TAGS and self._skip_depth:
            self._skip_depth -= 1

    def handle_data(self, data):
        if not self._skip_depth:
            text = data.strip()
            if text:
                self.chunks.append(text)

    def text(self):
        return " ".join(self.chunks)


def main_text(html: str) -> str:
    try:
        import trafilatura  # noqa: PLC0415
        extracted = trafilatura.extract(
            html, include_comments=False, include_tables=False, favor_recall=True
        )
        if extracted:
            return extracted
    except ImportError:
        pass
    parser = MainText()
    try:
        parser.feed(html)
    except Exception:  # noqa: BLE001 - malformed markup still yields partial text
        pass
    return parser.text()


def tokens(text: str) -> list:
    return re.sub(r"[^a-z0-9\s]", " ", text.lower()).split()


def shingles(words: list, width: int = SHINGLE_WIDTH) -> set:
    if len(words) < width:
        return {" ".join(words)} if words else set()
    return {" ".join(words[i:i + width]) for i in range(len(words) - width + 1)}


def jaccard(a: set, b: set) -> float:
    union = a | b
    return len(a & b) / len(union) if union else 0.0


def containment(a: set, b: set) -> float:
    """How much of A lives inside B. Asymmetric, and that is the point."""
    return len(a & b) / len(a) if a else 0.0


def fetch(url: str):
    request = urllib.request.Request(url, headers={"User-Agent": "seo-blueprint-pro/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
            return response.status, response.read().decode("utf-8", "ignore")
    except Exception as error:  # noqa: BLE001
        return 0, f"__ERROR__{error}"


def discover(base: str, pattern: str, cap: int = 200) -> list:
    """Crawl from / and keep same-origin URLs matching the pattern."""
    seen, queue, found = {base + "/"}, [base + "/"], []
    while queue and len(seen) < cap:
        url = queue.pop(0)
        status, body = fetch(url)
        if status != 200:
            continue
        if pattern in url and url not in found:
            found.append(url)
        for href in re.findall(r'href="(/[^"#?]*)"', body):
            nxt = base + href.rstrip("/")
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return sorted(found)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--base", required=True, help="site root, e.g. http://localhost:3000")
    ap.add_argument("--pattern", default="/services/", help="only compare URLs containing this")
    ap.add_argument("--urls", nargs="*", help="explicit URLs instead of crawling")
    args = ap.parse_args()
    base = args.base.rstrip("/")

    urls = args.urls or discover(base, args.pattern)
    if len(urls) < 2:
        print(f"Need 2+ pages matching '{args.pattern}' to compare. Found {len(urls)}.")
        return 0

    print(f"Comparing {len(urls)} pages matching '{args.pattern}'\n")

    raw = {}
    for url in urls:
        status, body = fetch(url)
        if status != 200:
            print(f"  skipped {url} (HTTP {status})")
            continue
        raw[url] = shingles(tokens(main_text(body)))

    if len(raw) < 2:
        print("Not enough pages fetched successfully.")
        return 0

    # Step 2: strip the site's OWN boilerplate. The highest-leverage step here.
    df = Counter(s for st in raw.values() for s in st)
    total = len(raw)
    boiler = {s for s, count in df.items() if count / total > BOILERPLATE_DF}
    clean = {url: st - boiler for url, st in raw.items()}
    print(f"Removed {len(boiler)} boilerplate phrases present on >{int(BOILERPLATE_DF*100)}% of pages.\n")

    failures, warnings = [], []
    ordered = sorted(clean)

    for url in ordered:
        own = len(clean[url])
        if own < UNIQUE_SHINGLE_FLOOR:
            failures.append(
                f"{url}\n      owns only {own} distinct phrases after boilerplate removal "
                f"(floor {UNIQUE_SHINGLE_FLOOR}) - it says almost nothing its siblings don't"
            )

    for i, a in enumerate(ordered):
        for b in ordered[i + 1:]:
            jac = jaccard(clean[a], clean[b])
            c_ab, c_ba = containment(clean[a], clean[b]), containment(clean[b], clean[a])
            worst = max(c_ab, c_ba)
            if jac >= JACCARD_DUPE:
                failures.append(f"{a}\n   vs {b}\n      DUPLICATE - {jac:.0%} identical. Consolidate: keep one, 301 the other.")
            elif worst >= CONTAINMENT_CLONE:
                inner, outer = (a, b) if c_ab >= c_ba else (b, a)
                failures.append(
                    f"{inner}\n   vs {outer}\n      TEMPLATE CLONE - {worst:.0%} of the first page is contained in the second "
                    f"(overlap {jac:.0%}). Same page, different label."
                )
            elif jac >= JACCARD_NEAR:
                warnings.append(f"{a}\n   vs {b}\n      near-duplicate - {jac:.0%} overlap (Broder threshold 50%). Differentiate before publishing.")

    if failures:
        print(f"FAIL - {len(failures)} problem(s):\n")
        for item in failures:
            print(f"  - {item}\n")
    if warnings:
        print(f"WARNINGS - {len(warnings)}:\n")
        for item in warnings:
            print(f"  - {item}\n")

    if not failures and not warnings:
        print("PASS - every page owns enough distinct content to justify its URL.")

    print("\nWhat to do: differentiate the PROBLEM, not the place name. Real jobs done there,")
    print("real neighbourhoods, city-specific FAQ answers, a real local review.")
    print("Full checklist: references/doorway-pages.md")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
