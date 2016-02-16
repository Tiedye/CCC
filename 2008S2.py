__author__ = 'Daniel'
from math import *


file = open('2008/s2/s2.3.in')
radi = [int(r) for r in file.readlines()[:-1]]

for r in radi:
    # store r^2 so we don't have to recalculate it
    r2 = r**2
    corner = 0
    # calculate the volume of a corner row by row
    for y in range(1, r):
        corner += floor(sqrt(r2 - y**2))
    # print 4 corners plus the 4 radi (the lines connecting the corners) plus one (the center)
    print(corner*4+r*4+1)