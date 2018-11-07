#!/usr/bin/env python

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def reverse(a, n):
    i = 0
    n -= 1

    while (i < n):
        swap(a, i, n)
        i += 1
        n -= 1


array = [1, 2, 3, 4]

print array
reverse(array, 2)
print array
reverse(array, 3)
print array
reverse(array, 2)
print array
reverse(array, 3)
print array
reverse(array, 2)
print array
reverse(array, 4)
print array
reverse(array, 2)
print array
reverse(array, 3)
print array
reverse(array, 2)
print array
reverse(array, 3)
print array
reverse(array, 2)
print array
reverse(array, 4)
print array
reverse(array, 2)
print array
reverse(array, 3)
print array
reverse(array, 2)
print array
reverse(array, 3)
print array
reverse(array, 2)
print array
reverse(array, 4)
print array
reverse(array, 2)
print array
reverse(array, 3)
print array
reverse(array, 2)
print array
reverse(array, 3)
print array
reverse(array, 2)
print array
