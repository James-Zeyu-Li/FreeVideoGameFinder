"""
Reuseable widgets to be called in view.
"""
import streamlit as st


def button_widget(label):
    """
    Create a button widget in Streamlit.
    """
    button = st.button(label)
    return button


def input_box_widget(label, value):
    """
    Create an input box widget in Streamlit.
    """
    search_box = st.text_input(label, value)
    return search_box


def divider():
    """
    Create a divider line in Streamlit.
    """
    st.divider()
