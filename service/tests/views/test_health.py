"""Tests for the /health endpoints."""


def test_ping(app):
    """Test the ping endpoint returns the expected 200, 'Pong' response."""
    response = app.get('/health/ping')

    assert response.status_code == 200
    assert 'Pong' in str(response.data)
