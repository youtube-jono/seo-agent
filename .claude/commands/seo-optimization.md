---
description: Fix a page - on-page + technical + images + speed, smallest edits, voice untouched
argument-hint: "[page path or url] [focus: meta | headings | keywords | content | images | links | schema | faq | ai-layer | proof | speed]"
---

Fix the page: $ARGUMENTS (ask if not given).

**Focus mode:** if a subpoint is named (`/seo-optimization /services images`, `/seo-optimization speed`), run ONLY that slice - the matching category (or categories) from `references/on-page-seo.md`, or just the Lighthouse pass for `speed` - at full depth with the same loop-to-perfect standard. No focus = the full pass below.

## ⛔ THE COPY RULE

**This command does not rewrite copy.** Same rule as `/audit`, and it is the reason this command is safe to run on a page the owner is proud of.

**MAY change:** title tags, meta descriptions, alt text, heading TAGS (the tag, not the words), schema, canonicals, internal link anchors, image formats and file names, URL slugs, genuinely broken markup. Inserting a missing keyword into a heading or opening paragraph is allowed only where it fits the sentence that is already there.

**MAY change, PERFORMANCE - this is explicit because Pass 3 cannot work without it.** How assets LOAD is mechanical, not authorial, and it is the only lever that moves a Lighthouse performance score:
- **Font loading** - inline the `@font-face` rules (snapshot them into `app/fonts.css` and read them into the `<head>`) instead of a render-blocking `<link>` to fonts.googleapis.com. On this template that single change is usually the whole gap between 93 and 98, because it is what holds First Contentful Paint at ~2.5s.
- **Scripts** - add `defer`, `async`, `next/script` strategies, or a facade. **Swapping HOW a script loads is not deleting it** - the deletion rule bans removing it, never moving it.
- **Images** - preload the LCP image, `fetchpriority="high"` on the hero, lazy-load below the fold, width/height to stop layout shift.
- **CSS** - inline critical CSS, drop unused stylesheet requests.
- **Missing assets** - a 404 on `/favicon.ico` or any referenced file is broken markup: add the file. Console errors cap Best Practices and are always worth fixing.
- **`app/layout.tsx` and build config are in scope for these changes ONLY.** Never for copy, structure or design.

**⛔ Performance did not improve = say WHY, in the report.** Never report a flat score with no explanation. Either you were blocked (name the rule and what it would take), the remaining gap is measurement noise (say so, with the three run values), or the page is genuinely at its ceiling (say which metric caps it).

**MAY NOT change:** any body sentence, for any reason - not flow, not clarity, not readability, not keyword density. Not the stories, jokes, asides, opinions or turns of phrase. Not the order of an argument. Never because it "reads better" your way.

**The test before every edit: mechanical SEO problem, or me writing?** If it's the second, stop. A page that genuinely needs new content routes to `/blog-post` or `/service-page`, where the voice files load and I approve the draft.

If a sentence truly must change, make the smallest possible insertion, keep every other word, and show me before/after so I can veto it. Report the count of body sentences altered at the end - zero is the expected answer.

## ⛔ THE DELETION RULE

**You delete nothing.** No images, videos, embeds, sections, paragraphs, pages, plugins or scripts - not even a thin page, an orphan, or a 4MB hero image. Every one of those has a fix that isn't deletion: compress and convert the image, lazy-load the video, defer the script, improve or canonicalize the thin page, link to the orphan.

**This rule is about REMOVING things from the page, never about how they load.** Replacing a render-blocking font `<link>` with the same fonts inlined, deferring a script, or preloading an image keeps every asset - it changes delivery only. Those are performance fixes, permitted above, and treating them as deletions is how a run ends with an unchanged score and nothing to show for it.

If removal genuinely is the right answer, it goes in the report as a RECOMMENDATION and waits for an explicit yes: *what it is · why · what it costs to keep · what happens if we remove it, including any redirect needed.* Grouped at the end under **"Needs your approval to remove."** Then stop and wait. Never bundle a deletion into a batch of fixes and mention it after the fact. Consolidations and 301 merges count as deletions - same approval.

**Pass 1 - Grade.** Read `references/on-page-seo.md` and grade the page against every item. Show me the report card first: each category, a score like 9/9, and a plain-English note on each fail. Wait for nothing - proceed straight into fixing.

**Pass 2 - Fix.** Fix ONLY the failing items with the smallest edits possible:
- Never touch my stories, jokes, or voice - just add what's missing
- Meta title/description: read `references/meta-info.md` and produce 2-3 high-CTR variants; recommend one, apply it, show me the alternates
- Images: descriptive alt text under 125 chars, WebP compression, width/height set, descriptive filenames, lazy-load below the fold only (never the hero - `fetchpriority="high"` there)

