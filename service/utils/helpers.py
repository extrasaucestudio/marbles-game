"""A collection of helps for use in the application."""
import random


def make_guess() -> str:
    """Return an odd or even response at random."""
    return "even" if random.randint(1, 10) % 2 == 0 else "odd"


def select_random_stake(marbles: int) -> int:
    """Returns a random stake."""
    return random.randint(1, marbles)
