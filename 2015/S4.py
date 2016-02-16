from heapq import *

file = open('s4.7.in')
K, N, M = map(int, file.readline().split())
routes = [{} for n in range(N)]
for m in range(M):
    a, b, t, h = map(int, file.readline().split())
    routes[a-1].setdefault(b-1, []).append((t, h))
    routes[b-1].setdefault(a-1, []).append((t, h))


INF = 10**10


p, q = map(int, file.readline().split())
p, q = p-1, q-1

min_time = INF
distance = [[INF for i in range(200+1)] for n in range(N)]
distance[p][K] = 0
visited = set()
que = [(0, p, K)]
while que:
    island = heappop(que)
    if island[1] == q:
        min_time = island[0]
        break
    if island[1:] in visited:
        continue
    visited.add(island[1:])
    for destination in routes[island[1]]:
        for route in routes[island[1]][destination]:
            to_add = (distance[island[1]][island[2]] + route[0], destination, island[2] - route[1])
            if to_add[2] > 0:
                if to_add[0] < distance[to_add[1]][to_add[2]]:
                    distance[to_add[1]][to_add[2]] = to_add[0]
                heappush(que, to_add)
if min_time == INF:
    min_time = -1

print(min_time)