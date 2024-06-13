"""
This class will be used to manage user profile and user register
"""
from model.user import User


class UserManagement:

    def __init__(self):
        self.users = {}

    def register_user(self, username, password):
        user_id = str(len(self.users) + 1)
        if username in self.users:
            return None
        user = User(user_id, username, password)
        self.users[username] = user
        return user

    def get_user(self, username):
        return self.users.get(username)

    def login_user(self, username, password):
        user = self.get_user(username)
        if user and user.login(password):
            return user
        return None
