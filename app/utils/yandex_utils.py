from decimal import Decimal
from geopy.distance import geodesic
from app.constant.mkad import MKAD_COORDINATES
from app.constant.yandex import YANDEX_CLIENT
from .logger_utils import logger
from shapely.geometry import Point, Polygon
from yandex_geocoder.exceptions import InvalidKey, NothingFound, UnexpectedResponse


def find_distance_to_mkad(address: str):
    if len(address) <= 0:
        print("Invalid address input; Please enter specific address")
        return None
    try:
        distance = 0
        coordinate = YANDEX_CLIENT.coordinates(address)
        # Check the address is inner MKAD or not
        result = is_coordinate_in_mkad(coordinate)
        if result:
            logger.info("The {} is inner MKAD".format(address))
            return distance

        # Find distance
        distance = find_shortest_distance_to_mkad(coordinate)
        logger.info("Distance from: {} to MKAD is: {}Km".format(address, distance))
        return distance
    except NothingFound:
        return -1
    except UnexpectedResponse:
        return -2
    except InvalidKey:
        return -3


def is_coordinate_in_mkad(coordinate: tuple):
    if len(coordinate) <= 1:
        print("Invalid coordinate; Right coordinate format: (lat, long)")
        return False
    point = Point(coordinate)
    poly = Polygon(MKAD_COORDINATES)
    return point.within(poly)


def find_shortest_distance_to_mkad(coordinate: tuple):
    # Init min distance
    min_distance = geodesic(MKAD_COORDINATES[0], coordinate).km
    for i in range(1, len(MKAD_COORDINATES) - 1):
        distance = geodesic(MKAD_COORDINATES[i], coordinate).km
        if distance > min_distance:
            min_distance = distance
    return min_distance
