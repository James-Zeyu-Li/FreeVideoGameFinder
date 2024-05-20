"""
Search page
"""

import streamlit as st
from view.utils.widget import button_widget, input_box_widget, divider


def search_page_title():
    """
    Displays the title of the search page on the Streamlit app.
    """
    st.title("Search for your favorite free game!")
    divider()


def search_page_buttons():
    """
    Creates and displays a button for initiating a game search.
    """
    show_data_button = button_widget('Search Game Title')
    return show_data_button


def input_box():
    """
    Creates and displays an input box widget.
    """
    search_box = input_box_widget(
        "Enter Game Title", st.session_state.get('search_query', ''))
    return search_box


def search_rendering():
    """
    Render the search page of the Streamlit app.
    """
    search_page_title()
    search_page_buttons()
    input_box()
