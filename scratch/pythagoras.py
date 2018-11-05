#!/usr/bin/env python
import math


def is_pythagoras(a, b):
    c = a * a + b * b

    for s in range(a, a + b):
        if c == s * s:
            print math.atan2(a, b) * 180.0 / math.pi, s, a, b


for a in range(1, 50):
    for b in range(a, 50):
        is_pythagoras(a, b)
