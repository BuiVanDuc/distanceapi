import pytest
from flask_sqlalchemy import inspect
from pytest import mark as m
from sqlalchemy.orm.exc import UnmappedInstanceError
from app import db
from app.models import Profile
from tests.helpers import compare_dict


@pytest.fixture()
def new_profile():
    profile = Profile(create_time=1, update_time=1, traversed=False, age_history=[1], processed_age=1,
                      gender_history=[1], processed_gender=1, id_history=["test"], processed_id="test")

    return profile


@m.describe("Test distance model")
class TestProfileModel(object):

    @m.context("Create a new distance")
    @m.it("Init a distance object")
    def test_new_profile(self):
        profile = Profile(1, 1, False, [1], 1, [1], 1, ["test"], "test")
        assert profile.create_time == 1
        assert profile.update_time == 1
        assert profile.traversed is False
        assert profile.age_history == [1]
        assert profile.processed_age == 1
        assert profile.gender_history == [1]
        assert profile.processed_gender == 1
        assert profile.id_history == ["test"]
        assert profile.processed_id == "test"

    @m.context("Save distance object on database")
    @m.it("Successfully saved a distance")
    def test_save_data(self, client, new_profile, init_table):
        # Transactions
        insp = inspect(new_profile)
        db.session.add(new_profile)
        db.session.commit()
        # Assert
        assert insp.persistent is True

    @m.context("Save distance object on database")
    @m.it("Fail to save a distance. 'start_time' field is None")
    def test_save_data(self, client, init_table):
        # Set value for start time
        profile = new_profile.start_time = None
        # Transactions
        with pytest.raises(UnmappedInstanceError):
            db.session.add(profile)

    @m.context("Get all distance")
    @m.it("Return all profiles")
    def test_get_all_profile(self, client, init_table):
        profiles = Profile.query.all()
        # Compare dict
        assert len(profiles) >= 1

    @m.context("Get distance by id")
    @m.it("Return a distance. 'id' is 1")
    def test_get_profile_by_id(self, client, init_table):
        profile = Profile.query.get(1)
        # Compare dict
        assert profile is not None

    @m.context("Update distance by id")
    @m.it("Successfully Updated a distance. 'id' is 1")
    def test_update_profile_by_id(self, client):
        # Input
        new_data = {
            "id": 1,
            "start_time": 1.0,
            "update_time": 1.0,
            "traversed": False,
            "age_history": [1],
            "processed_age": 1,
            "gender_history": [1],
            "processed_gender": 1,
            "id_history": ["updated test"],
            "processed_id": "test",
        }
        Profile.query.filter_by(id=1).update(new_data)
        db.session.commit()

        resp = Profile.query.filter_by(id=1).first()
        actual_data = resp.to_dict()
        # Compare dict
        is_equal = compare_dict(actual_data, new_data)
        assert is_equal is True

    @m.context("Delete distance by id")
    @m.it("Successfully deleted a distance. 'id' is 1")
    def test_update_profile_by_id(self, client):
        Profile.query.filter_by(id=1).delete()
        db.session.commit()

        profile = Profile.query.filter_by(id=1).first()
        assert profile is None
