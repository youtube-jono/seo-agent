import type { MetadataRoute } from "next";
import { site } from "@/lib/site.config";

export const dynamic = "force-static"; // required for static export (SSG)

// The sitemap mirrors your page tree exactly.
// DELIBERATELY EXCLUDED: /thank-you (must never be indexed - it would
// wreck your conversion count) and the legal pages (no search value).
export default function sitemap(): MetadataRoute.Sitemap {
  const pages = ["", "/services", "/about", "/contact", "/quote", "/reviews", "/pricing"];
  return pages.map((path) => ({
    url: `${site.url}${path}`,
    lastModified: new Date(),
    priority: path === "" ? 1 : 0.8,
  }));
}
