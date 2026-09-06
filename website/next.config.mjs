import { fileURLToPath } from "node:url";

/** @type {import('next').NextConfig} */
const nextConfig = {
  // Static-first, with a server available where one is genuinely needed.
  // Next prerenders every page to plain HTML at build time by default, so the
  // whole marketing site is still static - fastest loads, best Core Web Vitals.
  // What this leaves working that a full `output: "export"` would kill:
  //   - /api/lead      the form endpoint (keeps the webhook URL server-side)
  //   - /proposal/[slug]  reads Supabase at request time
  // Confirm it on the build output: every marketing route stays ○ (Static).
  images: { unoptimized: true }, // no image CDN bill; compress to WebP at build instead

  // A stray package-lock.json in the home directory makes Next guess the wrong
  // workspace root, which breaks file tracing. Pin it to this folder.
  // fileURLToPath, NOT .pathname - .pathname leaves a folder with a space in it
  // percent-encoded ("Claude%20Code"), which points at a directory that does not exist.
  outputFileTracingRoot: fileURLToPath(new URL(".", import.meta.url)),

  // 301 redirects live at the HOST layer so they work identically on any host.
  // On Vercel: vercel.json "redirects". The SEO Blueprint's /build-website
  // writes them there automatically during a restructure.
};

export default nextConfig;
