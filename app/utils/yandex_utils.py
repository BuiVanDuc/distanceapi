from yandex_geocoder import Client

client = Client("")

coordinates = client.coordinates("MKAD")

print(coordinates)
