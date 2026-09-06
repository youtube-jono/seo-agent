#!/usr/bin/env python3
"""Catch styling bugs that every other check calls green.

    python3 code/check_css_integrity.py

Undefined CSS custom properties and undefined class names are both LEGAL CSS.
Nothing errors, nothing warns, the build passes, and the page renders flat.
This is the only check that sees them.

Three gates:
  1. Every var(--token) used in app/ or components/ is defined somewhere.
  2. Every custom className used in components is defined in a stylesheet.
  3. Tailwind Preflight resets h1-h6 - the base layer must restore size AND weight.
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "website"
KIT  = ROOT / "design" / "kit"

TW = {"container","group","peer","sr-only","not-sr-only","prose","dark","antialiased",
      # Bare Tailwind utilities - real classes, generated at build time, so they
      # never appear in a source stylesheet for the checker to find.
      "underline","italic","truncate","block","inline","hidden","flex","grid",
      "relative","absolute","fixed","static","sticky","uppercase","lowercase",
      "capitalize","rounded","border","shadow","invisible","visible"}

# Build output is not source. Scanning .next/ and out/ pulled in Tailwind's own
# internals (--tw-leading, --default-font-feature-settings), which are defined
# by Tailwind at runtime and always carry fallbacks. They are noise, and noise
# in a gate is how a real failure gets ignored.
SKIP = (".next", "node_modules", "/out/")

def skipped(f):
    s = f.as_posix()
    return any(x in s for x in SKIP)

def css_files():
    for base in (SITE, KIT):
        if base.exists():
            for f in base.rglob("*.css"):
                if not skipped(f): yield f

def css_text():
    parts = [f.read_text(encoding="utf-8", errors="ignore") for f in css_files()]
    # CSS-in-JSX counts as defined CSS. The proposal chassis ships its whole
    # stylesheet inside a <style> tag in ui.tsx; without this the checker calls
    # every one of its classes undefined.
    for f in src_files():
        t = f.read_text(encoding="utf-8", errors="ignore")
        for m in re.findall(r"__html:\s*`(.*?)`", t, re.S) + re.findall(r"<style[^>]*>\{`(.*?)`\}</style>", t, re.S):
            parts.append(m)
    return "\n".join(parts)

def src_files():
    if not (SITE).exists(): return []
    return [p for p in SITE.rglob("*")
            if p.suffix in {".tsx",".ts",".jsx",".js"} and not skipped(p)]

def main():
    if not SITE.exists(): print("No website/ folder."); return 0
    css = css_text()
    files = src_files()
    if not files: print("No source files."); return 0
    fails = []

    defined_vars = set(re.findall(r'(--[a-zA-Z0-9_-]+)\s*:', css))
    used = {}
    for f in files + list(css_files()):
        t = f.read_text(encoding="utf-8", errors="ignore")
        for v in re.findall(r'var\(\s*(--[a-zA-Z0-9_-]+)', t):
            used.setdefault(v, set()).add(f.relative_to(ROOT).as_posix())
    missing = {v: fs for v, fs in used.items() if v not in defined_vars}
    if missing:
        top = sorted(missing.items(), key=lambda kv: -len(kv[1]))[:10]
        lines = [f"     {v} - used in {len(fs)} file(s)" for v, fs in top]
        fails.append(("UNDEFINED CSS VARIABLES", len(missing),
            "An undefined custom property makes the whole declaration invalid at computed-value time.\n"
            "     The element silently inherits base ink, so every intended grey, accent and surface\n"
            "     collapses to one colour. Nothing errors. The build passes. The page goes flat.\n"
            + "\n".join(lines)))

    defined_cls = set(re.findall(r'\.([a-zA-Z][a-zA-Z0-9_-]*)\s*[,{:]', css))
    used_cls = {}
    for f in files:
        t = f.read_text(encoding="utf-8", errors="ignore")
        for m in re.findall(r'className=(?:"([^"]*)"|\{`([^`]*)`\})', t):
            for token in (m[0] + " " + m[1]).split():
                if not re.fullmatch(r'[a-z][a-z0-9-]*', token): continue
                if "-" in token and not token.islower(): continue
                if token in TW: continue
                if re.match(r'^(text|bg|p|m|w|h|flex|grid|gap|border|rounded|font|items|justify|max|min|top|left|right|bottom|space|leading|tracking|overflow|z|opacity|shadow|col|row|self|order|object|aspect|list|cursor|select|transition|duration|ease|hover|focus|md|lg|sm|xl|sr)$|^[a-z]+-', token): continue
                used_cls.setdefault(token, set()).add(f.relative_to(ROOT).as_posix())
    orphan = {c: fs for c, fs in used_cls.items() if c not in defined_cls}
    if orphan:
        lines = [f"     .{c} - used in {len(fs)} place(s)" for c, fs in sorted(orphan.items(), key=lambda kv: -len(kv[1]))[:10]]
        fails.append(("UNDEFINED CLASS NAMES", len(orphan),
            "A className no stylesheet defines does nothing at all. The design system's signature\n"
            "     devices (uppercase eyebrows, tabular figures) render as plain body text everywhere.\n"
            + "\n".join(lines)))

    base = re.search(r'@layer\s+base\s*\{(.*?)\n\}', css, re.S)
    blob = base.group(1) if base else css
    hblocks = re.findall(r'(h[1-6][^{]*)\{([^}]*)\}', blob)
    sized = any(re.search(r'font-size|font\s*:|@apply[^;]*text-', b) for _, b in hblocks)
    weighted = any(re.search(r'font-weight|font\s*:|@apply[^;]*font-', b) for _, b in hblocks)
    if hblocks and not (sized and weighted):
        miss = " and ".join(x for x, ok in [("size", sized), ("weight", weighted)] if not ok)
        fails.append(("HEADINGS NOT RESTORED AFTER PREFLIGHT", 1,
            f"Tailwind Preflight resets h1-h6 to font-size:inherit and font-weight:inherit.\n"
            f"     The base layer styles headings but never sets {miss}, so every heading computes\n"
            f"     to body text. Only headings carrying an inline utility class look like headings.\n"
            "     Bind h1-h6 to the design system's type tokens in @layer base."))


    # ---- LANDING PAGES MUST BE COPIES OF THE TEMPLATE, NOT NEW DESIGNS ----
    # landing-page.md says "DUPLICATE, NEVER DESIGN" in three places and a build
    # ignored it anyway: it hand-wrote helper classes, inherited the kit's tokens
    # (right blue, right font) and none of its design. Prose did not stop it, so
    # this does. A page that never touches the template's structural signature
    # was not copied from the template.
    SIGNATURE = {
        "--surface-brand": "the hero band - the template's hero sits on the brand surface, never on grey",
        "gw-container":    "the container - every template section wraps its content in one",
        "--space-":        "the spacing scale - hand-rolled padding means hand-rolled design",
    }
    for p in ROOT.glob("website/app/lp/**/page.tsx"):
        txt = p.read_text(encoding="utf-8", errors="ignore")
        missing = [f"{k} ({why})" for k, why in SIGNATURE.items() if k not in txt]
        # a band rhythm: at least two different surface tokens down the page
        surfaces = set(re.findall(r"--surface-(brand|card|tint|sunken|accent)", txt))
        if len(surfaces) < 3:
            missing.append(f"section rhythm (found {len(surfaces)} surface tone(s), the template alternates at least 3)")
        if missing:
            rel = p.relative_to(ROOT)
            fails.append((f"LANDING PAGE NOT COPIED FROM THE TEMPLATE - {rel}", len(missing),
                "landing-page.md: \"DUPLICATE, NEVER DESIGN. A landing page is a COPY of the chosen\n"
                "     style's page (app/bold/page.tsx or app/calm/page.tsx).\" This page is missing the\n"
                "     template's structural signature, which means it was written rather than copied:\n       - "
                + "\n       - ".join(missing) +
                "\n     Copy the sections out of app/calm/page.tsx and swap the words. Do not rebuild them."))

    if not fails:
        print("PASS - tokens and classes resolve, headings restored, landing pages copied from the template."); return 0
    print("CSS INTEGRITY FAILED\n")
    for title, n, why in fails:
        print(f"  {title} ({n})\n     {why}\n")
    print("  These are invisible to `next build`. It type-checks TypeScript, not CSS.")
    return 1

if __name__ == "__main__": sys.exit(main())
