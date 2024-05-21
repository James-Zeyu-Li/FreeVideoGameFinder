"""
This is the controller between model and view.
"""

import streamlit as st
from model.game_list import GameList
from view.home import Homepage


class HomepageController:
    def __init__(self, url):
        self.game_list = GameList.load_model(url)
        self.homepage_view = Homepage()

    def home_rendering(self):
        """
        Render the home page of the Streamlit app.
        """
        self.homepage_view.show_home_title()

        # Make a random_game key in session state, to save returned random game
        if 'random_game' not in st.session_state:
            st.session_state.random_game = None

        # if random button clicked, find random game is saved in session state.
        if self.homepage_view.show_random_button():
            st.session_state.random_game = self.find_random_game()

        if st.session_state.random_game:
            self.homepage_view.show_random_game_with_detail(
                st.session_state.random_game)
        else:
            st.write("Click to explore a game!")

    def find_random_game(self):
        """
        Find and return a random game from the loaded game list.

        Returns:
        Game object: A random game from the loaded list.
        """
        return self.game_list.select_random_game()
