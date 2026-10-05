# Source checklist

Each hourly check opens these primary pages (not just keyword searches) and records in `reports/YYYY-MM-DD.md` which ones it read. The 7:52am check reads all of them.

**Every check:** CFTC press releases; DOJ press releases (EDNY, EDPA); Supreme Court docket (Kalshi / New Jersey); AP, Reuters, ESPN, Axios top gambling headlines.

**Daily (7:52am):** FEC (Win for America C00925586, DraftKings PAC C00908699); Senate LDA; Federal Register (event contracts); AGA revenue tracker; investor releases (DraftKings, Flutter/FanDuel, MGM/BetMGM, Caesars, Penn); trade press (Covers, SBC Americas, Legal Sports Report, InGame, Yogonet, iGaming Business); Discussions for reader tips.

**State actions, swept weekly and on every daily run:** attorney general cease-and-desist letters and suits against prediction markets; state gaming regulator fines and rulings (NJ DGE, PA PGCB, NY GC, MA GC, OH, IL, MD, NV, AZ, MI, MO, TN); state AG press pages for Missouri, New York, Maryland, Nevada, Ohio, Illinois, Massachusetts, Arizona.

**Courts:** Ninth Circuit (Nevada), Third Circuit (NJ), Fourth Circuit (MD), Sixth Circuit (OH/TN), N.D. Ill. (Illinois), SDNY/EDNY criminal dockets (Rozier, Clase/Ortiz, Billups).

If a page cannot be fetched, try Firecrawl before skipping it, and note the skip in the report.

## How to fetch (learned 2026-10-05)

- The sandbox proxy blocks some domains for WebFetch (cftc.gov, espn.com, nbcsports.com and others). **Always retry a blocked or failed page with Firecrawl `firecrawl_scrape` (markdown, onlyMainContent) before skipping it.** Firecrawl read the CFTC press page, DOJ EDNY news, the AGA tracker, ESPN and NBC Sports fine. The FEC committee page is too large; use the FEC API (`api.open.fec.gov`) or a Firecrawl `query`/`json` format instead.
- On the CFTC press page, read every release dated since the last check, not just ones whose title mentions "prediction". Titles on insider trading, event-contract advisories and "mention markets" are in scope.
- Use `maxAge: 0` for pages that change hourly (CFTC, DOJ, court dockets).

## Staleness calendar (check on the 7:52am run)

| Item | Cadence | Where it lands |
|---|---|---|
| AGA monthly revenue (July 2026 posted Sept 24; August expected late Oct) | monthly | `numbers` "lost by bettors in <month>" tile |
| AGA annual revenue | Feb/Mar | `losses`, `take` chart, `numbers` |
| Win for America FEC report (Q3 due Oct 15; pre-general ~Oct 22; post-general ~Dec 3) | quarterly | `pac`, `pacNext`, `donors`, `split`, Political ledger rows |
| Senate LDA lobbying (Q3 due ~Oct 20) | quarterly | Lobbying ledger rows |
| DraftKings / Flutter / MGM / Caesars / Penn earnings (early Nov for Q3) | quarterly | `diverge` chart, `numbers` |
| State fines (NJ, PA, NY, MA, OH, IL, MD, NV, AZ, MI, MO, TN, NC) | ongoing | feed + Fine ledger rows |

If a tile's "as of" period is older than its cadence, say so in the report.

## Every-check search set (run after the primary pages)

sportsbook fined; sports betting indicted OR pleads guilty OR sentenced; Kalshi OR Polymarket ruling OR lawsuit OR attorney general OR city sues; prediction market CFTC OR insider trading; DraftKings OR FanDuel lawsuit OR settlement; sports betting super PAC OR ballot measure; sports betting tax legislature; sportsbook OR prediction market partnership athlete OR league OR network; sports betting study OR poll. Add "today" on later checks. Check the feed AND archive for the entity before posting, since late catches are the usual gap (Baltimore v. Kalshi/Polymarket and three CFTC insider-trading and advisory items were found 6 to 10 weeks late on 2026-10-05).

## Reports

Write one section per check, but for a check with no changes write a single line ("### Check at HH:MM ET: nothing new. Read: <sources>.") instead of a full block.
