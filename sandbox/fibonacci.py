#!/usr/bin/env python


def fibonacci(n):
    if n > 1:
        return fibonacci(n - 1) + fibonacci(n - 2)
    else:
        return n


if __name__ == "__main__":
    n = 40
    f = fibonacci(n)
    print(f)
