__author__ = 'Daniel'
from math import *
from itertools import accumulate


file = open('2009/S5/S5.6.in')

# read the number of east west streets M,  the number of north south streets N, and the number of coffee shops
M = int(file.readline())
N = int(file.readline())
K = int(file.readline())

# initialize the grid that will hold the signal strength at every point
signal = [[0 for m in range(M+1)] for n in range(N)]

# read all the shops into memory
shops = []
for k in range(K):
    shops.append(tuple([int(t) for t in file.readline().split()]))

for shop in shops:
    # for each shop cycle through each vertical column it effects
    x, y, r, b = shop
    r2 = r**2
    for n in range(max(x - r, 1), min(x + r + 1, N + 1)):
        xd = x - n
        yd = floor((r2 - xd**2)**(1/2))  # find the range that this column effects
        signal[n-1][max(y - yd - 1, 0)] += b
        signal[n-1][min(y + yd, M)] -= b

bit = 0
count = 0
# count up the coffee shops with the highest bit counts
for n in signal:
    for m in accumulate(n):
        if m > bit:
            bit = m
            count = 1
        elif m == bit:
            count += 1

print(bit, count, sep='\n')