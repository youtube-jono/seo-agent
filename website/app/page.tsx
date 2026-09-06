// The picker. First thing you see on `npm run dev`.
//
// Both styles are the SAME site with a different personality. Pick one and
// /build-website swaps the placeholders for the real business, pulls photos,
// and drops in the proof. Nothing here gets redesigned.

const STYLES = [
  {
    slug: "bold",
    name: "Bold",
    who: "Trades and home services",
    for: "Plumbing · HVAC · roofing · electrical · landscaping · cleaning · pest control · garage doors · restoration",
    feel: "Loud hero, phone everywhere, reviews above the fold, an offer strip across the top. Built for somebody deciding whether to call you in the next ten seconds.",
  },
  {
    slug: "calm",
    name: "Calm",
    who: "Professional services",
    for: "Lawyers · accountants · dentists · clinics · consultants · agencies · financial services",
    feel: "Quieter, more white space, credentials doing the persuading. Built for somebody who will read three pages before they enquire.",
  },
];

export default function Picker() {
  return (
    <main
      style={{
        minHeight: "100vh",
        background: "var(--surface-page, #f9f8f6)",
        padding: "64px 24px",
        fontFamily: "var(--font-core, system-ui)",
      }}
    >
      <div style={{ maxWidth: "980px", margin: "0 auto" }}>
        <p
          style={{
            font: "var(--type-label)",
            letterSpacing: "0.08em",
            textTransform: "uppercase",
            color: "var(--text-muted, #73726e)",
            margin: 0,
          }}
        >
          Step one
        </p>
        <h1
          style={{
            font: "var(--weight-black, 800) 44px/1.1 var(--font-core, system-ui)",
            letterSpacing: "-0.03em",
            color: "var(--text-strong, #1a1a19)",
            margin: "12px 0 8px",
          }}
        >
          Pick the site you want.
        </h1>
        <p
          style={{
            font: "var(--type-body-lg)",
            color: "var(--text-body, #3f3f3c)",
            maxWidth: "60ch",
            margin: "0 0 40px",
          }}
        >
          Same site underneath, two personalities. Open both, pick the one that fits the
          business, then run <code>/build-website</code> and it swaps every placeholder for
          the real thing.
        </p>

        <div
          style={{
            display: "grid",
            gap: "20px",
            gridTemplateColumns: "repeat(auto-fit, minmax(320px, 1fr))",
          }}
        >
          {STYLES.map((s) => (
            <a
              key={s.slug}
              href={`/${s.slug}`}
              style={{
                display: "block",
                padding: "28px",
                borderRadius: "var(--radius-card, 14px)",
                border: "1px solid var(--line-hairline, #e3e2de)",
                background: "var(--surface-card, #fff)",
                textDecoration: "none",
                color: "inherit",
              }}
            >
              <span
                style={{
                  font: "var(--type-label)",
                  letterSpacing: "0.08em",
                  textTransform: "uppercase",
                  color: "var(--text-brand, #0b62c9)",
                }}
              >
                {s.who}
              </span>
              <h2
                style={{
                  font: "var(--weight-black, 800) 30px/1.15 var(--font-core, system-ui)",
                  letterSpacing: "-0.02em",
                  margin: "10px 0 12px",
                  color: "var(--text-strong, #1a1a19)",
                }}
              >
                {s.name} style
              </h2>
              <p style={{ margin: "0 0 16px", color: "var(--text-body, #3f3f3c)" }}>{s.feel}</p>
              <p
                style={{
                  margin: "0 0 20px",
                  font: "var(--type-body-sm)",
                  color: "var(--text-muted, #73726e)",
                }}
              >
                {s.for}
              </p>
              <span style={{ font: "var(--type-body)", color: "var(--text-brand, #0b62c9)" }}>
                View this one &rarr;
              </span>
            </a>
          ))}
        </div>

        <p
          style={{
            marginTop: "40px",
            font: "var(--type-body-sm)",
            color: "var(--text-muted, #73726e)",
          }}
        >
          Not sure? Take Bold for anything where somebody phones in a hurry, Calm for
          anything they research first. You can switch later - it is one command.
        </p>

        <p style={{ marginTop: "16px", font: "var(--type-body-sm)", color: "var(--text-muted, #73726e)" }}>
          The pyramid structure ships with the site, whichever you pick:{" "}
          <a href="/services" style={{ color: "var(--text-link, #0b62c9)" }}>/services</a> and{" "}
          <a href="/blog" style={{ color: "var(--text-link, #0b62c9)" }}>/blog</a> are real index
          pages already - <code>/build-website</code> fills them from your keyword map.
        </p>
      </div>
    </main>
  );
}
