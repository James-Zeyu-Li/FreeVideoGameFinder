"""
This file fetches data from the API
"""

import requests
from requests.exceptions import (HTTPError, ConnectionError, Timeout,
                                 TooManyRedirects)


def fetch_games_list(url):
    """
    Fetches and returns a list of games.

    Args:
        url (str): The URL from which to fetch the games list.

    Returns:
        list of dict: A list of dictionaries where each dictionary contains
                    data for a single game.

    Raises:
        HTTPError: 404 Not Found or 500 Internal Server Error.
        ConnectionError: A connection error occurred.
        Timeout: The request timed out.
        TooManyRedirects: Too many redirects.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()

        if response.status_code == 200:
            data = response.json()
            return data

    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except TooManyRedirects as redirect_err:
        print(f"Redirect error occurred: {redirect_err}")
