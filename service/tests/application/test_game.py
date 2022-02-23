"""A collection of tests for the game application."""
import pytest
from service.application import get_game_application


@pytest.mark.parametrize(
    [
        'taker_in',
        'maker_in',
        'taker_out',
        'maker_out',
        'stake',
        'guess',
        'round_winner',
        'winner'
    ],
    [
        (10, 10, 12, 8, 2, 'odd', 'taker', None),
        (10, 10, 8, 12, 2, 'even', 'maker', None),
        (5, 9, 0, 14, 5, 'odd', 'maker', 'maker')
    ]
)
def test_play(
    taker_in, maker_in, taker_out, maker_out,
    stake, guess, round_winner, winner
):
    """Test play returns correct result."""
    game = get_game_application(taker=taker_in, maker=maker_in)
    result = game.play(stake=stake, guess=guess)

    assert result == {
        'maker': maker_out,
        'round_winner': round_winner,
        'taker': taker_out,
        'winner': winner
    }
