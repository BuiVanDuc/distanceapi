import mock
import datetime

from pytest import mark as m

from app.utils.yandex_utils import is_coordinate_in_mkad, find_distance_to_mkad


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
    @m.it("Return None")
    def test_find_distance_to_mkad(self):
        # Input
        address = "somewhere"
        # Mock
        mock_yandex_client = mock.Mock()
        # Then
        actual_result = find_distance_to_mkad(address)
        assert actual_result == 0

    @m.context("Convert datetime to second with 'datetime' is smaller than 1970/01/01")
    @m.it("Return None and warning message")
    def test_convert_datetime_str_to_datetime(self, capsys):
        # Input
        date_time = datetime.datetime(1969, 1, 1)
        # Then
        actual_result = convert_datetime_to_second(date_time)
        captured = capsys.readouterr()
        assert actual_result is None
        assert "Time is start from 1970/1/1" in captured.out

    @m.context("Convert datetime to second with 'datetime' is string type")
    @m.it("Return None and warning message")
    def test_convert_datetime_str_to_datetime(self, capsys):
        # Input
        date_time = "test"
        # Then
        actual_result = convert_datetime_to_second(date_time)
        captured = capsys.readouterr()
        assert actual_result is None
        assert "Convert datetime to second is error" in captured.out
