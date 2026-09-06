# Hub and spoke pages - what they are, how to write them, how to link them

The formula behind every hub and spoke on the site. Built from 60+ sources (August 2026); every rule is tagged **[EVIDENCE]** (measured data exists) or **[CONVENTION]** (industry consensus, no study). Read by `/blog-post` and `/service-page`.
Next: find the page type you're writing below and follow its formula exactly.

---

# The two models - never confuse them

**Blog clusters:** flat URLs, linked hierarchy.
- Every post lives at `/blog/[slug]`. Folders never enter it.
- The PILLAR is the hub. Its spokes are posts on its subtopics. The hierarchy exists only in the links.

**Service clusters:** nested URLs, one axis.
- `/services/[service]` is the hub. `/services/[service]/[city]` are its spokes.
- The nesting IS the pyramid. Related services are SIBLINGS, never spokes (see keyword-clusters.md).

**Honesty note on the whole model [EVIDENCE of absence]:** Google has never endorsed topic clusters - it is a framework SEOs built ([Ahrefs says so plainly](https://ahrefs.com/blog/topic-clusters/)). The measurable mechanism underneath is internal linking and anchors, and the founding data is one 2015 HubSpot correlational experiment. It still works - but because links and coverage work, not because "clusters" are a ranking factor. The widely-quoted "43% average traffic increase from topic clusters" stat traces to no primary study - never cite it.

---

# The blog pillar - a router that teaches, not an encyclopedia

The field splits on whether a pillar is exhaustive or shallow. **The evidence favors shallow:** the best-performing pillars in Semrush's own example audit and thruuu's 100x case study were UNDER 1,000 words - short overviews that route readers into deep spokes ([thruuu case](https://thruuu.com/blog/topic-clusters/), [Semrush examples](https://www.semrush.com/blog/pillar-page-examples/)). Long-pillar prescriptions trace to a backlink correlation (3,000+ words earn more links), which measures links, not rankings. **[EVIDENCE leans short; length claims are CONVENTION]**

**The pillar formula:**

- **Targets the broad head term** - in URL, title, H1. Spokes take the long-tails. [CONVENTION, universal]
- **Opens by answering "what is X" in the first two paragraphs**, then a linked table of contents. [CONVENTION, universal]
- **One H2 section per spoke.** Each section: a 2-4 sentence passage that genuinely teaches the subtopic, with the spoke link INSIDE the passage. The section is the point; the link is its consequence. Never a bare "related posts" list, never links dumped at the bottom. [CONVENTION: HubSpot, Backlinko, Ahrefs all place spoke links inline in their sections]
- **⛔ Every spoke section appears in the page's table of contents.** A section the TOC doesn't announce is half-invisible - learned on a real page.
- **Breadth, not depth: each section deliberately stops short.** If a pillar section out-covers its spoke, the spoke is thin and cannibalizes - the #2 failure mode. [CONVENTION]
- **CTAs sparse** - one mid-text, one at the close. Pillar readers are early-funnel. [CONVENTION]
- **The pillar is a living index:** every new spoke means the pillar grows a section the same day. thruuu's pillar compounded to 100x over two years by being maintained. [EVIDENCE, single case]

---

# The blog spoke - one subtopic, all the way down

- **One subtopic, one primary keyword - never the pillar's head term.** This keyword split IS the cannibalization defense. [CONVENTION, universal]
- **Check SERP overlap before creating it:** if two candidate keywords share 4+ of the top 10, one page serves both (keyword-clusters.md has the gate). [CONVENTION with method]
- **Standalone depth:** the spoke could rank with no cluster around it. Deep on its one thing - the depth the pillar refused to have. [CONVENTION]
- **References its pillar by name EARLY** (intro or first section) and links up to it. [CONVENTION, universal]
- **1-3 sibling links to genuinely related spokes** - where the reader actually benefits, never a mesh of every spoke to every spoke. [CONVENTION, disputed between vendors - this is the middle path]
- **Links out to its money page** - the bridge CTA is why the post exists commercially. [CONVENTION + this repo's rule]
- **No fixed word count exists.** Every source refuses one. The bar: beat the current top 10 for the specific keyword. [CONVENTION]

---

# The service hub and its city spokes

**The service hub:**

- Carries the FULL sales content for the service - it is a money page first.
- **An H2 "Areas we serve" section: a short passage per city with the link inside it.** A wall of city names in a paragraph is a recognized spam pattern. Every live city spoke appears here - a spoke missing from the hub's section is an orphan in spirit. [CONVENTION: Sterling Sky, Whitespark]
- City spokes appear in a crawlable hierarchy (the hub's section + the services index). **Orphaned city pages are the #1 doorway tell** and nav inclusion was the first recovery step in documented deindex cases. [EVIDENCE](https://ricketyroo.com/blog/location-page-spam/)

**City spokes - the reality bar:**

- **Localize the PROBLEM, not just the place:** housing stock, climate, permits, real neighborhoods - things that change what the service looks like there. Name-swapping a template is duplication, not localization; even ~50% unique wasn't enough in one documented deindexing. [EVIDENCE](https://localsearchforum.com/threads/several-pages-got-deindexed.61290/)
- **First-party proof wins measurably:** hyperlocal content = +107% outranking probability, custom location photos +84%, inbound links to the city page +105% in [Wiideman's 300-page study](https://www.wiideman.com/location-pages-for-seo). (Embedded Google Maps correlated -34% - use a static area image.) [EVIDENCE]
- **References its service hub early and links up.** City spokes do NOT cross-link to every other city - discovery flows through the hub. [CONVENTION + Google's own doorway definition]
- **The honesty line for remote businesses:** city pages are legitimate only where you genuinely serve and can prove it. Say plainly "we serve X from our base in Y", never fake an address, target organic (not the map pack). [CONVENTION anchored to Google's written policy]

**⛔ Volume and the matrix - where city pages die:**

- **10-15 city pages is the number you can build WITHOUT distinct material per page - not a ceiling on a business that has it.** Build 2-3, measure, then scale. [CONVENTION: Whitespark, Rozek, Sangfroid converge here]

  **The material gate is the real cap.** A roofer with 40 real Toronto-area jobs, photos and reviews can legitimately run 40 city pages; `roofing-seo/toronto`, `/mississauga`, `/brampton` is a real structure. What kills a set is cloning, not counting - the 33,620-page site below indexed at 18% because the pages were templated, while hyperlocal content measured +107% outranking probability. **So the question is never "how many cities?" - it is "how many can pass 3-of-4 on the local-material gate?"** Almost everyone runs out of material first, which is why 10-15 is the useful default rather than a rule.
- **Never build the full service×city matrix by default.** The consensus-safe pattern is one page per service plus a small set of city pages; `/services/[service]/[city]` combo URLs are reserved for the 1-3 MONEY services in cities where the local-material gate passes (real jobs, photos, reviews from there - `/service-page` enforces this). [CONVENTION, strong consensus]
- **Enforcement is quiet, not dramatic:** templated city pages get "Crawled - currently not indexed" and mass-deindexed in spam updates (documented across 200+ sites, Aug-Dec 2022) - not manual penalties. Low authority + template = the death profile. [EVIDENCE](https://localbrandadvisor.com/website-location-page-helpful-content-update/)

---

# The linking numbers - what the data actually says

From [Zyppy's 23M-link study](https://zyppy.com/seo/internal-links/seo-study/), the only large-scale internal-linking dataset:

- **Give every target page ONE exact-match internal anchor** - pages with at least one got ~5x the search traffic. Then VARY every other anchor: anchor variety was the single strongest traffic correlate. One exact-match, then variants - never the same anchor from every spoke. [EVIDENCE]
- **Inlink sweet spot: benefits rise to ~40-44 internal links pointing at a page, then reverse past ~50.** Concentrate inlinks on money pages and pillars. [EVIDENCE]
- **Body links early in the page carry the most weight**; sitewide footer links can drag. [EVIDENCE-adjacent]
- **Every page within 3 clicks of the homepage** - crawl logs show shallower pages get crawled more. [CONVENTION with crawl-data support]
- **Zero orphans, ever:** when a new page publishes, add links TO it from 2-3 older relevant pages the same day. [CONVENTION, universal]
- **Link from strength:** a link from a page with real backlinks moves more than a diagram-pretty link from a page with none. When choosing where a money page's inlinks come from, prefer the pages that have earned external links. [CONVENTION: Kevin Indig's TIPR]

---

# Failure modes, ranked by how often they kill clusters

1. **Spoke keyword overlap → self-cannibalization** - clusters built by spinning near-identical keywords into separate posts. The SERP-overlap gate exists to stop this. [most-cited failure]
2. **Thin spokes weaker than the pillar's own section** - the spoke must out-cover the pillar's passage or it dilutes.
3. **Over-publishing / index bloat** - the strongest measured wins in the whole genre are from DELETING: QuickBooks pruned 2,000 posts for +44% traffic, +72% signups; another site pruned 10% of pages for +104% sessions. More pages is not the lever; coverage quality is. [EVIDENCE]
4. **A vague pillar that competes with its own spokes.**
5. **Orphaned/deep pages** - anything that matters sitting 4+ clicks deep or with no inlinks.

---

# The AI-search angle (2026) - what's real

- **Ranking still decides AI visibility:** 76% of 1.9M AI Overview citations also rank top-10 organic. Clusters help AI citations exactly as much as they help rankings - no separate magic. [EVIDENCE: Ahrefs]
- **The one strong pro-cluster data point:** pages covering a topic's fan-out sub-queries are 161% more likely to be cited - and covering sub-questions is literally what a cluster does. [EVIDENCE: Ahrefs]
- **Depth in one lane beats breadth:** topical authority transfers to adjacent topics 4x better than distant ones; own a topic before expanding. [EVIDENCE: Semrush, 283K citations]
- **Schema barely moves AI citations** (measured null: -4.6% to +2.4% across 1,885 pages) - schema is for rich results and eligibility, not a GEO lever. Freshness and existing rankings are what move citations. [EVIDENCE: Ahrefs]
