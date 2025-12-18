import os
import requests
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(dotenv_path=Path(".env"))


API_KEY = os.getenv("BALLDONTLIE_API_KEY")
if not API_KEY:
    raise RuntimeError("BALLDONTLIE_API_KEY not set")

BASE_URL = "https://api.balldontlie.io/v1"

def fetch_games(season=2025, per_page=5):
    headers = {"Authorization": API_KEY}
    params = {
        "seasons[]": season,
        "per_page": per_page
    }

    response = requests.get(
        f"{BASE_URL}/games",
        headers=headers,
        params=params,
        timeout=10
    )
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    data = fetch_games()

    print(f"Fetched {len(data['data'])} games\n")

    for game in data["data"]:
        print(
            f"{game['date'][:10]} | "
            f"{game['visitor_team']['abbreviation']} @ "
            f"{game['home_team']['abbreviation']} | "
            f"{game['visitor_team_score']}–{game['home_team_score']}"
        )