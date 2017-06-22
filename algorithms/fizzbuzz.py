print("0:")
for i in range(1,101):
    print("%i:" % i, sep='', end='')
    if (i % 3) == 0: print("fizz", end='')
    if (i % 5) == 0: print("buzz", end='')
    print()
