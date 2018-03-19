#!/usr/bin/env python
import time


def fibonacci(n):
    if n > 1:
        return fibonacci(n - 1) + fibonacci(n - 2)
    else:
        return n


if __name__ == "__main__":
    f = 40
    start = time.time()
    print(fibonacci(f))
    end = time.time()
    print(end - start)
