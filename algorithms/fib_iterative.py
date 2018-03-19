#!/usr/bin/env python
import time


def fibonacci(n):
    a, b = 0, 1
    while n > 0:
        n, a, b = n - 1, b, a + b
    return a


if __name__ == "__main__":
    n = 100
    start = time.time()
    f = fibonacci(n)
    stop = time.time()
    print(f, stop - start)
