#!/usr/bin/env python
import time


def fib(n):
    a, b = 0, 1
    while n > 0:
        n, a, b = n - 1, b, a + b
    return a


def fibonacci(n):
    if n > 1:
        return fibonacci(n - 1) + fibonacci(n - 2)
    if n == 1:
        return 1
    if n == 0:
        return 0


if __name__ == "__main__":
    start = time.time()
    print(fibonacci(40))
    end = time.time()
    print(end - start)
