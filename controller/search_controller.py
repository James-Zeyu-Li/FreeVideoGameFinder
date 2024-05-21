"""
Controller for the search page
"""
import streamlit as st
from view.search import SearchPage
from model.game_list import GameList


class SearchController:
    def __init__(self, url):
        self.game_list = GameList.load_model(url)
        self.search_page_view = SearchPage()

    def search_rendering(self):
        """
        Render the search page of the Streamlit app.

        Args:
        my_model: The model object used for the application.
        """
        self.search_page_view.search_page_title()

        # Use session state for the search query
        if 'search_query' not in st.session_state:
            st.session_state['search_query'] = "Overwatch 2"

        # Use custom input box widget
        st.session_state['search_query'] = self.search_page_view.input_box()

        # Use custom button widget
        # search_page_buttons() clicked, set the result at
        #   current session state.
        if self.search_page_view.search_page_buttons():
            st.session_state['search_results'] = \
                self.search_games_by_title(
                st.session_state['search_query'])

        self.search_page_view.display_search_result()

    def search_games_by_title(self, title):
        """
        Search and return games that match the given title.

        Args:
        title (str): The title to search for.

        Returns:
        list: List of games that match the title.
        """
        found_games = self.game_list.search_by_title(title)
        return found_games
