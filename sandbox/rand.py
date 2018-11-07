#!/usr/bin/env python

import random
import sys

try:
    a = float(sys.argv[1])
except:
    a = 0.0

try:
    b = float(sys.argv[2])
except:
    b = 1.0

print a, b

r = random
tot = 0.0
rnd = 0.0

for i in range(100):
    rnd = r.gauss(a, b)
    print '%1.4f' % r.gauss(a, b)
    tot += rnd

print 'rnd = ', rnd
