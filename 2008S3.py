__author__ = 'Daniel'
from collections import deque


file = open('2008/s3/s3.4.in')

T = int(file.readline())
# read the number of test cases

for t in range(T):
    # read the number of rows and columns for this case
    R = int(file.readline())
    C = int(file.readline())
    # this is a graph problem in which we are trying to find the shortest path, since the graph isn't weithed we use a
    #  breadth first search
    access = []     # this will hold our graph, each grid cell will contain a number telling which cells its connected
                    #  to
    for r in range(R):
        # read each row
        ac = []
        access.append(ac)
        c = file.readline()
        for i in c:
            # read each character in each row
            # if we can go up and down, we set the ones bit to true, if we can go right and left, we set the twos bit
            #   to true.  This is just one way to do it, it makes for a bit of an optimization.
            if i == '*':
                ac.append(0)
            elif i == '+':
                ac.append(0b11)
            elif i == '-':
                ac.append(0b01)
            elif i == '|':
                ac.append(0b10)
    intCnt = [[-1 for i in range(C)] for i in range(R)]     # this will hold the number of intersection passed through
                                                            #  to get to each cell
    intCnt[0][0] = 1        # the number of intersections passed through to get to the first cell is 1

    que = deque([(0, 0)])
    while que:
        cc = que.popleft()

        if cc == (R-1, C-1):
            # quit if we get to the bottom right corner, we found a path
            break

        # this crates two list containing the points that we would go to if we...
        crl = [(cc[0], min(cc[1] + 1, C-1)), (cc[0], max(cc[1] - 1, 0))]    # went right or left
        cdu = [(min(cc[0] + 1, R-1), cc[1]), (max(cc[0] - 1, 0), cc[1])]    # went up or down

        # this will store all the points we can go to
        cl = []
        if access[cc[0]][cc[1]] & 0b01 != 0:
            # if we can go right or left add those points
            cl.extend(crl)
        if access[cc[0]][cc[1]] & 0b10 != 0:
            # if we can go up or down add those points
            cl.extend(cdu)

        for nc in cl:
            # for each of these new points if it can be visited and hasnt been visited already add it to the que and set
            #  its intersection count the intersection count of this current point plus one
            if access[nc[0]][nc[1]] != 0 and intCnt[nc[0]][nc[1]] == -1:
                intCnt[nc[0]][nc[1]] = intCnt[cc[0]][cc[1]] + 1
                que.append(nc)

    # print the intersection count of the final intersection (if we couldn't get to it it will be -1
    print(intCnt[R-1][C-1])