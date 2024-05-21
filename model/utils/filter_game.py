"""
This file includes all functions for filter functionality.
"""
from datetime import datetime


def genre_filter_games(games, genre):
    """
    Filters a list of games based on a specified genre.

    Args:
    games (list): A list of game objects to filter.
    genre (str): The genre to filter the games by.
                    If 'All', no filtering is applied.

    Returns:
        list: A list of filtered games that match the specified genre.

    Raises:
        TypeError: If 'genre' is not a string.
    """

    if not isinstance(genre, str):
        raise TypeError("Genre must be a string")

    if genre == "All":
        return games

    filtered_games = []
    for game in games:
        if game.genre.lower() == genre.lower():
            filtered_games.append(game)

    return filtered_games


def validate_date_format(date_str):
    """
    Validates if the provided string is in the 'YYYY-MM-DD' format.

    Args:
        date_str (str): The date string to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    if isinstance(date_str, str) and len(date_str) == 10:
        year, month, day = date_str.split('-')

        if year.isdigit() and month.isdigit() and day.isdigit():
            return True

    return False


def get_release_date(game, sort_order="Latest to Oldest"):
    """
    Parses the release date of a game and
    provides a fallback value for sorting.

    Args:
        game (Game): A game object containing a 'release_date' attribute.
        sort_order (str): The order of sorting

    Returns:
        datetime: The release date of the game.
    """

    # If no release data on each game obj, return empty string
    release_date_str = getattr(game, 'release_date', '')

    if validate_date_format(release_date_str):
        return datetime.strptime(release_date_str, "%Y-%m-%d")

    if sort_order == "Latest to Oldest":
        return datetime.max
    elif sort_order == "Oldest to Latest":
        return datetime.min
    else:
        return None


def time_filter_games(games, sort_order="Latest to Oldest"):
    """
    Sorts a list of games based on their release dates.

    Args:
    games (list): A list of game objects to sort.
    sort_order (str): sort game by time.

    Returns:
    list: The list of games sorted based on their release dates.
    """
    def sort_key(game):
        return get_release_date(game, sort_order)

    # reverse the ascending sort
    games.sort(key=sort_key, reverse=(sort_order == "Latest to Oldest"))
    return games


def filter_games(all_games, genre, sort_order=None):
    """
    Applies genre filtering and release date sorting.

    Args:
        all_games (list): A list of all game objects.
        genre (str): The genre to filter by.
        sort_order (str): The order to sort the games by release date.

    Returns:
        list: A list of games that have been filtered and sorted.
    """
    # Apply genre filter
    genre_filtered_games = genre_filter_games(all_games, genre)

    # Apply time filter only if a sort order is specified
    if sort_order:
        sorted_games = time_filter_games(genre_filtered_games, sort_order)
    else:
        sorted_games = genre_filtered_games

    return sorted_games
