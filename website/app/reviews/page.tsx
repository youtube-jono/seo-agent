// Standard page, minimally styled to the shipped design system.
// /build-website fills it with the real business; until then it stays honest.
export const metadata = { title: "Reviews" };

export default function Page() {
  return (
    <main style={{ maxWidth: 720, margin: "0 auto", padding: "96px 24px", fontFamily: "var(--font-core, system-ui)" }}>
      <p style={{ font: "var(--type-label)", letterSpacing: "0.08em", textTransform: "uppercase", color: "var(--text-muted, #73726e)" }}>What customers say</p>
      <h1 style={{ font: "var(--type-h1)", color: "var(--text-strong, #1a1a19)", margin: "10px 0 16px" }}>Reviews</h1>
      <p style={{ color: "var(--text-body, #3f3f3c)" }}>
        Real reviews land here from <code>context/proof/proof-inventory.md</code> - copied word for word, never written by us. An empty page beats an invented one.
      </p>
      <p style={{ marginTop: 32 }}><a href="/" style={{ color: "var(--text-link, #0b62c9)" }}>&larr; Back to the site</a></p>
    </main>
  );
}
