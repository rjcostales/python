#!/usr/bin/env python


def swap(r, a, b):
    if a != b:
        temp = r[a]
        r[a] = r[b]
        r[b] = temp
        # print "  swap", a, b, r


def permute(r, n):
    i = n

    if i > 0:

        while (i != 0):
            i -= 1

            swap(r, n - 1, i)
            print("  b", i, r)

            permute(r, n - 1)

            swap(r, i, n - 1)
            print("  a", i, r)

    else:

        print(i, r)


array = [1, 2, 3, 4]

permute(array, len(array))
