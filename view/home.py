"""
Home page
"""

import streamlit as st
from view.utils.widget import button_widget, divider
from view.utils.show_game_detail import show_game_detail


def show_home_title():
    """
    Display the titles, with a divider line
    """
    st.title("Welcome to Free PC Games!🔥")
    st.header("Start Your Journey find Random Free PC Games!")
    divider()


def show_random_button():
    """
    Creates and displays a button for showing a random game.
    """
    return button_widget('Show Random Game')


def home_rendering():
    """
    Render the home page of the Streamlit app.
    """
    show_home_title()
    show_random_button()
    st.write("Click to explore a game!")


def show_random_game_with_detail(random_game):
    """
    Displays the details of a random game.
    """
    if random_game:
        show_game_detail(random_game)
    else:
        st.write("No game selected or game not found.")
