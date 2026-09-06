# Keyword strategy - how keywords get chosen, clustered and mapped

Built August 2026 · the evidence layer behind `/keyword-research`, `keyword-clusters.md` and `search-intent.md`.
Next: before your next map, pull the site's current top-10 rankings from Search Console and use that as the difficulty baseline instead of a generic ceiling.

**[E]** = backed by a published study with a stated sample and method. **[C]** = practitioner convention, widely used, never measured.

---

## The metrics and how much to trust them

**Read Keyword Difficulty as "how many links do the top 10 have", not "can I rank". [E]**
Ahrefs computes KD purely from referring domains to the top 10, and Semrush's own published weights are 41.22% median referring domains plus 16.99% median Authority Score, so roughly 58% of the score is a link count.
https://ahrefs.com/blog/keyword-difficulty/ · https://www.semrush.com/blog/most-accurate-keyword-difficulty/

**Never carry a KD number across tools. [E]**
The keyword "disposable face mask" scores anywhere from 46 to 72 depending on the tool, because the formulas share a 0-100 scale and nothing else.
https://ahrefs.com/blog/keyword-difficulty/

**Treat search volume as an order-of-magnitude sorting signal, never a traffic forecast. [E]**
Across 101,897 keywords carrying Keyword Planner figures only 1,462 distinct values existed (about 70 keywords sharing every value), median calibrated volume was 0.51x the reported number, and Ahrefs' own accuracy against Search Console impressions is 60%.
https://www.theia-digital.co/research/keyword-search-volume-accuracy · https://help.ahrefs.com/en/articles/72571-how-accurate-is-keyword-search-volume-in-ahrefs

**Estimate page traffic from what the current #1 page earns, not from one keyword. [E]**
The average #1 page also ranks in the top 10 for nearly 1,000 other keywords, median about 400, which is why traffic-potential style metrics beat single-keyword volume.
https://ahrefs.com/blog/also-rank-for-study/

**For local terms, ignore volume ordering entirely and rank by revenue per job. [C]**
City-level demand sits in exactly the range where bucketing destroys the signal (genuinely different demand all reported as 0, 10 or 20), so build the full services-by-cities grid and let volume only break ties.

---

## Clustering by SERP overlap

**Cluster by SERP overlap, not word similarity - it is the only method using Google's own judgment as the answer key. [E]**
A head-to-head of 17 tools on the same 216-keyword set scored SERP-based tools 70-89 out of 100 on cluster quality versus 33-47 for semantic tools and 11-35 for string matching.
https://www.keywordinsights.ai/blog/keyword-clustering-tools/

**Use 4 shared URLs in the top 10 (40%) as the default same-page threshold. [C]**
Oncrawl recommends 4 to 6 and calls 2-3 "too inclusive", Keyword Insights ships 40%, SE Ranking exposes a 1-9 slider, and Semrush hides its threshold - so the number is a vendor default, not a finding.
https://www.oncrawl.com/on-page-seo/keyword-clustering-using-python-serp-api/

**Flag any pair sitting exactly at the threshold for manual review instead of auto-deciding it. [E]**
The same query checked repeatedly from the same location returns different results with no underlying change, and 1-3 position moves are constant background noise, so a borderline pair built on one snapshot is a coin flip.
https://nightwatch.io/blog/serp-volatility-tracking/

**Use hard clustering (every keyword shares URLs with every other) for one-page-or-two decisions, soft only for exploratory topic maps. [E]**
Hard produces fewer, tighter clusters and far more ungrouped leftovers, which is exactly what you want when the output is a page.
https://seranking.com/blog/keyword-clustering/

**Never let embeddings make the final call - they are intent-blind. [E]**
Pure semantic clustering groups "how to roast coffee" with "buy roasted coffee" because they read alike, even though Google returns entirely different result sets.
https://contentgecko.io/kb/keyword-research/semantic-vs-serp-clustering/

**Split when the SERPs diverge, the required format differs, or the ranking pages have different authority profiles. [E]**
Ahrefs' chocolate cake example splits because pure recipe SERPs averaged DR 74 with 318 referring domains while the coffee-flavoured variant averaged DR 33 with 11 - same words, different competitive game.
https://ahrefs.com/blog/keyword-clustering/

**Re-cluster annually and immediately after any core update. [E]**
Surfer tracked 37,000 keywords over 15 months: 15.7% cumulative intent change, 10.5-13.3% per core update, but 39-51% of those changes later reverted, so knee-jerk rewrites are as risky as ignoring the shift.
https://surferseo.com/blog/search-intent-case-study/

