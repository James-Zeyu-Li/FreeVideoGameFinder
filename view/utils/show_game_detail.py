"""
Zeyu Li, CS5001, Final Project

The files showns the layout of game detail.
"""

import streamlit as st
from view.utils.widget import divider


def show_game_detail(game):
    """
    Display game details in a Streamlit app.
    """

    col1, col2 = st.columns(2)

    with col1:
        st.subheader(game.title)
        st.image(game.thumbnail, width=300)

    with col2:
        st.write("Description:", game.short_description)
        st.write("Official Website:", game.game_url)
        st.write("Genre:", game.genre)
        st.write("Developer:", game.developer)
        st.write("Release Date:", game.release_date)

    divider()
