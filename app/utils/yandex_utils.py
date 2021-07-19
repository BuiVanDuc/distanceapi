from decimal import Decimal

from yandex_geocoder import Client


client = Client("af81ec10-d933-43fb-90f0-6157977e812d")


coordinates = client.coordinates("Москва Льва Толстого 16")

print(coordinates)