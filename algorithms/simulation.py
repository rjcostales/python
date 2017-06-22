#!/usr/bin/env python
import random


class Human:
    birth, sex = 0, 'f'

    def __init__(self, year):
        self.birth = year
        if (random.randint(0, 1)):
            self.sex = 'm'
        else:
            self.sex = 'f'

    def __str__(self):
        return str(self.birth) + " " + self.sex


males = females = 0
world = []

for year in range(2000):
    person = Human(year)

    if person.sex == 'm':
        males += 1
    else:
        females += 1

    print(person)
    world.append(person)

print(males, females)
print(len(world))
