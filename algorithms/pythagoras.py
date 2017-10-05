#!/usr/bin/env python
import math

limit = 60
solutions = []


def is_pythagoras(a, b):
    c = a * a + b * b

    for s in range(a, a + b):
        ang = 0.0
        if c == s * s:
            ang = math.atan2(a, b) * 180.0 / math.pi
            if ang not in solutions:
                print(ang, s, a, b)
            break
    return ang


if __name__ == "__main__":

    for a in range(1, limit):
        for b in range(a, limit):
            ang = is_pythagoras(a, b)

            if ang not in solutions:
                solutions.append(ang)

    solutions.sort()
    print(solutions)
    print(len(solutions))
