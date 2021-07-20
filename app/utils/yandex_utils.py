from decimal import Decimal
# from app.logger.logger import log
from yandex_geocoder import Client
from geopy.distance import geodesic

from logger_utils import log

MKAD = (Decimal('37.632206'), Decimal('55.898947'))
YANDEX_CLIENT = Client("af81ec10-d933-43fb-90f0-6157977e812d")


def find_distance_from_somewhere_to_mkad(address: str):
    distance = -1
    if not address and len(address) == 0:
        return distance
    coordinates = YANDEX_CLIENT.coordinates(address)
    distance = geodesic(MKAD, coordinates).km
    log.info("Distance from: {} to MKD is: {}".format(address, distance))
    print(distance)
    return distance


if __name__ == '__main__':
    address = "MKAD"
    find_distance_from_somewhere_to_mkad("MKAD")