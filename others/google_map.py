import datetime

import googlemaps

# Replace the API key below with a valid API key.
gmaps = googlemaps.Client(key='AIzaSyBZ8tzhKfcs6rOuRvLAjap6dKT39G9g3xw')

# Geocoding and address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)
