---
description: One money page from a service keyword - duplicate the template page, swap the words, wire the proof
argument-hint: "[service or service+city keyword, optional]"
---

## Step 0 ⛔ The lead webhook + the calendar - FIRST RUN ONLY

**Both values are asked ONCE, together, in one message - then never again.** Read CLAUDE.md "## My setup" first: if `LEAD_WEBHOOK_URL` and `GHL_CALENDAR_URL` are both recorded (a recorded "skipped" counts as recorded), say nothing and go straight to the page. Re-asking on run four is the fastest way to make a working skill feel broken.

If either is missing, your first message is this question and nothing else:

> "Two one-time things before I build money pages, both from GoHighLevel:
> **1. Where should leads go?** Your inbound webhook: GHL → Automation → new workflow → trigger 'Inbound Webhook' → copy the URL.
> **2. Your booking calendar** (optional - skip if you'd rather every lead come through the form): GHL → Calendars → the calendar you use for sales calls → copy the booking link.
> Any form webhook works here (Make, Zapier, n8n, your CRM). No CRM yet? Members of my community get GoHighLevel for $1/month: https://www.skool.com/automatable/classroom/32447943?md=47d1df7d71c449baa5ab88c94340718c - sign up, then the same clicks."

Save both to "## My setup" and to `website/lib/site.config.ts` → `leadWebhook` and `bookingUrl`.

- **Calendar given: it goes on `/thank-you`, NOT on the money page.** The money page keeps ONE job and one primary action - the form. The calendar embeds on the thank-you page they land on the instant they submit, because that is the moment intent is highest and they have already converted. Two competing CTAs on a sales page split the decision and lower both; a booking widget after the form costs nothing and converts a slice of leads into booked calls the same minute. The template's thank-you page renders the embed automatically when `bookingUrl` is set - just save the value.
- **Calendar skipped:** form-only, thank-you page stays as-is. Record the skip so this never asks twice.
- **Webhook skipped:** placeholder form, say plainly it goes nowhere, never publish that state.

## Which page

Never ask. No argument = next unwritten `## N. Service page:` row in `keyword-map.md`, lowest N, hubs before city spokes. Skip anything in `website-index.md` or already routed under `app/services/`. A named argument overrides. All rows written? Say so, point at `/keyword-research expand`.

## ⛔ Duplicate = `cp` the file

```
cp app/<SITE_STYLE>/services/page.tsx app/services/[slug]/page.tsx   # first ever
cp app/services/[existing]/page.tsx  app/services/[new-slug]/page.tsx  # every one after
```

City pages copy their parent service page. Then edit ONLY words, metadata, photos, schema. Layout, sections, inline styles stay byte-identical. Composing a page from components or writing new CSS is designing - banned.

WordPress lane: `references/examples/wordpress-service-page-example.md` is the finished page - match its shape, never its content.

## The words

1. **Spec:** scan the top 3 organic results - format, length, H2s, and the trust elements they show. If a local pack shows, the conversion model comes from the map-pack businesses, not the organic 10 (those set coverage only). End with THE GAPS your proof beats.
2. **Buyer:** name the ONE person this page is for in a sentence - who they are, what they fear, what they typed into Google. Their fears = the FAQ, their words (from real reviews) = the words on the page.
3. **Proof-first copy:** every claim traceable to something I gave you - ask me for real numbers, reviews and credentials before writing, and never invent one. Real reviews word for word. Humour dial: charm, one or two grins.
4. **City pages are never clones:** real local jobs, neighbourhoods, city-specific FAQ answers - or flag and skip the city. Never find-and-replace the city name. **Read `references/doorway-pages.md`** - the 3-of-4 local material test, the sibling test, and `code/check_page_similarity.py` to prove it rather than assume it. **Localize the PROBLEM, not the place:** different housing stock, permit rules, weather damage and price bands make a different page; the same page with a different label does not. **Read `references/hub-spoke-pages.md` before any hub or city page** - the hub's "Areas we serve" H2 grows a passage + link for every new city the same day it ships, the city page references its hub early, and the caps/doorway evidence there (10-15 cities max, localize the PROBLEM not the place) are load-bearing.
5. **Photos - every placeholder frame gets resolved, none survive.** The page you copied is full of labelled frames ("JOB PHOTO", "PORTRAIT", "BEFORE - THE OLD UNIT"). For each one, in order: a real photo I dropped in `website/public/images/` → industry stock via `code/fetch_stock_photos.py` (pull a pool 2-3x bigger than the frames need, pick the best fit per frame - never a photo already placed elsewhere on the site, check `public/images/stock/stock-manifest.md`) → if neither exists, DELETE the frame and let the layout close up. **Swapping means replacing the entire frame element with an `<img>`** - the overlay span (icon + uppercase label) goes with it, never left rendering on top of the photo. Look at every photo before it ships, and never a stock face as a real person. **People photos go where people belong:** team/crew shots only in team or about sections, never the hero - the hero and job frames show the WORK (the job, the result, the equipment), and portrait slots are the only place a face goes.

## ⛔ Less is more. Hide everything you can.

**A money page is sales copy, not a document, and the DEFAULT IS COLLAPSED.** Don't ask "should this be hidden" - ask "does the page fail to sell without this on screen". If no, it goes in an accordion. Full rule in `references/service-page-template.md`.

**Only these stay visible:** the H1 and hero promise · the offer, price and guarantee · ONE proof line (the strongest number, not the stack) · every CTA and the form · one line naming the service area. **Everything else collapses** - the proof stack, what's included, the process, jobs done, tables, timelines, and every FAQ answer (questions visible, answers shut).

**Costs nothing in rankings** - accordion content is indexed and weighted normally under mobile-first indexing. Write the depth in full, then collapse nearly all of it.

**The test: screenshot the page with every accordion shut.** If that screenshot doesn't sell on its own, cut a line or promote one - never open a section back up.

## Register + verify

**The exit gate - the skill does not finish until this passes:**

```
python3 code/check_page_done.py /services/[slug]
```

It fails on any surviving frame label or template string, and on any dead link on the page. Fix → re-run → repeat until PASS; never show me a failing page with an explanation. Then screenshot at 1440px and 390px and LOOK - no overlay text on photos, no empty bands. The gate is the floor, your eyes are the bar.

Append to `website-index.md` - **`references/examples/website-index-example.md` is the row shape, match it** - and MOVE the whole map row into `# Written` in `keyword-map.md`, keeping its number - never add a `Status:` field, because a block's position IS its status the moment the file saves. **The loop rule: the gate decides when you're done, not you.** Run the gate → fix every failure → run it again. Repeat until it passes. Do not report progress instead of finishing, do not ask permission to keep fixing, do not stop because a fix is tedious (37 routes to build means 37 routes get built), and never present a failing site with an explanation attached. The ONLY reasons to stop early: you need a value only I have (a key, a webhook, a photo), or a real decision is mine to make. Everything else, you finish.

Test the form posts. Screenshot at 1440px and 390px, look at both, show me. Don't publish - that's `/publish`.


**Add the page to the `/services` index.** Open `website/app/services/page.tsx` and add one section for the new service - name, 2-4 real sentences, photo, descriptive link - replacing a placeholder section if one is left. City pages get a link from their parent service page's "Areas we serve" section, never a top-level index entry.
