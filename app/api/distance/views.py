from flask_restplus import Resource, Api

from app.api import api
from ...utils.yandex_utils import find_distance_to_mkad

api = Api(api, doc="/docs")

name_space = api.namespace("api/distance", description="Search distance to MKD")


@name_space.route("/<string:address>")
@api.param("address", "Enter address here")
class Distance(Resource):
    def get(self, address):
        """ Get distance by address"""
        result = find_distance_to_mkad(address)
        if result == 0:
            return {"message": "The address in MKAD"}
        if result == -1:
            return {"message": "Not Found"}
        elif result == -2:
            return {"message": "Unexpected Response"}
        elif result == -3:
            return {"message": "Invalid key"}
        return {'distance': '{}.Km'.format(result)}
