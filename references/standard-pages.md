# Standard pages - build these on every site, every time

Every page that must exist before any keyword-driven page gets written. Not optional, not "nice to have later".
`/build-website` creates all of these from the pyramid at Layer 1. `/publish` will not report a clean launch until they exist.
Next: build the thank-you page first, with tracking wired, before any form goes live.

---

## 1. Build the thank-you page first - `/thank-you`

The single most-skipped page, and the one everything else depends on. Every conversion - form fill, booking, call-back request - redirects here. It is the only reliable place a conversion event can fire.

Without a distinct thank-you URL, conversion tracking has to rely on click or event triggers, which break silently and undercount. A site that skips this page cannot run `/tracking` properly and cannot run ads that optimise.

**Must have**

- A real confirmation message in the owner's voice, not "Thank you for your submission"
- What happens next, with a time: "We'll call you back within 30 minutes during business hours". This is the single biggest reducer of buyer's remorse and no-shows
- The phone number, clickable, in case they don't want to wait
- The conversion tracking snippet - Google Ads conversion, GA4 event, and any Meta or pixel - firing on page load
- `noindex` in the head. It must never appear in search results, or the conversion count becomes garbage
- Excluded from sitemap.xml

**Must NOT have**

- Navigation that pulls them back into browsing before the event fires
- Any second ask ("now follow us on Instagram") that dilutes the moment

Consider a second variant, `/thank-you-call`, if phone and form conversions need separating. Different value, different optimisation signal.

---

## 2. Build the six sitelink pages

Google Ads sitelinks need real, distinct, useful pages behind them. Google will not show sitelinks pointing at anchors on the same page, and thin duplicates get disapproved or ignored. These same pages are the Layer-1 set the SEO pyramid needs anyway, which is why they are built once and used by both tracks.

**Services** · `/services/`
A real hub page: short intro, link to every service with descriptive anchors. Never a bare list. The highest click-through sitelink on almost every account.

**About** · `/about`
The owner, the story, real photos, credentials, years in business, team. Carries the E-E-A-T load AND is the trust sitelink.

**Contact** · `/contact`
Phone (clickable), email, address, hours, map embed, the form. A sitelink, and the name-address-phone source of truth for citations.

**Get a quote** · `/quote`
The conversion page: short form, what happens next, response-time promise. The money sitelink, and the target every blog post bridges to.

**Reviews** · `/reviews`
Real review quotes with names and sources, the star rating, review schema. Highest-trust sitelink, and it feeds rich results.

**Pricing** · `/pricing`
Real numbers or honest ranges, what's included, what changes the price. Filters tyre-kickers before the click costs money.

### Add these when they apply

- `/areas-served` - local businesses with a wide radius. Links to every city page, so it doubles as the city-page hub
- `/faq` - FAQ schema, and it feeds AI overviews directly (see `references/geo.md`)
- `/financing` - anything with a large ticket price
- `/emergency` or `/book-now` - trades and any business where speed is the pitch

### Sitelink rules that decide whether these actually work

- Each page must be genuinely different. Google suppresses sitelinks that lead to near-identical content
- Never point a sitelink at the same page as the ad's final URL - it wastes the slot
- Sitelink descriptions are 35 characters, two lines. Write them when the page is built, while the value proposition is fresh
- Four sitelinks minimum for them to serve reliably. Six gives Google room to choose

---

## 3. Build the legal and trust pages

Cheap to build, and their absence is a live problem. Google Ads REQUIRES a privacy policy for remarketing and for most verticals, and missing legal pages are a documented trust signal for both users and quality raters.

**Privacy policy** · `/privacy-policy`
Required by Google Ads for remarketing and data collection. Must mention cookies, forms and any pixel in use.

**Terms** · `/terms`
Required for anything taking payment or bookings.

**Accessibility** · `/accessibility`
Optional, but it is a real trust signal and it is one page.

Link all of these in the footer, never in the main nav.

---

## 4. Build the technical must-haves

Built by `/build-website`, verified by `/audit`.

- `/404` - a real page with the search box, links to the Layer-1 set, and the phone number. A dead end loses a customer who was already looking for you
- `robots.txt` - allows GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot and Google-Extended (see `references/geo.md`), and points at the sitemap
- `sitemap.xml` - mirrors the pyramid exactly. Excludes `/thank-you` and the legal pages
- `llms.txt` - the AI-readable summary of what the business does (see `references/geo.md`)

---

## The build order

1. Home plus the Layer-1 set: `/services/`, `/blog/`, `/about`, `/contact`, `/quote`
2. `/thank-you` with tracking wired, before any form goes live, or the first conversions are lost forever
3. `/reviews` and `/pricing` - the remaining sitelink targets
4. Legal pages in the footer
5. `/404`, robots.txt, sitemap.xml, llms.txt
6. Then, and only then, the keyword-driven pages from `keyword-map.md`

---

## How to use this

1. `/build-website` builds sections 1-4 as part of the pyramid, before any keyword page.
2. `/tracking` for Ads and `/publish` for SEO both assume `/thank-you` exists. If it doesn't, stop and build it.
3. `/audit` flags any missing standard page as a finding, not a suggestion.
4. Existing site? Check which of these already exist before building. Never duplicate a page the owner already has under a different URL.
5. Sitelink descriptions get written at build time and stored with the page, so `/write-ads` isn't inventing them cold months later.
