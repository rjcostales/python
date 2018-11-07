import random

l = []
for i in range(1, 70):
    l.append(i)

l.remove(4)
l.remove(35)
l.remove(48)
l.remove(56)
l.remove(60)

l.remove(9)
l.remove(30)
l.remove(47)
l.remove(52)
l.remove(54)

l.remove(1)
l.remove(7)
l.remove(13)
l.remove(32)
l.remove(39)

l.remove(24)
l.remove(28)
l.remove(38)
# l.remove(52)
l.remove(59)

# l.remove(1)
# l.remove(3)
# l.remove(26)
# l.remove(47)
# l.remove(68)
r = random

r.seed(4995)
r.shuffle(l)

c = 0
for i in l:
    c += 1
    print(i, )
    if (c % 5) == 0:
        print

print(len(l))
