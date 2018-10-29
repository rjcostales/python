#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup

url = 'https://www.raspberrypi.org/'
response = requests.get(url=url, verify=False)

page = BeautifulSoup(response.content, 'html.parser')

for a in page.find_all('a'):
    print("----")
    print(a.string, a['href'])
