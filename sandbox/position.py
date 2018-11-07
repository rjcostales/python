#!/usr/bin/env python

from math import acos, atan2, cos, modf, pi, sin

# from math import sqrt

a2r = pi / 180.0
r2a = 180.0 / pi
e_rad = 6378.0 * 1000.0
e_cir = 2 * pi * e_rad


def distance(p, q):
    a = p[0] * a2r
    b = q[0] * a2r
    d = (q[1] - p[1]) * a2r

    c = cos(a) * cos(b) * cos(d) + sin(a) * sin(b)

    try:
        return acos(c) * e_rad
    except ArithmeticError:
        return 0.0


def bearing(p, q):
    a = -sin(p[1] - q[1]) * cos(q[0])
    b = cos(p[0]) * sin(q[0]) - sin(p[0]) * cos(q[0]) * cos(p[1] - q[1])

    return atan2(a, b) * r2a


def move(pos, ang, dst):
    dx = dst * sin(ang * a2r)
    dy = dst * cos(ang * a2r)

    deg_m_lat = 360.0 / e_cir

    try:
        deg_m_lon = deg_m_lat / cos(pos[0] * a2r)
    except ArithmeticError:
        deg_m_lon = 0

    lat = pos[0] + (dy * deg_m_lat)
    lon = pos[1] + (dx * deg_m_lon)

    return (lat, lon)


def dms(d):
    (f, d) = modf(d)
    (f, m) = modf(f * 60)
    s = f * 60

    return (d, m, s)


def deg(d, m, s):
    return d + (m + s / 60.0) / 60.0


def lat(p):
    return p[0]


def lon(p):
    return p[1]


################################################################################

old = (10.0, 0.0)
new = move(old, 123, 456.7)
print(dms(lat(new)))
print(dms(lon(new)))
print('distance %03.1f' % distance(old, new))
print('bearing  %03.1f' % bearing(old, new))
