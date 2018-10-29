import json

import requests

API_KEY = "20ETF5kMibhng2nxxVe5G01NKBx3XUO8"

r = requests.get("http://api.giphy.com/v1/gifs/search?q=puppies&api_key=%s" % API_KEY)

print(r.status_code)

j = json.loads(r.text)

print(json.dumps(j["data"][0], indent=2))
