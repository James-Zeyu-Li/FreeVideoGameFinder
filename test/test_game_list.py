"""
Unit test for Gamelist Class.
"""

import unittest
from model.game_list import GameList


class TestGameList(unittest.TestCase):
    """
    Unit tests for the GameList class.
    """

    def setUp(self):
        """
        Set up a test environment for each test method.
        """
        self.game_data = [
            {"title": "Game 1", "thumbnail": "thumb1.jpg",
             "short_description": "Description 1",
             "game_url": "url1.com", "genre": "Genre1",
             "publisher": "Publisher1", "release_date": "2022-01-01"}]
        self.game_list = GameList()

    def test_init_with_invalid_type(self):
        """Test initializing GameList with invalid type."""
        with self.assertRaises(TypeError):
            GameList("not a list")

    def test_load_data_with_valid_data(self):
        self.game_list.load_data(self.game_data)
        self.assertEqual(len(self.game_list.games), 1)

    def test_load_data_with_invalid_data_type(self):
        with self.assertRaises(TypeError):
            self.game_list.load_data("not a list")

    def test_select_random_game(self):
        self.game_list.load_data(self.game_data)
        selected_game = self.game_list.select_random_game()
        self.assertIn(selected_game, self.game_list.games)

    def test_select_random_game_no_games(self):
        with self.assertRaises(ValueError):
            self.game_list.select_random_game()

    def test_search_by_title(self):
        self.game_list.load_data(self.game_data)
        results = self.game_list.search_by_title("Game 1")
        self.assertEqual(len(results), 0)


if __name__ == "__main__":
    unittest.main()
# python3 -m unittest test.test_game_list
