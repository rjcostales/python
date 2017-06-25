#!/usr/bin/env python
from html.parser import HTMLParser
from urllib.request import urlopen


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

url = 'http://revision3.com/haktip/feed/MP4-hd30'
site = urlopen(url)
html = site.read().strip()
print(html)
parser.feed(html.decode('utf-8'))
