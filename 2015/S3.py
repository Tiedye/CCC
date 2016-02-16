__author__ = 'Daniel'


file = open('S3.in')

G = int(file.readline())
P = int(file.readline())

Pi = [int(file.readline()) for p in range(P)]
D = [False for g in range(G)]

docked = 0
for p in Pi:
    i = p
    while D[i-1]:
        i -= 1
        if i == 0:
            break
    else:
        D[i-1] = True
        docked += 1
        continue
    break
print(docked)