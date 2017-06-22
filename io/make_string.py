n = 105

cids = ''

for i in range(n * 1000, (n + 1) * 1000):
    cids += str(i) + ','
print(cids[0:-1])
