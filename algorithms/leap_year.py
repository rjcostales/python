#!/usr/bin/env python

for y in range(0, 2001):

    if y % 400 == 0:
        print(y)
    elif (y % 100 != 0) & (y % 4 == 0):
        print(y)
        # if y % 4 == 0:
        #     if y % 100 != 0:
        #         print(y)
        #     elif y % 400 == 0:
        #         print(y)
