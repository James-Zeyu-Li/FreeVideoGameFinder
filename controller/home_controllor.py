"""
This is the controller between model and view.
"""

from model.game import Game
from model.game_list import GameList
from view.home import Homepage
from view.search import SearchPage
from view.all_games import AllGamesPage


def home_rendering():
    """
    Render the home page of the Streamlit app.
    """
    Homepage().show_home_title()

