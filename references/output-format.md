# Output format - how every file in this repo must look

The shape rules for every markdown file a member opens · rewritten August 2026
Next: read [file-examples.md](file-examples.md) for the finished pictures, then match the one you are about to write.

**EVERY markdown file. No exceptions.** Keyword maps, audits, queues, registries, drafts, notes - all of them. There is no such thing as an "internal" file here. A file that is hard to read is a file nobody checks, and unchecked files are how wrong facts reach a live page.

**Re-read every file you wrote before you finish a command.** If it fails the test below, fix it before replying. This is not a review step to skip when the run went long.

The test, every time: **could a non-technical business owner open this file and know what to do within 10 seconds?**

---

## ⛔ THE SPLIT - decide this before writing a single line

**If a human needs to read it, it goes in the human file. If only Claude needs it, it goes in `references/`.**

This is the rule that keeps every file short. Most bloat is not bad writing, it is **the wrong material in the file** - reasoning, methodology, caveats, decision history and trade-off analysis living inside a file whose job is to be a checkable list.

Goes in the human file:
- The fact, the claim, the number
- What to do next
- What is blocking
- The decision
- Anything they must check or approve

Goes in `references/`:
- Why we chose it
- The methodology behind it
- The trade-offs considered
- The reasoning for the decision
- Anything they would never act on

**The test:** would the owner ever DO something differently because of this paragraph? No means cut it or move it to `references/`.

Worked example. A proof file exists so a human can check "am I allowed to say this?" So it holds the claim and its source, and nothing else. It does NOT hold a paragraph weighing whether a 213 area code hurts local trust in Vancouver. That is Claude's reasoning, the owner will never act on it, and it triples the length of the one file they most need to scan.

**Two things this kills on sight:**
- **Reasoning written into a data file.** If you found something worth explaining, put the conclusion in the file and the explanation in chat.
- **History nobody needs.** "Re-verified on the 13th, then superseded on the 18th, originally sourced from..." A fact needs its source and its date. It does not need its biography.

---

## The eight bans (learned the hard way)

**1. No tables. Period.** Not "where a list works" - EVER, in any file a member opens, including this one. A markdown table is a spreadsheet in disguise: pipes and alignment that collapse the moment one cell runs long, unreadable on a phone, unreadable in a plain editor. The owner has banned them repeatedly. Data that genuinely only makes sense as a grid belongs in `code/` for scripts, not in a deliverable. (Tables rendered on WEB PAGES - a pricing table on a service page, a comparison table in a blog post - are different: those are HTML on the site, good for readers and AI extraction, and stay.)

**2. No raw payloads as deliverables.** No YAML blocks, JSON, CSV, ISO timestamps, field names, record IDs or API shapes in any file a human opens. `account_name: "accounts/[ACCOUNT_ID]"` is not information, it is a hole with quotes around it. Machine formats get built at send time and cached under `code/`.

**3. No bare numbers.** `viral hooks (37)` - is that searches, difficulty, position? Label it in words or leave it out.

**4. No walls.** No paragraph of `·`-separated items. No list past 10 items without a `+ 23 more` line. No unbroken block longer than about four lines. Whitespace and headings do the grouping that columns were doing.

**5. No jargon a business owner would not use.** "Update", not `"Call to action"`. "Button · Book", not `cta_action: BOOK`. "Tuesday 18 August", not `2026-08-18T00:00:00-07:00`. If a word only exists because some API needs it, it does not belong in a file.

**6. Bullets are the DEFAULT for any list of things.** One item per line, each on its own bullet. Never a `·`-separated run inside a bold line:

Never: **Funeral · personal injury · oncology · bankruptcy · addiction · divorce**

Always:
- Funeral and cremation
- Personal injury
- Oncology and serious illness

The `·` separator is only for a handful of short attributes on ONE item ("Coupon · FREEAUDIT · Runs · 18 to 25 August"). The moment it is listing separate things, it becomes bullets.

**7. Delete retired things. Never document them.** A section explaining what NOT to use is wasted space and a trap - somebody will read it and use it. If an offer, number, claim or file is retired, remove it. The only exception is one line at the point of confusion when a stale version is still live somewhere public.

