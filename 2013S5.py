__author__ = 'Daniel'


file = open('2013/S5/s5.15.in')

N = int(file.readline())
points = 0

while N != 1:
    factor = 2
    while N % factor != 0:
        factor += 1
    N -= N // factor
    points += factor-1

print(points)