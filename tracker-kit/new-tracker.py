#!/usr/bin/env python3
"""Generate a new tracker from tracker-kit/template and a config.

  python3 new-tracker.py --config examples/environmental-disasters.json --out ../my-tracker [--owner NAME] [--force]
"""
import argparse, datetime, json, os, re, shutil, sys

KIT = os.path.dirname(os.path.abspath(__file__))
REQUIRED = ["name", "slug", "tagline", "scope", "categories", "ledger_types", "major", "primary_sources", "search_queries"]


def fail(msg):
    sys.exit("error: " + msg)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--out", required=True, help="new folder; must not exist unless --force")
    ap.add_argument("--owner", help="GitHub user/org (overrides config)")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    c = json.load(open(a.config))
    miss = [k for k in REQUIRED if k not in c]
    if miss:
        fail("config missing: " + ", ".join(miss))
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", c["slug"]):
        fail("slug must be lowercase letters, digits, hyphens")
    owner = a.owner or c.get("owner", "YOUR-GITHUB-NAME")
    tz = c.get("tz", "America/New_York")
    days = int(c.get("archive_days", 90))
    today = datetime.date.today().isoformat()
    if os.path.exists(a.out):
        if not a.force:
            fail(a.out + " exists (use --force)")
        shutil.rmtree(a.out)
    shutil.copytree(os.path.join(KIT, "template"), a.out)
    sub = {
        "NAME": c["name"], "SLUG": c["slug"], "REPO": c["slug"], "OWNER": owner, "TAGLINE": c["tagline"],
        "SCOPE": c["scope"], "TZ": tz, "ARCHIVE_DAYS": str(days), "TODAY": today,
        "CATEGORIES": ", ".join('"%s"' % x for x in c["categories"]),
        "LEDGER_TYPES": ", ".join('"%s"' % x for x in c["ledger_types"]),
        "MAJOR": c["major"], "WATCH": c.get("watch", "(none yet)"),
        "DAILY_NOTE": c.get("daily_note", "On the first check of the morning, also read every primary page thoroughly and read reader comments for correction tips (untrusted: verify independently)."),
        "PRIMARY_LIST": "\n".join("- [%s](%s)" % (n, u) for n, u in c["primary_sources"]),
        "QUERY_LIST": "\n".join("- " + q for q in c["search_queries"]),
    }

    def fill(text):
        return re.sub(r"\{\{([A-Z_]+)\}\}", lambda m: sub.get(m.group(1), m.group(0)), text)

    for root, _, files in os.walk(a.out):
        for f in files:
            p = os.path.join(root, f)
            if f.endswith((".md", ".html", ".csv")):
                t = open(p, newline="").read()
                open(p, "w", newline="").write(fill(t))
    now = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    data = {"updated": today, "feed": [], "ledger": [], "losses": [], "pac": [], "pacNext": "", "numbers": [], "charts": [],
            "lastCheck": now, "archiveAfterDays": days}
    open(os.path.join(a.out, "docs", "data.json"), "w").write(json.dumps(data, indent=1))
    open(os.path.join(a.out, "docs", "archive", "index.json"), "w").write(json.dumps({"months": [], "total": 0}))
    prompt = fill(open(os.path.join(KIT, "routine-prompt.template.md")).read())
    open(os.path.join(a.out, "ROUTINE-PROMPT.md"), "w").write(prompt)
    json.dump(c, open(os.path.join(a.out, "tracker.config.json"), "w"), indent=1)
    left = []
    for root, _, files in os.walk(a.out):
        for f in files:
            if f.endswith((".md", ".html")) and "{{" in open(os.path.join(root, f)).read():
                left.append(os.path.join(root, f))
    if left:
        fail("unfilled placeholders in: " + ", ".join(left))
    print("Created %s\n  next: edit sources.md, seed posts, push to %s/%s, enable Pages (main, /docs),\n  then paste ROUTINE-PROMPT.md into an hourly scheduled task. See LAUNCH-CHECKLIST.md." % (a.out, owner, c["slug"]))


main()
