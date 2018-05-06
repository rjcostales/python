import json

import requests

r = requests.get("http://api.giphy.com/v1/gifs/search?q=puppies&api_key=20ETF5kMibhng2nxxVe5G01NKBx3XUO8")

print(r.status_code)

j = json.loads(r.text)

print(json.dumps(j["data"][0], indent=2))
