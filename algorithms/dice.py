#!/usr/bin/env python
import random


def roll3():
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    c = random.randint(1, 6)
    arr = [a, b, c]
    arr.sort(reverse=True)
    return arr


def roll2():
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    arr = [a, b]
    arr.sort(reverse=True)
    return arr


print(roll3())
print(roll2())
