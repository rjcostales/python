#!/usr/bin/env python
import time

sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


def fibonacci(n):
    if n > 10:
        return 55 * fibonacci(n - 9) + 34 * fibonacci(n - 10)
    else:
        return sequence[n]


if __name__ == "__main__":
    start = time.time()
    f = fibonacci(100)
    stop = time.time()
    print(f, stop - start)