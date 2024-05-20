"""
This is a test class for class game
"""

import unittest
from model.game import Game


class TestGame(unittest.TestCase):
    """
    This test file will check if the game data is working properly
    """

    def test_game_initialization(self):
        game = Game("Title", "thumbnail.jpg", "Short description",
                    "https://www.freetogame.com/api", "Genre",
                    "Developer", "2022-10-04")

        self.assertIsInstance(game, Game)

    def test_game_initialization_wrong_title_type(self):
        with self.assertRaises(TypeError):
            Game(1, "thumbnail.jpg", "Short description",
                 "https://www.freetogame.com/api", "Genre",
                 "Developer", "2022-10-04")

    def test_game_initialization_wrong_thumbnail_type(self):  # need work
        with self.assertRaises(TypeError):
            Game("Title", 1, "Short description",
                 "https://www.freetogame.com/api", "Genre",
                 "Developer", "2022-10-04")

    def test_game_initialization_wrong_description_type(self):
        with self.assertRaises(TypeError):
            Game("Title", "thumbnail.jpg", 1,
                 "https://www.freetogame.com/api", "Genre",
                 "Developer", "2022-10-04")

    def test_game_initialization_wrong_game_url_type(self):
        with self.assertRaises(TypeError):
            Game("Title", "thumbnail.jpg", "Short description",
                 1, "Genre",
                 "Developer", "2022-10-04")

    def test_game_initialization_wrong_genre_type(self):
        with self.assertRaises(TypeError):
            Game("Title", "thumbnail.jpg", "Short description",
                 "https://www.freetogame.com/api", 1,
                 "Developer", "2022-10-04")

    def test_game_initialization_wrong_developer_type(self):
        with self.assertRaises(TypeError):
            Game("Title", "thumbnail.jpg", "Short description",
                 "https://www.freetogame.com/api", "Genre",
                 1, "2022-10-04")

    def test_game_initialization_wrong_date_type(self):
        with self.assertRaises(TypeError):
            Game("Title", "thumbnail.jpg", "Short description",
                 "https://www.freetogame.com/api", "Genre",
                 "Developer", 1)

    def test_turn_game_to_str(self):
        game = Game("Title", "thumbnail.jpg", "Short description",
                    "https://www.freetogame.com/api", "Genre",
                    "Developer", "2022-10-04")
        expected_game = ("Game Title: Title "
                         "Short_description: Short description "
                         "Game game_url: https://www.freetogame.com/api "
                         "Game genre: Genre "
                         "Game publisher: Developer "
                         "Game release_date: 2022-10-04")
        self.assertEqual(str(game), expected_game)


if __name__ == "__main__":
    unittest.main()

# python3 -m unittest test.test_game.py
