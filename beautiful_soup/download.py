#!/usr/bin/env python3
import re
import ssl
from time import sleep
from urllib.request import Request, urlopen

import requests
from bs4 import BeautifulSoup

ssl._create_default_https_context = ssl._create_unverified_context


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

    for img in soup.find_all('img', class_='wallpapers__image'):
        count += 1
        src = img['src']
        link = re.sub(r'300x168', '1920x1080', src)
        name = re.sub(r'.*/', '', link)
        img = get_image(link)
        if img is not None:
            with open('./' + name, 'wb') as jpg:
                jpg.write(img.read())
                jpg.close()
            print(name)
    sleep(1)
    return count


url = 'https://wallpaperscraft.com/catalog/textures/1920x1080'

if process_page(url) == 0:
    exit()

for page in range(2, 10):
    if process_page(url + '/page' + str(page)) == 0:
        exit()
