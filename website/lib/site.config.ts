// THE ONE FILE TO EDIT FIRST.
// Every page reads from here - fill it in (or let /build-website fill it for you).

export const site = {
  name: "Your Business Name",
  tagline: "What you do, in one plain sentence",
  // GHL inbound webhook - /build-website step 6 collects this and writes it here.
  leadWebhook: null as string | null,
  // GHL calendar booking link - collected on the first /service-page run.
  // Set it and /thank-you renders the booking widget after a form submit (the
  // money pages stay form-only, one primary CTA each). Leave it null and that
  // section simply doesn't render.
  // GHL > Calendars > the calendar > copy the booking link.
  bookingUrl: null as string | null,
  phone: "(555) 555-5555",
  email: "hello@example.com",
  address: "123 Main St, Your City",
  city: "Your City",
  url: "https://example.com", // your live domain - used by sitemap + metadata

  // Your services - each becomes a card on the homepage.
  // The SEO Blueprint's /build-website turns these into full service pages.
  services: [
    { name: "Service One", slug: "service-one", blurb: "One line on what this is." },
    { name: "Service Two", slug: "service-two", blurb: "One line on what this is." },
    { name: "Service Three", slug: "service-three", blurb: "One line on what this is." },
  ],

  // Google Ads sitelinks. Written here at build time, while the value of each
  // page is fresh - /write-ads reads them rather than inventing them months later.
  // Titles max 25 characters, each description line max 35.
  sitelinks: [
    { title: "Get a Quote",  url: "/quote",    lines: ["Free quote, no pressure", "Reply within a day"] },
    { title: "Our Services", url: "/services", lines: ["Everything we do", "Plain pricing"] },
    { title: "Reviews",      url: "/reviews",  lines: ["Real customer stories", "Word for word"] },
    { title: "Pricing",      url: "/pricing",  lines: ["What it costs", "No surprise fees"] },
    { title: "About Us",     url: "/about",    lines: ["Who we are", "Local and licensed"] },
    { title: "Contact",      url: "/contact",  lines: ["Call or book online", "A person replies"] },
  ],
};
