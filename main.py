import streamlit as st
from view.home import Homepage
from view.search import SearchPage
from view.all_games import AllGamesPage

FREE_GAME_PC_URL = "https://www.freetogame.com/api/games?platform=pc"


def main():
    """
    The main function to initialize and run the Streamlit app.
    """
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "search", "All games"])

    if page == "Home":
        Homepage().home_rendering()
    elif page == "search":
        SearchPage().search_rendering()
    elif page == "All games":
        AllGamesPage().all_game_rendering()


if __name__ == "__main__":
    main()
