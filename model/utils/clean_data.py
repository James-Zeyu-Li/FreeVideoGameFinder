"""
This module provides functions for checking and cleaning game data.
"""


def check_game_data(data):
    """
    Check if a game's data is complete and valid
    If its a empty string return false.

    Args:
        games_data (list of dict): A list of dictionaries.

    Returns:
        bool: True if all required fields are present and valid
                False otherwise.

    Raises:
        TypeError: If the input data is not a dictionary.
    """

    if not isinstance(data, dict):
        raise TypeError("Game data must be a dictionary")

    fields_to_check = [
        'title', 'thumbnail', 'short_description', 'game_url',
        'genre', 'developer', 'release_date']

    for field in fields_to_check:
        if data.get(field) is None or data.get(field) == '':
            return False
    return True


def clean_games_data(games_data):
    """
    Add all games that is True in check game data into a clean data list.

    Args:
        games_data (list of dict): A list of dictionaries, each dictionary
                                   contains a single game's data.

    Returns:
        list of dict: A list of cleaned games.

    Raises:
        TypeError: If the input games_data is not a list.
    """
    if not isinstance(games_data, list):
        raise TypeError("Games data must be a list")

    cleaned_game = []
    for game in games_data:
        if check_game_data(game) is True:
            cleaned_game.append(game)
    return cleaned_game
