#!/usr/bin/env python
import math


def estimate(x):
    p = x * math.pi
    return int(round(p, 0))


if __name__ == "__main__":
    min = 1000.0
    for denominator in range(1, 1000):
        numerator = estimate(denominator)
        guess = 1.0 * numerator / denominator
        diff = abs(guess - math.pi)
        if diff < min:
            min = diff
            pin = numerator
            pid = denominator

        print(numerator, guess, diff)

    print(1.0 * pin / pid, pin, pid)
    print(math.pi, abs(1.0 * pin / pid - math.pi))
