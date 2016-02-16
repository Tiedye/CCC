__author__ = 'Daniel'
from itertools import *


file = open('2013/S3/s3.8.in')

T = int(file.readline())
G = int(file.readline())

remaining_games = [game for game in combinations(range(1, 5), 2)]
set_games = []


def pointify(x, o):
    lst = [0 for i in range(4)]
    if o == 1:
        lst[x[0]-1] = 3
    elif o == -1:
        lst[x[1]-1] = 3
    else:
        lst[x[0]-1] = 1
        lst[x[1]-1] = 1

    return tuple(lst)

for g in range(G):
    s, a, sa, sb = [int(t) for t in file.readline().split()]
    result = sa - sb
    if result != 0:
        result /= abs(sa - sb)
    remaining_games.remove((s, a))
    set_games.append(pointify((s, a), result))

win_count = 0
game_outcomes = product([1, 0, -1], repeat=6 - G)
for outcome in game_outcomes:
    current_tally = set_games.copy()
    for game in range(len(remaining_games)):
        current_tally.append(pointify(remaining_games[game], outcome[game]))
    game_sum = list(map(sum, zip(*current_tally)))
    t = game_sum.pop(T-1)
    if t > max(game_sum):
        win_count += 1

print(win_count)