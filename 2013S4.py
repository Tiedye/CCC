from collections import deque

__author__ = 'Daniel'


file = open('2013/S4/s4.6-5.in')

N, M = map(int, file.readline().split())

shorter = [set() for n in range(N)]

def taller(p, q):
    que = deque([p])
    while que:
        c = que.popleft()
        if c == q:
            return True
        que.extend(shorter[c])
    else:
        return False

for m in range(M):
    x, y = map(int, file.readline().split())
    shorter[x-1].add(y-1)

p, q = map(int, file.readline().split())
if taller(p-1, q-1):
    print('yes')
elif taller(q-1, p-1):
    print('no')
else:
    print('unknown')