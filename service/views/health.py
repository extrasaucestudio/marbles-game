"""Collection of health endpoints for the service."""
from flask import Blueprint

bp = Blueprint('health', __name__, url_prefix='/health')


@bp.route('')
@bp.route('/ping')
def ping():
    """Return a 200 pong response to check the application is responding."""
    return 'Pong1', 200
