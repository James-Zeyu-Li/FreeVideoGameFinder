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

    


# python3 -m unittest test.test_game
