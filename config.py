import os
from settings import DATABASE

basedir = os.path.abspath(os.path.dirname(__file__))

# Postgres config
DEV_POSTGRES = DATABASE["development"]
TEST_POSTGRES = DATABASE["test"]
PROD_POSTGRES = DATABASE["production"]
STAGE_POSTGRES = DATABASE["stage"]


def create_db_url(user, pw, url, port, db):
    return f"postgresql://{user}:{pw}@{url}:{port}/{db}"


# import .env variables for DB connection
# TODO: Unify these ENV variables by pulling from different dot files
def get_env_db_url(env_setting):
    # Init variable
    user = ""
    password = ""
    url = ""
    db = ""
    port = 5432
    # Check conditions
    if env_setting == "development":
        user = DEV_POSTGRES["user"]
        password = DEV_POSTGRES["password"]
        url = DEV_POSTGRES["url"]
        db = DEV_POSTGRES["db"]
        port = DEV_POSTGRES["port"]
    elif env_setting == "testing":
        user = TEST_POSTGRES["user"]
        password = TEST_POSTGRES["password"]
        url = TEST_POSTGRES["url"]
        db = TEST_POSTGRES["db"]
        port = TEST_POSTGRES["port"]
    elif env_setting == "production":
        user = PROD_POSTGRES["user"]
        password = PROD_POSTGRES["password"]
        url = PROD_POSTGRES["url"]
        db = PROD_POSTGRES["db"]
        port = PROD_POSTGRES["port"]
    elif env_setting == "stage":
        user = STAGE_POSTGRES["user"]
        password = STAGE_POSTGRES["password"]
        url = STAGE_POSTGRES["url"]
        db = STAGE_POSTGRES["db"]
        port = STAGE_POSTGRES["port"]

    return create_db_url(user, password, url, port, db)


# DB URLS for each Environment
DEV_DB_URL = get_env_db_url("development")
TESTING_DB_URL = get_env_db_url("testing")
PROD_DB_URL = get_env_db_url("production")
STAGE_DB_URL = get_env_db_url("stage")


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
    SQLALCHEMY_DATABASE_URI = DEV_DB_URL


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = TESTING_DB_URL


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = PROD_DB_URL


class StageConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = STAGE_DB_URL


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
    "stage": StageConfig,
}

key = Config.SECRET_KEY
