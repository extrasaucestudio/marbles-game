"""A collection of tests the game model."""
import pytest

from service.models.game import GameRound
from service.models.player import Player


@pytest.fixture
def game():
    """A fixture for use in tests."""
    return GameRound(
        taker=Player(name='test_taker', marbles=12),
        maker=Player(name='test_maker', marbles=12),
        stake=8,
        guess='even'
    )


def test_round_winner(game):
    """Test that round winner method returns expected results."""
    assert game.round_winner == Player(name='test_maker', marbles=12)


def test_not_winner(game):
    """Test that winner method returns expected results."""
    assert not game.winner


def test_winner():
    """Test that winner method returns expected results."""
    game = GameRound(
        taker=Player(name='test_taker', marbles=12),
        maker=Player(name='test_maker', marbles=12),
        stake=12,
        guess='even'
    )
    game.update_marble_count()

    assert game.winner == Player(name='test_maker', marbles=24)


def test_loser():
    """Test that loser method returns expected results."""
    game = GameRound(
        taker=Player(name='test_taker', marbles=12),
        maker=Player(name='test_maker', marbles=12),
        stake=12,
        guess='even'
    )
    game.update_marble_count()

    assert game.loser == Player(name='test_taker', marbles=0)


def test_is_stake_even(game):
    """Test is_stake_even method returns expected results."""
    assert game.is_stake_even


def test_odd_or_even_stake(game):
    """Test odd_or_even_stake method returns expected results."""
    assert game.odd_or_even_stake == GameRound.EVEN


def test_update_marble_count(game):
    """Test update_marble_count method returns expected results."""
    game.update_marble_count()
    assert game._taker.marbles == 4
    assert game._maker.marbles == 20


def test__validate_guess_raises_exception():
    """Validates that an incorrect guess raises an exception."""
    with pytest.raises(Exception):
        GameRound(
            taker=Player(name='test_taker', marbles=12),
            maker=Player(name='test_maker', marbles=12),
            stake=12,
            guess='FAKE'
        )
