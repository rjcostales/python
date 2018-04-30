import random


def flip(r):
    count = 0

    for i in range(r):
        call = random.randint(0, 1)
        coin = random.randint(0, 1)
        print(call, coin, coin == call)
        if coin == call:
            count += 1

    return count


print(flip(1000))
