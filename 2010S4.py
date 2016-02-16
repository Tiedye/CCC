__author__ = 'Daniel'
from heapq import *


INF = 1000*5000+1

file = open('2010/S4/s4.5.in')
M = int(file.readline())

# reading data
edges = [{} for j in range(M+1)]  # we will store the edges of the graph as a array of dictionaries
unclaimed = {}  # this will hold all of the fences that have yet to be paired up along with the node it is attached to


for m in range(M):
    t = [int(x) for x in file.readline().split()]  # read the pen data into memory
    ns = t[0]  # the first number is the number of sides on this pen
    sides = zip([tuple(sorted(x)) for x in zip(t[1:1+ns], t[2:1+ns] + t[1:2])], t[1+ns:])  # this pairs the sides with
                                                                                           #  the cost of that side
    for side in sides:
        # loop through every side
        if side[0] in unclaimed:
            # if the side has an unclaimed partner, add add edge between those two nodes to the graph with the right
            #  weight and remove it from the dict of unclaimed sides
            n = unclaimed.pop(side[0])[1]
            # this checks if there is already a side there already and sets that edge to the cheapest of the two
            edges[m][n] = min(side[1], edges[m].setdefault(n, INF))  # setdefault gets a value and returns INF if not
            edges[n][m] = min(side[1], edges[n].setdefault(m, INF))
        else:
            # otherwise add this side to the list of unclaimed sides with its cost information
            unclaimed[side[0]] = (side[1], m)

for side in unclaimed:
    # for every side that remains unclaimed, we assume its connected to the outside so we add a one way connection
    #  from the outside (M) to every node with an unclaimed side with the specified cost
    edges[M][unclaimed[side][1]] = min(unclaimed[side][0], edges[M].setdefault(unclaimed[side][1], INF))

# this converts our graph from an array of dicts to an array of lists that hold tuples that contain the cost of an edge
#  and then the node it connects to
processed_edges = [[tuple(reversed(pair)) for pair in pen.items()] for pen in edges]

# Prim's algorithm
# the starting edge is the outside node, as we cannot travel to the outside node this will be our with outside value
next_edges = processed_edges[M] + [(INF, -1)]  # add all the edges attached to the starting edge to the queue
heapify(next_edges)  # this allows us to quickly return the minimum in a list
visited = {M}  # nodes that we have evaluated
next_node = heappop(next_edges)
total = 0
while len(visited) != M+1:
    while next_node[1] in visited:
        # keep getting the next shortest edge until it leads to a node we have yet to visit
        next_node = heappop(next_edges)
    if next_node[1] == -1:  # if there are no more edges exit, and set the total to INF as we cannot create the tree
        total = INF
        break
    total += next_node[0]  # add the value of that edge to the total value of the tree
    visited.add(next_node[1])  # add this node to the visited set
    for e in processed_edges[next_node[1]]:
        heappush(next_edges, e)  # add all the attached edges to the queue

with_outside = total

# do all that again, but this time start on the inside so the outside node will be excluded
next_edges = processed_edges[0] + [(INF, -1)]
heapify(next_edges)
visited = {0}
next_node = heappop(next_edges)
total = 0
while len(visited) != M:
    while next_node[1] in visited:
        next_node = heappop(next_edges)
    if next_node[1] == -1:
        total = INF
        break
    total += next_node[0]
    visited.add(next_node[1])
    for e in processed_edges[next_node[1]]:
        heappush(next_edges, e)

with_inside = total


# print the smallest of the two trees
print(min(with_outside, with_inside))