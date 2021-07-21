import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))
APP_DIR = os.path.join(BASEDIR, "app")


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "hard to guess string"
    # Silence the deprecation warning
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # API settings
    API_PAGINATION_PER_PAGE = 10

    # Flask Settings
    DEBUG = False
    TESTING = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    #SQLALCHEMY_DATABASE_URI = DEV_DB_URL


class TestingConfig(Config):
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = TESTING_DB_URL


class ProductionConfig(Config):
    DEBUG = False
    #SQLALCHEMY_DATABASE_URI = PROD_DB_URL


class StageConfig(Config):
    DEBUG = False
    #SQLALCHEMY_DATABASE_URI = STAGE_DB_URL


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
    "stage": StageConfig,
}

key = Config.SECRET_KEY
