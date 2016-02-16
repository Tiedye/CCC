__author__ = 'Daniel'
from heapq import *
from operator import *
from itertools import *


INF = 1000*5000+1

file = open('2010/S4/s4.5.in')
M = int(file.readline())

# reading data

edges = [[INF for i in range(M+1)] for j in range(M+1)]
unclaimed = dict()

for m in range(M):
    t = [int(x) for x in file.readline().split()]
    ns = t[0]
    sides = zip([tuple(sorted(x)) for x in zip(t[1:1+ns], t[2:1+ns] + t[1:2])], t[1+ns:])
    for side in sides:
        if side[0] in unclaimed:
            n = unclaimed.pop(side[0])[1]
            edges[m][n] = min(side[1], edges[m][n])
            edges[n][m] = min(side[1], edges[n][m])
        else:
            unclaimed[side[0]] = (side[1], m)

for side in unclaimed:
    edges[M][unclaimed[side][1]] = min(unclaimed[side][0], edges[M][unclaimed[side][1]])

# Prim's algorithm


def min_heap(l):
    nl = []
    for n in range(len(l)):
        if l[n] != INF:
            heappush(nl, (l[n], n))
    heappush(nl, (INF, -1))
    return nl


min_edges_original = list(map(min_heap, edges))

min_edges = [m_s.copy() for m_s in min_edges_original]

total = 0
next_node = heappop(min_edges[M])
visited = {M}
while len(visited) != M+1:
    while next_node[1] in visited:
        next_node = heappop(min(map(getitem, repeat(min_edges), visited)))
    if next_node[1] == -1:
        total = INF
        break
    total += next_node[0]
    visited.add(next_node[1])

with_outside = total

min_edges = [m_s.copy() for m_s in min_edges_original]

total = 0
next_node = heappop(min_edges[0])
visited = {0}

while len(visited) != M:
    while next_node[1] in visited:
        next_node = heappop(min(map(getitem, repeat(min_edges), visited)))
    if next_node[1] == -1:
        total = INF
        break
    total += next_node[0]
    visited.add(next_node[1])

with_inside = total

print(min(with_outside, with_inside))

