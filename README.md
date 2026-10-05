# Bankrolled

A daily, sourced record of the money behind American sports betting: who pays whom, who loses, and who writes the rules.

### → [Read Bankrolled: chrisqtruong.github.io/bankrolled](https://chrisqtruong.github.io/bankrolled/)

Bankrolled tracks four things:

- **Political money.** Super PACs, corporate PACs, ballot measure committees and lobbying by sportsbooks and sports prediction markets.
- **Deals.** League, team, media, college and athlete partnerships, with the amount when it has been disclosed.
- **Enforcement.** Fines, lawsuits, court rulings, legislation and integrity cases.
- **Harm.** How much bettors lose, who bets, and what peer-reviewed and official research finds.

The site is served from this repository with GitHub Pages and is checked for new information every two hours. This repository is also its public archive.

## What's here

| Path | What it is |
|---|---|
| `docs/index.html` | The page itself |
| `docs/data.json` | All content: feed posts, ledger rows, chart series and key figures |
| `ledger.csv` | The confirmed ledger as a spreadsheet |
| `docs/archive/` | Feed posts older than 90 days, one file per month. Posts are archived, never deleted. |
| `reports/YYYY-MM-DD.md` | One report per daily run, listing what was added or corrected, or noting that nothing met the bar |

## Built with

| Part | Tool |
|---|---|
| Site | One static page: HTML, CSS and plain JavaScript. No framework or build step. |
| Charts | Hand-drawn SVG and HTML, with no charting library, so the page stays fast |
| Type | [Young Serif](https://fonts.google.com/specimen/Young+Serif), [Source Serif 4](https://fonts.google.com/specimen/Source+Serif+4) and [IBM Plex Sans](https://fonts.google.com/specimen/IBM+Plex+Sans) from Google Fonts |
| Data | JSON files (`docs/data.json` plus monthly archives) and `ledger.csv` |
| Hosting | [GitHub Pages](https://pages.github.com/), served from `docs/` |
| Comments | [giscus](https://giscus.app/), backed by GitHub Discussions |
| Research and updates | A scheduled [Claude](https://claude.ai) task that runs every two hours, checks public records and the news, verifies each item, and commits the results here |

## Rules for what gets published

Every item has one of three labels:

- **Confirmed.** Backed by a primary record (a campaign finance or lobbying filing, a court document, a regulator's action, a company filing or statement) or by reputable reporting that cites one.
- **Reported.** Credible but not verifiable yet: a single outlet, unnamed sources, an estimate, or a deal in talks.
- **Disputed.** Reported by a credible outlet and publicly denied by the subject.

Only confirmed items go into the ledger. Reported and disputed items appear in the feed, labeled as such.

Other standards:

- Criminal defendants are described as charged or accused until they plead guilty or are convicted.
- Lawsuits are allegations, and sums sought are claims, not judgments.
- When sources disagree on a number, the number is left out.
- Corrections are made in place, with the date and what changed.

## How the daily update works

A scheduled run checks every two hours from 7:52 a.m. to 11:52 p.m. Eastern without anyone prompting it. Each check:

1. Loads the current `data.json`.
2. Checks primary sources first: FEC, Senate lobbying disclosures, DOJ, CFTC, court dockets, state gaming regulators, and company investor pages.
3. Scans wire, national and trade press.
4. Reads each candidate item at its source and classifies it. Duplicates are skipped.
5. Writes new posts and confirmed ledger rows, and updates the charts when new official data appears.
6. Republishes the site and commits the updated files and that day's report here.

If nothing meets the bar, nothing new is posted, and the day's report says so.

## Comments

Each post has its own comment thread, stored in this repository's [Discussions](https://github.com/chrisqtruong/bankrolled/discussions) (Announcements category) through giscus. Commenting needs a GitHub account. Comments that harass people or make unsupported accusations are removed.

## Sources watched

- FEC: [Win for America](https://www.fec.gov/data/committee/C00925586/) and [DraftKings PAC](https://www.fec.gov/data/committee/C00908699/)
- [Senate lobbying disclosures](https://lda.gov/api/v1/filings/) and [OpenSecrets](https://www.opensecrets.org/)
- [AGA commercial gaming revenue tracker](https://www.americangaming.org/resources/commercial-gaming-revenue-tracker/)
- [CFTC press releases](https://www.cftc.gov/PressRoom/PressReleases), [DOJ EDNY](https://www.justice.gov/usao-edny/pr), [DOJ EDPA](https://www.justice.gov/usao-edpa/pr) and the [Federal Register](https://www.federalregister.gov)
- Research: [NBER](https://www.nber.org/papers), [New York Fed](https://libertystreeteconomics.newyorkfed.org/), [Pew](https://www.pewresearch.org/), [Siena](https://sri.siena.edu/), [NCPG](https://www.ncpgambling.org/)

## Limits

- Athlete and celebrity endorsement fees are almost never disclosed. The ledger records these deals with the amount marked "not disclosed."
- Industry revenue figures come from the American Gaming Association, an industry group.
- Prediction-market volume is notional (the face value of contracts traded) and is not directly comparable to sportsbook handle.
- Super PAC totals move only when quarterly FEC reports are filed.

## Credits

- Typefaces: Young Serif, Source Serif 4 and IBM Plex Sans, all under the SIL Open Font License, served by Google Fonts.
- Comments: [giscus](https://github.com/giscus/giscus) (MIT License).
- Facts are drawn from public records and news reporting, linked from each entry. Summaries are written in Bankrolled's own words.

## License

- **Code** (the site itself): [MIT](LICENSE).
- **Content and data** (posts, ledger, archive, reports): [CC BY 4.0](LICENSE-CONTENT). Reuse it freely; credit "Bankrolled" with a link to https://chrisqtruong.github.io/bankrolled/.

## Help

If gambling is causing problems for you or someone you know, the National Problem Gambling Helpline is **1-800-GAMBLER** (call or text).

## Maintainer

Bankrolled is maintained by Chris Truong, who wants a fairer, more equitable world and started this project to track how large corporations use their money and power. Sports betting is the first industry it covers.
