import streamlit as st
from controller.home_controller import HomepageController

FREE_GAME_PC_URL = "https://www.freetogame.com/api/games?platform=pc"

homepage_controller = HomepageController(FREE_GAME_PC_URL)


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

    if st.session_state['page'] == 'home':
        homepage_controller.home_rendering()


if __name__ == "__main__":
    main()
