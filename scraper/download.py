#!/usr/bin/env python3
import re
from time import sleep
from urllib.request import Request, urlopen

import requests
from bs4 import BeautifulSoup


def get_image(url):
    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0',
        'Accept': 'image/jpg,image/*,*/*',
        'Accept-Encoding': 'gzip,deflate,br',
        'Accept-Language': 'en-US,en'
    }
    try:
        req = Request(url, headers=headers)
        return urlopen(req)
    except ValueError:
        print(ValueError)
        print('ERROR:' + url)
        return None


def process_page(url):
    count = 0
    print(url)
    html = requests.get(url)
    print(html.status_code)
    soup = BeautifulSoup(html.text, 'html.parser')

    for div in soup.find_all('div', class_='pre_name'):
        count += 1
        href = div.a['href']
        name = re.sub(r'.*/', 'macro/', href) + '.jpg'
        link = re.sub(r'.*/', 'http://wallpaperscraft.com/image/', href) + '_1024x768.jpg'
        print(link)
        img = get_image(link)
        sleep(1)
        if img is not None:
            with open(name, 'wb') as jpg:
                jpg.write(img.read())
                jpg.close()
    sleep(3)
    return count


url = 'http://wallpaperscraft.com/catalog/macro/1024x768'

if process_page(url) == 0:
    exit()

for page in range(2, 100):
    print(page)
    if process_page(url + '/page' + str(page)) == 0:
        exit()
