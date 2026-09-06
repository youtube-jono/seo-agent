---
description: Keywords, filtered and clustered into keyword-map.md - one file, your whole build plan. "expand" mode goes deep (10 roots → 1,000) - run it up front for depth AND again whenever the map thins
argument-hint: "[industry or service, optional] [expand]"
---

Build my keyword map. Topic: $ARGUMENTS (if empty, ask me: what's the business and what city does it serve?).

**Expand mode (`/keyword-research expand`)** - skip to the EXPANSION flow at the bottom instead of the base flow. **Run it TWICE in the life of a map, for two different reasons, and say which one is happening:**

- **Up front, right after the base run** - this is the one people skip, and it is the bigger lever. The base run goes wide across the industry, so it under-covers every individual root by design; expand pulls each root's FULL family (~100 variants) and that is what makes hubs arrive complete instead of two spokes short. **Front-load the depth. Do not wait for the map to run dry to get it.**
- **Ongoing, whenever the map thins out** - the refill. This one cannot be front-loaded, and not because of effort: keywords quarantined by the difficulty ceiling are unrankable *today* and genuinely reopen as Authority Score climbs. Same for new services, new cities, and standalone pages a later hub absorbs. No amount of up-front pulling surfaces those; only running it again does.

**Both, not either.** A big pull up front and a standing loop on top of it. If someone asks which one to do, the answer is the up-front pull first, because it is worth more - and then the loop forever, because the ceiling keeps lifting.

**0. Ask the market FIRST - before pulling a single number.** Semrush keeps a separate keyword database per country, and it defaults to the US. Pull US data for a business in Manchester or Calgary and every volume, difficulty and CPC on the map is for the wrong country - the map looks perfect and is quietly worthless.

So, before any data pull, ask: **"Which country are your customers searching from?"** (and if the business serves more than one, which is the primary market). If CLAUDE.md "## My setup" already records it, confirm it back to me rather than asking cold.

Then set the Semrush database to match - `us`, `uk`, `ca`, `au`, `nz`, `ie`, `de`, `fr` and so on - and **say on screen which database you're using** so I can catch it if it's wrong. Record it in CLAUDE.md "## My setup" so it's never asked twice.

Two traps worth knowing:
- **Language and spelling shift with the market.** UK searches "boiler repair" where the US searches "water heater repair"; "gutter cleaning" vs "eavestrough cleaning" in parts of Canada. Ask which words locals actually use, and never assume the US phrasing translates.
- **National volume is not local volume.** Semrush reports country-level volume; a business serving one city sees a fraction of it. Never present a national number as if it's their addressable demand - say plainly that it's the country figure and that local share is a slice of it.

**Then ask the business type - it changes the whole shape of the map.** Ask: **"Are you ecommerce, a local/national brand, or an internet business?"** If "## My setup" already has it, confirm rather than ask cold, and record it there. Never assume - these three get completely different maps from the same command, and guessing wrong wastes the whole research pass.

**Ecommerce** - you sell physical products.
- Category pages own the broad terms ("running shoes"), product pages own the specific ones (brand + model + attribute). Never let both chase the same term.
- The money modifiers are transactional: buy, best, review, cheap, size, colour, "for [use case]", "vs".
- Watch for terms Google fills with Shopping results - organic room there is thin, and that's a paid signal, not an SEO opportunity. Say so rather than mapping a page that can't rank.
- Informational terms feed the blog and route internally to categories, never compete with them.

**Local / national brand** - you sell a service or run a business with a real-world footprint.
- **Local:** service × city. City modifiers and "near me" are the money terms. National volume is irrelevant - what matters is the slice inside the service area, so never present a country figure as their addressable demand. Service pages per city at Layer 3; GBP and citations carry real weight. Low volume is normal and fine: 40 searches a month for "emergency plumber [city]" can outearn 4,000 informational visits.
- **National:** drop the city axis entirely. Head terms and their long tail, higher difficulty across the board, so the KD-vs-authority rule bites much harder - expect to win the long tail first and work up. Comparison terms ("X vs Y", "best X for Z") matter far more.
- Ask which one they are; a brand serving one city and a brand serving a country share nothing but the label.

**Internet business** - SaaS, agency, info products, courses, anything delivered online with no geography.
- **Problem-led, not service-led.** People search the pain before they know the category ("how to stop double-booking clients" long before "scheduling software"), so map the problem terms as well as the product terms.
- The highest-intent terms are comparison and alternative: "[competitor] alternative", "best X for [use case]", "X vs Y", "X pricing", "X review". These convert hardest and are usually the least defended.
- **Geo is irrelevant** - never add city modifiers. Segment by use case, audience or integration instead ("for agencies", "for Shopify", "for freelancers").
- Difficulty is brutal on head terms because everyone is chasing the same words with real budgets. The realistic lane is the specific long tail; say that plainly rather than mapping head terms they can't win.

If they're more than one (a local shop that also ships nationally, an agency with a productised tool), ask which is the priority and build that map first. Say clearly the second is a separate pass - never blend two into one confused map.

**0c. ⛔ CONFIRM THE SERVICE LIST OUT LOUD. This is the step that stops a whole map being wrong.**

Before pulling a single keyword, ask me for the exact list of services I sell, and what I do NOT do. Then **say back the exact list of services this map will be built for**, numbered, then wait:

> **"I'm building the map for these services: 1) SEO Sprint · 2) Google Ads Sprint · 3) Growth Retainer. Anything missing, anything on there you don't sell? A wrong list here wastes the whole run."**

Everything downstream inherits this list. Get it wrong and 1,000 keywords, 50 clusters and months of content point at a business that does not exist - and it looks completely convincing, which is why nobody catches it until the pages are written.


**0d. ⛔ NEVER silently overwrite an existing `keyword-map.md`.** If one exists, read it first and report what is there: how many pages, targeting what, how many already written. Then ask:

> **"You already have a map of 52 pages targeting SEO and Google Ads services, 6 of them written. Do you want me to add to it, replace it, or is this a different service line that needs its own pass?"**

A keyword map is hours of research plus everything built on top of it. Replacing one is a deletion, and it falls under the same rule as any other deletion: it needs an explicit yes. **Default to appending** (that is what `expand` mode is for). If replacement is genuinely wanted, say what is being lost, get the yes, then write over it. **No archive folder** - git already holds every previous version.


### ⛔ The difficulty ceiling applies to BLOG POSTS. Money pages are governed by what the business sells.

The two page types have different jobs, so one ceiling cannot govern both.

**Blog posts: the ceiling is a hard gate.** A blog post's only job is to rank. If it cannot rank, it is wasted work, so a term above the ceiling is cut or quarantined until authority catches up. No exceptions.

**Service pages: build what they SELL, not what they can rank for today.** Ranking is only one of the ways someone arrives on a money page. It is also where ads land, where the Google Business Profile points, where internal links flow, and where a referral checks them out. A business with no page for its flagship service looks broken to every visitor regardless of what it ranks for - and there is nothing for the rest of the site to link up to.

**So a hard head term still gets its page. The RANKABLE version is the city or modifier variant underneath it.**

- `seo services` · difficulty 65 · unrankable today · **still build the hub page**, because it is the destination and the linking target
- `seo services vancouver` · far softer · **this is the page that ranks**, at tier 3
- Same shape everywhere: `emergency plumber` is brutal, `emergency plumber [suburb]` is winnable

Say this out loud in the map block rather than hiding it. The honest line is *"the hub exists to convert and to be linked to, and these three city pages underneath it are what actually earn the rankings."*

**What the ceiling DOES still decide on a money page:**

- **Which phrasing becomes the primary keyword.** Between `organic seo services` at 20 and `seo services` at 65, the winnable one is the H1 and title. The hard one appears naturally in the copy and is never the target.
- **How many city pages the hub needs**, and how quickly. A hub whose head term is far out of reach leans harder on its tier-3 spokes.
- **The order.** Winnable money pages get built before unwinnable ones, because they return something this quarter.

**Never cut a service the business actually sells because its keyword is hard.** That is optimising a keyword map at the cost of the website.

**1. Gather.** Cast wide first - cutting comes next, and it all happens in one pass.
- If the Semrush MCP is connected, pull volume, KD and intent for everything, AND the site's current Authority Score - that score sets the difficulty ceiling, so get it before anything else.
- If not connected: FIRST recommendation is the **Semrush 14-day free trial** (https://www.semrush.com/partner/jonocatliffseo_7401436/?irclickid=UodwPVRilxyZWxsygXUph16GUkr03ZTt3xLWws0&irgwc=1&afsrc=1) - two weeks is enough to build the entire map with real data, and the filters below can't run properly on guesses. Only if I decline: fall back to the free stack (autocomplete, People Also Ask, Trends, trade knowledge), volumes marked ESTIMATE, and note the map needs re-validating when Semrush connects.

**2. Filter - all four cuts in one pass, in this order.** Every keyword either survives all four or goes to the cut list with the reason. Never filter halfway and come back later.

**Cut 1 - Junk.** Anything that could never become a page worth having: misspellings, brand names that aren't mine, job and career terms, salary, courses, training, licensing, DIY, tools, parts, wholesale, suppliers, "free", trivia. Also anything on the DON'T list I gave you in step 0c - a service I don't offer is junk no matter how good the volume looks.

**Cut 2 - Wrong intent, verified on Google. Read `references/search-intent.md` - it IS the rule:** search the term, classify the top 10 results, and 6 or more of one type decides it. Under 6 for every type is a mixed SERP and gets handled per that file. **The 6-of-10 threshold is our internal convention, not a documented standard** - never cite it as best practice. When a call is genuinely close, **err toward transactional**: modifier-based guessing systematically over-labels things informational (82% of measured classification errors ran that direction). **Semrush's intent label is frequently wrong - never trust it alone.** For every keyword that survives Cut 1 and matters, search it and read the actual results page:
- Top 10 full of guides, "how much does X cost" articles, Reddit threads, calculators → **informational**, and it belongs to a blog, not a service page
- Top 10 full of service pages, local businesses, a map pack, ads running → **commercial**, that's a money page
- Mixed → read what Google chose to rank FIRST, that's the dominant intent
- Ads showing is a strong commercial signal; a map pack means local intent specifically

Then route it: **blogs own the info terms** (cost, how to, what is, vs), **service pages own the hire terms** (near me, emergency, [city], service, company). Never let both target the same keyword - if a term genuinely fits both, the service page wins and the blog links to it. Say in the report which keywords Semrush labelled wrong; it's usually a handful and it's usually the expensive ones.

**Cut 3 - Volume floor: 100+ searches a month.** Under 100 goes to the cut list. **One deliberate exception:** an ultra-high-intent local term with near-zero difficulty ("emergency plumber [small suburb]", 50/mo, KD 4) can earn its place - if you keep one, say so explicitly with the reason, never let it through silently.

**How to hold a volume number - this changes what you may say to a client.** Tool volume is heavily bucketed and unreliable. Across 101,897 keywords carrying Keyword Planner figures, only 1,462 distinct values existed - about 70 keywords sharing every value. Median calibrated volume came out at 0.51x the reported figure, and Ahrefs' own measured accuracy against Search Console impressions is 60%.

So:

- **Use volume ONLY to rank keywords against each other**, as an order-of-magnitude signal. "This one is roughly ten times bigger than that one" is supportable. "This one gets 2,400 a month" is not.
- **Never present volume to a client as predicted visits.** No "this page will bring 2,400 visits". If a traffic number is genuinely needed, estimate from what the current top-ranking page earns across all its keywords, and say plainly that it is an estimate.
- **Never sum the volumes of close variants.** Google reports the family total onto each member, so adding "plumber" and "plumbers" double-counts the same demand.
- **On local terms, do not sort by volume at all.** City-level demand sits exactly where bucketing is most destructive - genuinely different demand all reported as 0, 10 or 20. Build the full services-by-cities grid, rank by revenue per job, and let volume only break ties.

**Cut 3b - AI Overviews have split the keyword universe. Weight the map accordingly.** Organic CTR on queries showing an AI Overview fell 61% (1.76% to 0.61% across 3,119 terms and 25.1M impressions), and that damage is concentrated on informational and educational queries. Transactional and local queries largely do not trigger an AI Overview at all, because a summary does not help someone ready to hire.

For a local service business this is a directive, not a nuance:

- **Weight the map toward transactional and local terms.** Hire, book, quote, emergency, near me, [city] + [service]. These keep close to their pre-AI-Overview click behaviour.
- **Treat informational posts as top-of-funnel and internal-linking fuel, not traffic plays.** Still worth writing - they build topical coverage and they feed links down to the money pages - but do not forecast traffic off them and do not let them dominate the build order.
- **Say this in the report** when the map skews informational, rather than shipping a list of blog posts whose clicks have already been taken.

**Cut 4 - Difficulty ceiling. A rule of thumb, not a law.** The guardrail from `references/keyword-clusters.md`: **KD at least 30 points BELOW the Authority Score**, and any site with Authority under 60 gets a flat **KD ≤ 30** ceiling.

- Brand new or under 60 · ceiling 30
- Authority 70 · ceiling 40
- Authority 80 · ceiling 50

**Say out loud that this is a rule of thumb, because it is.** No study supports it. KD and Authority Score come from different vendors computed on different bases, so subtracting one from the other is not a dimensionally meaningful operation - it is a useful habit dressed as arithmetic. Keep the ceiling; it does stop a new site burning months on keywords it cannot win. Just never defend it as a law.

**And KD itself is mostly a link count.** Ahrefs computes it purely from referring domains to the top 10, and about 58% of the Semrush score is referring domains plus Authority Score. The same keyword reads anywhere from 46 to 72 depending on the tool, so a KD number is never comparable across tools and a threshold set in one tool cannot be applied to another's score.

**Two things predict a new site's chances better than KD, so check both on every root:**

- **Age of the current top 10.** Across 1.3 million US keywords, 72.9% of top-10 pages are more than 3 years old and the average page at position 1 is 5 years old. A SERP with no recent entrants is telling you something KD cannot. A SERP with a page published this year in the top 5 is an opening.
- **Topical proximity.** Pages on topics a domain already ranks for reached their first click materially faster (roughly 35-40% within three weeks versus about 20% for unrelated topics). Keywords adjacent to existing coverage beat isolated higher-volume ones.

State the ceiling AND the Authority Score it came from in the file header, so the number is never a mystery and the user knows exactly what unlocks as the score climbs. Full evidence and sources: `references/keyword-strategy.md`.

Everything cut is **quarantined, never deleted** - it goes in the cut section grouped by *when it becomes useful*, not by rejection reason. A wrong cut is invisible forever; a quarantined keyword gets a second look.

**3. Cluster into roots.** Read `references/keyword-clusters.md`. Every surviving keyword joins a cluster built around a **root keyword**:
- **The root is the highest-volume term that ALSO has the right intent.** Both, not either. If a lower-volume term is the root, the block must say why in one clause - otherwise it is a mistake, not a decision.
- **The root can never have lower volume than one of its own secondaries without a stated reason.** That is the single easiest error to spot on review and it happens constantly. Check every cluster for it before saving.
- **Supporting keywords scale with the page, they are not a fixed number.** Service and city pages: 4-5. Blog spokes: 4-8. Blog hubs and comprehensive guides: 8-15. A short page cannot carry fifteen without padding; a 2,000-word hub with four is under-mapped and leaves its own subtopics uncovered.
- **⛔ The floor is 4 - and a thin cluster means the pull isn't done, not that the map ships thin.** No cluster ships with fewer than 4 secondaries until its root's FULL family has been pulled (the ~100-variant pull expand mode does - run it for that root NOW, inside this run, not as homework for later). After the full pull, if fewer than 4 real same-intent secondaries exist, ship what is real with the reason on the block: "narrow family - N is everything with this buyer's intent." That is a verified fact about the market. "None mapped yet" is NOT a shippable state - it is an IOU that someone builds a page on top of months later. Never invent a secondary to reach 4: a fake secondary becomes a filler H2 on a real page.
- Each one becomes an H2 section, so the count IS the outline length - if you cannot picture a real section for a keyword, it does not belong in the cluster
- **⛔ Synonyms are not secondaries.** Word-order flips ("google ads vs seo" for "seo vs google ads"), brand renames (adwords/ppc for google ads), and spelling variants are the SAME query - Google resolves them to one intent and one page ranks for all of them automatically. They never count toward the 4-secondary floor and never get an H2. Record them on ONE line in the block - "Also ranks for: [variants, combined volume]" - so the volume isn't lost and nobody re-adds them later. The test: if two keywords would produce the same H2, they are one keyword.
- **They must share SERP intent with the primary** (the cluster-vs-spoke test below decides this, never a guess). Secondaries appear naturally when the page covers its topic properly - never force one in
- **The cluster-vs-spoke test:** Google both terms and compare the top 10. 4 or more shared URLs (40%) = same page. 0-2 shared = separate pages. Exactly 3 is the grey zone - decide it by hand. The threshold is a convention, not a finding, and SERP overlap is not deterministic, so never auto-decide a borderline pair. Run this on every borderline pair rather than guessing
- **Hubs and spokes - label the pair ONLY when the spoke DECOMPOSES the hub.** The test: could the spoke's entire topic be ONE H2 section of the hub's page? "Audit your Google Business Profile" decomposes "how to do a local SEO audit" - real spoke. "SEO for contractors" does not decompose it - same industry is not same topic; that is a SIBLING. Never force a pairing to make the map look structured: a stretched spoke reads as a stretch on the live page, with no natural section for the hub to give it. A broad root with decomposing roots underneath is a HUB; record which is which and what links to what - `/service-page` and `/blog-post` both read it
- **⛔ Most pages are Standalone, and that is the correct outcome.** A pull of 50 keywords does not contain 50 pages' worth of structure - maybe 15 of them decompose into clean hubs and the rest are simply pages. Label those **Standalone** and move on. Never invent a hub to house leftovers, and never stretch a spoke to fill a hub: a forced pairing becomes a forced H2 on a live page, where the hub has to write a passage about something that isn't a subtopic of it. That paragraph reads exactly as strained as it was to write. Cluster what clusters, label the rest Standalone, THEN refill the real hubs (next bullet). Standalone pages still get linked from their index page and their nearest money page - it means no hub relationship, never no links
- **⛔ Every hub block carries its spoke count, and a hub with fewer than 3 natural spokes is marked `Cluster: open - needs spokes` - and this run TRIES TO FILL IT before saving.** Same rule as the 4-secondary floor: a thin hub means the pull isn't done, not that the map ships thin. Run the ~100-variant pull for that root NOW, inside this run, and see whether real decomposing subtopics exist that the wide first pass missed - they usually do. Everything found that way clears the same four cuts and the same decompose test; "it fills the hub" is never a reason to admit a keyword. If the full pull genuinely returns nothing, that is a finding: write `full pull done - N spokes is everything this topic decomposes into` on the block and stop. If nothing decomposes it at all, it was never a hub - relabel it **Standalone**. Anything still open at the end of the run is the debt the map owes, and **expand mode feeds open hubs FIRST, before opening any new topic.** The evidence backs depth-first: topical authority transfers to adjacent topics 4x better than to distant ones, and pages covering a topic's sub-queries are 161% more likely to be cited by AI (`references/hub-spoke-pages.md`). Fifty scattered pages is a weaker map than thirty pages in five complete clusters


### The "who is actually typing this" test - run it on every root

Volume tells you how many. It never tells you **who**, and three different people search the same phrase:

- **The buyer** - wants to hire someone. This is the only one a money page can convert.
- **The DIYer** - wants to do it themselves. Reads the page, never calls. Belongs to a blog post.
- **The peer** - a competitor or agency researching the niche. Worth nothing, ever.

**The trap: `[service] for [audience]`.** "SEO for contractors", "bookkeeping for restaurants", "marketing for dentists". The audience is right, which is why it feels correct, but the phrasing is how a GUIDE is titled, so the results fill with how-to content and the searchers are mostly DIYers and peers. High volume, low buyers.

**The buying signal is a noun, not the audience.** These are the words that mean somebody is hiring:

- services · company · agency · consultant · firm
- near me · in [city]
- pricing · cost · quote · packages (buying-adjacent - verify, these can go either way)
- hire · best · top rated

So in a cluster like this one:

- `seo for contractors` · 3,600/mo · reads like a guide title · likely DIY and peers
- `contractor seo services` · 1,000/mo · "services" · someone hiring
- `plumber seo services` · 880/mo · "services" plus a trade · someone hiring

**The 1,000/mo term is the better root** even at a third of the volume, because a page ranking #1 for the guide term earns readers and a page ranking #1 for the services term earns calls. Say this out loud when it happens rather than silently taking the bigger number.

**Where the losing term goes:** never delete it. `seo for contractors` is a genuinely good BLOG post that links to the service page. High-volume informational terms are the top of the funnel, not junk - route them, don't cut them.


**3b. ⛔ Every root gets searched. The block shows a verdict, not an essay.**

Cut 2 verifies intent on the live results page. The block records only the outcome:

```
**Google check:** passed
```

That is the whole line. **A keyword that fails is not in the map as that page type** - it was routed to a blog post at Cut 2 and never reached a service-page block, so a failure never appears here.

**Three things this line must never do:**

- **Never explain a pass.** "Six agency pages out of seven results, commercial" is working shown for a decision nobody is going to overturn. Keep it in the run, out of the file.
- **Never hedge.** "Not re-checked on this run, the previous pass recorded..." is noise pretending to be diligence.
- **Never ship unchecked.** There is no "I could not verify this" state. Either the search ran and the block exists, or it did not and the keyword waits. An unchecked root is not a finding, it is unfinished work.

**The one exception:** a genuinely mixed SERP, where the answer changes what gets built. Then say it in under ten words - `**Google check:** mixed, money page wins the term` - because that page needs watching and the reader has to know why.

**3b-dedupe. ⛔ THE CANNIBALIZATION GATE - every surviving keyword is tested against the EXISTING map, not just against the other new ones.**

Exact-match dedupe is not enough and it is the failure everyone ships. `emergency plumber toronto` and `24 hour emergency plumber toronto` are different strings, pass any string check, and are the same page - build both and they split their own rankings forever. **Two pages competing for one intent is worse than one page, and it is invisible until months of GSC data show it.**

So before a keyword becomes a new block, run it against every primary AND secondary already in `keyword-map.md`:

- **Cheap pass first - is it already a SECONDARY somewhere?** A term sitting in an existing cluster's secondary list is already covered by that page. It never becomes its own block. Say which row owns it and move on.
- **Then the SERP-overlap test against the closest existing primary**, exactly as `references/keyword-clusters.md` defines it: Google both, compare the top 10. **4 or more shared URLs = same page** - add the new term as a SECONDARY on the existing row instead of creating a block. 0-2 shared = genuinely separate, it gets its block. Exactly 3 is the grey zone and gets decided by hand, never automatically.
- **Only run the test on plausible collisions.** Same head noun, same intent, same city. Testing 60 new keywords against 40 existing rows is 2,400 searches nobody will run; testing the handful that share a subject is about a dozen and catches essentially all of it.
- **A term absorbed as a secondary is not a loss - say so.** `"24 hour emergency plumber toronto" folded into row 1 as a secondary - 7 of 10 shared results, same page.` That sentence is more valuable than a new row, because it is the page that did NOT get built.

**⛔ Never resolve a collision by making the new page "more specific".** Narrowing the angle to justify a second page is how doorway-adjacent near-duplicates get into a map with a straight face. If Google shows the same results for both, it is one page. Full method and the honest caveats (the 40% threshold is a convention, and SERP overlap is not deterministic) in `references/keyword-clusters.md`.

**3c. ⛔ Re-sort the standalones. EVERY run, base and expand, before saving.**

Standalone is a permanent-until-proven state, not a permanent one. A page sits standalone because on the day it was mapped nothing it decomposed into existed yet. Every later run changes that: new roots arrive, new hubs form, and a page that had no home in March genuinely has one in June. **If nobody re-checks, the map calcifies** - it accumulates loose pages forever while hubs sit two spokes short of complete, and the two never meet.

**⛔ Two guards make this cheap and safe. Both are hard rules, not preferences.**

**Guard 1 - the sweep only ever promotes. Standalone → Spoke, never the reverse.** The decompose test is a judgment call, not a deterministic check, so an unguarded sweep lets a page flip standalone → spoke on one run and back on the next. That is not a cosmetic wobble: the hub page will already carry a passage linking to it, and demoting the page leaves that hub with a paragraph about something that is no longer its spoke, which nothing cleans up. So **this step never demotes anything.** A page leaves a hub only by explicit human decision, never by sweep.

**Guard 2 - test against OPEN hubs only** (those marked `Cluster: open - needs spokes`, i.e. fewer than 3 spokes). A hub that is already complete does not need more spokes, so testing against it is pure waste. This is what keeps the sweep to roughly a dozen comparisons instead of every standalone against every hub, which is the version that quietly gets skipped.

So before writing the file, take every existing `**Standalone**` block and test it against the OPEN hubs only - both the ones already in the map and any this run just created:

- **Run the decompose test, unchanged.** Could this page's entire topic be ONE H2 section of that hub? Yes = relabel it `**Spoke** · hub: N (Title)` and add it to that hub's spoke list. No = it stays standalone, and nothing is said about it.
- **The bar does not drop because the sweep is running.** This step finds pairings that became true; it never manufactures one to close an open hub. A standalone page surviving ten sweeps is a page that is genuinely just a page.
- **A promotion is a real change downstream.** `/service-page` and `/blog-post` read these labels, so a page moving into a hub means the hub's spoke section needs a short passage and a link for it - add that when the spoke ships. Say so when reporting the move.

**Report the moves in chat, never silently.** One line each: `"citation audit" was standalone, now a spoke of hub 3 (local SEO audit) - the hub needs a passage linking to it`. If nothing moved, say `standalone sweep: 12 checked against 3 open hubs, none cluster yet` in one line. Never a table, never a per-page essay.

**No open hubs on the map? Skip this step entirely and say `standalone sweep: skipped, no open hubs`.** Nothing to promote into means nothing to test, and running it anyway is the failure mode this step was written to avoid.

**4. Prioritise and save. ONE file: `keyword-map.md`.**

**Write `keyword-map.md` plus its companion `keyword-map.html` (step 4b) and NOTHING else. There is no `keyword-list.md` - it was retired on 2026-08-13. If a `keyword-list.md` exists in the project, delete it.** Two markdown files means the user cross-references two documents to make one decision, which is the exact problem this merge solved. The HTML is not a second document - it is the same map rendered as a table, regenerated from the markdown every save.

Sort for quick wins: real volume, low difficulty, highest commercial intent first. Hubs always appear before their spokes.

**Use EXACTLY this shape. Copy it. Do not invent a table, do not add columns, do not abbreviate.**

```markdown
# Your keyword map

63 pages to build, in order. Nothing here is harder than your site can
rank for today (difficulty ceiling 30, from your authority score of 9).

---

# To build · 61

## 1. Service page: Emergency plumber

**Hub** · spokes: 4 · 5 · 9

**Checked on Google:** top results are plumber service pages plus a map pack and ads - commercial.

**Primary keyword**
- emergency plumber toronto · 2,400 searches a month · Easy to rank for (18 out of 100)

**Secondary keywords**
- 24 hour plumber toronto · 300 a month · Easy (16)
- urgent plumber toronto · 200 a month · Easy (14)
- after hours plumber toronto · 170 a month · Easy (12)
- same day plumber toronto · 90 a month · Easy (11)

**Why first:** highest volume on the list, someone searching this is
ready to call today, and three other pages need it to exist before
they have anything to link to.

---

## 2. Blog post: How much does a plumber cost

**Hub** · spokes: 6 · 7 · 8

**Primary keyword**
- how much does a plumber cost · 1,900 searches a month · Medium (22 out of 100)

**Secondary keywords**
- plumber cost per hour · 590 a month · Easy (18)
- how much do plumbers charge · 320 a month · Easy (16)
- plumber call out fee toronto · 90 a month · Easy (9)

**Why second:** people researching price today hire within a few weeks,
and it's the hub for everything about pricing.

---

## 4. Service page: Burst pipe repair

**Spoke** · hub: 1 (Emergency plumber)

**Primary keyword**
- burst pipe repair toronto · 590 searches a month · Easy (14 out of 100)

**Secondary keywords**
- emergency pipe repair toronto · 210 a month · Easy (12)
- flooded basement plumber toronto · 170 a month · Easy (15)
- water leak repair toronto · 140 a month · Easy (11)

**Why here:** lower volume, but the people searching it are in a crisis
and convert better than almost anything else on the list. Page 1 has to
exist first so this has somewhere to link.

---

# Written · 2

Moved here once `/service-page` or `/blog-post` has drafted them.
What happens next (review, publish date, live) is tracked in website-index.md.

## 7. Service page: Drain cleaning

**Hub** · spokes: 12 · 13

**Primary keyword**
- drain cleaning toronto · 1,900 searches a month · Medium (21 out of 100)

**Secondary keywords**
- blocked drain toronto · 480 a month · Easy (18)
- clogged drain service toronto · 320 a month · Easy (16)

---

## Keywords saved for later · 41

**Opens up when your authority score reaches about 40 · 12 keywords**
white label seo · seo for lawyers · ppc management services

**Opens up around 55 · 18 keywords**
seo retainer · technical seo audit · google ads agency

**Too few searches to be worth a page · 6 keywords**
seo sprint · ads sprint · content sop

**Google shows something else for these · 5 keywords**
content machine - the top results are a comedy duo, not software
claude alternative - tool shoppers, not buyers
```

**The saved-for-later section has hard limits, because this is where the file turns into a wall of text.**

- **Show at most 10 keywords per group.** More than that, show 10 and write `+ 23 more` on its own line. Nobody reads keyword 34 in a run-on list, and the whole point of this section is the HEADING - "these open up at authority 40" is the information, the individual words are not.
- **Never a bare number in brackets.** `viral hooks (33)` is meaningless - is that searches, difficulty, position? Either label it or leave it out. In this section, leave it out: the group heading already says why they are here.
- **Never let a group run past three lines.** A paragraph of `·`-separated keywords wrapped at 72 characters is exactly the data dump `output-format.md` rule 9 bans, just with prettier separators.
- **"Google shows something else" gets one keyword per line with its reason**, because that reason is genuinely useful and it is lost the moment it is crammed into a run-on list.
- **Never repeat a group that has nothing in it.**

**Two lists, and pages MOVE between them.**

- **`# To build`** holds every page that hasn't been written yet, in priority order. This is the whole list - it's what the file is for.
- **`# Written`** holds pages `/service-page` or `/blog-post` has drafted. A page's whole block MOVES down here, keeping its number, so numbering never gets reused and the history stays readable.

**This file stops at "written".** Review, publish dates and going live are tracked in `website-index.md` - never duplicate those stages here or the two files drift and neither can be trusted.

**Only write sections that have something in them.** `# Written` appears the first time a page moves into it, never as an empty placeholder. "Saved for later" appears only if something was actually cut. Under about 10 pages, drop `# To build` as a heading too and just number the blocks.

**No `## How to use this` block.** The blocks say what to do by being shaped
the way they are. Instructions on top of a self-evident file are furniture.

**The non-negotiables in that shape:**
- **One block per page. Never a table of pages.** Tables force the reader to rebuild the page in their head.
- **Every number is labelled.** "2,400 searches a month", never `2,400`. "Easy to rank for (18 out of 100)", never `KD 18`.
- **Every secondary keyword carries its OWN volume and difficulty.** That's what tells the user how much of the page to spend on each one.
- **The heading says the page type AND the topic:** `## 1. Service page: Emergency plumber`.
- **Every page has a "Why".** Without it people build in a random order regardless of the numbers.
- **No Status column, ever.** A block is in `# To build` or `# Written`. That IS the status.
- **On the money side, hub-and-spoke has ONE axis: a service page is a **Hub** only if it has city pages beneath it, and a **Spoke** only if it IS a city page. Two related services are **Siblings**, never hub and spoke - `/services/saas-seo` and `/services/b2b-seo` do not nest, so labelling one a spoke invents a build dependency that does not exist. Blog clusters keep the normal pillar-and-supporting shape.

**Every block declares its label on one line.** Hubs list their spokes by number: `**Hub** · spokes: 4 · 5 · 9`. Spokes name their hub by number and title: `**Spoke** · hub: 1 (Emergency plumber)`. Standalone is the bare word on its own: `**Standalone**`. Nothing else on that line - no sentence, no explanation, and never a note apologising for being standalone. This is what `/service-page` and `/blog-post` read to wire hub and spoke links, and what makes "build hubs first" enforceable.
- **A hub is always numbered before its spokes.** A spoke can never come first - it would have nothing to link to on the day it's published.
- **No abbreviations.** No KD, Vol, SV, CPC, KW. Spell it out or leave it out.
- **Header is two lines maximum**, and caveats ("these are estimates") are one line inside it, never their own section.
- **Never write an empty section.** No "Started / Nothing yet".

Grouped headings (`# Service pages`, `# Blog posts`, `# City pages`) once there are more than about 20 blocks. Never collapse the tail into a stripped table - two formats in one file is the cross-referencing problem all over again.

**How many keywords should survive?** There is no target number - the filters decide, not a quota. As a sanity check: a normal run lands somewhere around **40-80 clusters**, which is 6-12 months of content at a realistic publishing pace. Well under 20 usually means the roots were too narrow or the ceiling is biting hard on a new domain - say so rather than padding the list with keywords that failed Cut 3 or 4. Well over 100 means it's worth splitting into tiers so the first month is obvious.

**Never pad the map to hit a number, and never cap it artificially either.** The map is meant to be re-run: `/keyword-research expand` refills it from new roots whenever it runs dry, and the ceiling itself lifts as Authority Score climbs, so keywords rejected today reopen later. A member running this every few months will keep finding new ground - that's the design, not a shortfall.

**4b. Generate `keyword-map.html` - the build-off-it table view. Every time `keyword-map.md` is written or updated, base run or expand.**

The markdown blocks are for reading and deciding. The HTML table is for BUILDING: one screen where someone scans down the priority order and builds pages off it without opening the map. The NO TABLES rule bans tables in markdown deliverables; this HTML file is the one sanctioned table, and it exists precisely because a table is the right shape for this job.

- **One file, `keyword-map.html`, saved next to `keyword-map.md` at the project root.** Self-contained: inline CSS, no external scripts or images. Opens in any browser.
- **The house style, exactly:** cream canvas (`#f5f4ed`) with one ivory card (`#faf9f5`, 16px radius, hairline border, soft shadow) holding the table. Primary rows sit on sand (`#eeece3`) with a serif cluster number, a coral (`#d97757`) uppercase mono label for the page type, and bold keyword. Secondary rows indent with a `↳` arrow in muted grey. Numbers right-aligned in mono. Difficulty as a small pill: green under 30, amber 30-49, red 50+, with the word (Easy/Medium/Hard) beside it. If a `keyword-map.html` already exists in the repo, copy its CSS verbatim.
- **One table, clusters in map priority order** - same order and same numbering as the markdown. Nothing here is re-sorted.
- **Each cluster is a group of rows:** the primary keyword row first (visually distinct - bold with a shaded background), its secondary keywords indented beneath it. Columns: **# · Page type and topic · Role (Hub / Spoke / Standalone, with hub or spoke numbers) · Keyword · Searches a month · Difficulty**. Primary/secondary must be obvious at a glance - that hierarchy is the whole point of the table.
- **Cover `# To build` and `# Written`** (with Written visibly marked, e.g. a muted row style and a Written tag). Skip saved-for-later entirely - it is not buildable, so it does not belong in the build view.
- **Same labelling rules as the map:** every number labelled in the header ("Searches a month", "Difficulty (out of 100)"), no abbreviations, no KD/Vol.
- **Regenerate the WHOLE file from `keyword-map.md` every time.** The markdown is the single source of truth. Never hand-edit the HTML, never patch it incrementally - stale HTML that disagrees with the map is worse than no HTML.
- **End the chat report with the clickable absolute path on its own line:** `file:///.../keyword-map.html` - so it opens in one click.

**5. Report - IN CHAT, not in the file.** The file stays tight. The reasoning goes here, in plain English, so I understand the thinking rather than just receiving a list.

Cover five things, short:

**Why these keywords.** Not "they passed the filters" - say what they have in common and why they suit THIS business. "Your site is new, so everything here is under difficulty 30. The top five are all people ready to hire rather than people researching, because you need leads before you need traffic."

**Why these are first.** Name the top 3 and give one line each on what earned that position - volume, difficulty, buyer intent, or that other pages need it to exist first.

**Why I cut what I cut, grouped by reason with counts.** Never a raw list of rejects. "23 were too competitive for a site your age - they open up as your authority grows. 8 had under 100 searches a month. 6 looked commercial in Semrush but Google actually shows guides for them, so they'd be blog posts, not money pages. 4 were services you told me you don't offer."

**What got folded in, not built.** Every keyword absorbed into an existing row as a secondary instead of becoming its own page, with the row it joined and the overlap count. These are the pages you did not build and the cannibalization you did not ship - name them, because a shorter map is the win here, not a shortfall.

**Where Semrush was wrong.** Name every keyword where the live Google result disagreed with Semrush's intent label, and what you did about it. This is usually a handful and usually the expensive ones - it's the most valuable thing in the report.

**What this map is worth, honestly.** Total monthly searches, roughly how many months of content it is at a realistic pace, and the single biggest gap you noticed. If the map is thin, say so plainly rather than dressing it up.

Then: the next command is `/service-page` or `/blog-post` on page 1. When the map runs dry, `/keyword-research expand` refills it. Last line of the report is the `file://` link to `keyword-map.html` (step 4b).
---

## EXPAND mode - industry → 10 roots → 1,000 next-of-kin keywords

**E0. ⛔ Open hubs eat first, and the standalones get re-sorted.** Two housekeeping passes before any new pull, in this order: **(a)** run step 3c's standalone sweep against the map as it stands - some open hubs get fed for free by pages already mapped, and there is no sense pulling new keywords for a hub that a standalone page already completes; **(b)** then read the map for every hub marked `Cluster: open - needs spokes` (and any hub whose spokes are all written while the hub still has uncovered subtopics). The FIRST expansion job is pulling the keyword families that fill those hubs with natural, decomposing spokes - new topics only start after every open hub has been fed or verified as genuinely narrow ("full pull done - N spokes is everything this topic decomposes into"). Depth-first is the evidence-backed order, and it is what keeps hub sections from ever being forced.

The 12-month content pipeline. Same qualification rule, same clustering - pointed wider.

**E1. Roots.** Identify ~10 ROOT keywords - the trunk topics of this industry (plumbing: water heaters, drains, leaks, toilets, pipes, pricing, emergencies, fixtures, sewer, maintenance). Confirm the roots with me before expanding - 30 seconds now saves an hour of wrong-direction expansion.

**E2. Expand each root into its next-of-kin.** Per root, the full family: cost/pricing variants, how-to, comparisons (X vs Y), problem/symptom phrasings ("why is my..."), lifespan/timing, buying guides, seasonal angles, local-intent variants. Semrush for volume/KD; target ~100 per root, ~1,000 total.

**E3. Cut ruthlessly, then cluster.** The same four cuts from step 2, in the same order - junk, wrong intent verified on Google, 100+ searches a month, difficulty under the ceiling, then drop intent-duplicates, trivia, and anything on the DON'T list from step 0c. Cluster survivors per `references/keyword-clusters.md`, cluster-vs-spoke test on borderline pairs.

**E4. Append to the map.** New blocks BELOW the existing ones in `keyword-map.md`, never reordering what's there, numbered on from the last one, quick-win sorted, hubs before spokes. Same block shape as step 4 - no exceptions. **Run the cannibalization gate (step 3b-dedupe) on every survivor before appending** - exact-primary matching alone lets near-duplicates straight in, and expand mode is where they arrive by the dozen because it pulls a root's whole family. Anything that collides is folded into the existing row as a secondary, not appended as a block. Never create a second markdown file. **Then regenerate `keyword-map.html` from the full updated map (step 4b) and end the report with its file:// link.**

**E5. Report:** pipeline size, months of content at my pace (ask if unknown), and the 10 best pages I'm not building yet with one line each on why they'd win. The pipeline is only worth what gets written - `/service-page` and `/blog-post` consume it, one page per run.
