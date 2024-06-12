"""
A class to help with login and mark favorite.
"""
import re


class User:
    """
    The class to represent a user in a gaming application.
    """

    def __init__(self, username, password):
        """
        Constructs all the necessary attributes for the user object.

        Args:
            user_id (int): The unique identifier for the user.
            username (str): The username of the user.
        """
        if not isinstance(username, str):
            raise TypeError('username must be a string')

        self.username = username
        self.password = password
        self.logged_in = False
        self.favorite_games = set()

    def login(self, password):
        """
        Sets the user's login status to True.
        """
        if self.password == password:
            self.logged_in = True
            return True
        return False

    def logout(self):
        """
        Sets the user's login statue to be false.
        """
        self.logged_in = False

    def toggle_favorite(self, username):
        """
        Toggle favorite status for given game.
        if it's already favorite, remove the game.
        """
        if username in self.favorite_games:
            self.favorite_games.remove(username)
        else:
            self.favorite_games.add(username)

    def is_favorite(self, username):
        """
        Check if a game is in user's favorite. 
        """
        return username in self.favorite_games

    @staticmethod
    def validate_password(self, password):
        """
        Set the limitation to the structure of the password.
        """
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not re.search(r'[A-Z]', password):
            raise ValueError(
                "Password must contain at least one uppercase letter")
        if not re.search(r'[a-z]', password):
            raise ValueError(
                "Password must contain at least one lowercase letter")
        if not re.search(r'[0-9]', password):
            raise ValueError("Password must contain at least one number")
        if not re.search(r'[\W_]', password):
            raise ValueError(
                "Password must contain at least one special character")
