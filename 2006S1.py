__author__ = 'Daniel'
import string
from functools import *
from itertools import *
from operator import *


file = open('2006/s1/s1.3.in')

P1_raw = file.readline()
P2_raw = file.readline()


def interpret(s):
    if s.isupper():
        return 3
    elif s.islower():
        return 1
    else:
        return 2

P1 = [interpret(P1_raw[i:i+2]) for i in range(0, 10, 2)]
P2 = [interpret(P2_raw[i:i+2]) for i in range(0, 10, 2)]

PT = map(max, zip(P1, P2))
PT = list(map(lambda x: x%3+1, PT))

N = int(file.readline())

for n in range(N):
    baby_raw = file.readline()
    baby = [interpret(baby_raw[i]) for i in range(5)]
    baby = map(lambda x: x % 3+1, baby)
    if reduce(min, map(and_, baby, PT), 3) != 0:
        print('Possible baby.')
    else:
        print('Not their baby!')