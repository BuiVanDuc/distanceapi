import os
from dotenv import load_dotenv
from pathlib import Path

# Init base dir
basedir = os.path.dirname(os.path.realpath(__file__))
venv_path = os.path.join(basedir, "venv")

# Load dotenv
env_path = Path(venv_path) / ".env"
load_dotenv(dotenv_path=env_path)


def get_env_variable(name):
    try:
        return os.environ.get(name)
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise EnvironmentError(message)


DATABASE = {
    "production": {
        "url": get_env_variable("POSTGRES_URL"),
        "user": get_env_variable("POSTGRES_USER"),
        "password": get_env_variable("POSTGRES_PASSWORD"),
        "db": get_env_variable("POSTGRES_DB"),
        "port": get_env_variable("POSTGRES_PORT"),
    },
    "development": {
        "url": os.getenv("DEV_POSTGRES_URL"),
        "user": os.getenv("DEV_POSTGRES_USER"),
        "password": os.getenv("DEV_POSTGRES_PW"),
        "db": os.getenv("DEV_POSTGRES_DB"),
        "port": os.getenv("DEV_POSTGRES_PORT"),
    },
    "test": {
        "url": os.getenv("TEST_POSTGRES_URL"),
        "user": os.getenv("TEST_POSTGRES_USER"),
        "password": os.getenv("TEST_POSTGRES_PW"),
        "db": os.getenv("TEST_POSTGRES_DB"),
        "port": os.getenv("TEST_POSTGRES_PORT"),
    },
    "stage": {
        "url": os.getenv("STAGE_POSTGRES_URL"),
        "user": os.getenv("STAGE_POSTGRES_USER"),
        "password": os.getenv("STAGE_POSTGRES_PW"),
        "db": os.getenv("STAGE_POSTGRES_DB"),
        "port": os.getenv("STAGE_POSTGRES_PORT"),
    }
}
