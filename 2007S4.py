__author__ = 'Daniel'


file = open('2007/s4/s4.5.in')

N = int(file.readline())
connections = [set() for n in range(N)]     # initialize the empty graph
path_counts = [0 for n in range(N)]         # stores the number of ways we cen get to a particular marker backwards
path_counts[0] = 1                          # there is 1 way to get to the first marker (get on the slide)
while True:
    # read each connection into the graph
    x, y = map(int, file.readline().split())
    if x == 0:
        break
    connections[x-1].add(y-1)
for n in range(N):
    # for each marker, add the number of ways you can get to that marker to the markers its attached to
    for connection in connections[n]:
        path_counts[connection] += path_counts[n]
# print the number of ways you can get to the final marker
print(path_counts[-1])