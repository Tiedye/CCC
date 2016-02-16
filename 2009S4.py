__author__ = 'Daniel'
from heapq import *


file = open('2009/s4/s4.5.in')
N = int(file.readline())
T = int(file.readline())
# read the number of cities N and the number of routes T


routes = [[-1]*(N+1) for n in range(N+1)]  # construct our blank matrix to hold our graph
# this graph has one additional node which a city will be connected to if it can sell pencils, the weight of that edge
#  will be the cost of a pencil in that city, this node will be node zero

for t in range(T):
    # input each edge into the graph
    tokens = file.readline().split()
    routes[int(tokens[0])][int(tokens[1])] = int(tokens[2])
    routes[int(tokens[1])][int(tokens[0])] = int(tokens[2])

# read the cites that can sell pencils into the graph
K = int(file.readline())
for k in range(K):
    tokens = file.readline().split()
    routes[int(tokens[0])][0] = int(tokens[1])

# read the destination city
D = int(file.readline())


# now we will use Dijkstra's algorithm to find the shortest path between node zero and the destination

def get_routes(x):
    # this returns all of the cities attached to city x as a list, it could also be a set it would have the same effect
    #  (though when you are not using the 'in' keyword, lists can be faster as in this case)
    cr = []
    for i in range(len(routes[x])):
        if routes[x][i] != -1:
            cr.append(i)
    return cr

# we define infinity to be a big number (25,000,000 x 10,000 + 10000)
INF = 250000010000
# we start with the distance to each node set to infinity, and since we're starting at our destination city we set the
#  distance to that city to zero
distance = [INF] * (N+1)
distance[D] = 0

nxt = []
heappush(nxt, (0, D))  # we add the fist node with distance zero to the queue
while nxt:
    cc = heappop(nxt)[1]  # we get the next closest city (heapq returns the minimum value in the set)

    if distance[cc] == -1:
        continue
    if cc == 0:
        print(distance[0])
        break
    nc = get_routes(cc)
    for c in nc:
        distance[c] = min(distance[c], distance[cc] + routes[cc][c])  # is the distance from this point to the next
                                                                      #  smaller than the previously calculated distance
        heappush(nxt, (distance[c], c))
    distance[cc] = -1