import streamlit as st
from view.home import home_rendering
from view.search import search_rendering


def main():
    """
    The main function to initialize and run the Streamlit app.
    """
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "search"])

    if page == "Home":
        home_rendering()
    elif page == "Search":
        search_rendering()


if __name__ == "__main__":
    main()
