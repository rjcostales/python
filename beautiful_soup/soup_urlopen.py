#!/usr/bin/env python
from urllib.error import HTTPError
from urllib.request import urlopen

from bs4 import BeautifulSoup


def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        soup = BeautifulSoup(html.read(), features="html.parser")
        title = soup.body.h1
    except AttributeError as e:
        return None
    return title


title = get_title("http://www.pythonscraping.com/pages/page1.html")
if title is None:
    print("Title could not be found")
else:
    print(title)
