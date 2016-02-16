__author__ = 'Daniel'
from operator import le, and_
from functools import reduce


file = open('2007/s2/s2.1.in')

# first read all the box sizes into an array with their volume, and then sort them by volume
N = int(file.readline())
boxes = []
for n in range(N):
    # we store the dimensions of the box smallest to greatest because we need each individual dimension to be larger or
    #  equal to the items dimension, if its not sorted, the comparison will not work
    s1, s2, s3 = sorted(map(int, file.readline().split()))
    boxes.append((s1*s2*s3, s1, s2, s3))
boxes.sort()

# read all of the item dimensions into an array as well
M = int(file.readline())
items = []
for m in range(M):
    s1, s2, s3 = sorted(map(int, file.readline().split()))
    items.append((s1, s2, s3))

for item in items:
    # check if each item can fit into one of the boxes
    for box in boxes:
        # this checks if each of the dimensions of the item are less  than or equal to the dimensions of the box
        if reduce(and_, map(le, item, box[1:]), True):
            print(box[0])
            break
    else:
        print('Item does not fit.')