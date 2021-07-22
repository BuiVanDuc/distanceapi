from urllib.parse import urlencode

import pytest

from app import create_app


@pytest.fixture(scope="module", autouse=True)
def client():
    print("init config")
    flask_app = create_app()
    # Create a tests client using the Flask application configured for testing
    with flask_app.test_client() as client:
        # Establish an application context
        with flask_app.app_context():
            yield client  # this is where the testing happens!
