#!/usr/bin/env python
import random
import sys

try:
    spin = float(sys.argv[1])
except:
    spin = 38

rand = random
tot = 0
oe = 0
hl = 0
lg = 0
md = 0
sm = 0
color = 0
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
blk = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

for i in range(spin):

    n = rand.randint(-1, 36)
    tot += n
    print(n, '\t', )

    # odd/even
    if n % 2:
        oe += 1
        print('odd', '\t', )
    else:
        oe -= 1
        print('eve', '\t', )

    if n > 18:
        hl += 1
        print('hi', '\t', )
    elif n > 0:
        hl -= 1
        print('lo', '\t', )
    else:
        print('-', '\t', )

    if n > 24:
        lg += 1
        print('lg ', '\t', )
    elif n > 12:
        md += 1
        print('md ', '\t', )
    elif n > 0:
        sm += 1
        print('sm ', '\t', )
    else:
        print('-', '\t')

    if n in red:
        color += 1
        print('red')

    if n in blk:
        color -= 1
        print('blk')

print('----------')
print('%1.4f' % (tot * 1.0 / spin))
print('odd/even\t\t', oe)
print('high/low\t\t', hl)
print('red/black\t', color)
print('large\t\t', lg)
print('medium\t\t', md)
print('small\t\t', sm)
print(spin - (lg + md + sm))
