#!/usr/bin/python
import ephem

location = ephem.Observer()
location.lat = '32.22'  # Tucson, AZ
location.lon = '-110.97'  # Tucson, AZ
location.elevation = 112
print(location.date)

sun = ephem.Sun()
r1 = location.next_rising(sun)
s1 = location.next_setting(sun)

location.horizon = '-0:34'
r2 = location.next_rising(sun)
s2 = location.next_setting(sun)
print("Visual sunrise %s" % r1)
print("Visual sunset %s" % s1)
print("Naval obs sunrise %s" % r2)
print("Naval obs sunset %s" % s2)
