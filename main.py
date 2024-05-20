import streamlit as st
from view.home import show_home_title


def home_rendering():
    """
    Render the home page of the Streamlit app.
    """
    show_home_title()


def main():
    """
    The main function to initialize and run the Streamlit app.
    """

    home_rendering()


if __name__ == "__main__":
    main()
