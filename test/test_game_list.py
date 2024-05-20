"""
Unit test for Gamelist Class.
"""

# import unittest
# from model.game_list import GameList
# from model.game import Game


# class TestGameList(unittest.TestCase):
#     """
#     Unit tests for the GameList class.
#     """

#     def setUp(self):
#         """
#         Set up a test environment for each test method.
#         """
#         self.game_data = [
#             {"title": "Game 1", "thumbnail": "thumb1.jpg",
#              "short_description": "Description 1",
#              "game_url": "url1.com", "genre": "Genre1",
#              "publisher": "Publisher1", "release_date": "2022-01-01"}]
#         self.game_list = GameList()

#     def test_init_with_invalid_type(self):
#         """
#         Test initializing GameList with invalid type.
#         """
#         with self.assertRaises(TypeError):
#             GameList("not a list")

#     def test_load_data_with_valid_data(self):
#         """Test loading data with valid data."""
#         self.game_list.load_data(self.game_data)
#         # Debug print statement
#         print("Loaded Games in Test:", self.game_list.games)
#         self.assertEqual(len(self.game_list.games), 1)
#         self.assertIsInstance(self.game_list.games[0], Game)
#         self.assertEqual(self.game_list.games[0].title, "Game 1")

# def test_load_data_with_invalid_data_type(self):
#     with self.assertRaises(TypeError):
#         self.game_list.load_data("not a list")

# def test_select_random_game(self):
#     self.game_list.load_data(self.game_data)
#     selected_game = self.game_list.select_random_game()
#     self.assertIn(selected_game, self.game_list.games)

# def test_select_random_game_no_games(self):
#     with self.assertRaises(ValueError):
#         self.game_list.select_random_game()

# def test_search_by_title(self):
#     self.game_list.load_data(self.game_data)
#     results = self.game_list.search_by_title("Game 1")
#     self.assertEqual(len(results), 0)

# def test_filter_by_genre(self):
#     self.game_list.load_data(self.game_data)
#     results = self.game_list.filter_game("Genre1")
#     self.assertEqual(len(results), 1)
#     self.assertEqual(results[0].genre, "Genre1")

# def test_filter_by_genre_invalid_type(self):
#     with self.assertRaises(TypeError):
#         self.game_list.filter_game(123)


# if __name__ == "__main__":
#     unittest.main()
# python3 -m unittest test.test_game_list
