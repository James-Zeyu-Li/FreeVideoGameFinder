"""
This file fetches data from the API
"""

import requests


def fetch_games_list(url):
    response = requests.get(url)
    response.raise_for_status()

    if response.status_code == 200:
        data = response.json()
        return data
