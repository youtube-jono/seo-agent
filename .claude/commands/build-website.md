---
description: Customise the pre-built site to this business - style pick, real copy, photos, one colour. Never a rebuild.
---

**A guided walkthrough, not a batch job.** Every step: say what it is in one line → do it → show the result (link, screenshot, exact values) → wait at every decision. Never chain steps silently.

**The site is already built.** Two styles + a picker ship in `website/`. This command swaps WORDS, PHOTOS and ONE COLOUR. It never touches structure, layout or the design system in `app/ds.css`. It does not build service pages, city pages or blog posts - `/service-page` and `/blog-post` do that, one page per run, off `keyword-map.md`. Want a different design? Only if I say so - paste a screenshot or a Claude design kit.

## Step 0 ⛔ Five facts, then wait

First message is this question and nothing else:

> "Five quick things and I'll have the template wearing your name in two minutes: **business name · what you do (the trade) · the city you serve · phone · email.** Address, licence number and prices can come later."

Record the answers in CLAUDE.md under "## My setup" so nothing gets asked twice. Already there? Confirm them back in one line and move on.

## Step 1 ⛔ Show both, let me pick, then wait

`cd website && npm install && npm run dev` - actually run it, confirm 200s, then:

> "Open **localhost:3000/bold** (trades - loud, phone-forward) and **localhost:3000/calm** (professional services - quiet, credential-led). Which one is this business?"

Recommend one from the trade if it's obvious; the choice is mine. Record `SITE_STYLE` in "## My setup".

Then promote the pick to the root - **style names never appear in live URLs**:
1. `app/[style]/page.tsx` → `app/page.tsx` (keep the picker as `app/_picker.tsx.bak`)
2. `app/[style]/about|blog|contact` → `app/about` etc. The `/services` and `/blog` INDEX pages already ship at the top level - keep them, they are what `/service-page` and `/blog-post` add entries to
3. Delete `app/bold/` and `app/calm/`
4. Rewrite every `href="/bold/..."` / `"/calm/..."` → `"/..."`
5. Verify: `grep -r "/bold\|/calm" app/` is empty, every nav link resolves

## Step 2 Swap the words, in place

Every placeholder is a unique string in the chosen style's page files and in `lib/site.config.ts`:

- `Your Business Name`, phone, email, address, licence → the answers from Step 0
- Every number (`00+`, `0,000`, `000 reviews`, `4.9`) → ask me for the REAL figure. **No real number = it stays a placeholder and gets flagged.** Never invent one.
- Services + `From $000` → my real services and prices (ask)
- Reviews → real ones, word for word. Never written by you. None yet? The reviews section keeps its placeholder and is flagged.
- FAQ answers, towns, hours, team names → real values (the placeholder text says what belongs there - ask for what you can't know)
- Headline/lede: keep the sentence's shape, make it mine
- `public/llms.txt` → the same facts, plain text

Ask one question at a time, in plain words, and say why you need it. Never guess a fact, never leave a slot silently empty.

## Step 3 Photos

Ladder: my own photos (drop them in `website/public/images/`) → stock via `python3 code/fetch_stock_photos.py "[trade]" "[trade] team working" "[trade] tools closeup" --count 8` (no `PEXELS_API_KEY`? ask: pexels.com/api → Get Started, free, 30 seconds) → keep the labelled frame. **Overfetch on purpose: pull a pool 2-3x bigger than the frames need, across 2-3 different queries, LOOK at all of them, and pick the best fit per frame.** Never place the same photo twice on the site - a repeated stock photo reads as a template - and delete the rejects (file + manifest row) so a later run doesn't grab them. Then **replace each placeholder frame ENTIRELY with an `<img>`** - the frame's label text ("CREW & VAN", "JOB PHOTO") must be deleted with it, never left rendering on top of a real photo. **Look at every photo. Stock is atmosphere, never proof.**

**People photos go where people belong.** A team or crew photo lives in the team/about section - NEVER the hero. The hero sells the WORK: the job site, the finished result, the van outside a house. Portraits only in slots that name a person, faces only in sections about the people - and never a stock face presented as a real team member.

## Step 4 Accent

My brand colour (logo, or ask for one) → regenerate the nine `--blue-*` values in `app/ds.css`, same lightness ladder. The graphite accent stays.

## Step 5 Lead form

Forms POST to `/api/lead` → `leadWebhook` in `lib/site.config.ts` → 303 redirect to **`/thank-you`**. The template ships that page pre-built, noindexed and out of the sitemap - keep all of that. Get `LEAD_WEBHOOK_URL` from "## My setup" or ask. Any form webhook works (Make, Zapier, n8n, your CRM). GoHighLevel: Automation → new workflow → Inbound Webhook → copy URL. No CRM yet? Members of my community get GoHighLevel for $1/month: https://www.skool.com/automatable/classroom/32447943?md=47d1df7d71c449baa5ab88c94340718c. Send one test, confirm it lands and the redirect reaches `/thank-you`. No webhook yet? Say plainly the form goes nowhere, flag it, and never publish that state.

## Step 6 The exit gate, then ship

```
python3 code/check_site_complete.py
python3 code/check_css_integrity.py
```

**Both gates, every run.** The second one catches what nothing else can: an undefined `var(--token)` or a className no stylesheet defines are both LEGAL CSS, so `next build` passes, no error appears, and the page just renders flat. Step 4 regenerates the nine `--blue-*` values in `app/ds.css`, which is exactly when a token gets orphaned. A green build is not proof the design survived.

**The loop rule: the gate decides when you're done, not you.** Run the gate → fix every failure → run it again. Repeat until it passes. Do not report progress instead of finishing, do not ask permission to keep fixing, and never present a failing site with an explanation attached. The ONLY reasons to stop early: you need a value only I have (a key, a webhook, a photo, a real number), or a real decision is mine to make. Everything else, you finish.

It fails the run on: any route that errors, any placeholder text still visible on any page, any dead internal link on any page, any orphan page. **A dead link never gets solved silently** - if the target genuinely doesn't exist yet, ask me: remove the link, point it somewhere real, or build the page. Never invent a page just to make a link resolve. Only exception: a placeholder I explicitly told you to leave (no real number yet) - name each one in the report.

**The gate is the floor; your eyes are the bar.** After it passes, screenshot EVERY page at 1440px and 390px, and LOOK at each: no overlay labels on real photos, no broken sections, no empty bands. A page can return 200 and still look wrong; status codes never count as verification.

Report: **one clickable localhost URL per page, one line each** - never "8 pages created". Plus: filled from real data · deliberately left placeholder and why · next command (`/service-page` for the first money page, or `/publish` to get it live today). Never leave a built site unpublished - Google's clocks only start once it's live.
