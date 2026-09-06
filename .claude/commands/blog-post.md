---
description: One publish-ready blog post - duplicate the template page, research, write in voice
argument-hint: "[keyword, optional - pulls next from keyword-map.md]"
---

**⛔ THE HUMOUR RULE (Jono, Friday 4 September 2026). Every second sentence, minimum, is a bit. Hard rule. No exceptions in blog body copy.** The register is ONE thing and nothing else: a goofy, self-deprecating person talking straight to the reader, exactly the way the reference piece does it ([Writing Humor: The Art of Making Readers Laugh](https://www.hireawriter.us/creative/writing-humor-the-art-of-making-readers-laugh) - read its first ten paragraphs before writing a word). Open with a bit and undercut yourself in the first breath. Stage directions in brackets. The writer is the butt. Tease the reader directly. Own the corny out loud. One running bit per piece that comes back three times. NOT the clever style, NOT the wry style, NOT an analogy with a bow on it. Three straight sentences in a row in body copy means the paragraph is not finished. Straight zones stay straight: the quick answer, FAQ answers, tables, prices, proof numbers, the CTA line.

**Read first:** `references/blog-post-retention.md` (the 41 retention rules - subhead every 150-300 words, answer in the first 40-50 words, the mid-text CTA does 47-93% of the work), the humour rule above (full standup in the body; quick answers and FAQ straight - AI lifts those verbatim), and **`references/hub-spoke-pages.md` when the map row is a pillar or a spoke** - a pillar is a short router with an H2 section per spoke (passage + link inside it, section in the TOC) and it grows a section the same day any new spoke ships; a spoke takes one subtopic deep, never the pillar's head term, and references its pillar by name early.

**⛔ Before writing: check the route does not already exist.** No argument = the next unwritten `## N. Blog post:` row in `keyword-map.md`, lowest N. **But the map row is hand-maintained and drifts - the filesystem is the authority.** If `website/app/blog/<slug>/` already exists, skip it, move the row to `# Written`, say so in one line, and take the next row instead. Never overwrite an existing post: it may have been hand-edited, optimized, linked or already live, and a rebuild silently destroys all of it. All rows written? Say so and point at `/keyword-research expand`.

## Which keyword

Never ask. The ladder, top to bottom, no stopping:

1. Next unwritten `## N. Blog post:` row in `keyword-map.md`, lowest N, skipping anything in `website-index.md` or routed under `app/blog/`
2. Map empty of blog rows? Best "saved for later" keyword under difficulty 40
3. Everything taken? A fresh long-tail variant of the closest cluster

State the pick in one line and build. The ONLY stop: a keyword I typed is already written - show me it, ask update-or-new.

## ⛔ Duplicate = `cp` the file

```
cp templates/blog-post.tsx        app/blog/[slug]/page.tsx      # first ever (saved there by /build-website)
cp app/blog/[existing]/page.tsx   app/blog/[new-slug]/page.tsx  # every one after
```

No `templates/blog-post.tsx` yet? `/build-website` has not run - run it first, or copy `app/bold/blog/example-post/page.tsx` if the style folders still exist.

Edit ONLY words, images, metadata, schema. Composing a fresh page from components is designing - banned.

## The work

1. **Spec:** top 3 organic results - word count, H2 outline, tables, FAQs. Target = their average ±20%, plus THE GAPS.
2. **Research, 50+ sources:** parallel sub-agents across ranking articles, YouTube transcripts, Reddit, studies, expert quotes - and MY numbers - ask me for real results, reviews and credentials before writing, and use only what I give you. Original data is the citation lever. **`references/examples/research-dossier-example.md` is what the gathered material should look like before you write a word** - match its shape, never its content. WordPress lane: `references/examples/wordpress-blog-example.md` is the finished post.
3. **Buyer:** name the ONE person this post is for in a sentence - who they are, what they fear, what they typed into Google - and write to them.
4. **Write INTO `references/blog-post-template.md`'s skeleton** - quick answer → proof line → main table → cluster H2s → field section → FAQ → bridge CTA → author box. Write it STRAIGHT and correct first. Never a disclaimer about proof you don't have - write from what IS true.
5. **The humour rewrite - a separate, full pass, and it is the point.** **⛔ THE HUMOUR RULE (Jono, Friday 4 September 2026). Every second sentence, minimum, is a bit. Hard rule. No exceptions in blog body copy.** The register is ONE thing and nothing else: a goofy, self-deprecating person talking straight to the reader, exactly the way the reference piece does it ([Writing Humor: The Art of Making Readers Laugh](https://www.hireawriter.us/creative/writing-humor-the-art-of-making-readers-laugh) - read its first ten paragraphs before writing a word). Open with a bit and undercut yourself in the first breath. Stage directions in brackets. The writer is the butt. Tease the reader directly. Own the corny out loud. One running bit per piece that comes back three times. NOT the clever style, NOT the wry style, NOT an analogy with a bow on it. Three straight sentences in a row in body copy means the paragraph is not finished. Straight zones stay straight: the quick answer, FAQ answers, tables, prices, proof numbers, the CTA line.

    Rewrite every line against the humour rule above. The bar: **at least every second line lands a light beat, like a comedy set the whole way through** - then the useful info lands clean right after. Quick answers, FAQ, tables and numbers stay straight. This is a line-by-line rewrite, not a find-and-replace.
   - **Sweep BOTTOM-UP: last section first, intro last.** Drafts fatigue - the writing copies its own recent output, so humour starts strong and thins through the back half, and a top-down punch-up pass fatigues the exact same way. Working from the end gives the tired sections the freshest attention.
   - **The floor: every H2 section carries at least one line that would make a stranger grin.** FAQ, quick answers and the CTA are exempt. After the pass, count per section. A section with zero isn't done - a funny intro doesn't carry a dry section six.
   - **The density check: three straight sentences in a row, outside the protected zones, means the pass isn't done there.** The target is a beat every second line - mostly SMALL beats (a word choice, a half-sentence aside, a personification), with one or two big builds per section. Ten set pieces per section is exhausting; ten dry sentences is worse.
   - **Every stat carries a live external link to its source.** An attribution with no link ("per industry data", "Semrush-cited") is not a citation. If the source can't be found and linked, the stat doesn't ship - swap it for one that verifies. Degrade, never decorate.
6. **Images:** hero + one visual per ~350 words. Ladder: real → `code/fetch_stock_photos.py` (overfetch: pool 2-3x the slots, pick the best per slot, never a photo already used on the site) → none. Look at each. **People photos go where people belong:** body images show the work, the tools, the result - not stock faces. A face appears only in the author box (the real author) or beside a real quoted person, never as decoration.
7. **On-page while writing:** `references/on-page-seo.md`; 2-3 title/meta variants per `references/meta-info.md`.

## Gates, then register

```
python3 code/check_page_rhythm.py /blog/[slug]
python3 code/check_page_done.py /blog/[slug]
```

**The loop rule: the gate decides when you're done, not you.** Run the gate → fix every failure → run it again. Repeat until it passes. Do not report progress instead of finishing, do not ask permission to keep fixing, do not stop because a fix is tedious (37 routes to build means 37 routes get built), and never present a failing site with an explanation attached. The ONLY reasons to stop early: you need a value only I have (a key, a webhook, a photo), or a real decision is mine to make. Everything else, you finish.

Fix and re-run until both pass - never show a failing draft with an explanation, and never declare a score. Then screenshot at 1440px and 390px and LOOK at both - no horizontal overflow, no table spilling off a phone screen, images scaling intact. Then: save as draft, verify every internal link target exists, append to `website-index.md`, MOVE the whole map row into `# Written` in `keyword-map.md`, keeping its number - never add a `Status:` field. Publishing is `/publish`.


**Add the post to the `/blog` index.** Open `website/app/blog/page.tsx` and add one entry for the new post - title, one-line blurb, descriptive link - as its own section in date order, newest first. Never let a post exist without a link from the index, and never replace the index with an article.
