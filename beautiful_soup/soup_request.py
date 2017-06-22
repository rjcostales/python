#!/usr/bin/env python
from urllib.request import urlopen

from bs4 import BeautifulSoup

url = 'http://www.raspberrypi.org/downloads/'
page = urlopen(url)

soup = BeautifulSoup(page, 'html.parser')

print(soup.text)
print(soup.prettify())

for link in soup.find_all('a', href=True):
    href = link['href']
    if href.startswith('http'):
        print('href =', href)
