from flask_restplus import Resource, Api

from app.api import api
from ...utils.yandex_utils import find_distance_to_mkad

api = Api(api, doc="/docs")

name_space = api.namespace("api/distance", description="Find the distance from the MKAD to the specified address")


@name_space.route("/<string:address>")
@api.param("address", "Enter address here")
class Distance(Resource):
    def get(self, address):
        """ Get distance"""
        result = find_distance_to_mkad(address)
        if result == 0:
            return {"message": "The address is inner MKAD"}, 200
        if result == -1:
            return {"message": "Not Found"}, 404
        elif result == -2:
            return {"message": "Unexpected Response"}, 500
        elif result == -3:
            return {"message": "Invalid key"}, 400
        return {'distance': '{} Km'.format(result)}, 200
