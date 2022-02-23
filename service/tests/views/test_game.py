"""Tests for the game endpoints."""


def test_index(app):
    """Test the index endpoint returns the expected 200."""
    response = app.get('/')

    assert response.status_code == 200
    assert 'Welcome to the Marble Game' in str(response.data)


def test_start(app):
    """Test the start endpoint returns the expected 200."""
    response = app.post(
        '/start',
        data={'marbles': 10},
        content_type='multipart/form-data',
        follow_redirects=True
    )

    assert response.status_code == 200
    assert 'You have 10 marbles' in str(response.data)


def test_play_as_maker(app):
    """Test the play endpoint returns the expected 200."""
    response = app.post(
        '/play',
        data={
            'bot': '10',
            'player': '10',
            'guess': 'even'
        },
        content_type='multipart/form-data',
        follow_redirects=True
    )

    # if you play as maker then you should be returned the taker page next
    assert response.status_code == 200
    assert 'You are the BET TAKER' in str(response.data)


def test_play_as_taker(app):
    """Test the play endpoint returns the expected 200."""
    response = app.post(
        '/play',
        data={
            'bot': '10',
            'player': '10',
            'stake': '2'
        },
        content_type='multipart/form-data',
        follow_redirects=True
    )

    # if you play as taker then you should be returned the maker page next
    assert response.status_code == 200
    assert 'You are the BET MAKER' in str(response.data)
