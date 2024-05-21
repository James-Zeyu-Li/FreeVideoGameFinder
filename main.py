import streamlit as st
from controller.home_controller import HomepageController
from controller.search_controller import SearchController

FREE_GAME_PC_URL = "https://www.freetogame.com/api/games?platform=pc"

home_page_controller = HomepageController(FREE_GAME_PC_URL)
search_page_controller = SearchController(FREE_GAME_PC_URL)


def main():
    """
    The main function to initialize and run the Streamlit app.
    """
    with st.sidebar:
        st.sidebar.title("Select Your Page")

        if 'page' not in st.session_state:
            st.session_state['page'] = "home"

        if st.sidebar.button('Home'):
            st.session_state['page'] = 'home'
        if st.sidebar.button('Search Game'):
            st.session_state['page'] = 'search'
        if st.sidebar.button('Explore All Games'):
            st.session_state['page'] = 'all_games'

    if st.session_state['page'] == 'home':
        home_page_controller.home_rendering()
    elif st.session_state['page'] == 'search':
        search_page_controller.search_rendering()


if __name__ == "__main__":
    main()
