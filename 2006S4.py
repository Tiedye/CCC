from itertools import combinations_with_replacement

__author__ = 'Daniel'


file = open('2006/s4/s4.3.in')

while True:
    N = int(file.readline())
    if N == 0:
        break
    m = [list(map(int, file.readline().split())) for n in range(N)]
    # test for identity
    identity = 0
    for r in range(N):
        for c in range(N):
            if m[r][c] != c+1:
                break
        else:
            identity = r+1
            for r2 in range(N):
                if m[r2][identity-1] != r2+1:
                    identity = 0
    # test for inverse
    failed = False
    for r in range(N):
        for c in range(N):
            if m[r][c] == identity:
                if m[c][r] != identity:
                    failed = True
                    break
        else:
            continue
        break
    # test for associativity
    combos = combinations_with_replacement(range(N), 3)
    associative = True
    for combo in combos:
        if m[m[combo[0]][combo[1]]-1][combo[2]] != m[combo[0]][m[combo[1]][combo[2]]-1]:
            associative = False
            break
    if identity and not failed and associative:
        print('yes')
    else:
        print('no')