**Pass 3 - Speed.** Run a Lighthouse check (`npx lighthouse [url] --quiet --chrome-flags="--headless"`). Run MOBILE (Lighthouse's default) - that's where local customers are - and **name the mode next to every score you report**; a bare "98" is a soft number.

**⛔ Never score a dev server.** `next dev` serves unminified, unoptimized code with hot-reload attached - it scores 20-40 points below what visitors get, and its Total Blocking Time alone (870ms vs 0ms measured on this template) throws away a third of the performance score. A Lighthouse number from it is fiction. Tell the member what's happening in one plain line: "I'm building the real version of the site first - the dev server you preview on is deliberately slow, so testing it would give fake numbers."

**The exact sequence, and it is NOT `npm run start` on this template:**

```bash
cd website && npm run build            # writes .next/ (server build) or out/ (static export)
# SERVER BUILD (no output: export) - THIS TEMPLATE'S DEFAULT:
npx next start -p 4321
# STATIC EXPORT (only if a member has added output: "export" back):
npx --yes serve@latest out -l 4321     # `next start` ERRORS on output: export
```

Check `next.config.*` for `output: "export"` BEFORE choosing - guessing wrong wastes a cycle on an error message. **The dev server keeps running on its own port and never reflects the build**, so score the new port, never the one the member has been previewing on.

```bash
npx lighthouse http://localhost:4321/[path] --quiet --chrome-flags="--headless" --only-categories=performance,accessibility,best-practices,seo
```

**Always the CLI with `--headless`, never DevTools.** DevTools Lighthouse runs inside the member's own Chrome with their extensions loaded, and extensions inject scripts that wreck Total Blocking Time - the same page can read 77 in DevTools and 99 headless. If the member reports a score that disagrees with yours, ask which one they ran before debugging anything.

Kill the preview server when the pass is done. If the build fails, fixing the build IS the speed task - report it and fix it, never fall back to scoring dev.

**The tell that you scored the wrong thing:** on this template a dev run reports "Minify CSS", "Minify JavaScript", "missing source maps" and "Document does not have a meta description" as failures, and SEO lands at 92 instead of 100. See those, you are on dev - rebuild and rescore rather than fixing phantom problems.

**The targets, and the loop runs until they're hit:** SEO 100, Best Practices 100, Accessibility 100 (items needing design-token changes go to the recommendations list instead - the copy rule applies to design too). Performance: run three times, take the median, and loop until it's **95+ mobile** - take the 100 when it's there, but between 95 and 100 the score wobbles a few points run to run, so chasing a perfect 100 through the noise burns hours fixing the measuring tape. Below 95 there is always a real fix left: render-blocking CSS/fonts, image formats, layout shift. On WordPress, push fixes through Novamira with the same targets.

**Pass 4 - The loop. Re-grade against ALL 80 checks and KEEP LOOPING - fix, re-grade, fix, re-grade - until every single check passes.** Done means 100%: every category at full score, or a remaining item explicitly WAIVED with a one-line reason (genuinely inapplicable to this page type, or needs something only I can provide - a photo, a credential). Waived means consciously skipped and listed, never quietly dropped. Final report: before → after score per category, loop count, the waived list, and confirm the voice survived by quoting one untouched paragraph.

**Pass 5 - Baseline, log, re-index. The run is not done until the improvement is measurable later.**

- **Capture the BEFORE in `optimization-log.md`** (repo root - create from the header in that file if missing). One entry per run, newest first: date, page, category scores before → after, Lighthouse scores before → after with the mode named, and the page's GSC baseline - last 28 days: clicks, impressions, average position, top 5 queries with their positions. Getting the GSC numbers takes 30 seconds and I walk the member through it: search.google.com/search-console → Performance → filter Page = this URL → read the four totals, then the Queries tab for the top 5. They paste, I log it verbatim. No GSC property yet? Log "no baseline - GSC not verified" and point at the Search Console steps in `/publish` - never skip the entry.
- **Book the AFTER.** Every entry ends with `Re-measure on: <date 6 weeks out>` left unfilled. Every run of this command STARTS by checking the log for due re-measures and filling in the delta from today's GSC numbers. That before → after line is the proof a member shows a client, and it only exists if the baseline was captured first.
- **Request re-indexing.** If metadata, schema, or structure changed, the page needs a recrawl: GSC → URL Inspection → paste the URL → Request indexing (the same clicks `/publish` walks through). Say plainly that recrawls take days, not hours - the log's re-measure date is when the numbers mean something.
- **Flag shelf-life fixes.** Any fix that can rot - a snapshotted third-party stylesheet, a pinned CDN URL, a hotlinked asset - gets its own "has a shelf life" list in the report, each with the permanent fix named (fonts: self-host the files). A speed fix that breaks silently in six months isn't a fix, it's a deferral.
- **Look at what you generated.** Every image this run created (og image, WebP conversions) gets opened and looked at before the report ships. A checklist can't catch "this looks wrong", and the og image is the face of the site in every shared link.

**The report ends with three separated lists - what's on whom, unmissable.** Anything waiting on the member must never hide mid-report; the final block, in this order:

1. **Waiting on you.** Each item: what it is, why it's blocked, and EXACTLY what to send or say to unblock it. The model: "sameAs profile links - the schema is live but has no social/profile URLs in it. Send me your Google Business Profile, LinkedIn, YouTube, whatever exists publicly, and I'll wire them in. This is the only actual checklist item waiting." If nothing is waiting, say so in one line.
2. **Optional recommendations.** Things deliberately not applied (design tokens, deletions, anything needing approval), each with the one-line trade-off and the exact words to greenlight it: "Say the word and I'll bump it one shade."
3. **Waived.** Each with its one-line reason AND where it will matter instead: "keyword in the H1 - inapplicable to a tagline homepage; matters on service pages and blogs."

---

## The report page (added 28 Aug 2026)

When the loop finishes, write the same HTML report `/audit` writes: copy `references/audit-report-template.html` to `audit-report.html`, replace only the JSON block, `open` it. Scope it to the page or pages this run touched: `pages` holds only those, section 02 carries on-page, technical and AI readiness, and `other` lists the speed and image changes. Same field rules as `/audit` (see the end of `.claude/commands/audit.md`): plain English, no em-dashes, the after score moves only where this run moved it, waivers carry a type and a reason.
