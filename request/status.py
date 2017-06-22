import requests

url = 'http://codex'

response = requests.get(url)

status_code = response.status_code

print(status_code)
