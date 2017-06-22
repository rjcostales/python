#!/usr/bin/env python
import sys

f = open(sys.argv[0], "rb")

while 1:

    try:

        x = f.read(4)
        print(hex(ord(x[0])), hex(ord(x[1])), hex(ord(x[2])), hex(ord(x[3])))

    except Exception:

        break
