from collections import deque
from functools import reduce
from itertools import *
from operator import *

__author__ = 'Daniel'


def bigger_not_smaller(a, b):
    if a > b:
        return not reduce(and_, map(lt, a, b), True)
    else:
        return False


def wider(a, b):
    return a[0] < b[0] and a[1] > b[1]


def thinner(a, b):
    return a[0] > b[0] and a[1] < b[1]

file = open('S5.in')

N = int(file.readline())
original_pie = []
for n in range(N):
    original_pie.append(int(file.readline()))

M = int(file.readline())


pie_ordered = original_pie.copy()
pie_to_add = set()
for m in range(M):
    pie_to_add.add(int(file.readline()))
pie_to_add = frozenset(pie_to_add)

states = [{} for i in range(M+N-1)]
initial_states = permutations(pie_to_add | frozenset([-1]), 2)
for state in initial_states:
    cul = (0, 0)
    val = (0, 0)
    if -1 in state:
        rn = pie_to_add - frozenset([state[(state.index(-1) + 1) % 2]])
        cul = tuple(accumulate((pie_ordered[0] if s == -1 else s for s in state), max))
        val = (1, rn)
    else:
        rn = pie_to_add - frozenset(state)
        cul = tuple(accumulate(state, max))
        val = (0, rn)
    co = states[0].setdefault(val, [(0, 0)])
    i = 0
    while i < len(co):
        if bigger_not_smaller(cul, co[i]):
            co[i] = cul
            i += 1
            while i < len(co):
                if bigger_not_smaller(co[i-1], co[i]):
                    del co[i]
                else:
                    break
            break
        elif thinner(cul, co[i]):
            co.insert(i, cul)
            break
        elif wider(cul, co[i]):
            i += 1
        else:
            break
    states[0][val] = co
states[0].setdefault((2, pie_to_add), []).append(tuple(accumulate(pie_ordered[0:2], max)))

for i in range(0, M+N-1):
    for state in states[i]:
        for np in state[1]:
            val = (state[0], state[1] - frozenset([np]))
            co = states[i+1].setdefault(val, [(0, 0)])
            for pcul in states[i][state]:
                cul = (pcul[1], max(pcul[1], pcul[0] + np))
                j = 0
                while j < len(co):
                    if bigger_not_smaller(cul, co[j]):
                        co[j] = cul
                        j += 1
                        while j < len(co):
                            if bigger_not_smaller(co[j-1], co[j]):
                                del co[j]
                            else:
                                break
                        break
                    elif thinner(cul, co[j]):
                        co.insert(j, cul)
                        break
                    elif wider(cul, co[j]):
                        j += 1
                    else:
                        break
            states[i+1][val] = co
            # states[i+1].append(((state[0][1], max(state[0][1], state[0][0] + np)), state[1], state[2] - frozenset([np])))
        if state[0] < N:
            val = (state[0]+1, state[1])
            co = states[i+1].setdefault(val, [(0, 0)])
            for pcul in states[i][state]:
                cul = (pcul[1], max(pcul[1], pcul[0] + pie_ordered[state[0]]))
                j = 0
                while j < len(co):
                    if bigger_not_smaller(cul, co[j]):
                        co[j] = cul
                        j += 1
                        while j < len(co):
                            if bigger_not_smaller(co[j-1], co[j]):
                                del co[j]
                            else:
                                break
                        break
                    elif thinner(cul, co[j]):
                        co.insert(j, cul)
                        break
                    elif wider(cul, co[j]):
                        j += 1
                    else:
                        break
                else:
                    co.insert(j, cul)
            states[i+1][val] = co
            #states[i+1].append(((state[0][1], max(state[0][1], state[0][0] + pie_ordered[state[1]])), state[1]+1, state[2]))
max = 0
for state in states[-1]:
    for ss in states[-1][state]:
        if ss[1] > max:
            max = ss[1]
print(max)