# Tracker Kit

A scaffold for starting a **sourced, hourly-updated public tracker** on any subject, built from the method behind [Bankrolled](../README.md): every fact linked to a source, honest labels for how certain it is, a permanent archive, and a scheduled AI run that does the legwork.

Use it for anything where the public record is scattered and easy to forget: money in politics, corruption, corporate conduct, environmental disasters, financial markets, human-rights documentation.

## What you get

| Path | Purpose |
|---|---|
| `new-tracker.py` | Generates a new tracker folder (or repo) from `template/` and a config |
| `template/` | The starter site, data files, source checklist, pinning and image rules, README |
| `routine-prompt.template.md` | The scheduled-task prompt, filled in for your topic by the script |
| `METHOD.md` | The standards every tracker follows (status labels, evidence tiers, sensitive-topic rules) |
| `LAUNCH-CHECKLIST.md` | Steps from "idea" to "running hourly" |
| `examples/` | Ready-made configs: corporate lobbying, environmental disasters, conflict accountability, tech and data-center power (`tech-power.json`, used for [Tracewire](https://github.com/chrisqtruong/rackwatch)) |

## Start a new tracker (about 10 minutes)

```bash
python3 tracker-kit/new-tracker.py --config tracker-kit/examples/environmental-disasters.json --out ../my-tracker
```

Or write your own config (copy any file in `examples/`). The script produces:

- a complete tracker folder, ready to push as its own GitHub repo with Pages served from `docs/`
- `ROUTINE-PROMPT.md` inside it: paste this into a scheduled Claude task (hourly)
- a validated starter `docs/data.json`

Then follow `LAUNCH-CHECKLIST.md`.

## Why a separate repo per topic

Each tracker keeps its own data, comment threads, reports and schedule, so a mistake in one can never leak into another, and each can be handed to someone else. This kit is the only thing they share.

## Moving this kit to its own repo

It is self-contained. To give it a home of its own:

```bash
git subtree split -P tracker-kit -b tracker-kit-only   # then push that branch to a new repo
```

## Design rules (keep these when you change things)

1. One data file (`docs/data.json`) holds all current content. One folder (`docs/archive/`) holds the rest. Nothing is ever deleted.
2. The routine's behavior is defined by repo files it reads each run (`sources.md`, `PINNING.md`, `IMAGES.md`), so improving a tracker means editing a file, not re-prompting.
3. Status labels are `confirmed`, `reported`, `disputed`. Only `confirmed` reaches the ledger.
4. IDs are permanent. Corrections are made in place and noted in the entry.
