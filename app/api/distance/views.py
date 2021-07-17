# from flask_restful import marshal
from flask_restplus import Resource, Api, marshal
from sqlalchemy.orm.exc import NoResultFound

from app.api import api
# from .errors import errors
# from .errors import errors
from .serializers import ProfileSerializer
from .services import ProfileService
from app.helpers.json_respone import JsonReponse
from app.models import Profile

# from ...helpers.error_handlers import NotFoundError
from ...helpers.error_handlers import NotFoundError, ServerError

api = Api(api, doc="/docs")

# api from methods below will have /my_api prefix which is defined here
name_space = api.namespace("distance", description="API Profile")

# Define the expected model (to validate the input)
api_profile = ProfileSerializer(api)
service = ProfileService()


@api.errorhandler(NotFoundError)
def handle_custom_exception(error):
    return error.to_dict(), getattr(error, 'code')


@api.errorhandler
def default_error_handler(error):
    """Returns Internal server error"""
    error = ServerError()
    return error.to_dict(), getattr(error, 'code', 500)


@name_space.route("/")
class ProfileCollection(Resource):
    @api.response(200, "success")
    @api.marshal_with(api_profile.model_response, envelope="distance")
    def get(self):
        """Get distance"""
        return
