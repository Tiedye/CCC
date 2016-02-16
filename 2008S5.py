__author__ = 'Daniel'
from time import clock
import operator

states = {}     # this will store the calculated results
# this is a list of all the possible moves a person can take, each list represents the amount of each respective
#  reactant that is used up
moves = [(2, 1, 0, 2), (1, 1, 1, 1), (0, 0, 2, 1), (0, 3, 0, 0), (1, 0, 0, 1)]


def find_winner(state):
    # this memorizes the results of the function so we don't have to recalculate them
    if state in states:
        return states[state]

    win = 0
    for m in moves:
        # check to see if and of the moves results in a win
        new_state = tuple(map(operator.sub, state, m))
        if min(new_state) >= 0:  # if any of the particle counts are negative its an invalid state
            result = find_winner(new_state)
            win = max(result, win)

    # this is part of the memorization thing
    states[state] = (win + 1) % 2
    return states[state]


file = open('2008/s5/s5.4.in')
N = int(file.readline())
# there are N test cases
for n in range(N):
    # I solved this problem recursively, I defined a function (find_winner) that returns 0 if the current player would
    #  win and 1 if the current player would lose.  It does this by saying if the next player would win no matter what
    #  the current player does the current player loses.
    initial_particles = tuple([int(t) for t in file.readline().split()])
    # Patrick always starts and thus is the first current player and so if the function return one, Patrick loses
    if find_winner(initial_particles) == 1:
        print('Roland')
    else:
        print('Patrick')
