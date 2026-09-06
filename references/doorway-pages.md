# Doorway pages: what they actually are, and the gate that stops you building them

Read this before building any set of pages that share a template - city pages above all. `/service-page` rule 4 enforces what is on this page.

Researched 2026-08-24 across 74+ sources: Google's spam policies and their full Wayback history, the Search Quality Rater Guidelines, Google patents, the 1997 and 2007 near-duplicate detection papers, documented penalty cases, and the local-SEO authorities (Sterling Sky, Whitespark, BrightLocal). Every number below is labelled with its provenance. Where the industry repeats a figure with no source, that is stated instead of repeated.

---

## 1. The three things everybody gets wrong

**Myth 1: "Google says city pages are doorway pages."** It said that until March 2015, then deleted the sentence. The pre-2015 policy listed *"Multiple pages on your site with similar content designed to rank for specific queries like city or state names"* as a doorway example. The March 16 2015 rewrite **removed that bullet entirely** and changed the surviving one to *"Having multiple domain names or pages targeted at specific regions or cities **that funnel users to one page**."*

**The funnel became the test, not the city targeting.** Anyone quoting "Google says city pages are doorways" is quoting a definition Google retired over a decade ago.

**Myth 2: the famous Mueller quote.** This line is attributed to John Mueller across dozens of SEO sites:

> *"You can't swap out the city name or a few pictures and then call it good..."*

**No primary source exists.** Every trail leads to SEO blogs quoting each other. It reads like a blogger's paraphrase promoted to a quotation. Do not cite it. (The advice is fine. The attribution is fabricated.)

**Myth 3: "80% similar is the duplicate threshold."** Folklore, most plausibly leaked from article-spinner software configured to output text "at least 80% unique." Mueller, September 2022, asked directly for a duplicate-content percentage: *"There is no number (also how do you measure it anyway?)"*

---

## 2. What Google actually says

**Doorway abuse** (current wording, unchanged since 2015):

> Doorway abuse is when sites or pages are created to rank for specific, similar search queries. They lead users to intermediate pages that are not as useful as the final destination.
> - Having multiple domain names or pages targeted at specific regions or cities **that funnel users to one page**
> - Creating substantially similar pages that are closer to search results than a clearly defined, browseable hierarchy

**Scaled content abuse** is a *separate* policy with a *different* test (added March 5 2024):

> Scaled content abuse is when many pages are generated for the primary purpose of manipulating search rankings and not helping users... large amounts of unoriginal content that provides little to no value to users, **no matter how it's created**.

**They are different failures and a page set can fail either, both, or neither:**

| | Doorway abuse | Scaled content abuse |
|---|---|---|
| The test | Do the pages **funnel** users to one destination more useful than the pages? | Are **many** pages **unoriginal** and low-value? |
| Volume needed | No - two pages can qualify | Yes, "many pages" is definitional |
| Uniqueness the issue? | No. Unique pages can still be doorways | Yes, that is the whole test |
| Cares how it was made? | Silent | No - "no matter how it's created", so hand-written counts |

300 city pages with genuinely distinct local content that all push to one central contact form: **doorway**. 300 city pages with a swapped token and identical boilerplate: **scaled content**. Both at once is common.

**What Googlers have actually said** (verified statements only):

- **Physical locations are fine.** Mueller, June 2021, asked about 500 landing pages for 500 physical shops: *"No, that would be essentially fine... These are unique locations."*
- **The funnel is the offence.** Mueller, October 2021: *"we would call things doorway pages if they essentially lead to the same funnel afterwards."*
- **Intent decides the ambiguous cases.** Gary Illyes, Google's own *Search Off the Record* podcast, January 2022: *"if you have a site for every single state in the US, because you have shops in all those states, then technically, that's a doorway page. But does it violate our guidelines? I don't know. It depends on other factors, like are you trying to manipulate the search results or not?"*
- **The operational test, and the best single line on this topic.** Mueller, r/TechSEO AMA, March 2018: *"If you don't have unique information to add to a page other than a city-name, then I'd fold those pages together and instead make a single (or few) really strong pages instead."*
- **The warning.** Mueller, December 2019, on a plan for ~1,300 [keyword + city] pages: *"That sounds like doorway pages, not something I'd recommend."*

