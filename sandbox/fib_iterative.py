#!/usr/bin/env python
import time


def fibonacci(n):
    a, b = 0, 1
    while n > 0:
        n, a, b = n - 1, b, a + b
    return a


if __name__ == "__main__":
    nn = 100
    start = time.time()
    ff = fibonacci(nn)
    stop = time.time()
    print(ff, stop - start)
