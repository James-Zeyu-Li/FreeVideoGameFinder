"""
A class representing a list of games.
"""

from model.game import Game
from random import choice
from model.utils.clean_data import clean_games_data
from model.utils.fetch_data import fetch_games_list
# from model.utils.filter_game import genre_filter_games


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
        """
        Load game data into the GameList.

        Args:
            data (list): A list of dictionaries containing game data.

        Raises:
            TypeError: If 'data' is not a list.
        """
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

    def select_random_game(self):
        """
        Select a random game from the list of games.

        Returns:
            Game: Randomly selected Game.

        Raises:
            ValueError: If there are no games available to choose from.
        """
        if not self.games:
            raise ValueError("No games available to choose from.")

        return choice(self.games)

    def search_by_title(self, title):
        """
        This function allows matched the title string with game title

        Args:
            title (str): The game title

        Returns:
            list: A list of Game matching the title.
        """
        matched_game = []
        for game in self.games:
            if title.lower() in game.title.lower():
                matched_game.append(game)
        return matched_game

    def filter_game(self, genre):
        """
        Filter games by genre and sort by release date if specified.

        Args:
            genre (str): The genre to filter by.

        Returns:
            list: A list of Game objects matching the genre.

        Raises:
            TypeError: If 'genre' is not a string.
        """
        if not isinstance(genre, str):
            raise TypeError("Genre must be a string")

        matched_game = []
        for game in self.games:
            if genre.lower() in game.genre.lower():
                matched_game.append(game)
        return matched_game

    @staticmethod
    def load_model(url):
        """
        Fetches a list of free PC games from the 'FREE_GAME_PC_URL'
        Initializes 'GameList' object and load using method in GameList class.

        Returns:
            GameList: An instance of the GameList class
                    loaded using the 'load_data' method of the 'GameList' class.
        """
        game_data = fetch_games_list(url)
        game_list = GameList()
        game_list.load_data(game_data)
        return game_list
