import streamlit as st
from view.home import home_rendering
from view.search import search_rendering
from view.all_games import all_game_rendering


def main():
    """
    The main function to initialize and run the Streamlit app.
    """
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "search", "All games"])

    if page == "Home":
        home_rendering()
    elif page == "search":
        search_rendering()
    elif page == "All games":
        all_game_rendering()


if __name__ == "__main__":
    main()
