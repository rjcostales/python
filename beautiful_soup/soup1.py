#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup

url = 'https://www.ultimate-guitar.com/top/top100.htm'
response = requests.get(url=url, verify=True)

page = BeautifulSoup(response.content, 'html.parser')

for a in page.find_all('a'):
    print("----")
    print(a.string, a['href'])
