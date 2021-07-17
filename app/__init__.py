from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()
web_admin = Admin(name='AI WEB')


def create_app(config_name):
    app = Flask(__name__)

    @app.errorhandler(Exception)
    def handle_exception(error):
        print("handled exception!")

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Register web
    from app.web import web as main_blueprint
    app.register_blueprint(main_blueprint)
    web_admin.init_app(app)

    # Register distance api
    from app.api import api as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix="/v1")

    # Error handling
    from app.helpers.error_handlers import error_handler
    app.register_blueprint(error_handler)

    db.init_app(app)
    return app
