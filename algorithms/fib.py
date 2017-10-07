#!/usr/bin/env python
import time


def fibonacci(n):
    if n > 1:
        return fibonacci(n - 1) + fibonacci(n - 2)
    if n == 1:
        return 1
    if n == 0:
        return 0


if __name__ == "__main__":
    start = time.time()
    print(fibonacci(100))
    end = time.time()
    print(end - start)
