# Launch checklist

1. **Pick the scope.** One sentence: what is tracked, what is not. Narrow beats broad.
2. **Write the config.** Copy an `examples/*.json`; set name, slug, tagline, scope, categories, ledger types, the entities to watch, primary sources and search queries.
3. **Generate.** `python3 new-tracker.py --config <your.json> --out ../<slug>`
4. **Fill `sources.md`.** The generator adds a skeleton; add the real primary pages (agency press pages, dockets, registries, datasets) and note which ones need Firecrawl.
5. **Seed 10 to 20 posts by hand or by a first manual run.** A tracker with an empty feed looks abandoned. Backfill key events with true dates.
6. **Create the GitHub repo.** Push. Settings > Pages > deploy from `main`, folder `/docs`.
7. **Enable Discussions** (Announcements category) and set up giscus if you want per-post comments. Update the repo ID in `docs/index.html` (search `GISCUS`). Skip if not wanted.
8. **Create the scheduled task.** Paste `ROUTINE-PROMPT.md` as the prompt, attach the repo, set hourly. Run it once manually and check the commit.
9. **Verify:** page loads, search works, a permalink (`#p-<id>`) scrolls to its post, `data.json` and every archive file validate, `lastCheck` updates.
10. **Add the tracker to your own index** (a list of your trackers) so nothing is lost.

## Weekly upkeep (5 minutes)
- Read the last week of `reports/`: look for repeated "could not fetch" lines and fix the source or fallback.
- Skim for late catches; add the missing source to `sources.md`.
- Check that figures in `numbers` and charts are not older than their publication cadence.
