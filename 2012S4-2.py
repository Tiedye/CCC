__author__ = 'Daniel'
from collections import deque
from time import clock


def is_valid(state, pos):
    if len(state[pos]) == 1:
        return True
    elif state[pos][-1] < state[pos][-2]:
        return True
    else:
        return False


def next_moves(state):
    if len(state) <= 1:
        return []
    new_states = []
    new_state = (state[0][:-1], state[1]+state[0][-1:])+state[2:]
    if new_state != state and is_valid(new_state, 1) and new_state not in moves:
        new_states.append(new_state)
        moves[new_state] = moves[state] + 1
    new_state = state[:-2]+(state[-2]+state[-1][-1:], state[-1][:-1])
    if new_state != state and is_valid(new_state, -2) and new_state not in moves:
        new_states.append(new_state)
        moves[new_state] = moves[state] + 1
    for i in range(1, len(state)-1):
        new_state = state[:i]+(state[i][:-1], state[i+1]+state[i][-1:])+state[i+2:]
        if new_state != state and is_valid(new_state, i+1) and new_state not in moves:
            new_states.append(new_state)
            moves[new_state] = moves[state] + 1
        new_state = state[:i-1]+(state[i-1]+state[i][-1:], state[i][:-1])+state[i+1:]
        if new_state != state and is_valid(new_state, i-1) and new_state not in moves:
            new_states.append(new_state)
            moves[new_state] = moves[state] + 1
    return new_states

file = open('2012/S4/s4.5.in')
srt_time = clock()
while True:
    n = int(file.readline())
    if n == 0:
        break
    start_state = tuple((int(t),) for t in file.readline().split())
    end_state = tuple((n,) for n in range(1, n+1))
    moves = {start_state: 0}
    que = deque()
    que.append(start_state)
    while que:
        nxt = que.popleft()
        if nxt == end_state:
            print(moves[end_state])
            break
        que.extend(next_moves(nxt))
    else:
        print('IMPOSSIBLE')
end_time = clock()
print(end_time-srt_time)