"""A collection of tests for the player model."""
import pytest

from service.models.player import Player


@pytest.fixture
def player():
    """A fixture for use in tests."""
    return Player(name='test_player', marbles=8)


def test_subtract_marbles(player):
    """Test subtract marbles returns correct response."""
    assert player.subtract_marbles(7) == 1


def test_subtract_marbles_never_negative(player):
    """Test subtract marbles is never negative."""
    assert player.subtract_marbles(56) == 0


def test_add_marbles(player):
    """Test add marbles returns correct response."""
    assert player.add_marbles(5) == 13
