"""Write the owned board games of a BoardGameGeek user to _data/boardgames.yml.

Usage: BGG_API_TOKEN=... python3 scripts/bgg_sync.py [username]
"""
import os
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET

USER = sys.argv[1] if len(sys.argv) > 1 else "codingnirvana"
URL = (
    "https://boardgamegeek.com/xmlapi2/collection"
    f"?username={USER}&own=1&subtype=boardgame&excludesubtype=boardgameexpansion"
)
OUT = os.path.join(os.path.dirname(__file__), "..", "_data", "boardgames.yml")


def fetch():
    req = urllib.request.Request(
        URL, headers={"Authorization": f"Bearer {os.environ['BGG_API_TOKEN']}"}
    )
    # BGG answers 202 while it prepares the collection. Retry until it is ready.
    for _ in range(10):
        with urllib.request.urlopen(req) as resp:
            if resp.status == 200:
                return resp.read()
        time.sleep(5)
    sys.exit("BGG did not return the collection after 10 tries")


def main():
    root = ET.fromstring(fetch())
    games = []
    for item in root.findall("item"):
        year = item.findtext("yearpublished")
        games.append((item.findtext("name"), item.get("objectid"), year))
    if not games:
        sys.exit("BGG returned no games; leaving the data file unchanged")

    lines = [
        f"# Owned board games, from https://boardgamegeek.com/collection/user/{USER}?own=1&subtype=boardgame",
        "# Written by scripts/bgg_sync.py. Traditional games have no year.",
        "",
    ]
    for name, bgg_id, year in sorted(games, key=lambda g: g[0].lower()):
        safe = name.replace("\\", "\\\\").replace('"', '\\"')
        lines.append(f'- name: "{safe}"\n  bgg_id: {bgg_id}')
        if year and int(year) >= 1900:
            lines.append(f"  year: {year}")
    with open(OUT, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Wrote {len(games)} games")


if __name__ == "__main__":
    main()
