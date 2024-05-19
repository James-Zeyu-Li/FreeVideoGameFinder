"""
A class representing a list of games.
"""

from model.game import Game
from random import choice
from model.utils.clean_data import clean_games_data


class GameList:
    """
    This class loads game data, selecting random games,
    searching for games by title, and filtering games by genre.
    """

    def __init__(self, games=None):
        """
        Initializes the GameList class.

        Args:
            games (list, optional): A list of Games.

        Raises:
            TypeError: If 'games' is not None or a list.
        """
        if games is not None and not isinstance(games, list):
            raise TypeError("games should be None or a list.")

        self.games = games if games is not None else []

    def load_data(self, data):
        if not isinstance(data, list):
            raise TypeError("The data is not a list.")

        cleaned_data = clean_games_data(data)
        for game_data in cleaned_data:
            game = Game(
                game_data["title"],
                game_data["thumbnail"],
                game_data["short_description"],
                game_data["game_url"],
                game_data["genre"],
                game_data["publisher"],
                game_data["release_date"]
            )
            self.games.append(game)

    # def select_random_game(self):

    # def search_by_title(self):

    # def filter_by_genre(self):
