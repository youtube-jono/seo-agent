#!/usr/bin/env python3
"""Single-page exit gate for /service-page and /blog-post.

    python3 code/check_page_done.py /services/drain-cleaning [--port 3000]



Fails on: non-200, any surviving placeholder frame label, any template
string, any dead internal link on the page. The skill loops until this passes.
"""
import re
import sys
import urllib.request
from pathlib import Path

args = [a for a in sys.argv[1:] if not a.startswith("--")]
PORT = sys.argv[sys.argv.index("--port") + 1] if "--port" in sys.argv else "3000"
BASE = f"http://localhost:{PORT}"
if "--base" in sys.argv:
    BASE = sys.argv[sys.argv.index("--base") + 1].rstrip("/")
route = args[0] if args else sys.exit("usage: check_page_done.py /route")

STRINGS = [
    "JOB PHOTO", "PORTRAIT", "CREW", "BEFORE - THE OLD UNIT", "AFTER - NEW INSTALL",
    "FINISHED INSTALL", "FINISHED JOB", "SIGNATURE FRAME", "US, WORKING", "DETAIL SHOT",
    "Service one", "Service two", "Customer name", "Client name", "Area one",
    "From $000", "$000", "Your City", "(555) 010-0199", "(555) 555-5555",
    "Business Name", "Month 2026", "Project · location", "Choose one",
    "yourbusiness", "Licence #000000", "Engagement one", "Publication",
]

# Shape-based patterns: catch placeholders nobody thought to list.
PLACEHOLDER_PATTERNS = [
    (r"\b0{2,}[,+]|\b0,000\b", "zeroed-out number (00+, 0,000)"),
    (r"\$0[,0]*\b|\bFrom \$0", "zeroed-out price ($0, From $000)"),
    (r"\(555\) ?\d{3}", "555 phone number"),
    (r"\b[Ll]orem\b|\bipsum\b", "lorem ipsum"),
    (r"TODO|FIXME|PLACEHOLDER|placeholder", "literal TODO/placeholder marker"),
    (r"Add your real|Replace with|Fill this in|goes here\b", "instruction text left on page"),
    (r"Your (City|Business|Name|Trade)\b", "Your X template phrase"),
    (r"\bExample\b", "the word Example"),
    (r"@(example|yourbusiness)\.", "example email domain"),
    (r"\b00 Month\b|\byyyy-mm-dd\b", "template date placeholder in a form field"),
]

def pattern_hits(html):
    import re as _re
    html = _re.sub(r"<(script|style)[^>]*>.*?</\\1>", " ", html, flags=_re.S | _re.I)
    attrs = " ".join(_re.findall(r'(?:placeholder|value|aria-label)="([^"]*)"', html))
    text = _re.sub(r"<[^>]+>", " ", html) + " " + attrs
    return [label for pat, label in PLACEHOLDER_PATTERNS if _re.search(pat, text)]

def fetch(r):
    try:
        with urllib.request.urlopen(BASE + r, timeout=30) as x:
            return x.status, x.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception as e:
        return 0, str(e)

failures = []
status, html = fetch(route)
if status != 200:
    print(f"FAIL {route} -> {status}"); sys.exit(1)

hits = [t for t in STRINGS if t in html] + pattern_hits(html)
if hits:
    failures.append("placeholders/frames still present: " + ", ".join(hits[:8]))

for href in sorted(set(re.findall(r'href="(/[^"#?]*)"', html))):
    s2, _ = fetch(href)
    if s2 != 200:
        failures.append(f"dead link on page: {href} -> {s2}")

if failures:
    print(f"PAGE NOT DONE  {route}")
    for f in failures:
        print("  -", f)
    print("\nFix and re-run. The skill does not finish until this passes.")
    sys.exit(1)
print(f"PASS  {route} - renders, no placeholders, no dead links.")