---

## Choosing the primary and its secondaries

**Pick the primary by traffic to the winning page, not by the raw volume of the term. [E]**
Ahrefs' Parent Topic takes the #1-ranking page for a keyword and identifies the query sending it the most traffic - a volume-weighted-by-outcome choice, not a volume lookup.
https://help.ahrefs.com/en/articles/13040767-what-is-parent-topic-and-how-to-use-it

**When volume and intent conflict, intent wins. [C]**
A high-volume term whose SERP has a different shape belongs on its own page; naming a cluster after its highest-volume member is a labelling convenience, not an intent judgment.
https://ahrefs.com/blog/secondary-keywords/

**Cap explicit secondary optimisation at 3-5 terms and spend the rest on subtopic coverage. [C]**
Ahrefs' guidance is 3-5 with the caveat "don't count keywords, focus on topic coverage" - the long tail arrives on its own once the topic is genuinely covered.
https://ahrefs.com/blog/secondary-keywords/

**Map 3-15 keywords per cluster; under 3 means you over-split, over 15 means two intents got fused. [C]**
Fewer than three means Google already treats the queries as identical; more than fifteen signals distinct intents that need separating.
https://nightwatch.io/blog/keyword-clustering/

---

## Hub and spoke, and the internal links that make it work

**Aim for 10-40 internal links pointing INTO each important page. [E]**
Across 23 million internal links on 1,800 sites, URLs receiving 40-44 internal links averaged about 4x the clicks of URLs receiving 0-4, and the relationship inverts past roughly 45-50.
https://zyppy.com/seo/internal-links/study/

**Vary the anchor text every time, but include at least one exact-match anchor. [E]**
Anchor-text variety was the strongest signal in that dataset and kept climbing with no visible ceiling, while pages with at least one exact-match internal anchor got roughly 5x more traffic than pages without.
https://zyppy.com/seo/internal-links/study/

**Never link twice to the same spoke from one page expecting both anchors to count. [E]**
Controlled Search Console tests found Google registers at most the first text link plus the first image link and ignores the rest.
https://zyppy.com/seo/selective-link-priority/

**Put cluster links in body copy, high on the page, not in nav or a related-posts footer stub. [E]**
Sitewide nav links only performed on large high-authority sites, and the reasonable-surfer model ranks editorial in-content links above nav above footer.
https://ahrefs.com/blog/internal-links-for-seo/

**Never ship a spoke with zero inbound internal links. [E]**
66.2% of web pages have only one internal link pointing at them, and pages with none receive no PageRank flow and are crawled rarely or never.
https://ahrefs.com/blog/internal-links-for-seo/

**Do not restructure URLs to build a cluster - linking is the mechanism, folders are not. [E]**
Google's position is that folder structure will not make or break SEO and subdomains and subdirectories are essentially equivalent for search quality.
https://medium.com/predict/googles-john-mueller-says-your-url-folder-structure-won-t-make-or-break-your-seo-d45c512be555

**Give the hub its own head term and its own job. [C]**
A pillar that is only a link list has nothing to rank for and nothing for a passage retriever to cite; the link architecture only redistributes what the content earns.
https://www.conductor.com/academy/topic-clusters/

**Write each spoke section as a self-contained 130-170 word answerable passage. [E]**
AI Mode fans one query into roughly 8-15 sub-queries and retrieves chunked passages evaluated independently, so a tight passage beats a 3,000-word article with no clean boundaries.
https://nogood.io/blog/query-fan-out-guide/

---

## What changed with AI Overviews

**Weight the map toward transactional and local terms - for a local service business this is a directive, not a nuance. [E]**
Seer tracked 3,119 terms and 25.1M impressions and found organic CTR on AI Overview queries fell from 1.76% to 0.61% (a 61% drop), concentrated on informational and educational queries, while AI Overviews rarely trigger on transactional local queries because a summary does not help someone ready to hire.
https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-september-2025-update

**Treat informational posts as top-of-funnel and internal-linking fuel, not traffic plays. [E]**
Ahrefs measured a 58% CTR reduction for the top result when an AI Overview is present, up from 34.5% eight months earlier, so the penalty is deepening rather than stabilising.
https://ahrefs.com/blog/ai-overviews-reduce-clicks/

---

## What actually predicts a new site ranking

**Check the age of the current top 10 before choosing a keyword - it is a harder signal than KD. [E]**
Across 1.3 million US keywords, 72.9% of top-10 pages are over 3 years old, only 13.7% are under a year, and the average page at position 1 is 5 years old.
https://www.tryanalyze.ai/blog/how-long-does-it-take-to-rank-in-google-and-how-old-are-top-ranking-pages

