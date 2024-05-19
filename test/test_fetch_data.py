"""
Unit test for fetch data
"""


import requests
from requests.exceptions import (
    HTTPError, ConnectionError, Timeout, TooManyRedirects)
import unittest
import requests_mock


class TestFetchData(unittest.TestCase):
    """
    unit tests for the fetch_games_list function
    """

    def test_fetch_games_list_from_url(self):
        test_url = "https://www.freetogame.com/api/games?platform=pc"

        excepted_data = {"title": "Overwatch 2",
                         "thumbnail":
                         "https:\/\/www.freetogame.com\/g\/540\/thumbnail.jpg",
                         "short_description":
                         "A hero-focused first-person team shooter from \
Blizzard Entertainment.",
                         "game_url":
                         "https:\/\/www.freetogame.com\/open\/overwatch-2",
                         "genre": "Shooter", "platform": "PC (Windows)",
                         "publisher": "Activision Blizzard",
                         "release_date": "2022-10-04",
                         "freetogame_profile_url":
                         "https:\/\/www.freetogame.com\/overwatch-2"
                         }

        with requests_mock.Mocker() as m:
            m.get(test_url, json=excepted_data)
            response = requests.get(test_url)

            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()['title'], "Overwatch 2")

    def test_fetch_games_list_with_http_error(self):
        test_url = "https://www.freetogame.com/api/games?platform=pc123123"

        with requests_mock.Mocker() as m:
            m.get(test_url, status_code=404)
            self.assertRaises(HTTPError)

    def test_fetch_games_list_with_connection_error(self):
        test_url = "https://www.freetogame.com/api/games?platform=pc1"

        with requests_mock.Mocker() as m:
            m.get(test_url, exc=ConnectionError)
            self.assertRaises(ConnectionError)

    def test_fetch_games_list_with_timeout_error(self):
        test_url = "https://www.freetogame.com/api/games?platform=pc"

        with requests_mock.Mocker() as m:
            m.get(test_url, exc=Timeout)
            self.assertRaises(Timeout)

    def test_fetch_games_list_with_redirect_error(self):
        test_url = "https://www.freetogame.com/api/games?platform=pc"

        with requests_mock.Mocker() as m:
            m.get(test_url, exc=TooManyRedirects)
            self.assertRaises(TooManyRedirects)


if __name__ == "__main__":
    unittest.main()

# python3 -m unittest test_fetch_data.py
