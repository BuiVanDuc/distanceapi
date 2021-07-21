from decimal import Decimal
from geopy.distance import geodesic
from app.constant.mkad import MKAD_COORDINATE
from app.constant.yandex import YANDEX_CLIENT
from .logger_utils import logger
from shapely.geometry import Point, Polygon
from yandex_geocoder.exceptions import InvalidKey, NothingFound, UnexpectedResponse

MKAD = (Decimal('37.632206'), Decimal('55.898947'))


def find_distance_to_mkad(address: str):
    distance = 0
    try:
        coordinates = YANDEX_CLIENT.coordinates(address)
        print(coordinates)
        # Check the address is in MKAD or not
        result = is_coordinate_in_mkad(coordinates)
        if result:
            logger.info("{} is inner MKAD")
            return distance

        distance = geodesic(MKAD, coordinates).km
        print(distance)
        logger.info("Distance from: {} to MKAD is: {} Km".format(address, distance))
        return distance
    except NothingFound:
        return -1
    except UnexpectedResponse:
        return -2
    except InvalidKey:
        return -3


def is_coordinate_in_mkad(coordinate: tuple):
    point = Point(coordinate)
    print(point)
    poly = Polygon(MKAD_COORDINATE)
    return point.within(poly)
