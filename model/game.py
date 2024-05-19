"""
The gam class will be providing game information.
which helps on different search function and allow users to
enter different infos to find a games or games.
"""


class Game:
    """
    The game class turn api fetched data to a list.
    """

    def __init__(self, title, thumbnail, short_description,
                 game_url, genre, developer,
                 release_date):
        """
        Initializes the class Game
        """

        self.title = title
        self.thumbnail = thumbnail
        self.short_description = short_description
        self.game_url = game_url
        self.genre = genre
        self.developer = developer
        self.release_date = release_date
        self.thumbs_up_count = 0
        self.has_thumbs_up = False
