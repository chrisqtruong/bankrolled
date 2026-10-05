# Changelog

A record of changes to the Bankrolled site and project. Daily content updates (new posts, ledger rows, corrections) are not listed here: they are committed as "Update YYYY-MM-DD HH:MM ET" and summarized in `reports/`. Design and feature changes are listed below, newest first, and from here on go through a pull request.

## 2026-10-05

- **Tracker Kit: Rackwatch and a generator fix.** `new-tracker.py` no longer crashes when `template/docs/archive/` is missing (git does not keep empty folders). Added `tracker-kit/examples/tech-power.json`. Used to generate Rackwatch (tech, AI and data-center power), which lives in its own repository: https://github.com/chrisqtruong/rackwatch. Bankrolled itself is unchanged.

- **Tracker Kit.** New `tracker-kit/` folder: a scaffold and generator for starting sourced, hourly-updated trackers on other subjects (see `tracker-kit/README.md`). About tab gained a "Known blind spots" section, a purpose statement, and wording that covers prediction markets alongside sportsbooks.

- **Cadence and links corrected.** Site and README now say checks run every hour (they said every two hours); the status line reads "Checked X ago · checks every hour" instead of a fixed next-check time. The About tab links to the project README on GitHub. `sources.md` now records the Firecrawl fallback for blocked pages, a staleness calendar for figures, and the standard search set.

- **Pinned developing story.** A major, still-moving story can sit above the feed with a running list of updates, then unpin automatically after its `pinUntil` date. Rules in `PINNING.md`. Also added `sources.md`, the checklist of primary pages each check reads.
- **Post images.** Posts can carry one optional image under the headline, with a credit, license and source link, in the feed and archive. Only public-domain or freely licensed images are used; see `IMAGES.md`. First image: the Supreme Court building on the New Jersey v. Kalshi petition post.
- **Archive search.** A search box on the Archive tab filters archived posts by company, person or topic, with a live match count.
- **Archive tab.** New tab explaining the 90-day rule (the feed holds the last 90 days; older posts move to the archive, are never deleted, and keep their links) and listing archived posts by month. The feed's archive button now opens it. ([9df0778](../../commit/9df0778))
- **Search moved above the posts.** The feed search sits directly above the list with a lighter underline style. ([836e38d](../../commit/836e38d))
- **Feed keyword search.** Search by company, person or topic across headlines, summaries, topics and sources, with quick links. Typing also searches the archive. ([00af9b9](../../commit/00af9b9))
- **Reaction and comment counts on posts.** A scheduled GitHub Action (every 20 minutes) reads the Discussions and writes `docs/reactions.json`; the page shows the counts beside Comments and Copy link. ([aac1b0c](../../commit/aac1b0c))
- **Loss-pace counter persists.** The "since you arrived" counter keeps running across tabs of the site within a visit instead of restarting on each page load. ([5d62e1d](../../commit/5d62e1d))
- **Broader tagline.** "The money behind American gambling, from sportsbooks to prediction markets." ([3234fbe](../../commit/3234fbe))
- **Scope clarified.** README now states that sportsbooks and all prediction markets are tracked equally. ([45cb227](../../commit/45cb227))
- **Content:** added the New York v. Polymarket post. ([2c60b67](../../commit/2c60b67))

## 2026-10-04

- **License.** MIT for code, CC BY 4.0 for content and data. ([1e8b173](../../commit/1e8b173), [bb57b27](../../commit/bb57b27))
- **README.** Prominent link to the live site, "Built with" and credits sections. ([c44550c](../../commit/c44550c), [209ab74](../../commit/209ab74), [93eb6b1](../../commit/93eb6b1))
- **Favicon.** Halftone favicon matching the masthead logo. ([af8e01f](../../commit/af8e01f))
- **Archive and comments.** Posts older than 90 days move to `docs/archive/`, posts get permanent links, and each post has a comment thread through giscus. ([77a8242](../../commit/77a8242))
- **Navigation.** One-word tab names: Feed, Ledger, Numbers, About. ([2ce8207](../../commit/2ce8207))
- **Live features.** Live status line, loss-pace counter, new-post alerts, topic counts and an About section. ([111c24e](../../commit/111c24e))
- **Feed controls.** Theme toggle, back-to-top button, date and status filters with paging. ([8588ee2](../../commit/8588ee2))
- **Page head.** Mobile viewport, favicon and link previews. ([18e96ac](../../commit/18e96ac))
