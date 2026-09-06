#!/usr/bin/env python3
"""The /build-website exit gate. The run is not done until this passes.

    python3 code/check_site_complete.py [--port 3000]



Checks the three ways a "finished" build has actually shipped half-done:
  1. A route that errors or 404s
  2. Placeholder text still on a page (Business Name, (555)..., Service one...)
  3. Keyword-map rows marked Written that have no live route
"""

import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "website"
PORT = sys.argv[sys.argv.index("--port") + 1] if "--port" in sys.argv else "3000"
BASE = f"http://localhost:{PORT}"
# Any site, any stack: --base https://example.com (imported site, WordPress,
# staging). With --base, routes are discovered by CRAWLING from / instead of
# walking website/app, so the checks work on sites this repo didn't build.
if "--base" in sys.argv:
    BASE = sys.argv[sys.argv.index("--base") + 1].rstrip("/")

PLACEHOLDERS = [
    "Business Name", "(555) 010-0199", "(555) 555-5555", "hello@example.com",
    "hello@yourbusiness.example", "000 Example Street", "Your City",
    "Licence #000000", "Service one", "Area one", "Trade &amp; Speciality",
    "Trade & Speciality", "A headline with a bit of swagger",
    "One quiet line about the work", "Engagement one", "Publication",
    "Customer name", "Client name", "000+ verified", "00+", "0,000",
    # frame labels that must not survive once real photos are placed
    "CREW &amp; VAN", "ON THE JOB", "FINISHED INSTALL", "JOB PHOTO",
    "PORTRAIT", "SIGNATURE FRAME", "US, WORKING", "THE CREW, 2026",
    "Project · location", "Month 2026", "Choose one", "yourbusiness",
    "From $0,000", "From $000", "$0M insured", "Example Street",
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
    # strip script/style FIRST: Next.js mirrors form placeholders and email
    # hints into its flight-data <script>, false-positiving every form page
    html = _re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html, flags=_re.S | _re.I)
    # placeholder/value/aria-label attrs vanish with the tags - harvest them
    # first so template-ese inside form fields gets scanned too
    attrs = " ".join(_re.findall(r'(?:placeholder|value|aria-label)="([^"]*)"', html))
    text = _re.sub(r"<[^>]+>", " ", html) + " " + attrs
    return [label for pat, label in PLACEHOLDER_PATTERNS if _re.search(pat, text)]


def crawl_routes(max_pages=80):
    """Discover routes by following internal links from /. Works on any stack."""
    skip = ("privacy", "terms", "thank-you", "wp-admin", "wp-login", "feed",
            "wp-json", "cart", "checkout", "tag/", "author/", "#")
    seen, queue = [], ["/"]
    while queue and len(seen) < max_pages:
        route = queue.pop(0)
        if route in seen:
            continue
        seen.append(route)
        status, html = fetch(route)
        if status != 200:
            continue
        for href in set(re.findall(r'href="(/[^"#?]*)"', html)):
            href = href.rstrip("/") or "/"
            if href not in seen and href not in queue and not any(k in href for k in skip):
                queue.append(href)
    return seen


def routes_on_disk():
    app = SITE / "app"
    # --base means a foreign site (imported, WordPress, staging): the local
    # tree is irrelevant, discovery is always by crawl.
    if "--base" in sys.argv or not app.exists():
        return crawl_routes()
    skip = {"privacy-policy", "terms", "thank-you", "api"}
    out = []
    for page in sorted(app.rglob("page.tsx")):
        parts = page.relative_to(app).parts[:-1]
        if any(x in skip or x.startswith("[") or x.startswith("_") for x in parts):
            continue
        out.append("/" + "/".join(parts))
    return out


def fetch(route):
    try:
        with urllib.request.urlopen(BASE + route, timeout=30) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception as e:
        return 0, str(e)


def map_expected_routes():
    """Every keyword-map row under `# Written` must have a route.

    Rows still under `# To build` are fine without a page - /service-page and
    /blog-post build them one at a time. A row moves to Written when drafted,
    and from then on a missing route is a failure."""
    km = ROOT / "keyword-map.md"
    if not km.exists():
        return []
    text = km.read_text()
    if "# Written" not in text:
        return []
    text = text.split("# Written", 1)[1]
    text = text.split("## Keywords saved for later", 1)[0]
    expected = []
    for m in re.finditer(r"^## \d+\. (Service page|Blog post): (.+)$", text, re.M):
        kind, title = m.group(1), m.group(2).strip()
        def slugify(x):
            return re.sub(r"[^a-z0-9]+", "-", x.lower()).strip("-")
        # "Local SEO services in Austin" -> city spoke under its hub
        city = re.match(r"(.+?) in ([A-Za-z .-]+)$", title)
        if kind == "Service page":
            if city:
                expected.append((title, f"/services/{slugify(city.group(1))}/{slugify(city.group(2))}"))
            else:
                expected.append((title, f"/services/{slugify(title)}"))
        else:
            expected.append((title, f"/blog/{slugify(title)}"))
    return expected