**The Quality Rater Guidelines** are stricter than the public policy and use templating as their recurring example of the **Lowest** rating: *"each page is created automatically by filling in a template"*, *"substituting different product names into a generic template"*. Swap "product" for "city" and it is the same mechanism. The QRG also adds a comparative test the public policy omits - value *"compared to other similar pages on the web on the same topic"* - and tells raters to judge **the website** after sampling **several pages**. That is how a page-level problem becomes a site-level signal.

---

## 3. The real risk is economic, not a penalty

Be honest about this, because overstating it destroys trust and understating it builds junk.

**Confirmed doorway penalties are rare, old, and mostly involved cloaking rather than plain duplicate city pages.** BMW.de and Ricoh.de (2006) were JavaScript redirect cloaking. Joy Hawkins - among the most credible local SEO practitioners alive - said of penalties for city landing pages: *"I have never actually seen a site get penalized for this."*

**What actually happens is that the pages never get indexed:**

| Evidence | Number |
|---|---|
| Programmatic ZIP/city site, 33,620 templated pages (practitioner, real GSC data) | **~18% indexed.** ~18,000 "Crawled - currently not indexed", ~8,500 "Discovered", ~700 soft 404s |
| Same site, after hand-writing 80-120 words of genuinely region-specific content for the top 15 states | **Indexation +15% over six weeks** |
| Doorway set, 140,000-160,000 programmatic pages (Glenn Gabe case study, Dec 2024 spam update) | Only ~18K ranking in the top 100 - a **12% ranking rate before the update even hit** |
| All pages, everywhere (Ahrefs, ~14bn page index) | 96.55% get zero Google traffic |

**The tail risk is real but small:** a UK home-services company with ~3,000 location pages took a *"Thin content with little or no added value"* manual action in April 2023 - and doorways are enforced under that label, since **there is no manual action called "doorway"**. That case has **no documented recovery**; it goes dark. Algorithmic suppression has no reconsideration path at all, and Google's own guidance is that recovery takes *"many months"*.

**So the argument to make is: near-duplicate city pages mostly don't get indexed, they drag site-wide quality signals when they dominate URL count, they are first to go in spam sweeps, and there is a small tail risk of a domain-wide manual action nobody has documented recovering from.** Not "you will get penalised."

---

## 4. ⛔ The pre-build gate

**Run this BEFORE writing a single word.** Catching a clone after it is built means the research, the optimization and the linking were all spent on a page that gets held.

### 4a. Local material - need 3 of these 4 per city

Sourced from Sterling Sky, Whitespark and BrightLocal. Each is a yes/no with real evidence from the owner:

1. **A real job done in or near that city** - what it was, what it cost, what went wrong. With photos if they exist.
2. **Real local specifics** - at least 2-3 named neighbourhoods, landmarks, or city nicknames, plus any local condition that genuinely differs: climate quirk, building codes, permit rules, housing stock, the problem that city actually has.
3. **A city-specific FAQ answer** - a *different answer*, not the same answer with the city name inserted.
4. **A real person from there** - a review or testimonial from a customer in that city, or a staff member who lives/works there.

**3 or more: build it. Fewer: `Status = Held`, one line saying which of the four is missing, and it never enters the build.** The fix belongs to the owner - a job, a photo, a review from that city - so report held cities as a group with what each one needs.

### 4b. The sibling test

For every pair of city pages under one service, **name in one sentence what will be genuinely different about each, beyond the place name.** If you cannot, they are one page and only one gets built.

**Localize the PROBLEM, not the place.** Inserting "in Burlington" into every heading is the failure mode. Different housing stock, different permit rules, different weather damage, different price bands - that is a different page. Same page with a different label is not.

### 4c. Volume cap

**Whitespark's guidance: 10-15 city pages maximum.** *"Any more can be excessive."* Service area shouldn't extend past ~2 hours' drive from base, and areas shouldn't overlap. If the map asks for 60 cities, the map is wrong - say so rather than complying.

### 4d. Structural red flags - any one is a fail

