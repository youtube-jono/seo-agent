# On-page SEO checklist

The 80 checks every page is written against and then graded against. Updated Wednesday 13 August 2026.
Next: read this before writing a page, then run the audit against it after.

**Two directions, one file.** Generation reads it BEFORE writing a word, so on-page SEO is applied at write time and nothing gets retrofitted. The audit reads it AFTER and grades the draft against every item. If it is not on this list, it does not get checked.

**Scoring.** 80 checks across 15 groups. A draft only ships at a clean pass, or with every remaining fail consciously waived. Fix only the failed items, smallest possible edit, body copy and voice untouched.

**How to read a check.** `- [ ]` is the item. The note after the hyphen is the plain-English why.

---

## 1. Set the head tags - 8 checks

- [ ] Title tag 50-60 characters - longer gets truncated in results
- [ ] Primary keyword sits near the front of the title - earns the click
- [ ] One title tag only, unique to this page - no duplicates across the site
- [ ] Meta description 140-160 characters, written for the click - Google rewrites it 62 to 70 percent of the time, so write it for the human, not the bot
- [ ] Primary keyword appears once in the meta description - gets bolded in results
- [ ] Canonical tag points to this page's own clean URL - prevents duplicate-content confusion
- [ ] `<meta name="viewport">` present - required for mobile rendering
- [ ] `lang` attribute and charset set on the page - basic crawl hygiene

## 2. Build the URL - 5 checks

- [ ] URL is short, lowercase, hyphen-separated - readable by humans and crawlers
- [ ] Primary keyword in the slug - the URL is part of the map
- [ ] No dates, IDs, or junk parameters in the path - keep it clean and permanent
- [ ] Folder reflects the site map (e.g. /services/water-heater-repair) - structure signals topic
- [ ] URL stays stable once published - changing it later needs a 301 redirect

## 3. Structure the headings - 5 checks

- [ ] Exactly one H1, and it contains the primary keyword - the page's single main title
- [ ] H2s map to the subtopics the top-3 winners cover - matches the shape Google rewards
- [ ] Cluster keyword variants woven into H2/H3 text naturally - covers the whole topic, not one phrase
- [ ] Heading order is logical (H1 > H2 > H3, no skipped levels) - readable structure for people and AI
- [ ] No keyword stuffing in headings - they read like a human wrote them

## 4. Place the keyword and match the intent - 5 checks

- [ ] Primary keyword in the first 100 words - confirms the topic fast
- [ ] Page format matches the SERP intent (guide vs listicle vs service page) - answer what the search actually wants
- [ ] Cluster variants appear through the body naturally - topical depth, not repetition
- [ ] No exact-match keyword stuffing - density is a non-goal, relevance is the goal
- [ ] The page answers the searcher's real question, not just contains the keyword - intent over match

## 5. Match the winners on depth, beat them on a gap - 6 checks

- [ ] Length within about 20 percent of the top-3 average for this keyword - match the proven range, do not pad
- [ ] Covers the subtopics and questions the winners cover, plus at least one they miss - match on shape, beat on a gap
- [ ] Original information gain present (your numbers, jobs, examples) - the one thing the top 3 cannot copy
- [ ] Reads in your voice, not generic AI phrasing - passes the read-out-loud test
- [ ] No fluff intros ("In today's fast-paced world...") - get to the answer
- [ ] Content is genuinely useful to a real reader - the only signal that outweighs the other 79

## 6. Prepare the images - 6 checks

- [ ] Every image has descriptive alt text under 125 characters - accessibility plus image search
- [ ] At least one original photo, screenshot, or graphic - real media beats stock
- [ ] Images compressed to WebP (AVIF via `<picture>` as progressive enhancement), aim under about 100KB each - speed is a ranking and conversion factor
- [ ] Width and height set on images - prevents layout shift (CLS)
- [ ] Descriptive file names (water-heater-anode-rod.webp, not IMG_2831.jpg) - another relevance signal
- [ ] Lazy-load below-the-fold images, but never the hero/LCP image (use `fetchpriority="high"`) - faster paint without hurting LCP

## 7. Link internally - 5 checks

- [ ] 3 to 5 internal links in the body - spreads authority and keeps readers on the site
- [ ] Anchors are descriptive, never "click here" or "read more" - the anchor text is a ranking signal
- [ ] Links point at the money pages (services, booking) - blogs feed the pages that convert
- [ ] At least one link back up to the relevant hub/pillar page - reinforces the topic cluster
- [ ] No broken internal links - dead links waste crawl budget and trust

