"""
This file includes all functions for filter functionality.
"""


def genre_filter_games(games, genre):
    """
    Filters a list of games based on a specified genre.

    Args:
    games (list): A list of game objects to filter.
    genre (str): The genre to filter the games by.
                    If 'All', no filtering is applied.

    Returns:
        list: A list of filtered games that match the specified genre.
    """
    if genre == "All":
        return games

    filtered_games = []
    for game in games:
        if game.genre.lower() == genre.lower():
            filtered_games.append(game)

    return filtered_games
