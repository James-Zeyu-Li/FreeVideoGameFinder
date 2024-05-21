import streamlit as st
from view.utils.widget import divider
from view.utils.show_game_detail import show_game_detail


class AllGamesPage:
    def __init__(self):
        self.title = "All Games"

    def title_for_all_game(self):
        """
        Display the title for the "All Free Games" page.
        """
        st.title("All Free Games just For You!")
        divider()

    def filter_display_on_sidebar(self):
        """
        The visualize the sidebard for all game page
        """
        st.sidebar.title("Filter to Find Your Game")
        st.sidebar.write(
            "Here's more detailed information or additional controls.")

        sort_order = st.sidebar.radio(
            "Sort By Time", ['Recommendation', 'Latest to Oldest', 'Oldest to Latest'])

        if sort_order == 'Recommendation':
            sort_order = None

        genre = st.sidebar.selectbox(
            'Filter by Genre', ["All", "Shooter", "MMORPG", "Sports",
                                "Racing", "Strategy", "Social",
                                "MOBA"])

        return genre, sort_order

    def show_game_detail(self, game):
        """
        Display the details of a single game.
        """
        show_game_detail(game)
