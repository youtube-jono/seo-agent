import { NextResponse } from "next/server";
import { site } from "@/lib/site.config";

// Every form on the site posts here; this forwards to the GHL inbound webhook.
// /service-page collects the webhook up front and writes it into site.config.ts
// as `leadWebhook`. Until then, submissions return a clear error instead of
// vanishing - a lead disappearing silently is the worst failure a money page has.

export async function POST(request: Request) {
  const form = await request.formData();
  const payload = Object.fromEntries(form.entries());

  const webhook = (site as Record<string, unknown>).leadWebhook as string | null | undefined;
  if (!webhook || String(webhook).includes("TODO")) {
    return NextResponse.json(
      { ok: false, error: "Lead webhook not connected. Run /service-page or set leadWebhook in lib/site.config.ts." },
      { status: 503 },
    );
  }

  const res = await fetch(webhook, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ ...payload, source: "website", page: request.headers.get("referer") ?? "" }),
  });

  if (!res.ok) {
    return NextResponse.json({ ok: false, error: `Webhook responded ${res.status}` }, { status: 502 });
  }
  return NextResponse.redirect(new URL("/thank-you", request.url), 303);
}
