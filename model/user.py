import re

class User:
    def __init__(self, username, password):
        if not isinstance(username, str):
            raise TypeError('username must be a string')

        self.username = username
        self.password = password
        self.logged_in = False
        self.liked_games = set()

    @staticmethod
    def validate_password(self, password):
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not re.search(r'[A-Z]', password):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r'[a-z]', password):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r'[0-9]', password):
            raise ValueError("Password must contain at least one number")
        if not re.search(r'[\W_]', password):
            raise ValueError("Password must contain at least one special character")

