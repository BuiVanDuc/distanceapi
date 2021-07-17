import json
from pytest import mark as m
from tests.constants import PROFILE_API, PROFILE_RESPONSE
from tests.helpers import compare_dict


@m.describe("Test v1 api distance")
class TestProfileCollection(object):

    @m.context("The 'v1/profiles/' api is requested (GET)")
    @m.it("Return all profiles")
    def test_get_all_profiles(self, client, init_table):
        response = client.get(PROFILE_API)
        # Compare dict
        expected_dict = PROFILE_RESPONSE
        actual_dict = response.json['profiles'][0]
        # Assert
        assert response.status_code == 200
        is_equal = compare_dict(expected_dict, actual_dict)
        assert is_equal is True

    @m.context("The 'v1/profiles/' api is requested (POST)")
    @m.it("Successfully created a distance")
    def test_create_new_profile(self, client, init_table):
        data = {
            "create_time": 1,
            "update_time": 1,
            "traversed": False,
            "age_history": [1],
            "processed_age": 1,
            "gender_history": [1],
            "processed_gender": 1,
            "id_history": ["test"],
            "processed_id": "test"
        }

        response = client.post(
            PROFILE_API,
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
        )
        assert response.status_code == 200
        assert response.json == {"code": 201, "message": "success", "status": "ok"}


@m.describe("Test v1 api distance")
class TestProfileItem(object):

    @m.context("The 'v1/profiles/1' api is requested (GET) with id is 1")
    @m.it("Return a distance. 'id' is 1")
    def test_get_profile_by_id(self, client, init_table):
        id = 1
        response = client.get("{}{}".format(PROFILE_API, id))
        expected_dict = PROFILE_RESPONSE
        actual_dict = response.json
        is_equal = compare_dict(actual_dict, expected_dict)
        assert response.status_code == 200
        assert is_equal is True

    @m.context("The 'v1/profiles/1' api is requested (PUT) with id is 1")
    @m.it("Successfully updated a distance. 'id' is 1")
    def test_update_profile_by_id(self, client, init_table):
        id = 1
        data = {
            "create_time": 1,
            "update_time": 1,
            "age_history": [1],
            "traversed": False,
            "processed_age": 1,
            "gender_history": [1],
            "processed_gender": 1,
            "id_history": ["Updated test"],
            "processed_id": "test"
        }

        response = client.put(
            "{}{}".format(PROFILE_API, id),
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
        )
        assert response.status_code == 200
        assert response.json == {"code": 200, "message": "success", "status": "ok"}

    @m.context("The 'v1/profiles/1' api is requested (DELETE)")
    @m.it("Successfully deleted a distance. 'id' is 1")
    def test_delete_profile_by_id(self, client, init_table):
        id = 1
        response = client.delete("{}{}".format(PROFILE_API, id))
        assert response.status_code == 200
        assert response.json == {"code": 200, "message": "success", "status": "ok"}
