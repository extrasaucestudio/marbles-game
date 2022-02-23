"""A collection of factories for instantiating applications."""
from .game import GameService


def get_game_application(taker: int, maker: int) -> GameService:
    """Return as instantiated GameService object.

    Args:
        taker: the number of marbles taker has to play game.
        maker: the number of marbles taker has to play game.

    Returns:
        An instantiated GameService object.
    """
    return GameService(taker=taker, maker=maker)
