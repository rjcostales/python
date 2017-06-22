import http.client

url = 'www.python.org'
conn = http.client.HTTPConnection(url)

conn.request("GET", "/")
response = conn.getresponse()

print('\nstatus')
print(response.status)

print('\nmsg')
print(response.msg)

print('\nheaders')
print(response.getheaders())
print(response.getheader("date"))
print(response.getheader('content-type'))
print(response.getheader('content-length'))

print('\nresponse')
length = response.length
print(length)
print(response.read(length))
