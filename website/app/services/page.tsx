// The /services branch index - baked into the template so the nav never lands
// on junk. This IS a real hub page shape (pyramid rule 7): kicker + H1 naming
// the branch, intro, one section per service, no forms, no offer pricing.
//
// /build-website Step 2 replaces the three placeholder sections below with one
// section per keyword-map service hub (name, 2-4 real sentences, photo,
// descriptive link) and keeps this page's shape exactly.
import type { CSSProperties } from "react";

export const metadata = {
  title: "Services",
  description: "Every service, in one place. Filled from your keyword map by /build-website.",
};

const wrap: CSSProperties = { maxWidth: "var(--container-max, 1160px)", margin: "0 auto", padding: "0 var(--gutter, 24px)" };
const eyebrow: CSSProperties = { font: "var(--type-label)", letterSpacing: "var(--track-label)", textTransform: "uppercase", color: "var(--text-muted)" };
const h1s: CSSProperties = { font: "var(--type-display)", letterSpacing: "var(--track-display)", color: "var(--text-strong)", margin: "var(--space-4) 0 0" };
const h2s: CSSProperties = { font: "var(--type-h2)", letterSpacing: "var(--track-heading)", color: "var(--text-strong)", margin: 0 };
const body: CSSProperties = { font: "var(--type-body-lg)", color: "var(--text-body)", margin: "var(--space-3) 0 0", maxWidth: "52ch" };

const SERVICES = [
  { name: "Service one", blurb: "Two to four sentences on what this service is and who it is for. /build-website fills this from your keyword map - every service hub in the map gets a section here, linking to its own page.", frame: "Job photo" },
  { name: "Service two", blurb: "Same shape. The section carries the service name as a heading, a short honest description, a real photo, and a descriptive link to the service page.", frame: "Job photo" },
  { name: "Service three", blurb: "City pages nest under each service. Each service section here links down to its page; each service page carries its own Areas We Serve section.", frame: "Job photo" },
];

export default function ServicesIndex() {
  return (
    <main style={{ background: "var(--surface-page, #f9f8f6)" }}>
      <section style={{ padding: "var(--space-9, 88px) 0 var(--space-7, 48px)" }}>
        <div style={wrap}>
          <p style={eyebrow}>What we do</p>
          <h1 style={h1s}>Services</h1>
          <p style={body}>
            Every service, one page each, cities nested underneath. This index is part of the
            site&rsquo;s structure - run <code>/build-website</code> and each section below becomes
            one of your real services, linked to its own page.
          </p>
        </div>
      </section>

      {SERVICES.map((s, i) => (
        <section
          key={s.name}
          style={{
            padding: "var(--space-8, 64px) 0",
            background: i % 2 ? "var(--surface-page, #f9f8f6)" : "var(--surface-card, #fff)",
            borderTop: "1px solid var(--line-hairline, #e3e2de)",
          }}
        >
          <div style={{ ...wrap, display: "grid", gap: "var(--space-7, 48px)", gridTemplateColumns: "minmax(0,1fr) minmax(0,420px)", alignItems: "center" }}>
            <div>
              <h2 style={h2s}>{s.name}</h2>
              <p style={body}>{s.blurb}</p>
            </div>
            <div
              aria-hidden="true"
              style={{
                aspectRatio: "4/3",
                borderRadius: "var(--radius-media, 14px)",
                background: "var(--ink-100, #f0efec)",
                display: "grid",
                placeItems: "center",
                font: "var(--type-label)",
                letterSpacing: "var(--track-label)",
                textTransform: "uppercase",
                color: "var(--text-faint, #9a9995)",
              }}
            >
              {s.frame}
            </div>
          </div>
        </section>
      ))}

      <section style={{ padding: "var(--space-8, 64px) 0", borderTop: "1px solid var(--line-hairline, #e3e2de)" }}>
        <div style={wrap}>
          <p style={{ ...body, margin: 0 }}>
            <a href="/" style={{ color: "var(--text-link, #0b62c9)" }}>&larr; Back to the site</a>
          </p>
        </div>
      </section>
    </main>
  );
}
