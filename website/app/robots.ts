import type { MetadataRoute } from "next";
import { site } from "@/lib/site.config";

export const dynamic = "force-static"; // required for static export (SSG)

// Search engines AND AI crawlers allowed - AI answers are a traffic source, not a threat.
export default function robots(): MetadataRoute.Robots {
  return {
    rules: [
      { userAgent: "*", allow: "/" },
      { userAgent: ["GPTBot", "ClaudeBot", "PerplexityBot", "Google-Extended"], allow: "/" },
    ],
    sitemap: `${site.url}/sitemap.xml`,
  };
}
