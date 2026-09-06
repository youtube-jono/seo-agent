# Keyword clusters and hub-and-spoke

The gates every keyword must pass before it enters keyword-map.md, and how keywords group into pages.
Applied by `/keyword-research`, `/keyword-research expand`, `/competitor-audit` and `/autopilot`.
Next: run every keyword through the three gates below before it goes anywhere near the map.

---

## Gate every keyword before it enters the map

A keyword only enters the map if it passes ALL three gates. Keywords that fail go to a `## Rejected` note with the reason - visible, not vanished.

**1. Winnable difficulty - a rule of thumb, not a law**
Difficulty must sit at least 30 points BELOW the site's Semrush Authority Score. A new or low-authority site (authority under 60) is capped at difficulty 30 or lower.

- Authority 70 · difficulty 40 or lower
- Authority 45 · difficulty 30 or lower
- Brand-new domain · difficulty 30 or lower

It keeps a new site off keywords it cannot win, which is worth having. But no study supports it, the two numbers come from different vendors on different bases, and difficulty is roughly 58% just a backlink count that reads anywhere from 46 to 72 across tools for the same keyword. Two better signals sit alongside it: the age of the current top 10, and how close the topic is to what the site already ranks for. Full evidence in [keyword-strategy.md](keyword-strategy.md).

**2. Real volume**
At least 100 searches a month. Below that, the page cannot pay for itself. One exception: a zero-difficulty gimme or an ultra-high-intent local term can pass at lower volume. Flag it, never sneak it.

**3. Intent matches page type**
Informational keywords (cost, how to, what is, vs) go to blog pages only. Transactional keywords (near me, emergency, [city], service, company) go to service and money pages only. Never crossed.

---

## Get the Semrush data the gates need

The rule needs real Semrush numbers: search volume, difficulty and Authority Score. No paid plan? Start the 14-day free trial - two weeks is enough to build the whole map.

https://www.semrush.com/partner/jonocatliffseo_7401436/?irclickid=UodwPVRilxyZWxsygXUph16GUkr03ZTt3xLWws0&irgwc=1&afsrc=1

When a keyword command runs without Semrush connected, its first recommendation is the trial, not the guess-stack.

---

## Build a cluster: one page, one primary plus four secondary keywords

```
type         (blog/service)
PRIMARY      how much does a plumber cost
SECONDARY 1  plumber cost per hour
SECONDARY 2  how much do plumbers charge per hour
SECONDARY 3  plumber hourly rate
SECONDARY 4  plumber call-out fee
```

Primary is the highest-volume term, and it becomes the title and the H1. Secondaries become the H2 sections.

---

## Build a hub-and-spoke: one hub plus four or more spokes, each its own page

```
HUB      how much does a plumber cost
SPOKE 1  cost to replace a toilet
SPOKE 2  clogged toilet plumber cost
SPOKE 3  drain cleaning cost
SPOKE 4  water heater replacement cost
```

The hub is the broad pillar page, and it is itself a cluster. Each spoke gets its own page.

---

## Decide cluster or spoke, then keep the pages off each other

**Cluster or spoke test**
Same intent and one page answers both, it is a secondary keyword - cluster it. Needs its own full article, it is a spoke with its own page. The objective check: Google both terms and compare the top 10 results.

- **4 or more shared URLs (40%)** means one page
- **0 to 2 shared URLs** means separate pages
- **Exactly 3** is the grey zone - decide it by hand, never automatically

**The 40% number is a convention, not a finding.** No study establishes any overlap threshold. Vendor defaults are all over the place: SE Ranking ships a 1-9 slider, LowFruits hard-codes 40%, Oncrawl recommends 4-6, Semrush hides its threshold entirely. We use 4 of 10 because it matches the most common shipped default, not because it was proven.

**And SERP overlap is not deterministic.** The same query checked at different times from the same location returns different results with no underlying change, and 1-3 position moves are constant background noise. So any pair sitting exactly at the threshold is a coin flip on a single snapshot - flag it for manual review rather than letting the count decide. See [keyword-strategy.md](keyword-strategy.md).

**No cannibalization**
Never target the same primary keyword on two pages. If a term fits both a blog post and a service page, the service page wins and the blog links to it.

**Linking**
Every spoke links up to its hub, and out to its money or service page, so blog traffic reaches conversions.

## Intent is decided elsewhere

Which page type a keyword gets is not a judgement call. [search-intent.md](search-intent.md) holds the rule: search the term, classify the top 10 results, 6 or more of one type decides it - our convention, labelled as one in that file. Run it before a keyword enters a cluster.

## Money pages use hub-and-spoke too, but a different shape

Both models exist in every site and they are not the same thing. Confusing them is why city pages get built wrong.

**Blog clusters are pure linking.** A pillar post and its supporting posts all sit flat under `/blog/`, related only by internal links. Folders never enter it.

**Money page clusters follow the URL nesting**, because that IS the pyramid:

- `/services/` - the top hub
- `/services/drain-cleaning` - a spoke of `/services/`, and at the same time the hub for its city pages
- `/services/drain-cleaning/burlington` - a spoke

**Every service page is both a hub and a spoke.** Its block says which service hub it belongs to and which cities hang off it.

### Two rules where money clusters behave differently

**1. City spokes do NOT all cross-link to each other.** Blog spokes benefit from sibling links because a reader genuinely wants the related article. Twelve city pages all linking to each other is a link web nobody navigates, and at scale it reads as manipulation on top of pages that already carry doorway risk. City pages link UP to their service hub and ACROSS only to a genuinely relevant neighbour - the next suburb over, not all eleven.

