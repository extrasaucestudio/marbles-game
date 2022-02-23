"""Collection of fixtures accessible globally to all test methods."""
import pytest

from app import app as application


@pytest.fixture()
def app():
    """Provide a testing Flask application for view testing."""
    with application.test_client() as context:
        yield context
