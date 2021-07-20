# from flask_restful import marshal
from flask_restplus import Resource, Api

from app.api import api
from ...helpers.error_handlers import NotFoundError, ServerError
from ...utils.yandex_utils import find_distance_from_somewhere_to_mkad

api = Api(api, doc="/docs")

name_space = api.namespace("distance_api", description="use api to find distance")


@api.errorhandler(NotFoundError)
def handle_custom_exception(error):
    return error.to_dict(), getattr(error, 'code')


@api.errorhandler
def default_error_handler(error):
    """Returns Internal server error"""
    error = ServerError()
    return error.to_dict(), getattr(error, 'code', 500)


@name_space.route("/")
@api.response(404, "address does not exist")
@api.param("address", "Enter address here")
class ProfileItem(Resource):
    @api.response(code=200, description='Success')
    @api.response(code=404, description='Not Found')
    def get(self, address):
        """ Get distance by address"""
        distance = find_distance_from_somewhere_to_mkad(address)
        return {'distance': distance}
