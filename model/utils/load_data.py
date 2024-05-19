"""
Loads a list of free PC games from a URL.
"""

from model.utils.fetch_data import fetch_games_list
from model.game_list import GameList

FREE_GAME_PC_URL = "https://www.freetogame.com/api/games?platform=pc"


def load_model():
    """
    Fetches a list of free PC games from the 'FREE_GAME_PC_URL'
    Initializes 'GameList' object and load using method in GameList class.

    Returns:
        GameList: An instance of the GameList class
                loaded using the 'load_data' method of the 'GameList' class.
    """
    game_data = fetch_games_list(FREE_GAME_PC_URL)
    game_list = GameList()
    game_list.load_data(game_data)
    return game_list
