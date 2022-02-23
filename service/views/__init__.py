"""Collection of views used by the service."""
from .game import bp as game_bp
from .health import bp as health_bp

VIEW_BLUEPRINTS = [health_bp, game_bp]
