import pytest

from app import create_app, db
from app.models import Profile


@pytest.fixture(scope="module", autouse=True)
def client():
    print("init config")
    flask_app = create_app("testing")
    # Create a tests client using the Flask application configured for testing
    with flask_app.test_client() as client:
        # Establish an application context
        with flask_app.app_context():
            yield client  # this is where the testing happens!


@pytest.fixture(scope="module", autouse=True)
def init_table(client):
    print("Create 'distance' table")
    Profile.__table__.create(db.session.bind)
    # Create the database and the database table
    # db.create_all()

    # Insert user data
    profile = Profile(create_time=1, update_time=1, traversed=True, age_history=[1], processed_age=1,
                      gender_history=[1], processed_gender=1, id_history=["test"], processed_id="test")

    db.session.add(profile)
    # db.session.add(profile_2)

    # Commit the changes for the users
    db.session.commit()

    yield  # this is where the testing happens!
    db.session.close()
    print("Drop 'distance' table")
    Profile.__table__.drop(db.session.bind)
    db.session.commit()
