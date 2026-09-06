import type { Metadata } from "next";

// Google Ads REQUIRES a privacy policy for remarketing and most verticals.
// Both of these live in the footer, never the main nav.
export const metadata: Metadata = {
  title: "Terms",
  robots: { index: false, follow: true },
  alternates: { canonical: "/terms" },
};

export default function Page() {
  return (
    <div className="mx-auto max-w-2xl px-4 py-16 prose">
      <h1 className="text-3xl font-bold">Terms</h1>
      <p className="mt-4 text-gray-700">
        Replace this with your real Terms. It must mention cookies, your
        forms, and any tracking pixel you run.
      </p>
    </div>
  );
}