**2. Blog clusters link INTO money clusters. Never the reverse as the main flow.** The bridge CTA at the end of a blog post pointing at its service page is the whole reason the blog exists commercially. A money page does not need to link back out to five blog posts - that sends a buyer away from the form. One link to a genuinely useful guide is the ceiling.

### What this means for the build order

The service hub must exist before its city pages, same as any hub. And `/services/` must exist before any service page, or the top of the pyramid is missing and every service page is an orphan of the tree.

### Money pages: hub-and-spoke has ONE axis, and it is service to city

This is the error to avoid, and it is easy to make: labelling two related SERVICES as hub and spoke because one is topically narrower than the other.

`/services/saas-seo` and `/services/b2b-seo` do not nest inside each other. Neither is above the other in the tree. SaaS SEO being a subset of B2B SEO is a topical observation, not a structural one, and calling it a spoke implies a link hierarchy that the URLs, the build order and the linking rules all disagree with.

**The only hub-and-spoke on the money side:**

- `/services/[service]` is the hub
- `/services/[service]/[city]` are its spokes

That is it. A service page is a hub if it has city pages under it, and a plain page if it does not.

**Related services are SIBLINGS.** Label them that way and link them contextually where a buyer would genuinely cross over:

```
**Sibling** · related: 4 (B2B SEO) · 7 (Ecommerce SEO)
```

**Why the distinction earns its keep:** hub and spoke drives build ORDER (a hub must exist before its spokes have anything to link to) and it drives the linking direction the page commands write. Siblings have neither property - neither has to exist first, and the links between them are optional and contextual. Mislabelling siblings as spokes creates a false dependency that delays pages for no reason.

**The four labels, and nothing else:**

- **Hub** - has city pages beneath it. Lists them.
- **Spoke** - is a city page. Names its service hub.
- **Sibling** - a related service at the same level. Names the services worth cross-linking, or says none.
- **Standalone** - belongs to no cluster. A legal, common, permanent state.

**⛔ Standalone is the DEFAULT, not the failure.** A real keyword pull returns 50 terms and maybe 15 of them decompose into clean hubs. The other 35 are just pages. Forcing them into a structure is worse than leaving them loose, because a forced pairing becomes a forced H2 on a live page - the hub has to write a passage about a spoke that isn't a subtopic of it, and that paragraph reads exactly as strained as it was to write.

The order of operations, every time:

1. **Cluster what genuinely clusters.** Run the decompose test on each candidate pair. Pass = label it.
2. **Whatever's left is Standalone.** No apology, no placeholder hub invented to house it.
3. **Then look at the hubs you DID find and ask what's missing from them** - that's the refill below, and it is where new spokes come from. Spokes are pulled to fit a hub; they are never assigned from leftovers.

Standalone pages still get wired when they are built - siblings, money-page links, contextual body links. Standalone means "no hub relationship", never "no links".

**A page can leave Standalone later.** If a refill or a later expand run produces a hub the page genuinely decomposes into, relabel it and grow the hub's section for it when the spoke ships. That relabel is normal maintenance, not a correction.

---

## Refill a thin hub - the map is pulled toward the structure, never bent into it

A hub with 1-2 spokes is not a broken hub, and it is not a hub to abandon. It is a hub whose keyword family has not been fully pulled. The fix is always **more keywords, never more forcing**.

**A hub with fewer than 3 natural spokes is marked `Cluster: open - needs spokes`** and the run tries to fill it *before* the map is saved:

- Pull that root's full family (the ~100-variant pull expand mode does), run the four cuts, and see whether real decomposing subtopics exist that the first pass missed. They usually do - the first pull goes wide across the industry, so it under-covers any single root by design.
- **Everything found this way is subject to the same gates.** A spoke pulled to fill a hub still has to clear volume, intent and difficulty, and still has to pass the decompose test. "It fills the hub" is not a reason to admit a keyword.
- If the full pull genuinely returns nothing, **the hub is narrow and that is a finding, not a shortfall.** Record it on the block - `full pull done, 2 spokes is everything this topic decomposes into` - and stop. A hub with two real spokes beats a hub with two real spokes and three stretched ones.
- If nothing decomposes it at all, the hub was never a hub. Relabel it **Standalone** and move on.

**Depth-first is the evidence-backed order.** Topical authority transfers to adjacent topics about 4x better than to distant ones, and pages covering a topic's sub-queries are 161% more likely to be cited by AI ([hub-spoke-pages.md](hub-spoke-pages.md)). Thirty pages in five complete clusters is a stronger map than fifty scattered ones - which is exactly why the refill runs before any new topic opens.

---

## The linking contract - a link is not enough, the STRUCTURE must be visible

Owner-defined and non-negotiable. A hub or spoke is not "linked" until this shape exists on the page - a single wrapped anchor buried in a paragraph does not satisfy it.

**Blogs - flat URLs, linked hierarchy:**

- Every post lives at `/blog/[slug]`. Folders never enter it.
- **The pillar carries an H2 section about each spoke:** a short passage introducing the subtopic with the link inside it. A bare "related posts" list fails; the passage is the point.
- **Each spoke references its pillar by name** early in the body and links up to it.
- Spokes link horizontally to genuinely related sibling posts.
- Every post links out to its money page - the bridge is why the post exists commercially.

**Services - nested URLs, one axis:**

- `/services/[service]` is the hub. `/services/[service]/[city]` are its spokes.
- **The hub carries an H2 section covering its cities** - a passage per city with the link inside it (the "Areas we serve" pattern). Every city spoke that exists appears there; a spoke missing from the hub's section is an orphan in spirit even if some other link exists.
- **Each city spoke references its service hub** early in the body and links up to it.
- City spokes do not all cross-link to each other (the doorway rule above stands).

`/service-page` and `/blog-post` build to this contract: a new spoke means the hub's section grows a passage the same day.
