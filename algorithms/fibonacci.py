#!/usr/bin/env python
import time


def fibonacci(n):
    if n > 1:
        return fibonacci(n - 1) + fibonacci(n - 2)
    else:
        return n


if __name__ == "__main__":
    nn = 40
    start = time.time()
    ff = fibonacci(nn)
    end = time.time()
    print(ff)
    print(end - start)