**8. No archive folders. Delete instead.** Git holds every previous version of every file, so an `archive/` folder is a second copy of something nobody will read, in a place they have to scroll past. When a file is superseded, overwrite it. When content is retired, remove it.

---

## The house shape - one pattern, every file

Two real files are the specimens. Match them: `gbp-posts-queue.md` (a queue of things going out) and `website-index.md` (a registry of things that exist). Everything else in this repo is one of those two jobs.

**The top is three lines and stops.** What it is, the state in counts and words, and the ONE next action:

```
# Website index

Updated Tuesday 25 August 2026 · 21 pages · 3 money pages scheduled · zero orphans
**Next:** paste the GHL lead webhook into website/lib/site.config.ts, then /publish.
```

No preamble, no methodology, no "I analysed 1,000 keywords and here's what I found."

**Blockers come before content, under their own heading.** Anything stopping the next step goes at the top where it cannot be missed, never buried mid-file or in closing prose:

```
# ⛔ Blockers before /publish

- **The GHL lead webhook is not connected.** Every form posts to /api/lead, which
  errors until leadWebhook is set. Do not publish before it is pasted in.
```

**Then sections, each with its count in the heading.** `# Written + linked · 14` · `# The chassis · 9` · `# Private pages · 2`. The count in the heading is what makes the file scannable without reading it.

**One `##` block per item. The heading names the item and its type**, plus its state where the item has one:

```
## Local SEO services · service hub

## 2 · Offer · Friday 28 August · SCHEDULED
```

**Inside a block: bold field labels.** Short value on the same line. A list of values as indented `-` bullets underneath:

```
**Route:**
 - /services/local-seo-services
 - [file](website/app/services/local-seo-services/page.tsx)
**Cluster:** hub
 - spoke: Local SEO services in Austin
 - spoke: Local SEO services in Houston
**About:** the city-agnostic hub every city money page links up to.
**Status:**
 - written
 - linked
 - keyword-map row 1
**Warnings:** the form is a placeholder until the lead webhook lands
```

Same file name = same fields every time, in every repo, on every run. If a run genuinely needs a different field, say so out loud and ask - never silently change the shape of a file the user has learned to read.

**Where the block holds real content** - a post, a finding, a draft - the content is plain paragraphs in the body, and the bold labels sit underneath it as the metadata:

```
## 3 · Update · Tuesday 1 September · SCHEDULED

**An automation company telling you to do it by hand first. Yes, really**

Google finished a spam update on 21 August. In July somebody posted that they
had 2,170 pages indexed and 2,340 that Google crawled and refused to index.

I'm a huge advocate of starting manually. Run the process by hand, feel exactly
where it hurts, then automate the part that hurts most.

**Button:** Learn more → automatable.co
**Photo:** [owner-portrait.jpeg](website/public/images/team/owner-portrait.jpeg)
```

**The bottom stops when the content stops.** A closing paragraph summarising what the file already showed is fluff - cut it. A log the next run genuinely reads (the claims used this month, an AI-surface baseline) is allowed, kept short, under its own heading.

---

## The nine rules

**1. Three lines at the top. Nothing else.** As above.

**2. Lead with the decision, not the data.** The first section is always what to do first - blockers, quick wins, next actions. The full list goes below it. Nobody scrolls 300 rows to find the starting point.

**3. The block shape, always the same.** As above: `##` per item, bold field labels, `-` bullets for enumerations. Never invent a second shape inside one file - two formats in one file is the cross-referencing problem the shape exists to solve.

**4. Long lists collapse.** Show the top 50 blocks. Everything else goes under `## The rest (N more)` as one-line bullets. A 1,000-item file is a data dump wearing a markdown costume.

**5. No paragraphs inside data files.** No explanation between blocks, no field full of sentences. **And no `## How to use this` block either** - a file shaped the way this one describes explains itself, and instructions bolted on top are furniture. Genuine operating steps a member follows by hand (how to post one manually while a webhook is missing) are content, get their own named heading, and get deleted the moment they stop applying.

