__author__ = 'Daniel'
from itertools import takewhile


file = open('2013/S2/s2.1.in')

W = int(file.readline())
N = int(file.readline())
weights = [int(file.readline()) for n in range(N)]
weight_sum = [sum(weights[max(0, n-3):n+1]) for n in range(N)]
print(len(list(takewhile(lambda x: x<=W, weight_sum))))