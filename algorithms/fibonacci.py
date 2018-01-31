#!/usr/bin/env python
import time


def f(n):
    if n > 1:
        return f(n - 1) + f(n - 2)
    if n == 1:
        return 1
    if n == 0:
        return 0


if __name__ == "__main__":
	n = 40
    start = time.time()
    print(f(n))
    end = time.time()
    print(end - start)
