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
