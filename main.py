import streamlit as st
from view.home import show_home_title, show_random_button


def home_rendering():
    """
    Render the home page of the Streamlit app.
    """
    show_home_title()
    show_random_button()
    st.write("Click to explore a game!")


def main():
    """
    The main function to initialize and run the Streamlit app.
    """
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home"])

    if page == "Home":
        home_rendering()


if __name__ == "__main__":
    main()
