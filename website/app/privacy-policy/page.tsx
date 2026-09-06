import type { Metadata } from "next";

// Google Ads REQUIRES a privacy policy for remarketing and most verticals.
// Both of these live in the footer, never the main nav.
export const metadata: Metadata = {
  title: "Privacy policy",
  robots: { index: false, follow: true },
  alternates: { canonical: "/privacy-policy" },
};

export default function Page() {
  return (
    <div className="mx-auto max-w-2xl px-4 py-16 prose">
      <h1 className="text-3xl font-bold">Privacy policy</h1>
      <p className="mt-4 text-gray-700">
        Replace this with your real Privacy policy. It must mention cookies, your
        forms, and any tracking pixel you run.
      </p>
    </div>
  );
}
