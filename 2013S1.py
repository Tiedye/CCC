__author__ = 'Daniel'


file = open('2013/S1/s1.1.in')

Y = int(file.readline()) + 1

while len(set(str(Y))) != len(str(Y)):
    Y += 1

print(Y)