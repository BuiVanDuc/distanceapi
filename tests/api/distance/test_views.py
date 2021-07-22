from unittest import mock

from tests.constants import PROFILE_API
from pytest import mark as m


@m.describe("Test v1 distanceapi")
class TestDistanceAPI(object):

    @m.context("The '/v1/api/distance/' api is requested (GET)")
    @m.it("Address is inner MKAD")
    @mock.patch('app.api.distance.views.find_distance_to_mkad')
    def test_get_distance(self, mock_find_distance, client):
        # Mock
        mock_find_distance.return_value = 0
        # Input
        address = "somewhere"
        # Then
        response = client.get("{}{}".format(PROFILE_API, address))
        actual_message = response.json
        assert actual_message["message"] == "The address is inner MKAD"
        assert response.status_code == 200

    @m.context("The '/v1/api/distance/' api is requested (GET)")
    @m.it("Return not found")
    @mock.patch('app.api.distance.views.find_distance_to_mkad')
    def test_get_distance(self, mock_find_distance, client):
        # Mock
        mock_find_distance.return_value = -1
        # Input
        address = "somewhere"
        # Then
        response = client.get("{}{}".format(PROFILE_API, address))
        actual_message = response.json
        assert actual_message["message"] == "Not Found"
        assert response.status_code == 404

    @m.context("The '/v1/api/distance/' api is requested (GET)")
    @m.it("Return Unexpected Response")
    @mock.patch('app.api.distance.views.find_distance_to_mkad')
    def test_get_distance(self, mock_find_distance, client):
        # Mock
        mock_find_distance.return_value = -2
        # Input
        address = "somewhere"
        # Then
        response = client.get("{}{}".format(PROFILE_API, address))
        actual_message = response.json
        assert actual_message["message"] == "Unexpected Response"
        assert response.status_code == 500

    @m.context("The '/v1/api/distance/' api is requested (GET)")
    @m.it("Return distance")
    @mock.patch('app.api.distance.views.find_distance_to_mkad')
    def test_get_distance(self, mock_find_distance, client):
        # Mock
        mock_find_distance.return_value = 1.0
        # Input
        address = "somewhere"
        # Then
        response = client.get("{}{}".format(PROFILE_API, address))
        actual_message = response.json
        assert actual_message["distance"] == "1.0 Km"
        assert response.status_code == 200
