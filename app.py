from flask import Flask

from service.views import VIEW_BLUEPRINTS

app = Flask(__name__)

for bp in VIEW_BLUEPRINTS:
    app.register_blueprint(bp)

