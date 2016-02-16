__author__ = 'Daniel'


file = open('S2.in')

J = int(file.readline())
A = int(file.readline())

Js = set()
Jm = set()
Jl = set()
As = []
Am = []
Al = []

for j in range(J):
    s = file.readline().strip()
    if s == 'S':
        Js.add(j+1)
    elif s == 'M':
        Jm.add(j+1)
    elif s == 'L':
        Jl.add(j+1)

for a in range(A):
    s, n = file.readline().split()
    n = int(n)
    if s == 'S':
        As.append(n)
    elif s == 'M':
        Am.append(n)
    elif s == 'L':
        Al.append(n)

satisfied = 0
nAs = []
for p in As:
    if p in Js:
        Js.remove(p)
        satisfied += 1
    else:
        nAs.append(p)
As = nAs
nAs = []
for p in As:
    if p in Jm:
        Jm.remove(p)
        satisfied += 1
    else:
        nAs.append(p)
As = nAs
for p in As:
    if p in Jl:
        Jl.remove(p)
        satisfied += 1
nAm = []
for p in Am:
    if p in Jm:
        Jm.remove(p)
        satisfied += 1
    else:
        nAm.append(p)
Am = nAm
for p in Am:
    if p in Jl:
        Jl.remove(p)
        satisfied += 1
for p in Al:
    if p in Jl:
        satisfied += 1
print(satisfied)