"""
Home page
"""

import streamlit as st
from view.utils.widget import button_widget


def show_home_title():
    """
    Display the titles, with a divider line
    """
    st.title("Welcome to Free PC Games!🔥")
    st.header("Start Your Journey find Random Free PC Games!")


def show_random_button():
    """
    Creates and displays a button for showing a random game.
    """
    return button_widget('Show Random Game')
