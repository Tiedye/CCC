__author__ = 'Daniel'


file = open('2012/S5/s5.5.in')
R, C = map(int, file.readline().split())
cages = [[-1 for x in range(C)] for y in range(R)]
K = int(file.readline())
for k in range(K):
    r, c = map(int, file.readline().split())
    cages[r-1][c-1] = 0
cages[0][0] = 1

for x in range(1, C):
    if cages[0][x] != 0:
        cages[0][x] = cages[0][x-1]

for y in range(1, R):
    if cages[y][0] != 0:
        cages[y][0] = cages[y-1][0]

for y in range(1, R):
    for x in range(1, C):
        if cages[y][x] != 0:
            cages[y][x] = cages[y][x-1] + cages[y-1][x]

print(cages[-1][-1])