// Standard page, minimally styled to the shipped design system.
// /build-website fills it with the real business; until then it stays honest.
export const metadata = { title: "Get a quote" };

export default function Page() {
  return (
    <main style={{ maxWidth: 720, margin: "0 auto", padding: "96px 24px", fontFamily: "var(--font-core, system-ui)" }}>
      <p style={{ font: "var(--type-label)", letterSpacing: "0.08em", textTransform: "uppercase", color: "var(--text-muted, #73726e)" }}>Start here</p>
      <h1 style={{ font: "var(--type-h1)", color: "var(--text-strong, #1a1a19)", margin: "10px 0 16px" }}>Get a quote</h1>
      <p style={{ color: "var(--text-body, #3f3f3c)" }}>
        The quote form is on the homepage. This route exists for ads sitelinks and gets the full form when <code>/build-website</code> runs.
      </p>
      <p style={{ marginTop: 32 }}><a href="/" style={{ color: "var(--text-link, #0b62c9)" }}>&larr; Back to the site</a></p>
    </main>
  );
}
