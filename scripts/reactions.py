"""Write docs/reactions.json: comment and reaction counts per discussion (title = post id). Run by .github/workflows/reactions.yml."""
import json, os, urllib.request

Q = """query($o:String!,$n:String!,$after:String){repository(owner:$o,name:$n){discussions(first:100,after:$after){
pageInfo{hasNextPage endCursor} nodes{title comments{totalCount} reactionGroups{content reactors{totalCount}}}}}}"""
owner, name = os.environ["GITHUB_REPOSITORY"].split("/")
out, after = {}, None
while True:
    req = urllib.request.Request("https://api.github.com/graphql",
        data=json.dumps({"query": Q, "variables": {"o": owner, "n": name, "after": after}}).encode(),
        headers={"Authorization": "bearer " + os.environ["GH_TOKEN"], "Content-Type": "application/json"})
    d = json.load(urllib.request.urlopen(req))["data"]["repository"]["discussions"]
    for n in d["nodes"]:
        r = {g["content"]: g["reactors"]["totalCount"] for g in n["reactionGroups"] if g["reactors"]["totalCount"]}
        c = n["comments"]["totalCount"]
        if r or c:
            out[n["title"]] = {"c": c, "r": r}
    if not d["pageInfo"]["hasNextPage"]:
        break
    after = d["pageInfo"]["endCursor"]
new = json.dumps(out, sort_keys=True, indent=1)
path = "docs/reactions.json"
old = open(path).read() if os.path.exists(path) else ""
if new != old:
    open(path, "w").write(new)
