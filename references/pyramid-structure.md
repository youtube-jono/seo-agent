# Pyramid structure - the canonical site map

The single spec for how every site this repo builds is structured. `/build-website` builds to it (read this file BEFORE building the tree - it is the spec, not a suggestion), `/audit` grades against it, `code/check_site_complete.py` enforces the wiring. Three layers deep, maximum. No exceptions.
Next: check any URL you are about to create against the tree below before you create it.

---

## The tree every site is built to

```
Layer 0   home
Layer 1   /services/   /blog/   /about   /contact   /quote
Layer 2   /services/plumbing          /blog/how-to-fix-low-water-pressure
Layer 3   /services/plumbing/toronto
```

**Home**
Links to every Layer-1 page.

**/services/**
The index, then one page per service, then one page per service and city: `site.com/services/plumbing/toronto`. City pages are the ONLY thing that goes to Layer 3.

**/blog/**
The index, with every post living FLAT directly under it: `site.com/blog/how-to-build-a-website`. No `/blog/category/post` subfolders. Hubs and spokes are expressed through INTERNAL LINKS - the spoke links up to its hub post, the hub links down to its spokes - never through extra folder depth.

**/about, /contact, /quote**
Single pages at Layer 1. About carries the author and E-E-A-T load. Quote, or contact, is the conversion target every blog post bridges to.

**/thank-you - off-tree, and mandatory.**
Every form redirects to it (`/api/lead` → 303 → `/thank-you`), and it is the page conversion tracking fires on. Without a distinct thank-you URL, tracking falls back to click or event triggers that break silently and undercount - see `references/standard-pages.md` for the full build.

It sits OUTSIDE the pyramid on purpose, and all four of these are deliberate, not oversights: **`noindex`** (if it ranks, people land there without converting and the conversion count becomes fiction) · **excluded from `sitemap.xml`** · **not linked from the nav** · **exempt from the 3-click and orphan rules** - it is reached by submitting a form, not by browsing. The gate skips it for exactly this reason.

**The booking calendar lives HERE, not on the money pages.** Set `bookingUrl` in `lib/site.config.ts` (collected on the first `/service-page` run) and the page renders the GHL booking embed automatically. This is deliberate: a money page keeps ONE primary action - the form - and the calendar appears the instant after they convert, when intent is highest. Two competing CTAs on a sales page split the decision and lower both.

The full chain: form → `/api/lead` → POST to the GHL inbound webhook (payload carries `source` and the referring page) → 303 redirect to `/thank-you` → conversion tag fires → booking embed offered.

**The template ships it pre-built and pre-wired.** On the import and WordPress lanes it does not exist yet - build it there, with the same four properties, before any form goes live.

---

## The seven rules that keep the tree intact

1. **Three layers max.** If a URL needs a fourth folder, the structure is wrong - flatten it. Deep URLs bury pages, dilute authority and break the crawl.
2. **3-click rule.** Every page is reachable within 3 clicks from home. The pyramid guarantees it IF internal linking does its job. Orphans are an internal-linking failure, not a folder problem.
3. **URL equals hierarchy.** The folder path IS the topical signal: `/services/plumbing/toronto` tells Google service plus city with no other context. Never build a page whose URL contradicts its place in the tree.
4. **Hubs before spokes.** Never publish a spoke whose hub does not exist yet - links need a target. Service hub before its city pages, hub post before its spoke posts.
5. **One page per keyword, one place per page.** A page lives at exactly one canonical URL in the tree. If a term could live in blog and services, services wins and the blog links to it.
6. **Sitemap mirrors the tree.** sitemap.xml contains exactly the pyramid: every live page, nothing else.
7. **Indexes are real pages.** `/services/` and `/blog/` are not bare lists. They are the hub pages of their branch: short intro, then links to every child with descriptive anchors.

---

## Locations are conditional, and you pick ONE stack

**A location page requires a real address.** An office in North York earns `/locations/north-york`. A town you merely serve gets a service+city page (`/services/plumbing/barrie`) and NO location page - no address, no location page, ever.

**Then pick one road and never both:**

- **Service-first:** `/services/plumbing/toronto` - the default, right for most businesses
- **Location-first:** `/locations/toronto/plumbing` - branch chains only, used INSTEAD, never alongside

Building both stacks creates two URLs per topic and a duplicate-content penalty. One stack, same stack, every page.

## The doorway-page trap

