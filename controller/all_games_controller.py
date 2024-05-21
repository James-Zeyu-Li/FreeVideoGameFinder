"""
Controller for all games page
"""
import streamlit as st
from view.all_games import AllGamesPage
from model.game_list import GameList


class AllGamesController:

    def __init__(self, url):
        self.game_list = GameList.load_model(url)
        self.all_games_view = AllGamesPage()

    def all_games_rendering(self):
        """
        Render the filtered games based on the criteria selected on sidebar.
        """
        self.all_games_view.title_for_all_game()

        genre, sort_order = self.all_games_view.filter_display_on_sidebar()

        # Get filtered games based on criteria
        filtered_games = self.game_list.filter_games(
            genre, sort_order)

        if filtered_games:
            for game in filtered_games:
                self.all_games_view.show_game_detail(game)
        else:
            st.write("No games found for the selected criteria.")
