__author__ = 'Daniel'
import operator
from collections import Counter


file = open('2011/s2/s2.5.in')
lines = [line.strip() for line in file.readlines()]
N = int(lines[0])
set1 = lines[1:1+N]
set2 = lines[1+N:]
results = Counter(map(operator.eq, set1, set2))
print(results[True])