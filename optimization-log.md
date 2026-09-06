# Optimization log

Every `/seo-optimization` run records the page's state BEFORE the fixes, so the improvement is provable later. Newest entry first. The re-measure line gets filled about 6 weeks after the run - that before → after is the line you show a client.

Rules:
- The GSC baseline is pasted verbatim from Search Console (Performance → filter Page = the URL). Never estimated, never remembered.
- If GSC isn't verified yet, the entry says so and points at the Search Console steps in `/publish`. The entry still gets written.
- Every run of `/seo-optimization` starts by checking this file for due re-measures and filling in the delta.

---

## Entry format (copy for each run)

```
## <date> · <page path>

**Checks:** <category>: X/Y → X/Y (one line per category that moved) · loop count: N
**Lighthouse (<mobile|desktop>):** Perf XX → XX · SEO XX → XX · A11y XX → XX · BP XX → XX
**GSC baseline (last 28 days, pulled <date>):**
- Clicks: N · Impressions: N · Avg position: N.N
- Top queries: "query" pos N.N · "query" pos N.N · "query" pos N.N · "query" pos N.N · "query" pos N.N
**Shelf-life fixes:** <any fix that can rot, with its permanent fix> (or "none")
**Re-measure on:** <date +6 weeks> → _(fill in: clicks, impressions, avg position, and the delta)_
```

---

<!-- Entries begin below. Newest first. -->