**6. Numbers look the same everywhere.** Thousands separators (`1,200` not `1200`). Currency named once where it first appears (`$2,400 CAD`). One decimal maximum. Always labelled in words - `18,100 searches a month`, never a bare `18,100`.

**7. Status is the words the file already uses, and there is no Status field where position already says it.** `website-index.md` tracks a page's life as `written` · `linked` · `scheduled` · `published`, one per bullet. `keyword-map.md` has NO status field at all - a block sits under `# To build` or `# Written`, and its position IS its status. Never add a `Status:` line to a file whose sections already answer it. No emoji, no checkboxes, no percentages.

**8. Never CSV, JSON, TSV, or a raw data blob as a deliverable.** If a tool or API returns raw data, convert it before saving. Raw responses may be cached in `code/` for scripts to read, never handed to the user as the output.

**9. Dates in words, always.** "Tuesday 18 August 2026", never `2026-08-18`. A date a human reads at a glance is a date they can catch when it is wrong.

**Nesting:** one level of bullets. If you are reaching for a third level, it is a new section.

---

## The canonical files

### keyword-map.md - THE keyword file

**One file, not two.** Clusters, volume, difficulty and build order all live in `keyword-map.md`. Nobody should cross-reference two documents to make one decision.

Each block is a root keyword plus its cluster, sorted for quick wins, hubs before spokes. `/keyword-research` holds the full block spec and [file-examples.md](file-examples.md) shows the rendered shape.

### Audit and findings files

Findings are ranked by what it costs to ignore them, never grouped by category. One block per finding, worst first:

```
### 1. Your sitemap doesn't exist

One sentence saying the problem in plain English.

**What it costs you:** the consequence, with a number in it.
**The fix:** the command or the action · Impact: High
```

Impact vocabulary is `High` · `Medium` · `Low` - never a severity taxonomy with five levels. Never a compliance-style checklist of things that passed - only what needs doing, plus a one-line count of what was fine.

---

## Why these rules exist

Not opinion. Eye-tracking and technical-writing research says the same three things, and every rule above falls out of them.

**People read about a fifth of what is on a page.** They scan. Writing as though a file will be read start to finish is writing for a reader who does not exist.

**They scan in two shapes.** The **F-pattern** - hard across the top, weaker across a second line, then down the left edge. And the **layer-cake pattern** - jumping heading to heading and skipping the prose in between. Two consequences:

- **Headings must carry the meaning on their own.** Someone reading only your headings should get the whole answer. "Before any of these go out" works; "Notes" and "Overview" and "Section 3" are wasted lines.
- **Front-load every line.** The decision goes first, the reasoning second. The left edge and the first few words are the only part guaranteed to be read.

**Chunking beats density.** Miller's research puts short-term memory at five to nine items, which is why the 10-item cap and the `+ 23 more` rule exist.

**Three heading levels maximum, and never skip one.** H2 straight to H4 breaks the document outline and breaks screen readers. If a file needs a fourth level, it is two files.

**Plain language is understood faster AND trusted more.** Jargon does not read as expertise, it reads as friction.

Sources: [Scannability and eye-tracking patterns](https://kweri.co.uk/learn/scannability) · [Chunking for accessible content](https://dkconsultingcolorado.com/2024/04/30/chunking-for-more-accessible-online-content/) · [Google markdown style guide](https://google.github.io/styleguide/docguide/style.html) · [Plain language guidelines](https://digital.gov/guides/plain-language)

---

## Linking files in the response (MANDATORY)

Writing the file is only half the job - the user has to be able to open it.

Every file you create, rewrite or edit gets a **clickable markdown link** in your response, using the path relative to the project root:

- `[keyword-map.md](keyword-map.md)`
- `[keyword-map.md](keyword-map.md)`

Rules:
- **Never** name a file in prose without linking it ("I updated your keyword map" - which file? where?)
- **Never** paste a bare absolute path - it isn't clickable and it's unreadable
- **Never** summarise without links - "12 pages created" must be 12 links
- More than three files? Group them under a short **Files** heading at the end of the response
- Link the file even when the change was small - the user decides what's worth opening, not you

The test: can the user get to every single thing you just wrote with one click, without hunting through folders?
