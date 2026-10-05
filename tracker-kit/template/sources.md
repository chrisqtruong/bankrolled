# Source checklist

Each hourly check opens these primary pages (not just keyword searches) and records in `reports/YYYY-MM-DD.md` which it read and which failed. The first morning check reads all of them.

## Primary pages
{{PRIMARY_LIST}}

## Every-check search set
{{QUERY_LIST}}

Add "today" on later checks. Search the feed and archive for the subject before posting: late catches are the usual gap.

## Watch list
{{WATCH}}

## How to fetch
- If WebFetch is blocked or fails for a page, retry with Firecrawl `firecrawl_scrape` (markdown, onlyMainContent, `maxAge: 0` for hourly pages) before skipping it. Note any skip in the report.
- On agency press pages, read every release since the last check, not only titles that match the keywords.

## Staleness calendar
| Item | Cadence | Where it lands |
|---|---|---|
| (fill in: each official figure, how often it is published, which `numbers`/`charts` entry it feeds) | | |

If a figure is older than its cadence, say so in the report.

## Evidence tiers (if used)
See `METHOD.md`. Record the tier in the entry text for conflict, rights and disaster topics.

## Known blind spots (keep this list honest; the About tab mirrors it)
- List every source that blocks automated reading, is paywalled, or is too large, and the workaround used. Update it whenever a run records a failure.
