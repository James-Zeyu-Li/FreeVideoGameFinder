"""
This class is for login and registration.
"""
import streamlit as st


class LoginRegister:
    def show_login_page(self):
        """
        Displays the login page with input fields for username and password.

        Returns:
            tuple: A tuple containing the entered username and password.
        """
        st.title("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        return username, password

    def login_button_clicked(self):
        """
        Displays the login button.

        Returns:
            bool: True if the login button is clicked, False otherwise.
        """
        return st.button("Login")

    def show_register_page(self):
        """
        Displays the registration page with input fields for choosing
        a username and password.

        Returns:
            tuple: A tuple containing the chosen username and password.
        """
        st.title("Register")
        username = st.text_input("Choose a Username")
        password = st.text_input("Choose a Password", type="password")
        return username, password

    def register_button_clicked(self):
        """
        Displays the register button.

        Returns:
            bool: True if the register button is clicked, False otherwise.
        """
        return st.button("Register")
