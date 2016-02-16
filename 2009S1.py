__author__ = 'Daniel'
from math import *


def cool_less_than(n):
    # round to 12 decimal places to eliminate floating point error
    return floor(round(n**(1/6), 12))


file = open('2009/s1/s1.5.in')
lines = file.readlines()
# simply see how many cool number there are less than the minimum, and subtract that from the number of cool numbers
#  below the maximum
print(cool_less_than(int(lines[1])) - cool_less_than(int(lines[0]) - 1))