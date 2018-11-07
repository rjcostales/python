#!/usr/bin/env python

primes = [2]

lastprime = 2

for n in range(4):

    # lastprime = primes[len(primes) -  1]
    start = lastprime + 1
    end = (lastprime * lastprime) + 1

    for i in range(start, end):
        test = 1

        for p in primes:
            test *= (i % p)
        if test:
            lastprime = i
            print
            i
            primes.append(i)
