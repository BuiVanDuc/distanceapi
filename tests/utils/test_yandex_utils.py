import mock

from pytest import mark as m
from app.utils.yandex_utils import is_coordinate_in_mkad, find_distance_to_mkad, find_shortest_distance_to_mkad
from yandex_geocoder.exceptions import InvalidKey, NothingFound, UnexpectedResponse


@m.describe("Test yandex_utils")
class TestYandexUtils(object):

    @m.context("Check coordinate inner MKAD or not")
    @m.it("Return True")
    def test_is_coordinate_in_mkad(self):
        # Input
        coordinate = (37.841217, 55.739103)
        # Then
        result = is_coordinate_in_mkad(coordinate)
        assert result is True

    @m.context("Check coordinate inner MKAD or not")
    @m.it("Return False")
    def test_is_coordinate_in_mkad(self):
        # Input
        coordinate = (37.841217,)
        # Then
        result = is_coordinate_in_mkad(coordinate)
        assert result is False

    @m.context("Find out distance to MKAD")
    @m.it("Return distance is None")
    def test_find_distance_to_mkad(self):
        # Input
        address = ""
        # Then
        actual_result = find_distance_to_mkad(address)
        assert actual_result is None

    @m.context("Find out distance to MKAD")
    @m.it("Address is inner MKAD area. Return distance is 0")
    @mock.patch('app.utils.yandex_utils.YANDEX_CLIENT')
    def test_find_distance_to_mkad(self, mock_yandex_client):
        # Input
        address = "somewhere"
        # Mock
        mock_yandex_client.coordinates.return_value = (37.611212, 55.757972)
        # Then
        actual_result = find_distance_to_mkad(address)
        assert actual_result == 0

    @m.context("Find out distance to MKAD")
    @m.it("Exception: Not found")
    @mock.patch('app.utils.yandex_utils.YANDEX_CLIENT')
    def test_find_distance_to_mkad(self, mock_yandex_client):
        # Input
        address = "somewhere"
        # Mock
        mock_yandex_client.coordinates.side_effect = NothingFound
        # Then
        actual_distance = find_distance_to_mkad(address)
        assert actual_distance == -1

    @m.context("Find out distance to MKAD")
    @m.it("Exception:Unexpected Response")
    @mock.patch('app.utils.yandex_utils.YANDEX_CLIENT')
    def test_find_distance_to_mkad(self, mock_yandex_client):
        # Input
        address = "somewhere"
        # Mock
        mock_yandex_client.coordinates.side_effect = UnexpectedResponse
        # Then
        actual_distance = find_distance_to_mkad(address)
        assert actual_distance == -2

    @m.context("Find out distance to MKAD")
    @m.it("Exception:Invalid key")
    @mock.patch('app.utils.yandex_utils.YANDEX_CLIENT')
    def test_find_distance_to_mkad(self, mock_yandex_client):
        # Input
        address = "somewhere"
        # Mock
        mock_yandex_client.coordinates.side_effect = InvalidKey
        # Then
        actual_distance = find_distance_to_mkad(address)
        assert actual_distance == -3

    @m.context("Check coordinate is inner MKAD or not")
    @m.it("Return: False")
    def test_is_coordinate_in_mkad(self):
        # Input
        coordinate = (1,)
        # Then
        result = is_coordinate_in_mkad(coordinate)
        assert result is False

    @m.context("Check coordinate is inner MKAD or not")
    @m.it("Return: True")
    def test_is_coordinate_in_mkad(self):
        # Input
        coordinate = (37.611212, 55.757972)
        # Then
        result = is_coordinate_in_mkad(coordinate)
        assert result is True

    @m.context("Find shortest distance to MKAD")
    @m.it("min distance")
    def test_find_shortest_distance_to_mkad(self):
        # Input
        coordinate = (37.611212, 55.757972)
        # Then
        result = find_shortest_distance_to_mkad(coordinate)
        assert result >= 0
