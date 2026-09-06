# Website Starter

The chassis. A deliberately basic Next.js + Tailwind website so the platform decision is already made - the SEO and Google Ads Blueprints build into it.

## Quick start

1. Download this folder, open a terminal in it
2. `npm install`
3. Edit `lib/site.config.ts` - the ONE file with your business info (or run the SEO Blueprint's `/context-layer` and let Claude fill it)
4. `npm run dev` → open http://localhost:3000

## Deploy (free)

1. Push to a GitHub repo
2. [vercel.com](https://vercel.com) → New Project → import the repo → Deploy
3. Add your domain in Vercel's settings

## What's already handled

- `lib/site.config.ts` - one config file drives every page (name, phone, services)
- `app/sitemap.ts` + `app/robots.ts` - sitemap auto-generates; search AND AI crawlers allowed
- Click-to-call header, NAP footer (keep it matching your Google Business Profile exactly)
- `next.config.mjs` - the 301 redirects slot for when pages move

## What builds on top

This starter is intentionally empty. The blueprints do the real work:
- SEO Blueprint `/build-website` - the full pyramid: service pages, city pages, blog hubs
- SEO Blueprint `/blog-post` + `/service-page` - the content engine
- Ads Blueprint `/landing-page` - message-matched pages per ad group
