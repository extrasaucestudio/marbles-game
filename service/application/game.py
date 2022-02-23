"""A Game Service module."""
from service.models.game import GameRound
from service.models.player import Player


class GameService:
    """Handles logic relating to a game."""

    def __init__(self, taker: int, maker: int) -> None:
        """Initialise a GameService object.

        Args:
            taker: the number of marbles taker has to play game.
            maker: the number of marbles taker has to play game.
        """
        self._taker = taker
        self._maker = maker

    def play(self, stake: int, guess: str) -> dict:
        """Play a game in the game service.

        Args:
            stake: the number of marbles to stake in game round.
            guess: the 'odd' or 'even' guess in game round.

        Returns:
            A dictionary containing result data.
        """
        taker = Player(name="taker", marbles=self._taker)
        maker = Player(name="maker", marbles=self._maker)

        game_round = GameRound(
            taker=taker, maker=maker, guess=guess, stake=stake
        )
        game_round.update_marble_count()

        return {
            'taker': taker.marbles,
            'maker': maker.marbles,
            'round_winner': game_round.round_winner.name,
            'winner': game_round.winner.name if game_round.winner else None
        }
