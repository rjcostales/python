#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup

url = 'https://www.ultimate-guitar.com/tabs/bob_dylan_tabs4.htm.htm'
response = requests.get(url=url, verify=True)

page = BeautifulSoup(response.content, 'html.parser')

for a in page.find_all('a'):
    print("----")
    print(a.string, a['href'])
