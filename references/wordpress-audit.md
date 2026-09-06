# WordPress audit-fix loop - where every issue actually gets fixed

**What it is:** the map the agent reads before fixing a WordPress site from a Semrush (or any) audit. The prompt says how to behave; this says how to find what is really rendering a page, and where each issue type truly gets fixed.
**Standing reference** - keep the stack profile at the end LIVING, or it sends the agent to the wrong place.
**Next:** fill in "Your stack profile" for this site, then run the source-of-truth diagnostic below.

Written to work on any WordPress site, any host, any SEO plugin, any page builder. Anything stack-specific is a `[bracketed placeholder]` you fill in once.

---

## The #1 rule - fix the layer that emits the served HTML

**Editing the database does nothing if the page doesn't render through it. Always verify at the RENDERED front-end HTML, find where the `<head>` actually comes from, and fix THERE.**

The classic trap: you write perfect SEO-plugin titles, meta descriptions, noindex flags and canonicals, all confirmed saved in the database, and the audit barely moves. Some pages are rendered by a page builder, a custom template, or custom PHP that hardcodes the `<title>` and `<meta>` and exits before the SEO plugin or theme runs. The plugin was never in the loop.

Fix the wrong layer and you change something real that has zero effect on the page Google and the audit crawler actually see.

---

## Find the real source of truth - run this FIRST

For the specific pages that have issues, before touching anything. This is the step that turns an 8-call investigation into 1.

1. **Fetch the live rendered HTML of the actual URL** (not the editor, not the database). Look at the real `<title>` and `<meta name="description">` being served.
2. **Check whether the SEO plugin is even running on this page.** Look in the `<head>` for the plugin's signature (its HTML comment) and its Open Graph tags. If they are absent, the SEO plugin is NOT controlling this page - stop and find what is.
3. **Compare database against rendered.** Pull what the SEO plugin has stored. If the saved title or description does not match the served HTML, something downstream is overriding or bypassing it.
4. **Find the renderer.** Check in this order.
   - A page builder controlling layout and/or the head
   - A custom template in the (child) theme
   - `template_redirect` / `wp_head` hooks from a plugin or mu-plugin
   - Custom PHP echoing raw HTML and calling `exit` before `wp_head()`
   - A static HTML / JS-app file served for that route
5. **Map EVERY render path, not just one.** A site often has several, with different builders or templates for different page types. List them all before editing, or you fix one and leave the rest broken.
6. **Only then decide where to edit.** Fix the layer that actually emits the served HTML.

---

## Source-of-truth map - fill in for YOUR stack

Replace the bracketed values with what your site actually uses. Getting this right is the single most valuable thing in this document.

**Title, meta description, canonical, schema, sitemap**
Usually `[your SEO plugin]` - templates in its settings, per-page in its meta box. The exception that bites: pages rendered by a builder, custom PHP, or hardcoded HTML that bypass `wp_head()`. Edit the renderer instead.

**Caching, minify, GZIP, browser caching, fix-insecure-content**
Usually `[your caching layer: host-level cache, or one cache plugin]`. Use ONE caching layer. Two (host plus plugin) double-cache and serve stale pages. Leave CSS/JS combine and async OFF unless tested - they routinely break page builders.

**Page layout, on-page content, headings**
Usually `[your page builder, or theme templates, or block editor]`. The exception that bites: custom-PHP and static pages render their own HTML and ignore the builder entirely.

**Which CSS/JS file loads (minified or not)**
The enqueue call in the theme, plugin or renderer. The exception that bites: a hardcoded `<link>` to `styles.css` when `styles.min.css` exists beside it. That produces unminified-CSS warnings no plugin toggle will fix.

**Redirects**
Usually `[your redirect plugin, or .htaccess]`.

**Image alt text**
The Media Library plus the page or widget placing the image.

---

## Issue type to fix location - the playbook

Mapped to the audit findings that come up most.

**Unminified or uncompressed JS and CSS** (often the biggest bucket)
Your caching/optimizer layer's toggles first. If a page hardcodes the non-minified file, fix the enqueue or `<link>` in the renderer.

**Duplicate, missing, too-long or too-short titles and meta descriptions**
SEO plugin templates, then per-page. Unless the page hardcodes them, so verify the rendered HTML first.

**Mixed content, or no HTTP to HTTPS redirect**
The force-HTTPS setting in the host, the optimizer, or `[plugin]`. Confirm in the served HTML.

**Multiple or missing H1**
The builder widget or the renderer that emits the heading. Not usually the theme core.

**Duplicate content from clone or test pages**
noindex plus canonical, which is reversible, before any deletion. Never delete without sign-off.

**Missing ALT text**
Media Library or the widget. Human judgment - never auto-fill garbage alt text.

**Low word count, thin content, low text-to-HTML**
Human judgment. Do NOT automate. Flag for the owner.

**llms.txt not found, HSTS, and similar**
Server or host level. Note it, don't guess-edit.

---

## Verify the cache after every fix

A change isn't done until the LIVE page proves it. Stale cache is the number one reason fixes look like they didn't work.

1. Clear every cache layer after the change: `[host cache]`, `[plugin cache]`, object cache, and any CDN.
2. Re-fetch the live URL and check response headers for a cache MISS, or a low `age`. That confirms you are seeing a fresh render, not a cached copy.
3. Confirm the change is present in the served HTML, not just the database.
4. If it didn't stick, the renderer is overriding it. Go back to finding the real source of truth.
5. The audit tool only reflects changes on its next crawl. Trigger a fresh crawl for a real before-and-after; the old snapshot won't move on its own. Crawling a NEW project and re-running the existing one are different actions.

---

## Stay reversible - non-negotiable on a live site

