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
        if not isinstance(title, str):
            raise TypeError("Game title must be a string")
        if not isinstance(thumbnail, str):
            raise TypeError("Thumbnail must be a string")
        if not isinstance(short_description, str):
            raise TypeError("Game description must be a string")
        if not isinstance(game_url, str):
            raise TypeError("Game Url must be a string")
        if not isinstance(genre, str):
            raise TypeError("Game genre must be a string")
        if not isinstance(developer, str):
            raise TypeError("Game developer must be a string")
        if not isinstance(release_date, str):
            raise TypeError("Game release_date must be a string")

        self.title = title
        self.thumbnail = thumbnail
        self.short_description = short_description
        self.game_url = game_url
        self.genre = genre
        self.developer = developer
        self.release_date = release_date
        # self.thumbs_up_count = 0
        # self.has_thumbs_up = False

    def __str__(self):
        """
        String representation of the game class

        returns:
            str A formatted string with game information.
        """
        return (f"Game Title: {self.title} "
                f"Short_description: {self.short_description} "
                f"Game game_url: {self.game_url} "
                f"Game genre: {self.genre} "
                f"Game publisher: {self.developer} "
                f"Game release_date: {self.release_date}")
