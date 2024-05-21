"""
Search page
"""

import streamlit as st
from view.utils.widget import button_widget, input_box_widget, divider
from view.utils.show_game_detail import show_game_detail


class SearchPage:
    def search_page_title(self):
        """
        Displays the title of the search page on the Streamlit app.
        """
        st.title("Search for your favorite free game!")
        divider()

    def search_page_buttons(self):
        """
        Creates and displays a button for initiating a game search.
        """
        show_data_button = button_widget('Search Game Title')
        return show_data_button

    def input_box(self):
        """
        Creates and displays an input box widget.
        """
        search_box = input_box_widget(
            "Enter Game Title", st.session_state.get('search_query', ''))
        return search_box

    def display_search_result(self):
        """
        Displays the search results on the Streamlit app.
        If no results are found, error message is shown.
        """
        if 'search_results' in st.session_state:
            if st.session_state['search_results']:
                for game in st.session_state['search_results']:
                    show_game_detail(game)
            else:
                st.error("No game found with that title")