- **Back up every file before editing it** (copy to a `_backup/` dir on the server). Reverting is then a one-line copy-back.
- **Keep ONE change log** such as `CHANGE-LOG.md`, with every change, its original value, and a one-shot paste-to-revert snippet. Append as you go, not at the end. Never let two competing logs exist.
- **Prefer reversible fixes:** noindex plus canonical over deletion, setting toggles over destructive edits.
- **Stop and ask before anything risky:** deleting pages, bulk content changes, combine or async CSS-JS, theme-core edits.
- **Never blanket-overwrite existing good meta.** Some pages already have crafted titles. Check before mass-updating or you wipe good work.
- **The change log lives on the machine.** If you work in sessions and it gets wiped, recreate it complete, or also store the rollback snippet server-side.

---

## Gotchas from real runs - read before you start

These cost time on live runs. Knowing them up front prevents the most common dead-ends.

- **Map ALL render paths before editing.** Sites commonly have several renderers: one builder for marketing pages, another template for posts, a static file for the homepage. Fixing one leaves the others broken. Grep for every `template_redirect` and `wp_head` hook and every custom template first.
- **Verify by dumping the RAW `<head>`, and watch quote style.** SEO plugins often emit tags with single quotes (`content='noindex, follow'`). A double-quote regex check reports a false "missing" and sends you chasing a non-bug. Read the actual served `<head>` string.
- **Cache-purge APIs aren't always what you expect.** Some optimizer plugins' purge methods can't be called statically, need a specific action hook, or require the instance. Confirm the correct purge call for `[your caching layer]`, then verify a cache MISS.
- **Cache masks success.** A fix can be live in the database while the proxy still serves old HTML. Never conclude "it didn't work" before a full purge and re-fetch.
- **Use a count-then-replace edit pattern.** Match-count each find and replace before writing, so a non-matching edit is skipped safely instead of corrupting the file. A failed match should be the safe failure mode.
- **Some thin or duplicate findings are by design.** Inherently short pages such as contact, terms and privacy will always trip low word count. Flag them; never pad them with filler.

---

## Never automate these - flag for a human

- Thin content or low word count
- Image alt text wording
- Deleting any page (use noindex instead and let the owner decide)
- Slug renames (they need a 301 redirect plan)
- Anything where the fix is a content or editorial call, not a technical setting

---

## Your stack profile - fill this in once per site

Pre-answer these so the agent never guesses. This is the only site-specific part; everything above is universal. Keep a filled-in copy per site.

- **Host / server:** `[e.g. shared, managed WP, VPS]`
- **Caching layer (the ONE you use):** `[host-level cache | one cache plugin]` and its exact purge method
- **SEO plugin:** `[Yoast | Rank Math | AIOSEO | SEOPress]` and its head-tag signature
- **Theme:** `[theme name]`, and whether there is a child theme
- **Page builder / editor:** `[Elementor | Gutenberg | Bricks | Divi | none]`
- **Render paths that bypass the SEO plugin (CRITICAL):** `[list every custom template, mu-plugin, static file, or builder that emits its own <head>]`
- **How the agent reaches the site:** `[MCP name | WP-CLI | REST | admin]`
- **Backup location and change-log file:** `[paths]`

---

## Worked example - a filled-in profile

What a completed profile looks like. Your site's values will differ, so copy the blank template above, not these answers. This example is a demo site whose pages were deliberately seeded with on-page SEO issues to teach the audit-fix loop.

**Host / server**
Managed WordPress host with its own server-level cache. WP 7.0, PHP 8.2.

**Caching layer (the ONE)**
The host's built-in Speed Optimizer, server plus plugin. No cache plugin on top. Purge method is NOT static: call it via the instance plus the plugin's flush action hook, plus `wp_cache_flush()`, then confirm a cache MISS header. Safe toggles ON are minify HTML/CSS/JS, GZIP, browser caching and fix-insecure-content. CSS/JS combine and async are OFF because they broke the page builder.

**SEO plugin**
Yoast SEO. Head signature is the `<!-- This site is optimized with the Yoast SEO plugin -->` comment. It emits robots and canonical with SINGLE quotes (`content='noindex, follow'`), so a double-quote check false-alarms. Stored data lives in the `..._yoast_indexable` table and `_yoast_wpseo_*` post meta.

**Theme and builder**
A lightweight "shell" theme, with the site chrome overridden by custom PHP. The builder runs some content, but the main marketing pages are NOT built with it.

**Redirect manager**
A dedicated redirect plugin.

**Render paths that bypass the SEO plugin - there were THREE**
1. A shared marketing-page template in custom PHP that renders most pages, hardcodes `<title>` and `<meta>`, loads its own CSS, and exits before the SEO plugin runs.
2. A second custom-PHP renderer used by the homepage clone pages.
3. A static HTML / JS-app file served for the root homepage.

Blog posts DID render through the SEO plugin normally, so those fixes went in the plugin, not the templates.

**How the agent reaches the site**
An MCP server exposing `execute-php`, `read-file`, `edit-file` and `run-wp-cli`.

**Backup and change log**
A `_backup/` dir beside the templates (`<file>.php.bak`, copy back to revert), and a single `CHANGE-LOG.md` with the one-shot revert snippet.

### Where each fix landed on this site

- Titles, descriptions, H1, canonical and CSS-min for marketing pages went into the custom PHP templates, not the SEO plugin.
- Blog post titles, noindex and canonical went into the SEO plugin, because those render through it.
- Minify, GZIP, browser cache and HTTPS went into the host optimizer toggles.
- The generic site title `My WordPress` was changed to the real brand name in the `blogname` option, which fixed the generic suffix in post titles and OG tags.
