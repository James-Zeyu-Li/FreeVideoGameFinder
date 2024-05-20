"""
Home page
"""

import streamlit as st
from view.utils.widget import button_widget, divider
from view.utils.show_game_detail import show_game_detail


class Homepage:
    def show_home_title(self):
        """
        Display the titles, with a divider line
        """
        st.title("Welcome to Free PC Games!🔥")
        st.header("Start Your Journey find Random Free PC Games!")
        divider()

    def show_random_button(self):
        """
        Creates and displays a button for showing a random game.
        """
        return button_widget('Show Random Game')

    def home_rendering(self):
        """
        Render the home page of the Streamlit app.
        """
        self.show_home_title()
        self.show_random_button()
        st.write("Click to explore a game!")

    def show_random_game_with_detail(self, random_game):
        """
        Displays the details of a random game.
        """
        if random_game:
            show_game_detail(random_game)
        else:
            st.write("No game selected or game not found.")
