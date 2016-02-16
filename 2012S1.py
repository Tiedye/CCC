__author__ = 'Daniel'
from itertools import accumulate


file = open('2012/S1/s1.1.in')
print(list(accumulate([max((1+1/2*(n-4))*(n-3), 0) for n in range(100)]))[int(file.readline())])