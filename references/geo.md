# Get this site cited by AI

The 38 checks that decide whether ChatGPT, Google AI Overviews, Perplexity, Claude and Gemini quote this site. Updated Tuesday 18 August 2026.
Next: read this before writing a page, then grade the page against it after.

**Two rules that govern the file.** If a check is not on this list, it does not get checked. If this file and [on-page-seo.md](on-page-seo.md) ever disagree on an AI check, this file wins and on-page-seo.md gets updated to match.

**Scoring.** 38 checks across 8 groups. Site-level checks (groups 1 and 8) pass once. Page-level checks are graded on every page.

---

## Why this list exists

About 65 percent of Google searches end with zero clicks. Brands cited inside AI answers get about 120 percent more clicks per impression, and those visitors convert better. Citation is earned in the body of the page, not the title tag.

**Local businesses: the website is now the only lever on Ask Maps.** Google killed Business Profile Q&A on 3 November 2025 and replaced it with Ask Maps, which answers a searcher's question live from the website's content, the business's reviews and its profile fields. Nobody seeds an answer any more.

Practical consequence for FAQ work: write answers as plain, complete sentences. Ask Maps extracts an answer rather than displaying a page, so a bullet fragment with no context is unusable to it. One well-written answer serves Ask Maps, AI Overviews and the page itself. FAQ seeding is specced in [gbp-setup.md](gbp-setup.md) section 11 and lands on pages via `/service-page` and `/blog-post` with FAQ schema.

---

## 1. Let the AI crawlers reach the site - 6 checks, whole site

