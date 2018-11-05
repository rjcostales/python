import json

import requests

API_KEY = "20ETF5kMibhng2nxxVe5G01NKBx3XUO8"

response = requests.get("http://api.giphy.com/v1/gifs/search?api_key=%s&q=%s" % (API_KEY, "puppies"))

print(response.status_code)

text = json.loads(response.text)
data = text["data"]

for dat in data:
    print(json.dumps(dat["title"]), json.dumps(dat["images"]["preview"]["mp4"]))
