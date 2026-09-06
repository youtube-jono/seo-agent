"""Download industry stock photos into the site, never hotlink them.

Used by /build-website when the owner has no real photos yet.

    python3 code/fetch_stock_photos.py "furnace repair technician" "hvac van" --count 8

The count is deliberately bigger than any page needs: download a pool, look at
every photo, place the best fit per slot, and delete the rejects (file + its
manifest row). Never ship the first result, never place the same photo twice.

Source order:
  1. Pexels  - needs a free PEXELS_API_KEY in .env (30 seconds, no card). Better photos.
  2. Openverse - no key, no signup. The fallback so this never hard-blocks a build.

Files land in website/public/images/stock/ with descriptive, keyword-shaped
filenames, and every one gets a line in the manifest recording its query,
source, licence and the page it is meant for.
"""

import argparse
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DEFAULT_OUT = REPO / "website" / "public" / "images" / "stock"
MANIFEST = "stock-manifest.md"
TARGET_WIDTH = 1600
TIMEOUT = 30


def load_env():
    """Read .env without a dependency. Only fills what isn't already set."""
    env_file = REPO / ".env"
    if not env_file.exists():
        return
    for line in env_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def slugify(text, limit=60):
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug[:limit].rstrip("-") or "photo"


def get_json(url, headers=None):
    request = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
        return json.loads(response.read().decode("utf-8"))


def search_pexels(query, count, api_key):
    url = "https://api.pexels.com/v1/search?" + urllib.parse.urlencode(
        {"query": query, "per_page": count, "orientation": "landscape"}
    )
    payload = get_json(url, {"Authorization": api_key})
    results = []
    for photo in payload.get("photos", []):
        # Ask Pexels for the size we want so nothing has to be resized locally.
        src = photo.get("src", {})
        download_url = src.get("large2x") or src.get("large") or src.get("original")
        if not download_url:
            continue
        results.append(
            {
                "url": download_url,
                "credit": photo.get("photographer", "unknown"),
                "page": photo.get("url", ""),
                "licence": "Pexels licence - free commercial use, no attribution required",
                "source": "Pexels",
                "alt": photo.get("alt") or query,
            }
        )
    return results


def search_openverse(query, count):
    # Openverse ANDs every word, so "furnace repair technician" returns nothing
    # while "furnace repair" returns 154. Drop trailing words until something hits.
    words = query.split()
    payload = {"results": []}
    for stop in range(len(words), 0, -1):
        attempt = " ".join(words[:stop])
        url = "https://api.openverse.org/v1/images/?" + urllib.parse.urlencode(
            {
                "q": attempt,
                "page_size": count,
                "license_type": "commercial",
                "aspect_ratio": "wide",
            }
        )
        payload = get_json(url, {"User-Agent": "seo-blueprint-pro/1.0"})
        if payload.get("results"):
            if attempt != query:
                print(f"  (no results for '{query}', used '{attempt}')", file=sys.stderr)
            break

    results = []
    for image in payload.get("results", []):
        download_url = image.get("url")
        if not download_url:
            continue
        results.append(
            {
                "url": download_url,
                "credit": image.get("creator") or "unknown",
                "page": image.get("foreign_landing_url", ""),
                "licence": f"{(image.get('license') or '').upper()} {image.get('license_version') or ''}".strip(),
                "source": "Openverse",
                "alt": image.get("title") or query,
            }
        )
    return results


def download(photo, dest):
    request = urllib.request.Request(photo["url"], headers={"User-Agent": "seo-blueprint-pro/1.0"})
    with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
        data = response.read()
    dest.write_bytes(data)
    return len(data)


def write_manifest(out_dir, rows):
    path = out_dir / MANIFEST
    header = (
        "# Stock photos\n\n"
        "Downloaded by `/build-website` because no real photos were supplied.\n\n"
        "**These are placeholders with a decent haircut.** Stock never shows the team, "
        "a real job, a before/after, or anything a visitor would read as proof of THIS "
        "business. Swap each one for a real photo as it arrives, then delete its row.\n\n"
        "| File | Query | Source | Credit | Licence |\n"
        "|------|-------|--------|--------|--------|\n"
    )
    existing = ""
    if path.exists():
        text = path.read_text(encoding="utf-8")
        existing = "\n".join(
            line for line in text.splitlines() if line.startswith("| ") and not line.startswith("| File")
        )
        existing = existing.replace("|------|-------|--------|--------|--------|", "")
    lines = [
        f"| `{row['file']}` | {row['query']} | {row['source']} | {row['credit']} | {row['licence']} |"
        for row in rows
    ]
    body = "\n".join(filter(None, [existing.strip(), "\n".join(lines)]))
    path.write_text(header + body + "\n", encoding="utf-8")
    return path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("queries", nargs="+", help="what to search for, in the business's industry")
    parser.add_argument(
        "--count",
        type=int,
        default=8,
        help="photos per query (default 8 - a pool to choose from, not a quota to use)",
    )
    parser.add_argument("--out", default=str(DEFAULT_OUT), help="output directory")
    args = parser.parse_args()

    load_env()
    api_key = os.environ.get("PEXELS_API_KEY", "").strip()
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    if not api_key:
        print(
            "No PEXELS_API_KEY set - falling back to Openverse (no key needed).\n"
            "Better photos: pexels.com/api > 'Get Started' > copy the key into .env "
            "as PEXELS_API_KEY. Free, no card, 30 seconds.\n",
            file=sys.stderr,
        )

    rows = []
    failures = []
    for query in args.queries:
        try:
            photos = (
                search_pexels(query, args.count, api_key)
                if api_key
                else search_openverse(query, args.count)
            )
        except Exception as error:  # noqa: BLE001 - report and keep going
            failures.append(f"{query}: search failed ({error})")
            continue

        if not photos:
            failures.append(f"{query}: no results")
            continue

        for index, photo in enumerate(photos, start=1):
            suffix = Path(urllib.parse.urlparse(photo["url"]).path).suffix.lower()
            if suffix not in {".jpg", ".jpeg", ".png", ".webp"}:
                suffix = ".jpg"
            filename = f"{slugify(query)}-{index}{suffix}"
            dest = out_dir / filename
            try:
                size = download(photo, dest)
            except Exception as error:  # noqa: BLE001
                failures.append(f"{query} #{index}: download failed ({error})")
                continue
            rows.append(
                {
                    "file": filename,
                    "query": query,
                    "source": photo["source"],
                    "credit": photo["credit"],
                    "licence": photo["licence"],
                    "alt": photo["alt"],
                }
            )
            print(f"  {filename}  ({size // 1024} KB)  alt: {photo['alt']}")

    if rows:
        manifest = write_manifest(out_dir, rows)
        print(f"\nDownloaded {len(rows)} photo(s) to {out_dir}")
        print(f"Manifest: {manifest}")
        print(f"Reference them as /images/stock/<file> - the files are local, nothing is hotlinked.")
    else:
        print("\nNothing downloaded.", file=sys.stderr)

    if failures:
        print("\nProblems:", file=sys.stderr)
        for failure in failures:
            print(f"  - {failure}", file=sys.stderr)

    return 0 if rows else 1


if __name__ == "__main__":
    sys.exit(main())
