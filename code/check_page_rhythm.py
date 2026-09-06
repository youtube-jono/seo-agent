#!/usr/bin/env python3
"""Fail a page that reads as a wall of text.

    python3 code/check_page_rhythm.py                       # every route
    python3 code/check_page_rhythm.py /services/drain       # one route

check_design_adherence.py polices the tokens. check_page_quality.py polices the
copy. Nothing policed the LAYOUT, which is how a service page shipped with zero
images, zero forms and eight text cards in a row, and a blog post shipped at
9,600 pixels of unbroken paragraphs. Both had every required section.

Instructions get skipped. This does not.

Spec: design/page-structures/{blocks,service-page,blog-post}.md
"""

import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "http://localhost:3000"

MAX_TEXT_RUN = 2          # consecutive TEXT blocks before it is a wall
MAX_SENTENCES = 4         # per paragraph
WORDS_PER_MINUTE = 230
TOC_MINUTES = 6           # a post this long needs jump links
WORDS_PER_VISUAL = 350    # body stretch allowed without something to look at

# Things a reader LOOKS at. A bordered div of grey text is not one of them.
VISUAL_TAGS = ("<img", "<svg", "<video", "<iframe", "<table", "<form", "<ol", "<figure")


def fetch(route):
    try:
        with urllib.request.urlopen(BASE + route, timeout=30) as response:
            return response.read().decode("utf-8", "replace")
    except (urllib.error.URLError, OSError) as error:
        raise SystemExit(
            f"Could not reach {BASE}{route} ({error}).\n"
            "Start the dev server first: cd website && npm run dev"
        )


def routes_from_app():
    """Every route with a page.tsx, minus the ones nobody optimises."""
    app = ROOT / "website" / "app"
    if not app.exists():
        return []
    skip = {"thank-you", "privacy-policy", "terms", "not-found"}
    found = []
    for page in sorted(app.rglob("page.tsx")):
        parts = page.relative_to(app).parts[:-1]
        if any(p in skip for p in parts) or any(p.startswith("[") for p in parts):
            continue
        found.append("/" + "/".join(parts))
    return found


def strip_tags(html):
    html = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html, flags=re.S | re.I)
    return re.sub(r"<[^>]+>", " ", html)


def body_html(html):
    match = re.search(r"<main[^>]*>(.*)</main>", html, flags=re.S | re.I)
    return match.group(1) if match else html


def word_count(html):
    return len(strip_tags(html).split())


def sentence_count(text):
    return len([s for s in re.split(r"[.!?]+(?:\s|$)", text.strip()) if s.strip()])


def longest_text_run(body):
    """Walk the top-level sections in order and count TEXT blocks in a row.

    A block counts as VISUAL only if it actually contains something to look
    at, which is why this reads the rendered HTML rather than trusting the
    component names.
    """
    chunks = re.split(r"(?=<(?:section|aside|figure|form|table|div class=\"[^\"]*block)\b)", body, flags=re.I)
    run = 0
    worst = 0
    for chunk in chunks:
        if not strip_tags(chunk).strip():
            continue
        if any(tag in chunk.lower() for tag in VISUAL_TAGS):
            run = 0
        else:
            run += 1
            worst = max(worst, run)
    return worst


def gap_without_visual(body):
    """Longest stretch of words with nothing to look at in between."""
    pieces = re.split(r"(<img|<svg|<video|<iframe|<table|<figure|<form)", body, flags=re.I)
    return max((len(strip_tags(p).split()) for p in pieces), default=0)


def long_paragraphs(body):
    bad = []
    for para in re.findall(r"<p[^>]*>(.*?)</p>", body, flags=re.S | re.I):
        text = strip_tags(para).strip()
        if sentence_count(text) > MAX_SENTENCES:
            bad.append(text[:80] + "...")
    return bad


def check(route):
    html = fetch(route)
    body = body_html(html)
    failures = []
    words = word_count(body)
    minutes = words / WORDS_PER_MINUTE
    is_blog = route.startswith("/blog/") and route != "/blog"
    is_service = route.startswith("/services/") and route != "/services"

    if "<img" not in body.lower() and "<svg" not in body.lower():
        failures.append("no images at all - every page needs at least one photograph")
    elif "<img" not in body.lower():
        failures.append("no photographs (icons only) - see /build-website Images ladder")

    run = longest_text_run(body)
    if run > MAX_TEXT_RUN:
        failures.append(f"{run} text-only blocks in a row (max {MAX_TEXT_RUN}) - break it with a visual block")

    gap = gap_without_visual(body)
    if gap > WORDS_PER_VISUAL:
        failures.append(f"{gap} words with nothing to look at (max {WORDS_PER_VISUAL})")

    paras = long_paragraphs(body)
    if paras:
        failures.append(f"{len(paras)} paragraph(s) over {MAX_SENTENCES} sentences, first: \"{paras[0]}\"")

    if is_blog and minutes > TOC_MINUTES and "on this page" not in body.lower():
        failures.append(f"{minutes:.0f}-minute read with no table of contents (required over {TOC_MINUTES})")

    if is_service:
        if "<form" not in body.lower():
            failures.append("no form - a money page with no lead capture is not a money page")
        if "no results" in strip_tags(body).lower() or "not published here yet" in strip_tags(body).lower():
            failures.append("a section apologises for having no proof - show the best true material instead")

    return failures, words, minutes


def main():
    targets = sys.argv[1:] or routes_from_app()
    if not targets:
        raise SystemExit("No routes found. Run from the repo root with website/app present.")

    failed = 0
    for route in targets:
        failures, words, minutes = check(route)
        head = f"{route}  ({words} words, {minutes:.0f} min)"
        if failures:
            failed += 1
            print(f"\nFAIL  {head}")
            for f in failures:
                print(f"      - {f}")
        else:
            print(f"PASS  {head}")

    if failed:
        print(
            f"\nPAGE RHYTHM FAILED on {failed} page(s).\n"
            "These pages do not get shown to the owner until they pass.\n"
            "Fix per design/page-structures/ - blocks.md has the vocabulary."
        )
        return 1
    print(f"\nAll {len(targets)} page(s) passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
