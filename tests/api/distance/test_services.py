import mock
import pytest
from pytest import mark as m

from app.api.distance.services import ProfileService
from app.helpers.error_handlers import NotFoundError


@pytest.fixture()
def new_profile_service(mocker):
    print("setup")
    mocked_profile = mocker.patch('app.api.distance.services.Profile')
    mocked_session = mocker.patch('app.api.distance.services.db.session')

    yield ProfileService(mocked_profile, mocked_session)
    print("teardown")


@m.describe("Test distance service")
class TestProfileService(object):

    @m.context("Create distance")
    @m.it("Successfully created a distance")
    def test_create_profile(self, new_profile_service):
        # Input
        profile = {"test": 1}
        is_result = new_profile_service.create_profile(profile)
        new_profile_service.session.add.assert_called()
        new_profile_service.session.commit.assert_called()

    @m.context("Get distance by id")
    @m.it("Return a distance. 'id' is 1")
    def test_get_by_id(self, new_profile_service):
        # Input
        id = 1
        new_profile_service.model.query.get.return_value = {"id": 1, "test": 1}
        actual_result = new_profile_service.get_by_id(id)
        expected_result = {"id": 1, "test": 1}
        new_profile_service.model.query.get.assert_called()
        # Assert
        assert actual_result == expected_result

    @m.context("Get all profiles")
    @m.it("Return list profiles")
    def test_get_all(self, new_profile_service):
        # Expected input
        expected_result = [{"test": 1}]

        new_profile_service.model.query.all.return_value = [{"test": 1}]
        actual_result = new_profile_service.get_all()
        assert expected_result == actual_result

    @m.context("Get all profiles. Has no distance in DB")
    @m.it("Return a empty list")
    def test_get_all(self, new_profile_service):
        # Expect input
        expected_result = []

        new_profile_service.model.query.all.return_value = None
        actual_result = new_profile_service.get_all()
        assert expected_result == actual_result

    @m.context("Update distance by id")
    @m.it("Successfully updated distance")
    def test_update_by_id(self, new_profile_service):
        # Input
        id = 1
        new_data = {"test": 1}
        query_filter = mock.Mock()
        # Mock number of records
        query_filter.count.return_value = 1
        new_profile_service.model.query.filter_by.return_value = query_filter
        # Mock session
        session = new_profile_service.session
        # Then
        new_profile_service.update_by_id(id, new_data)
        # Assert
        print(query_filter.update)
        query_filter.update.assert_called()
        session.commit.assert_called()

    @m.context("Update distance by id. ID does not exist")
    @m.it("Fail to update a distance")
    def test_update_by_id_(self, new_profile_service):
        # Input
        id = 1
        new_data = {"test": 1}
        query_filter = mock.Mock()
        # Mock number of records
        query_filter.count.return_value = 0
        new_profile_service.model.query.filter_by.return_value = query_filter
        # Assert
        with pytest.raises(NotFoundError) as e_info:
            new_profile_service.update_by_id(id, new_data)

    @m.context("Delete distance by id")
    @m.it("Successfully deleted a distance. 'id' is 1")
    def test_delete_by_id(self, new_profile_service):
        # Input
        id = 1
        query_filter = mock.Mock()
        # Mock number of records
        query_filter.count.return_value = 1
        new_profile_service.model.query.filter_by.return_value = query_filter
        # Mock session
        session = new_profile_service.session
        # Then
        new_profile_service.delete_by_id(id)
        # Assert
        query_filter.delete.assert_called()
        session.commit.assert_called()

    @m.context("Delete distance by id. ID does not exist")
    @m.it("Fail to delete distance")
    def test_delete_by_id_(self, new_profile_service):
        # Input
        id = 1
        query_filter = mock.Mock()
        # Mock number of records
        query_filter.count.return_value = 0
        new_profile_service.model.query.filter_by.return_value = query_filter
        # Assert
        with pytest.raises(NotFoundError) as e_info:
            # Then
            new_profile_service.delete_by_id(id)
