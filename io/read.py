#!/usr/bin/env python
import sys

with open(sys.argv[1], 'rt') as file:
    for line in file:
        print(line.strip())
