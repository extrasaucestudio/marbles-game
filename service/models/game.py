"""Definition for a game round in the application."""
from service.models.player import Player
from typing import Optional


class GameRound:
    """Class used to represent a game round in application."""

    EVEN = "even"
    ODD = "odd"

    def __init__(self, taker: Player, maker: Player, stake: int, guess: str):
        """Initialise a GameRound model."""
        self._taker = taker
        self._maker = maker
        self._stake = stake
        self._guess = self._validate_guess(guess)

    @property
    def players(self) -> list:
        """Returns a list of players."""
        return [self._maker, self._taker]

    @property
    def round_winner(self) -> Player:
        """Returns the winner of the round."""
        return (
            self._maker
            if self.odd_or_even_stake == self._guess
            else self._taker
        )

    @property
    def loser(self) -> Optional[Player]:
        """Returns a loser if there is one or None."""
        return next(
            (player for player in self.players if player.marbles in [0, 1]),
            None
        )

    @property
    def winner(self) -> Optional[Player]:
        """Returns a winner if there is one or None."""
        if self.loser:
            return next(
                (
                    player for player in self.players
                    if player != self.loser
                ),
                None
            )
        return None

    @property
    def is_stake_even(self) -> bool:
        """Returns True if stake is even."""
        return self._stake % 2 == 0

    @property
    def odd_or_even_stake(self) -> str:
        """Returns if stake is odd or even."""
        return self.EVEN if self.is_stake_even else self.ODD

    def update_marble_count(self) -> None:
        """Updates the marble count of each player at rounds end."""
        if self._taker == self.round_winner:
            self._taker.add_marbles(self._stake)
            self._maker.subtract_marbles(self._stake)
        else:
            self._maker.add_marbles(self._stake)
            self._taker.subtract_marbles(self._stake)

    def _validate_guess(self, guess: str) -> str:
        """Returns guess if guess valid."""
        if guess not in [self.ODD, self.EVEN]:
            raise Exception
        return guess
