from datetime import date
from math import radians as rad, degrees as deg

import ephem

observer = ephem.Observer()
observer.name = 'Somewhere'
# observer.lat = '32.22'  # Tucson, AZ
# observer.lon = '-110.97'  # Tucson, AZ
observer.lat = rad(32.22)  # lat/long in decimal degrees
observer.long = rad(-110.97)

moon = ephem.Moon()

observer.date = date.today()  # local time zone, I'm in UTC+1
observer.date -= ephem.hour  # always everything in UTC

for i in range(24):  # compute position for every 15 minutes
    moon.compute(observer)

    nnm = ephem.next_new_moon(observer.date)
    pnm = ephem.previous_new_moon(observer.date)
    # for use w. moon_phases.ttf A -> just past  newmoon,
    # Z just before newmoon
    # '0' is full, '1' is new
    # note that we cannot use m.phase as this is the percentage of the moon
    # that is illuminated which is not the same as the phase!
    lunation = (observer.date - pnm) / (nnm - pnm)
    symbol = lunation * 26
    if symbol < 0.2 or symbol > 25.8:
        symbol = '1'  # new moon
    else:
        symbol = chr(ord('A') + int(symbol + 0.5) - 1)

    print('time, alt, az, phase, symbol')
    print(ephem.localtime(observer.date).time().strftime("%H:%M"),
          deg(moon.alt),
          deg(moon.az),
          moon.phase,
          symbol)
    observer.date += ephem.minute * 60
