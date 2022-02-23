"""Collection of game endpoints for the service."""
from flask import Blueprint, render_template, redirect, url_for
from webargs import fields
from webargs.flaskparser import use_args
from typing import Dict, Any

from service.utils.helpers import make_guess, select_random_stake
from service.application import get_game_application

bp = Blueprint('game', __name__)


view_args: Dict[str, Any] = {
    'player': fields.Int(required=False),
    'bot': fields.Int(required=False),
    'guess': fields.Str(required=False),
    'stake': fields.Int(required=False),
    'marbles': fields.Int(required=False)
}


@bp.route('/')
def index():
    """Return a 200 pong response to check the application is responding."""
    return render_template('index.html')


@bp.route('/start', methods=['POST', 'GET'])
@use_args(view_args, location='form')
def start(args):
    """Return a 200 pong response to check the application is responding."""
    marbles = args['marbles']

    return redirect(
        url_for('game.play', player=marbles, bot=marbles)
    )


@bp.route('/play', methods=['POST', 'GET'])
@use_args(view_args, location='form')
@use_args(view_args, location='query')
def play(args_form, args_query):
    """Return a 200 pong response to check the application is responding."""
    player = args_form.get('player', args_query.get('player'))
    bot = args_form.get('bot', args_query.get('bot'))
    guess = args_form.get('guess', args_query.get('guess'))
    stake = args_form.get('stake', args_query.get('stake'))

    _player_mapping = {}

    if stake:  # if stake then bot is taker
        _player_mapping.update({'taker': 'Bot', 'maker': 'Player'})
        guess = make_guess()
        game = get_game_application(taker=bot, maker=player)
        result = game.play(guess=guess, stake=stake)

        return render_template(
            'play_maker.html',
            guess=guess,
            bot=result['taker'],
            player=result['maker'],
            winner=_player_mapping.get(result['winner']),
            round_winner=_player_mapping.get(result['round_winner'])
        )

    elif guess:  # if guess then bot is maker
        _player_mapping.update({'taker': 'Player', 'maker': 'Bot'})
        stake = select_random_stake(marbles=bot)
        game = get_game_application(taker=player, maker=bot)
        result = game.play(guess=guess, stake=stake)

        return render_template(
            'play_taker.html',
            stake=stake,
            bot=result['maker'],
            player=result['taker'],
            winner=_player_mapping.get(result['winner']),
            round_winner=_player_mapping.get(result['round_winner'])
        )

    else:  # the game needs to start
        return render_template(
            'play_maker.html',
            bot=bot,
            player=player,
        )