## 8. Link out and cite sources - 4 checks

- [ ] Outbound links go to high-authority, original sources - borrows credibility
- [ ] Every stat cites the ORIGINAL source, never the article that quoted it - higher trust, better E-E-A-T
- [ ] External links open without breaking the reading flow - usability
- [ ] No links to spammy or irrelevant domains - bad neighborhoods hurt you

## 9. Control the social preview - 5 checks

- [ ] `og:title` set and compelling - controls how the link looks when shared
- [ ] `og:description` set - the share-preview blurb
- [ ] `og:image` present, 1200x630 pixels - a missing share image kills click-through on social
- [ ] `og:url` and `og:type` set - clean preview rendering
- [ ] Twitter/X card tags present - covers that platform's preview

## 10. Add the schema - 5 checks

- [ ] Correct schema type for the page (Article, LocalBusiness, Service, Product, Review) - these still earn rich results; FAQ and HowTo no longer do
- [ ] Organization or LocalBusiness schema with NAP - name, address, phone consistent everywhere
- [ ] Author/Person schema on content, linked to a real author page - resolves WHO wrote it
- [ ] Schema validates with no errors - broken markup is ignored
- [ ] sameAs links to your real profiles in schema - connects the page to your wider footprint

## 11. Write the FAQ block - 4 checks

- [ ] An FAQ block answering the real questions from the scan - feeds People Also Ask and AI answers
- [ ] FAQ questions phrased the way people actually search - matches real queries
- [ ] FAQ content stays even though FAQ rich results were removed in May 2026 - the SERP dropdown is gone, but People Also Ask and LLMs still read it
- [ ] Answers are concise and directly useful - no padding

## 12. Make the page easy for AI to extract - 6 checks, new for 2026

- [ ] Every question-style H2 has a 40 to 60 word self-contained answer directly beneath it - liftable verbatim into featured snippets, AI Overviews, and ChatGPT citations
- [ ] Answer-first structure: the direct answer comes before the deep explanation - AI quotes the top of the section
- [ ] At least about 3 comparison tables where it fits - pages with structured tables earn about 25.7 percent more AI citations
- [ ] Key data presented in clean tables, not buried in prose - AI parses tables cleanly
- [ ] Page covers the related entities and terms the winners share - topical completeness, not just your keyword
- [ ] First-person action language where true (I tested, we installed, we measured) - signals first-hand experience to AI and raters

## 13. Show first-hand proof - 6 checks

- [ ] Named author with a real bio and credentials - not "Admin" or "The Team"
- [ ] At least one original photo, screenshot, or dataset from real work - demonstrated experience
- [ ] Real numbers and specifics replace vague claims ("400 furnaces since 2011", not "experienced") - a number is checkable
- [ ] Trust signals visible (license number, insured, reviews, years) - checkable proof, not adjectives
- [ ] Links to the author page, about page, and contact page - the sibling trust pages Google looks for
- [ ] Claims are honest and verifiable - one fake testimonial poisons the whole page

## 14. Pass the technical basics - 6 checks

- [ ] Mobile-friendly and responsive - most local searches are on a phone
- [ ] Loads fast (Core Web Vitals in the green) - speed affects rank and conversion
- [ ] Served over HTTPS - baseline trust requirement
- [ ] No layout shift on load (CLS controlled) - stable, professional feel
- [ ] Page is crawlable and indexable (not blocked by robots or noindex) - if Google cannot save it, it does not exist
- [ ] In the sitemap and internally linked - discoverable, not orphaned

## 15. Keep it readable and accessible - 4 checks

- [ ] Short paragraphs and scannable formatting - people skim before they read
- [ ] Sufficient color contrast and readable font size - usable for everyone
- [ ] Descriptive link text and logical tab order - accessible navigation
- [ ] Reads at a natural, human reading level for the audience - not robotic, not over-complex

---

## Refreshing a page later

Real content refreshes (new sections, updated data, better answers) re-rank in roughly 2 to 4 weeks. Changing only the published date with no real change is explicitly debunked by Google and does nothing. Update the substance, not the timestamp.

## How the audit reports back

Group by group, score by score. For example `Head tags 8 of 8` or `Images 5 of 7, 2 missing alt text`.

Fails come back named and located, which makes the fix surgical: touch only the failed item, leave the prose and voice alone, then re-audit to confirm the checks pass AND the voice survived.
