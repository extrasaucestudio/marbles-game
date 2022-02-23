"""Definition for a player in the application."""
from dataclasses import dataclass


@dataclass
class Player:
    """Class used to represent a package in application."""

    name: str
    marbles: int

    def add_marbles(self, marbles):
        """Method to add marbles to player."""
        self.marbles = self.marbles + marbles
        return self.marbles

    def subtract_marbles(self, marbles):
        """Method to subtract marbles from player.

        Note: It is impossible to have negative marbles.
        """
        self.marbles = max(0, self.marbles - marbles)
        return self.marbles
