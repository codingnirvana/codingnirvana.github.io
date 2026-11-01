"""Write a BoardGameGeek user's owned games and played games to _data/.

Owned games go to _data/boardgames.yml. Plays go to _data/plays.yml. Plays
come from the user's own log and from the logs of friends in LOGGERS, kept
only when the friend tagged the user by BGG username.

Usage: BGG_API_TOKEN=... python3 scripts/bgg_sync.py [username]
"""
import os
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET

USER = sys.argv[1] if len(sys.argv) > 1 else "codingnirvana"
# Friends who log plays on BGG and tag USER in them.
LOGGERS = ["kranti"]
# BGG lists a game under its first edition title. These are the names I know them by.
NAMES = {
    15512: "Incan Gold",  # Diamant
    406321: "Take 5",  # 6 nimmt!: 30 Years Anniversary Edition
    63268: "Dobble",  # Spot it!
    45: "Perudo",  # Liar's Dice
}
API = "https://boardgamegeek.com/xmlapi2"
DATA = os.path.join(os.path.dirname(__file__), "..", "_data")


def fetch(url):
    req = urllib.request.Request(
        url, headers={"Authorization": f"Bearer {os.environ['BGG_API_TOKEN']}"}
    )
    # BGG answers 202 while it prepares a collection. Retry until it is ready.
    for _ in range(10):
        with urllib.request.urlopen(req) as resp:
            if resp.status == 200:
                return ET.fromstring(resp.read())
        time.sleep(5)
    sys.exit(f"BGG did not answer {url} after 10 tries")


def name_of(bgg_id, bgg_name):
    return NAMES.get(int(bgg_id), bgg_name)


def quote(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def sync_collection():
    root = fetch(
        f"{API}/collection?username={USER}&own=1&subtype=boardgame"
        "&excludesubtype=boardgameexpansion"
    )
    games = []
    for item in root.findall("item"):
        bgg_id = item.get("objectid")
        year = item.findtext("yearpublished")
        games.append((name_of(bgg_id, item.findtext("name")), bgg_id, year))
    if not games:
        sys.exit("BGG returned no games; leaving the data files unchanged")

    lines = [
        f"# Owned board games, from https://boardgamegeek.com/collection/user/{USER}?own=1&subtype=boardgame",
        "# Written by scripts/bgg_sync.py. Traditional games have no year.",
        "",
    ]
    for name, bgg_id, year in sorted(games, key=lambda g: g[0].lower()):
        lines.append(f"- name: {quote(name)}\n  bgg_id: {bgg_id}")
        if year and int(year) >= 1900:
            lines.append(f"  year: {year}")
    with open(os.path.join(DATA, "boardgames.yml"), "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Wrote {len(games)} owned games")


def plays_logged_by(logger):
    page = 1
    while True:
        root = fetch(f"{API}/plays?username={logger}&subtype=boardgame&page={page}")
        plays = root.findall("play")
        if not plays:
            return
        yield from plays
        page += 1
        time.sleep(2)


def sync_plays():
    seen = set()
    games = {}
    for logger in [USER] + LOGGERS:
        for play in plays_logged_by(logger):
            players = {p.get("username") for p in play.iter("player")}
            # Every play in the user's own log counts. A friend's play counts only when it tags the user.
            if logger != USER and USER not in players:
                continue
            if play.get("id") in seen:
                continue
            seen.add(play.get("id"))
            item = play.find("item")
            bgg_id = item.get("objectid")
            g = games.setdefault(
                bgg_id, {"name": name_of(bgg_id, item.get("name")), "plays": 0, "last": ""}
            )
            g["plays"] += int(play.get("quantity") or 1)
            g["last"] = max(g["last"], play.get("date"))

    lines = [
        f"# Board games {USER} has played, from BGG play logs by {', '.join([USER] + LOGGERS)}.",
        "# Written by scripts/bgg_sync.py.",
        "",
    ]
    for bgg_id, g in sorted(games.items(), key=lambda x: (-x[1]["plays"], x[1]["name"].lower())):
        lines.append(
            f"- name: {quote(g['name'])}\n  bgg_id: {bgg_id}\n  plays: {g['plays']}\n  last: {g['last']}"
        )
    with open(os.path.join(DATA, "plays.yml"), "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Wrote {len(games)} played games from {len(seen)} plays")


if __name__ == "__main__":
    sync_collection()
    sync_plays()
