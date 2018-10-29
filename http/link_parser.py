#!/usr/bin/env python
import ssl
from html.parser import HTMLParser
from urllib.request import Request, urlopen

ssl._create_default_https_context = ssl._create_unverified_context


class Parser(HTMLParser):
    tags = []

    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):

        self.tags.append(tag)

        if tag == 'enclosure':
            for attr, value in attrs:
                if attr == 'url' and value.startswith('http'):
                    print('url =', value)
                    break

    def handle_data(self, data):
        data = data.strip()
        if data.strip() != "":
            tag = self.tags[-1]
            print(tag, ':', data)

    def handle_endtag(self, tag):
        self.tags.pop()


parser = Parser()

headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0',
    'Accept': 'image/jpg,image/*,*/*',
    'Accept-Encoding': 'gzip,deflate,br',
    'Accept-Language': 'en-US,en'
}
url = "https://docs.python.org/3/library/urllib.html"
req = Request(url, headers=headers)
site = urlopen(url)
html = site.read()

parser.feed(html.decode('utf-8'))