- The page is reachable only from a store-locator or JavaScript-loaded list
- The page is orphaned: not in the nav, not in an "Areas we serve" section, not in the HTML or XML sitemap
- A footer block stuffed with city or ZIP names
- Every city page pushes to one central contact form and nothing else - **this is the literal doorway definition, and it is the one that bites**

---

## 5. Measuring it - the similarity checker

`code/check_page_similarity.py` implements this. The method matters more than the threshold.

**Strip boilerplate first, or every measurement is garbage.** On a templated site the nav, footer and shared sections can be 70% of the tokens, so every page looks like a near-duplicate of every other. Two passes:

1. **Main content extraction** with `trafilatura` - best performer in the 2023 ACM SIGIR comparison of extraction algorithms.
2. **Document-frequency filter** - build 5-word shingles for every page in the set, then drop any shingle appearing on **more than 30% of pages**. This converts a useless "all my pages are 95% similar" into a signal that actually discriminates, and it is the single highest-leverage step in the pipeline.

**Then measure containment, not just Jaccard.** A template clone is not "resembling" the master - it is *contained* in it. Containment catches "master page plus 40 words of city fluff" that Jaccard softens.

```
Jaccard    r(A,B) = |S(A) ∩ S(B)| / |S(A) ∪ S(B)|
Containment c(A,B) = |S(A) ∩ S(B)| / |S(A)|
```

**Thresholds, with provenance stated honestly:**

| Measure | Threshold | Where it comes from |
|---|---|---|
| Jaccard on shingles | **≥ 0.50 = near-duplicate** | Broder et al., *Syntactic Clustering of the Web*, WWW 1997 - shipped at AltaVista web-scale |
| Containment | **≥ 0.80 = template clone** even if Jaccard looks acceptable | Derived; the right measure for templated sets |
| Jaccard | ≥ 0.85 = duplicate, consolidate | Convention |
| Unique shingles after boilerplate removal | **the most actionable number the tool produces** | "How many distinct 5-word phrases does this page own." A page with 12 is a doorway page regardless of word count |
| 64-bit SimHash, Hamming ≤ 3 | web-scale near-dup | Manku/Jain/Das Sarma, Google, WWW 2007 - a *fingerprint distance*, not a content percentage. Anyone converting it to "97% similar" is misusing it |

**On uniqueness percentage:** the only figure from a named authority is **BrightLocal's 40-60% unique per location page**. Treat it as guidance, not as a Google rule - Google has published no number.

**⛔ Never use a word-count minimum.** Mueller, explicitly: word count is not a ranking factor and not a sign of thin content. The 300/500/800-word figures circulating are blog folklore. Use unique-shingle count instead - it measures the thing word count is a bad proxy for.

---

## 6. Reading Google's verdict instead of guessing

The argument settles empirically. **Search Console's URL Inspection API** returns per URL:

- `googleCanonical` vs `userCanonical` - if `/plumber-austin` self-canonicalizes but Google's chosen canonical is `/plumber-dallas`, **Google has clustered your whole city set as one document** and every other page is out of the index contributing nothing
- `coverageState` - "Crawled - currently not indexed" means Google fetched it, read it, and declined: a quality judgment. "Discovered - currently not indexed" means it hasn't even spent the crawl: a trust/pattern judgment.

Quota: 2,000 URLs/day per property, 600/minute. Join that against the similarity matrix and you get the table that ends the debate: *page → googleCanonical → coverageState → containment vs that canonical → unique shingles.*

---

## 7. Which fix, when

| Situation | Fix | Why |
|---|---|---|
| Near-identical pages, same query, no real differentiation | **Consolidate: 301 the clones into one strong page** | Doorway territory. Canonical or noindex leaves the crawl waste and the pattern intact |
| Real distinct locations, but templated copy | **Rewrite the body. Don't touch tags.** Target unique-shingle count | The pages deserve to exist; they have nothing unique in them. Canonicalizing them away destroys legitimate local pages |
| True technical duplicates (parameters, print views, trailing slash) | **rel=canonical** | The documented use case |
| Needed for users (paid landing pages) but zero organic value | **noindex, follow** | Keeps them live, out of the index. Never canonical these to an unrelated page |
| Google chose a different canonical and you disagree | **Differentiate the content, then realign every signal** | No amount of tag-fiddling beats "the page is genuinely a duplicate" |

