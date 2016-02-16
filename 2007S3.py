__author__ = 'Daniel'
import heapq


def separation(a, b):
    # calculates the degree of separation between two people
    visited = {a}
    que = []
    heapq.heappush(que, (-1, a))
    while que:
        nxt = heapq.heappop(que)
        if nxt[1] == b:
            return nxt[0]
        for f in friends[nxt[1]]:
            if f not in visited:
                heapq.heappush(que, (nxt[0]+1, f))
                visited.add(f)
    return -1

file = open('2007/s3/s3.2.in')
N = int(file.readline())
# initialize the array of sets that will store the graph
friends = [set() for x in range(10000)]
for n in range(N):
    # input each forced friendship into the graph
    x, y = map(int, file.readline().split())
    friends[x].add(y)

# read the two people we must find the degree of separation of
x, y = map(int, file.readline().split())
while x != 0:
    s = separation(x, y)
    # are they connected?
    if s != -1:
        print('Yes', s)
    else:
        print('No')
    # read the next pair
    x, y = map(int, file.readline().split())