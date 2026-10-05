# {{NAME}}

{{TAGLINE}}

### → [Read {{NAME}}: {{OWNER}}.github.io/{{REPO}}](https://{{OWNER}}.github.io/{{REPO}}/)

**Scope.** {{SCOPE}}

## What's here

| Path | What it is |
|---|---|
| `docs/index.html` | The page |
| `docs/data.json` | All current content: feed posts, ledger rows, charts, key figures |
| `docs/archive/` | Posts older than {{ARCHIVE_DAYS}} days, one file per month. Never deleted. |
| `ledger.csv` | The confirmed ledger as a spreadsheet |
| `reports/YYYY-MM-DD.md` | One report per day: what each check read, added or corrected |
| `sources.md`, `PINNING.md`, `IMAGES.md`, `METHOD.md` | The rules the scheduled run follows. Edit these to change its behavior. |
| `ROUTINE-PROMPT.md` | The scheduled-task prompt that runs this tracker every hour |

## Standards

Every item is labeled **confirmed**, **reported** or **disputed** (see `METHOD.md`). Only confirmed items enter the ledger. Defendants are accused until convicted; lawsuits are allegations; when sources disagree on a number, the number is left out; corrections are made in place.

## License

Content and data: CC BY 4.0. Add a code license of your choice.

Built with the Tracker Kit method.