**Anti-patterns, all documented errors:**
- `robots.txt` never works for canonicalization - blocking a duplicate means Google can't see the canonical tag and may index the URL anyway
- Never combine `noindex` with `rel=canonical` pointing elsewhere - Google may propagate the noindex to the target
- Don't 301 fifty city pages into one and expect rankings to merge. They won't. Consolidation is pruning, not stacking

---

## 8. One thing city pages do NOT do

**They do not get you into the map pack.** Sterling Sky's controlled test on the GBP service-area setting: *"the ranking is based on the address at which the business verified the listing. The only impact that the service area has is visual."* BrightLocal agrees - service area pages *"can potentially increase your visibility in organic results beneath that local pack."*

**The one exception is real and worth knowing:** the page your GBP *links to* does affect that profile's rankings. Sterling Sky moved a Staten Island GBP from a Queens-optimised homepage to a Staten Island page and saw *"dramatic ranking increases within the month."* Their rule: if the city page your GBP links to isn't ranking organically in that area for your money keyword, fix that page before anything else.

So: build city pages for organic capture and conversion. Never sell them as a map-pack lever.

---

## Sources

Google primary: [spam policies](https://developers.google.com/search/docs/essentials/spam-policies) · [the 2015 doorway update](https://developers.google.com/search/blog/2015/03/an-update-on-doorway-pages) · [March 2024 spam policies](https://developers.google.com/search/blog/2024/03/core-update-spam-policies) · [helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) · [gen-AI content](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content) · [canonicalization](https://developers.google.com/search/docs/crawling-indexing/canonicalization) · [page indexing statuses](https://support.google.com/webmasters/answer/7440203) · [manual actions](https://support.google.com/webmasters/answer/9044175) · [URL Inspection API](https://developers.google.com/search/blog/2022/01/url-inspection-api) · Search Quality Rater Guidelines §4.6.5-4.6.6 · Wayback captures of the doorway policy 2014-2026

Research: [Broder, Syntactic Clustering of the Web, WWW 1997](https://www.ambuehler.ethz.ch/CDstore/www6/Technical/Paper205/Paper205.html) · [Manku et al., Detecting Near-Duplicates for Web Crawling, Google, WWW 2007](https://research.google.com/pubs/archive/33026.pdf) · [Bevendorff et al., content extraction comparison, ACM SIGIR 2023](https://dl.acm.org/doi/pdf/10.1145/3539618.3591920)

Local SEO authorities: [Sterling Sky on service area pages](https://www.sterlingsky.ca/how-to-create-unique-and-helpful-service-area-pages-for-local-businesses/) · [Sterling Sky on GBP landing pages](https://www.sterlingsky.ca/google-business-profile-landing-pages/) · [Sterling Sky on the service-area setting](https://www.sterlingsky.ca/does-the-service-area-in-google-my-business-impact-ranking/) · [Whitespark on ranking a SAB with city pages](https://whitespark.ca/blog/rank-in-cities-with-no-physical-address/) · [Whitespark's service area landing page guide](https://whitespark.ca/guides/guide-to-the-perfect-service-area-landing-page/) · [BrightLocal on location pages](https://www.brightlocal.com/learn/location-pages/)

Cases and data: [Glenn Gabe, December 2024 spam update case studies](https://www.gsqi.com/marketing-blog/google-december-2024-spam-update-case-studies/) · [Mueller on city landing pages, and Joy Hawkins' response](https://www.seroundtable.com/google-city-landing-pages-doorway-pages-28670.html) · [UK manual action thread](https://localsearchforum.com/threads/google-manual-penalty-thin-content.60128/) · [33,620-page indexation report](https://dev.to/gaspricecheck/templating-got-me-to-33620-pages-indexing-them-was-the-hard-part-kem) · [Ahrefs, 96.55% of pages get no traffic](https://ahrefs.com/blog/search-traffic-study/) · [Mueller on duplicate-content percentages](https://www.searchenginejournal.com/google-on-percentage-that-represents-duplicate-content/465885/) · [Mueller on word count](https://www.seroundtable.com/google-word-count-34092.html)