**Choose keywords close to topics the site already ranks for. [E]**
Graphite scored 332 URLs across 12 domains on similarity to existing coverage and found 35-40% of high-proximity pages earned a first click within three weeks versus about 20% of low-proximity pages.
https://graphite.io/five-percent/topical-authority-white-paper

**Look for a visibly weak entrant in the live SERP as the real go/no-go. [C]**
A low-authority competitor already ranking, outdated content or thin pages in the top 10, plus intent match, is the check that survives when the score is unreliable - and the tool vendors themselves endorse it over their own metric.
https://ahrefs.com/blog/keyword-difficulty/

**For local pack visibility, keyword choice barely matters. [E]**
Whitespark's 2026 survey of 47 practitioners scoring 187 factors put primary GBP category, proximity to searcher, keywords in the business title, address in the search city and being open at search time as the top five - none affected by which keyword a page targets.
https://whitespark.ca/local-search-ranking-factors/

**For local organic below the map, build one dedicated page per service with the geo term in the title tag. [E]**
The top local organic factors in the same survey were dedicated page per service, geographic keyword relevance, quality inbound links and keywords in the landing page title tag.
https://whitespark.ca/local-search-ranking-factors/

---

## Myths

**Myth: there is a canonical "3 shared URLs" clustering standard with research behind it.**
No published study establishes any threshold. SE Ranking exposes 1-9, LowFruits hard-codes 40%, Oncrawl recommends 4-6, Semrush hides it entirely. Anyone citing a number as "the standard" is citing a tool default.

**Myth: "6 of 10 results decides intent" is a documented method.**
Ahrefs, Grow and Convert, Content Harmony and Google's Quality Rater Guidelines all use qualitative language only ("dominant", "most"). It is a fine internal convention. It must never be cited as best practice.

**Myth: every keyword has one intent.**
Google instructs its own raters that "many queries do not fit neatly into one and only one of these categories" and gives [walmart] as simultaneously Visit-in-person, Website and Know. Jansen 2008 measured that only 70-80% of queries classify cleanly.

**Myth: there are four types of search intent and it comes from research.**
Broder (2002) defined three - navigational, informational, transactional. "Commercial investigation" is an SEO-industry addition with no academic origin. Google's own taxonomy is a different four: Know, Do, Website, Visit-in-person.

**Myth: Semrush and Ahrefs intent labels are interchangeable.**
Ahrefs derives intent from SERP results only. Semrush's documented method mixes SERP features, lexical modifiers in the keyword string, and a branded flag - so it inherits the modifier-based error modes Jansen measured at 26%.

**Myth: "target keywords with KD below your DA."**
No study exists. The two numbers come from different vendors on different bases, so the comparison is arithmetic theatre. Keep it as a guardrail, never as a law.

**Myth: Domain Authority is a Google ranking factor.**
Explicitly denied by Illyes and Mueller. Google has internal site-level signals, but they are not the Moz, Ahrefs or Semrush scores.

**Myth: Search Console shows you true search volume.**
It shows impressions for your site, not searches for a query, and only for terms you already rank for. Best available reality check, not ground truth.

**Myth: zero-volume keywords convert better, here's a case study.**
Every widely-cited example is agency content with no methodology or control. The only measured test found 11.3 impressions per keyword on average. The two real exceptions are brand-new trending topics and high-value commercial queries.

**Myth: keyword cannibalisation is a ranking penalty.**
John Mueller: "If you have 3 different pages appearing in the same search result, that doesn't seem problematic to me." The term hides the real defects - near-duplicate pages, thin content, weak internal linking. Diagnose those.

**Myth: one page should target exactly one keyword.**
The median #1 page ranks in the top 10 for around 400 keywords. Single-keyword targeting under-uses a page and produces the thin near-duplicates it was meant to prevent.

**Myth: 20-30 spokes is the optimal cluster size.**
It is a HubSpot scope heuristic for judging whether a topic is pillar-sized. No study establishes an optimal spoke count.

**Myth: topical authority is a Google ranking factor.**
Google has never published a score, and no vendor metric measures it. What the evidence supports is narrower: strong existing coverage makes new pages visible faster.

**Myth: "bidirectional linking increases AI citation probability by 2.7x" and similar 2026 stats.**
Precise-sounding AI-citation numbers circulate with no reproducible methodology and heavy cross-citation between AI-written blogs. The directional claim is fine. The numbers must not be quoted.