def main():
    failures = []

    # 1. every route on disk renders
    for route in routes_on_disk():
        status, _ = fetch(route)
        if status != 200:
            failures.append(f"route {route} -> {status}")

    # 2. no placeholder text on the MAIN pages. Deep service and blog routes
    #    are checked by their own command's gate (check_page_done.py).
    MAIN = {"/", "/services", "/about", "/blog", "/contact", "/pricing", "/quote", "/reviews"}
    for route in routes_on_disk():
        if route not in MAIN:
            continue
        _, html = fetch(route)
        found = [ph for ph in PLACEHOLDERS if ph in html] + pattern_hits(html)
        if found:
            failures.append(f"{route}: placeholder(s) still visible: {', '.join(found[:5])}")

    # 3. every WRITTEN keyword-map row has a live route whose title
    #    carries its keyword
    for title, route in map_expected_routes():
        status, html = fetch(route)
        if status != 200:
            failures.append(f'keyword-map row "{title}" has no page at {route} (-> {status})')
            continue
        first_words = " ".join(title.lower().split()[:2])
        if first_words not in html.lower():
            failures.append(f'{route}: page exists but its content never mentions "{first_words}" - H1/meta not set to the keyword')

    # 4. every internal link on every page resolves
    links = {}
    for route in routes_on_disk():
        _, html = fetch(route)
        for href in set(re.findall(r'href="(/[^"#?]*)"', html)):
            links.setdefault(href, []).append(route)
    for href, sources in sorted(links.items()):
        status, _ = fetch(href)
        if status != 200:
            failures.append(
                f"dead link: {href} -> {status} (linked from {', '.join(sources[:3])})")

    # 5. required links: the hub and spoke wiring
    #    - every service hub linked from /services (below)
    #    - every city spoke linked from its hub, and links back up to it
    #    - every blog post linked from /blog
    #    - nav on every main page reaches /services and /blog
    route_set = set(routes_on_disk())
    for route in sorted(route_set):
        parts = route.strip("/").split("/")
        if route.startswith("/services/") and len(parts) == 3:
            hub = "/" + "/".join(parts[:2])
            _, hub_html = fetch(hub)
            if f'href="{route}"' not in hub_html:
                failures.append(f"hub {hub} does not link down to its spoke {route}")
            else:
                # a footnote link is not a section: the hub needs a heading
                # that names the areas/cities block the spokes live under
                heads = " ".join(re.findall(r"<h[23][^>]*>(.*?)</h[23]>", hub_html, re.S | re.I)).lower()
                if not re.search(r"area|cities|city|serve|location", heads):
                    failures.append(
                        f'hub {hub} links its spokes but has no "Areas we serve" section heading - city links must be a real section, not a footnote')
            _, spoke_html = fetch(route)
            if f'href="{hub}"' not in spoke_html:
                failures.append(f"spoke {route} does not link up to its hub {hub}")
    _, blog_html = fetch("/blog")
    for route in sorted(route_set):
        if route.startswith("/blog/") and route != "/blog":
            if f'href="{route}"' not in blog_html:
                failures.append(f"/blog index does not link {route}")
    for main in ("/", "/services", "/about", "/blog", "/contact"):
        _, html = fetch(main)
        for must in ("/services", "/blog"):
            if f'href="{must}"' not in html:
                failures.append(f"nav on {main} has no link to {must}")

    # 5b. index pages are real indexes, not a child's page type
    def first_h1(html):
        m = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S | re.I)
        return re.sub(r"<[^>]+>", "", m.group(1)).strip().lower() if m else ""
    _, blog_idx = fetch("/blog")
    if "<article" in blog_idx.lower():
        failures.append("/blog is an <article>, not an index - move the article to its own post URL")
    blog_h1 = first_h1(blog_idx)
    for route in sorted(route_set):
        if route.startswith("/blog/") and route != "/blog":
            _, ph = fetch(route)
            if blog_h1 and blog_h1 == first_h1(ph):
                failures.append(f"/blog has the same H1 as {route} - the index is a post")
    # An index is a page TYPE. Renaming the H1 on a sales page does not count:
    # index pages carry no enquiry form and no offer pricing - those live on
    # the child pages (spec rule 7 + the hub definition).
    for idx_route in ("/services", "/blog"):
        _, idx_html = fetch(idx_route)
        if "<form" in idx_html.lower():
            failures.append(f"{idx_route} contains a form - an index is not a sales page; forms live on child pages")
        body = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", idx_html, flags=re.S | re.I)
        body = re.sub(r"<[^>]+>", " ", body)
        if re.search(r"\$\s?\d{1,3},\d{3}", body):
            failures.append(f"{idx_route} shows offer pricing - an index names the branch; pricing lives on child pages")

    _, svc_idx = fetch("/services")
    svc_h1 = first_h1(svc_idx)
    if "service" not in svc_h1:
        failures.append(f'/services H1 "{svc_h1}" does not name the branch - an index H1 must contain "service"')
    for route in sorted(route_set):
        if route.startswith("/services/"):
            _, ph = fetch(route)
            if svc_h1 and svc_h1 == first_h1(ph):
                failures.append(f"/services has the same H1 as {route} - the index is a child page")

    # 6. no orphans: every service route is linked from the /services index
    _, services_html = fetch("/services")
    for route in routes_on_disk():
        if route.startswith("/services/") and route.count("/") == 2:
            if f'href="{route}"' not in services_html:
                failures.append(f"orphan: {route} is not linked from /services")

    if failures:
        print("SITE NOT COMPLETE\n")
        for f in failures:
            print(f"  - {f}")
        print(f"\n{len(failures)} failure(s). /build-website is not done. Fix and re-run.")
        return 1
    print("Site complete: every route renders, no placeholders, every written keyword-map row has its page.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
