#!/usr/bin/env python

for i in range(1, 101):
    # print("%i:" % i, sep='', end='')
    if (i % 3) == 0: print("fizz", end='')
    if (i % 5) == 0: print("buzz", end='')
    # print()
    if (i % 3) != 0 or (i % 5) != 0: print(i)
    # if (i % 15) == 0: print("fizzbuzz")
    # elif (i % 5) == 0: print("buzz")
    # elif (i % 3) == 0: print("fizz")
    # else: print(i)