- [ ] robots.txt explicitly ALLOWS the AI crawlers: GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot, Google-Extended - blocked crawler = invisible to that engine, full stop
- [ ] No CDN/firewall bot-blocking rules silently stopping AI crawlers (Cloudflare's AI-bot toggle is a common accidental kill switch - verify with the actual crawl logs or a user-agent fetch test)
- [ ] Pages are fast: AI engines favor fast pages - pages under 0.4 seconds First Contentful Paint average 6.7 citations against 2.1 for slow ones, roughly 3 times more. The Lighthouse loop handles this; verify it held
- [ ] Content renders WITHOUT JavaScript - most AI crawlers read raw HTML and skip JS execution; static site generation passes this by default, verify nothing critical is client-only
- [ ] `llms.txt` present at the site root - honest label: about 10 percent adoption and NO major AI lab has committed to reading it in production (crawler logs show them skipping it for HTML). It takes 10 minutes, zero downside, possible future upside - ship it, expect nothing from it
- [ ] Clean HTML structure: semantic headings, real `<table>` elements, lists as `<ul>/<ol>` - AI parses structure, not screenshots

## 2. Answer the question before explaining it - 6 checks, per page

- [ ] Every question-style H2 has a 40 to 60 word self-contained answer DIRECTLY beneath it - liftable verbatim into featured snippets, AI Overviews, and chatbot citations
- [ ] The direct answer comes BEFORE the deep explanation in every section - 44.2 percent of all LLM citations are extracted from the first 30 percent of a document
- [ ] The page's core answer appears in the first 30 percent of the page, not buried at the end
- [ ] Sentences average about 18 words - heavily-cited content is concise and declarative, not winding
- [ ] Clear H2/H3 skeleton a machine can outline - each section answers ONE question
- [ ] No fluff intros - the first 100 words state the topic and the answer

## 3. Give the model data it can lift - 6 checks, per page

- [ ] Key data lives in clean comparison/pricing/spec TABLES, not prose - structured tables earn about 25 percent more AI citations
- [ ] Statistics present and each cites its ORIGINAL source - statistical enrichment lifts citation odds about 26 percent, and sourcing lifts it about 25 percent
- [ ] At least one direct expert/customer QUOTE with attribution - quote addition is the single strongest measured lever, about a 28 percent lift
- [ ] Where the topic fits, use a numbered Top-N list format - 63 percent of all LLM citations point to listicle-style pages, and 71 to 86 percent of those are ranked lists
- [ ] FAQ block answering the real questions people ask - People Also Ask and LLMs still read FAQ content even though the SERP rich result is gone
- [ ] Units, dates, and prices written explicitly ("$180 in 2026", not "affordable recently") - vague claims can't be quoted

## 4. Mark the page up so AI can resolve it - 5 checks, per page

- [ ] Correct schema type per page (Article, LocalBusiness, Service, Person, Organization) - schema-marked pages are cited about 2.3 times more often
- [ ] Organization/LocalBusiness schema with NAP matching GBP exactly
- [ ] Author/Person schema linked to a real author page with credentials
- [ ] Schema validates clean (rich-results test) - broken markup is ignored markup
- [ ] `sameAs` links to real profiles - connects the page to the entity graph AI models resolve against

## 5. Cover the whole topic and name yourself in plain text - 4 checks, per page

- [ ] Page covers the related entities and terms the top-cited pages share - completeness, not keyword repetition
- [ ] Business name, location, and services stated in plain text on the page (not only in images/logos) - the model must be able to READ who you are
- [ ] Consistent naming everywhere - one canonical business name, not three variants
- [ ] First-person experience language where true ("we installed 400 of these") - signals first-hand experience to AI and quality raters

## 6. Publish something that exists nowhere else - 4 checks, per page

- [ ] The page contains data that exists NOWHERE else: your prices, your job counts, your before/afters from proof-inventory - original data and proprietary research are the highest-leverage content type across all platforms
- [ ] Case-study and pricing content exists on the site - these outperform generic "what is" guides for AI-referred traffic
- [ ] Real numbers replace adjectives ("since 2011", "1,400 jobs" - checkable beats impressive)
- [ ] At least one original photo/screenshot/dataset from real work per money page

## 7. Get mentioned off your own site - 4 checks, whole site, report as opportunities

- [ ] Brand mentions exist beyond your own site - mention frequency correlates about 0.664 with AI citation rates, roughly 3 times stronger than backlinks at 0.218
- [ ] Reddit presence checked: Reddit is the number 1 cited source across AI engines, cited about 40 percent of the time and about 24 percent of Perplexity citations alone - honest participation in the local/trade subreddits, never spam
- [ ] Listed in the "best [service] in [city]" roundup articles that AI answers lean on - being IN the listicles matters, since listicles are what gets cited
- [ ] Per-platform reality noted: only about 11 percent of domains cited by ChatGPT are also cited by Perplexity - winning one surface doesn't win the others; the fundamentals above are the shared core

## 8. Measure who is getting cited - 3 checks, whole site

- [ ] Monthly ask-the-models test: ask ChatGPT, Perplexity, and Google (AI mode) your top 5 money questions; log who gets cited - this is the GEO scoreboard
- [ ] AI referral traffic segmented in analytics (chatgpt.com, perplexity.ai referrers) - the conversions are real even when the volume looks small
- [ ] Re-run this checklist after major content changes - GEO is a moving surface; this file gets updated when the research does

---

## Do not bother with these

**Keyword stuffing for AI.** Models read meaning, not density.

**llms.txt as a strategy.** Ship the file, but 8 of 9 measured sites saw zero traffic change. The levers are structure, data, and mentions.

**Chasing recency for its own sake.** The median cited page is 14 months old. Substance beats freshness stunts.

**Blocking AI crawlers to "protect" content.** Invisible isn't protected, it's just invisible.

---

## Sources behind the numbers

- [Digital Applied - 1,000 AI Overviews citation-pattern study](https://www.digitalapplied.com/blog/we-analyzed-1000-ai-overviews-citation-pattern-study)
- [Attrifast - AI search ranking factors 2026, 400 million citations](https://attrifast.com/blog/ai-search-ranking-factors-2026)
- [Position Digital - 100+ AI SEO statistics 2026](https://www.position.digital/blog/ai-seo-statistics/)
- [Instant Press - AEO and GEO statistics 2026](https://www.instantpress.co/aeo-statistics)
- [Leapd - How ChatGPT, AI Overviews, and Perplexity source information](https://www.leapd.ai/blog/ai-visibility/how-chatgpt-google-ai-overviews-and-perplexity-source-information-in-2026)
- [aeo.press - The state of llms.txt in 2026](https://ai.aeo.press/the-state-of-llms-txt-in-2026)
- [Codersera - llms.txt: the honest guide](https://codersera.com/blog/llms-txt-complete-guide-2026/)
- [Digital Applied - GEO guide 2026](https://www.digitalapplied.com/blog/geo-guide-generative-engine-optimization-2026)
- [Wellows - AI Overviews ranking factors](https://wellows.com/blog/google-ai-overviews-ranking-factors/)
- [GenOptima - GEO best practices: 12 proven strategies](https://www.gen-optima.com/geo/generative-engine-optimization-best-practices/)
