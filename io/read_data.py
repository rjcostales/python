#!/usr/bin/env python3
import random

f = open("winnums-text.txt", "r")

print
f.readline()
c1 = []
c2 = []
c3 = []
c4 = []
c5 = []
pb = []
for l in f:
    date, d1, d2, d3, d4, d5, p, pp = l.split()
    c1.append(d1)
    c2.append(d2)
    c3.append(d3)
    c4.append(d4)
    c5.append(d5)
    pb.append(p)

random.shuffle(c1)
random.shuffle(c2)
random.shuffle(c3)
random.shuffle(c4)
random.shuffle(c5)
random.shuffle(pb)

size = len(pb)
r0 = random.randint(0, size)
r1 = random.randint(0, size)
r2 = random.randint(0, size)
r3 = random.randint(0, size)
r4 = random.randint(0, size)

print(c1[r0], c2[r0], c3[r0], c4[r0], c5[r0], pb[r0])
print(c1[r1], c2[r1], c3[r1], c4[r1], c5[r1], pb[r1])
print(c1[r2], c2[r2], c3[r2], c4[r2], c5[r2], pb[r2])
print(c1[r3], c2[r3], c3[r3], c4[r3], c5[r3], pb[r3])
print(c1[r4], c2[r4], c3[r4], c4[r4], c5[r4], pb[r4])
