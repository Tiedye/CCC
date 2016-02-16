__author__ = 'Daniel'
from math import *


# return the number of hydrants required to cover the houses with a given hose length
def hydrants_required(hl, l):
    # hl is a list of houses, l is the maximum length of hose available
    ml = 0  # minimum length of hose required
    hc = 1  # hydrant count
    cs = hl[0]  # current starting house for the group
    for h in hl[1:]:
        # loop through each house, if it is close enough to the current starting house, than it can be covered by the
        # same hose as that house
        if h - cs < l:
            ml = max(ml, h - cs)
            # keep track or the amount of hose required to cover the houses, its the longest hose required in the set
        else:
            # if the house is too far away, make it the beginning of the next group of houses and increment the hydrant
            # count
            cs = h
            hc += 1
    return hc, ml
    # return the hydrants required and the hose length used


# return the hose required to cover a given number of houses starting a a certain house
def hose_required(sh, l):
    if sh != 0:
        hl = houses[sh:]+[h + RL for h in houses[0:sh]]
    else:
        hl = houses
    # sh is the starting house, so make n array of the positions clockwise of all houses after that house, ill draw some
    # pictures and send them via facebook
    hc = 0  # hydrants required for the current hose length
    ll = 0  # current length being tested
    cl = l  # last resulting minimum length
    while hc <= hydrants:  # loop until the current length requires too many hydrants
        ll = cl  # if we have enough hydrants to satisfy the last length than the last length becomes the current one
        hc, cl = hydrants_required(hl, ll-1)  # make the length a bit smaller and see if it still works
    return ll

RL = 1000000  # road length
file = open('2010/S3/s3.8.in')
lines = file.readlines()
hydrants = int(lines[-1])
houses = []
for house in lines[1:-1]:
    houses.append(int(house))
houses.sort()
if hydrants >= len(houses):
    print(0)
    quit()
length = ceil(1000000 / hydrants)
i = 0
while houses[i] - houses[0] < length:
    # try starting at any house that's less than the smallest length found so far from the starting house
    length = hose_required(i, length)
    i += 1

# this took a loooong time to figure out, I first looked at it a month ago and just figured out the solution today
# I'll send some drawings to illustrate it better
print(ceil(length/2))