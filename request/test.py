import requests

## info
url = 'http://www.google.com/finance/info'

params = {'q': 'AAPL'}

response = requests.get(url, params,)

print(response.content.decode('utf-8'))


## historical
url = 'http://www.google.com/finance/historical'

params = {
    'q': 'GOOG',
    'startdate':'01-Jan-16',
    'enddate':'31-Dec-16',
    'output':'csv'
}

response = requests.get(url, params,)

data = response.content.decode('utf-8')
print(data)
print(len(data.split('\n')))
