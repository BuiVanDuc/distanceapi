import logging

from flask import Flask


def create_app():
    app = Flask(__name__)

    # Log configuration
    app.logger.disabled = True
    log = logging.getLogger('werkzeug')
    log.disabled = True

    # Register profile api
    from app.api import api as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix="/v1")

    return app
