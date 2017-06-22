#!/usr/bin/env python
from json import loads
from urllib.request import urlopen

apiUrl = "http://www.nhtsa.gov/webapi/api/SafetyRatings"
# apiParam = "/ModelYear/2016/Make/Ford/Model/Mustang"
apiParam = '/VehicleId/11570'
outputFormat = "?format=json"

# Combine all three variables to make up the complete request URL
response = urlopen(apiUrl + apiParam + outputFormat)
print(response.url)

# code below is only to handle JSON response object/format
# use equivalent sets of commands to handle xml response object/format
content = response.read()

enc = response.headers.get_content_charset()
data = loads(content.decode(enc))

# Load the Result (vehicle collection) from the JSON response
print('Result')
for datum in data['Results']:
    # Loop each vehicle in the vehicles collection
    for key, value in datum.items():
        print("/%s/%s" % (key, value))
    print('-----')
