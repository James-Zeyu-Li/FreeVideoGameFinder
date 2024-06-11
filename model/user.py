import re


class User:
    def __init__(self, username, password):
        if not isinstance(username, str):
            raise TypeError('username must be a string')

        self.username = username
        self.password = password
        self.logged_in = False
        self.favorite_games = set()

    def login(self):
        self.logged_in = True

    def logout(self):
        self.logged_in = False

    def toggle_favorite(self, game_id=None):
        if game_id in self.favorite_games:
            self.favorite_games.remove(game_id)
        else:
            self.favorite_games.add(game_id)

    def is_favorite(self, game_id):
        return game_id in self.favorite_games

    @staticmethod
    def validate_password(self, password):
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