**If you can swap the city name and the page reads the same, it is spam.** Google calls these doorway pages and penalizes them; John Mueller has told site owners directly not to build 1,300 "keyword + city" pages. The play: **15-20 genuinely unique city pages** - real local jobs, real projects, real photos per city - never 500 thin ones. No local material for a city yet = flag it and skip it, never template it.

## The five URL rules

`yoursite.com/services/web-design` - every URL passes all five:

1. **All lowercase**
2. **The keyword lives in the slug**
3. **Hyphens, never underscores**
4. **Static - no `?id=4837` query junk**
5. **One URL = one topic**

`yoursite.com/Services/p?id=4837&s=XYZ` fails a human, so it fails Google. The URL should read like the map: `/services/seo/toronto` says service + city with no other context.

## Authority flows down

The homepage holds the most authority; every layer down holds less. Money pages live at click 2-3 - **click 3 is the money layer, never deeper**. Five layers deep means authority runs out before Google finds the page. This is why the tree is shallow and the nav is wired: clicks from home, not folders, are what Google counts.

---

## The evidence layer (35+ sources, researched 2026-08)

**Clicks count, folders don't.** John Mueller: Google "doesn't count slashes in the URLs" - click depth from home is the importance signal. Folder depth is for humans and crawl grouping. So the 3-click rule is an engineering target for MONEY pages, not a Google law - and nav/footer links legitimately reduce click depth.

**Nested vs flat city URLs - the one real disagreement.** Local specialists (Joy Hawkins/Sterling Sky) prefer flat `/plumbing-austin`; enterprise guides prefer nested. Google treats them identically (see above). **This repo uses nested (`/services/plumbing/toronto`) because the URL reads as the map and the tree stays legible - the only hard rule is consistency: never mix patterns, and never change a URL that already ranks.**

**Loose silos win.** Strict never-link-across-silos is dead (Ahrefs: "silly"). Bias links toward the same topic, cross-link wherever relevance is real, and route extra internal links FROM pages that have backlinks TO money pages.

**Hub pages carry content or they cost traffic.** Kevin Indig case: replacing link-only hub pages with real content recovered 70% of lost traffic. `/services/` and `/blog/` get intro copy and a descriptive line per child - never bare lists.

**What a hub page IS, precisely - both failure modes are banned:**

- NOT a bare link list (the Indig failure)
- NOT a sales page for one offer with the children as a card row underneath (a hero selling a single sprint/retainer with a form is a SERVICE page wearing the hub URL)
- IS: an H1 naming the category → 2-3 sentence intro → **one real section per child** (heading with the child's name, 2-4 sentences of what it is and who it's for, its photo, a descriptive link) → shared trust/CTA at the end. The children are the page. Offer pricing and enquiry forms live on the service pages, not the hub.

## Per-page linking quotas

- **Homepage** → every service hub, the service-areas hub, 3-5 best/newest posts
- **Service hub** → every city spoke under it, **as a real "Areas we serve" SECTION**: its own heading, one tile/line per city with a descriptive anchor ("Local SEO in Austin, TX"). **Placement: one qualifier line in the hero** ("Serving X, Y + N more" - an anchor link to the section) answering "do you serve me?" immediately, **and the full section mid-page - after the proof/reviews, before the FAQ.** Never a lone footnote link, never below the final CTA, and never a link-list where the proof belongs. Plus sibling services, its supporting posts, up to `/services/`
- **City page** → up to its service hub, 2-3 neighbouring city pages, the service-areas hub
- **Blog post** → its hub post (keyword-ish anchor), ≥1 money page (the commercial bridge), 2-5 contextual links per 1,000 words, never 100+ links on a page
- **Hub post** → every spoke, from the relevant body section, not a list at the end
- **Anchors:** majority = the target page's keyword or a close variant, minority varied

## Navigation spec

- **Main nav:** Home · Services (dropdown to each service) · Areas We Serve · About · Reviews · Contact. Nothing else, plain HTML links.
- **Footer:** NAP matching the GBP exactly · city-page links (only pages with genuinely unique content) · privacy/terms · HTML sitemap link.
- **Breadcrumbs sitewide** with BreadcrumbList schema, mirroring the tree.

---

## Redirect every URL the restructure moves

Restructuring into this pyramid moves URLs, so every old URL gets a 301 to its new home. Static export lane uses `vercel.json` redirects. WordPress uses the redirect plugin. Old ranking URLs never 404. `/build-website` owns this.
