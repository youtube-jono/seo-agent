# Search intent - how to classify a keyword

The rule that decides which page type a keyword gets. `/keyword-research` runs it on every root before a page is planned.

Next: run the 10-result count below on any keyword you are unsure about.

---

## Semrush's label is a hint. The SERP is the verdict.

Semrush, Ahrefs and every other tool guess intent from the words in the phrase. They are frequently wrong, and they are most wrong on exactly the keywords that matter - the expensive commercial ones.

**Never classify from the phrase alone. Search it and count what Google returns.** Google has already decided what this query means; the results page is that decision, published.

---

## The count - 10 results, 6 decides it (our convention, not a documented standard)

**Label this honestly whenever you cite it.** The 6-of-10 threshold has no documented source anywhere - not Ahrefs, not Grow and Convert, not Content Harmony, not Google. Every published method uses unquantified language instead. It is a good internal consistency rule because it forces a countable observation instead of a vibe. It is not best practice and must never be presented as one. See [keyword-strategy.md](keyword-strategy.md) for the evidence.

Two things the real sources say instead:

- **Google's Quality Rater Guidelines section 12.5** uses Dominant Interpretation ("what most users mean when they type the query"), Common Interpretation ("what many or some users mean") and Minor Interpretation - no proportions, and it notes plainly that not all queries have a dominant interpretation.
- **Broder's 2002 paper**, which invented the whole informational/navigational/transactional taxonomy, says outright that "there is no assumption here that this intent can be inferred with any certitude from the query."

**When you are unsure, err toward transactional.** Jansen (2008) classified 1.5 million queries at 74% accuracy, and 82% of the errors were transactional or navigational queries wrongly labelled informational. That is exactly the bias a modifier-based guess carries, so a coin-flip call should break toward the money page, not the blog post.

Search the keyword. Ignore ads for a moment. **Classify each of the top 10 organic results by what the PAGE is**, not what it is about:

- **A guide, article, how-to, listicle, forum thread, video or Q&A** counts as **informational**
- **A service page, product page, pricing page, booking page or a business homepage** counts as **transactional**
- **A comparison, "best X", review or roundup page** counts as **commercial investigation** - it sits between the two

Then apply the threshold:

- **6 or more informational** → informational. This is a blog post. A money page here will not rank.
- **6 or more transactional** → transactional. This is a service page.
- **6 or more comparison or "best of"** → commercial investigation. Route to a comparison-style page or a blog post that links hard to the money page.
- **No group reaches 6** → mixed. See below.

**Write down what you counted**, not just the verdict. "7 of 10 are cost guides and Reddit threads" is checkable. "Informational" is a guess wearing a label.

## Mixed SERPs - the 5-5 case

A split result means Google is serving two audiences and has not committed. Three rules:

- **Read what Google put FIRST.** Positions 1-3 carry far more weight than 8-10. If the top three are service pages and the tail is guides, it is transactional.
- **When it is genuinely 50-50, the money page wins the term and the blog links to it.** Never build both against the same primary - that is cannibalisation, and the rule is one primary keyword per page, always.
- **Say it is mixed in the block.** A mixed term is a page that will need watching.

## The SERP features are evidence too

- **Ads running** - strong commercial signal. Advertisers only bid where money is.
- **A map pack** - local intent specifically. This term needs a location page and a Google Business Profile, not just a page.
- **A featured snippet or People Also Ask** - informational lean, and a snippet worth stealing with an answer-first block.
- **Shopping results** - transactional but crowded by paid; organic room is thin, so say so rather than mapping a page that cannot rank.
- **Video pack** - informational, and it means the page needs video or it is competing with one hand tied.

---

## Words are a hint, never the answer

Useful for a first guess before the search, never a substitute for it.

**Usually informational**
- how · why · what is · when · guide · tutorial · ideas · examples · DIY · yourself
- cost · price · how much (**verify these** - they are the most misread words in SEO, and they split by industry)

**Usually transactional**
- services · company · agency · consultant · firm · contractor
- near me · in [city] · [city] [service]
- hire · book · quote · emergency · same day · 24 hour

**Usually commercial investigation**
- best · top · review · vs · versus · alternative · comparison · cheapest

**The `[service] for [audience]` trap.** "SEO for contractors", "bookkeeping for restaurants", "marketing for dentists". The audience is correct, which is why it feels like a buyer term, but that phrasing is how a GUIDE gets titled. Results fill with how-to content and the searchers are mostly people who intend to do it themselves. Always count this one.

---

## What each verdict means for the build

**Informational** → a blog post. Its job is traffic, trust and a link down to the money page. It never tries to sell in the first screen.

**Commercial investigation** → a comparison page or a blog post built to convert, with the money page linked from every section. These are the highest-value blog posts you can write.

**Transactional** → a service page. This is where proof, the form and the call button live.

**Navigational** (someone searching a brand name) → nothing to build unless it is your own brand. Someone else's brand name is a cut, not an opportunity.

---

## Two rules that override the count

**The root must be the highest-volume term that ALSO passes the intent check.** Both, not either. A 3,600/mo informational term is worth less to a service page than a 1,000/mo transactional one, because ranking first for a guide earns readers and ranking first for a service term earns calls.

**Losing terms get routed, never deleted.** An informational term that lost a service-page slot is a genuinely good blog post that links to that page. High-volume informational keywords are the top of the funnel, not junk.
