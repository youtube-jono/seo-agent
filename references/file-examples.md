# File shapes - the only five, taken from real files

Every file this repo writes is one of five jobs. Find the job, copy the shape.
Next: match the shape, then check it against the rules in [output-format.md](output-format.md).

Every excerpt below is lifted from a real file a member actually reads. Match the SHAPE, never the content.

**All five open the same way** - three lines, then stop. What it is · where it stands, in counts and words · the ONE next action:

```
# Website index

Updated Tuesday 25 August 2026 · 21 pages · 3 money pages scheduled · zero orphans
**Next:** paste the GHL lead webhook into website/lib/site.config.ts, then /publish.
```

Anything blocking that next action goes immediately after, under `# ⛔ Blockers`, never buried further down:

```
# ⛔ Blockers before /publish

- **The GHL lead webhook is not connected.** Every contact and quote form posts
  to /api/lead, which errors until leadWebhook is set. Do not publish before it
  is pasted in.
```

---

## 1. A registry - what exists, and where each one stands

From `website-index.md`. Bold field label, short value on the same line, lists as indented bullets.

```
## Local SEO services · service hub

**Route:**
 - /services/local-seo-services
 - [file](website/app/services/local-seo-services/page.tsx)
**Cluster:** hub
 - spoke: Local SEO services in Austin
 - spoke: Local SEO services in Houston
 - spoke: Local SEO services in Dallas
**About:** the main city-agnostic hub for local SEO money pages, which links to
all the other city money pages.
**Status:**
 - written
 - linked
 - keyword-map row 1
**Warnings:** the form is a placeholder until the lead webhook lands
```

Same fields every time. The count lives in the section heading: `# Written + linked · 14`.

---

## 2. A queue - what goes out, and when

From `gbp-posts-queue.md`. The content is plain paragraphs. The settings sit underneath it.

```
## 2 · Offer · Friday 28 August · SCHEDULED

**Free lead audit while your phone's quiet. It won't be quiet in October**

September is the quiet month in home services. The air conditioning calls stop,
the heating calls haven't started, and the phone goes quiet enough that you start
checking it's still plugged in.

October ends that inside a week, and by then there's nothing left to build with.

Mention this post when you book.

**Coupon:** QUIETSEPT · **Runs:** Friday 28 August to Friday 4 September
**Button:** Get offer → automatable.co
**Photo:** [gbp-wet-autumn-street.jpg](website/public/images/stock/gbp-wet-autumn-street.jpg)
**Terms:** One audit per business. Cannot be combined with other offers.
```

The heading carries number, type, date and state, so the whole month reads from headings alone.

---

## 3. A build list - what to make, in order

From `keyword-map.md`. The section IS the status, so there is never a `Status:` field.

```
# Written · 7

## Service page: Local SEO services

**Hub** · spoke: SEO services in Austin

**Google check:** passed

**Primary keyword**
- local seo services · 27,100 searches a month · Medium (42 out of 100)

**Secondary keywords**
- local seo company · 18,100 a month · Medium (46)
- local seo packages · 4,400 a month · Medium (34)
- local seo services near me · 2,900 a month · Easy (26)

**Why it exists:** far above your ceiling, built anyway - it is where ads land,
where the Business Profile points, and what every vertical page links up to.
```

A block MOVES between `# To build` and `# Written`, keeping its number. Every number labelled in words - "27,100 searches a month", never a bare `27,100` and never `KD 42`.

---

## 4. A findings report - what is wrong, worst first

From `audit-report.md`. Ranked by what it costs to ignore, never grouped by category. A checkbox you tick as you go.

```
### [ ] 1. Create your sitemap · 23 pages Google can't reach

robots.txt has pointed Google at /sitemap.xml since launch. It returns
"not found", so Google has been guessing at your pages.

**Who:** me, in your code
**Time:** 10 min
**Changes:** adds app/sitemap.ts. No existing file edited. No content touched.

### [x] 2. Collapse the double site
Done 20 August, live. The apex already redirects to www at the host, and
canonicals on every page now name www as the one true copy. Verified live.
```

Two or three lines of explanation, maximum. If an item needs more, it is two items. **Who** is on every item, because some are clicks only the owner can do. Never list what passed - one line counting it is enough.

---

## 5. A fact file - what we are allowed to claim

Every fact carries its source and the date it was checked.

```
## Client results - FOUND, confirmed by the owner 19 August 2026

**Jordan Kilpatrick-Smith - psychotherapy clinic, Toronto** · live on the site with video
- Saved $50K+ a year (replaced admin staff) · 12+ leads a week on automated follow-up
- Video: https://youtu.be/pwL-DXOxuOM · headshot on file
- Owner confirmed: real, numbers stand, keep naming him.

**Roofing lead-qualifier bot - response time cut from 4 hours to 60 seconds**
- Owner confirmed real, 19 August 2026. OPEN: which client, and can they be
  named? Blocks publishing until answered.

## NEVER SAY
- "Best in Vancouver" · unprovable superlative
- Any client name without written permission on file
```

A claim with no source is not a claim. Undated facts rot silently, so date every one. An open question names the thing it blocks.

---

## The three that break every file

- **No tables.** Not one, anywhere a member opens. A `##` block per item with bold labels does the same job and survives a phone screen.
- **No raw data.** No JSON, CSV, YAML, ISO timestamps, record IDs or API field names in a file a human reads.
- **No walls.** Nothing unbroken past about four lines, no list past 10 items without a `+ 23 more`, no paragraph of `·`-separated things.

The test: could a busy non-technical business owner open this on a phone and know what to do in 10 seconds?
