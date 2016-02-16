__author__ = 'Daniel'


file = open('j5/j5.1.in')
N = int(file.readline())
K = int(file.readline())
states = []
for k in range(K):
    kstate = []
    for n in range(N):
        nstate = []
        for m in range(N):
            if k == 0 or n == 0:
                if m < n:
                    nstate.append(0)
                else:
                    nstate.append(1)
            else:
                nstate.append(-1)
        kstate.append(nstate)
    states.append(kstate)


def pie(lt, pc, mp):
    if states[lt][pc][mp] == -1:
        states[lt][pc][mp] = sum([pie(lt-1, p, min(pc-p, p)) for p in range(max(pc-mp, 0), pc)])
    return states[lt][pc][mp]

print(pie(K-1, N-K, N-K))