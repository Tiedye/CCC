__author__ = 'Daniel'
from itertools import *
from math import *
import operator

operators = [operator.add, operator.sub, operator.mul, operator.truediv]
INF = 13**4+1


def next_hands(c_hand):
    hands = set()
    to_combine = list(combinations(c_hand, 2))  # this gives us a list of all possible combinations of 2 cards
    to_leave = list(reversed(list(combinations(c_hand, len(c_hand)-2))))    # this gives us all the cards that aren't
                                                                            #  used for each pair of cards
    for op in operators:
        # apply each of the operators I defined earlier to each pair
        for i in range(len(to_combine)):
            try:
                result = op(*to_combine[i])
            except ZeroDivisionError:
                result = INF
            if floor(result) != result:
                result = INF
            if result != INF:
                # only add that result to the new set of hands if it didn't divide by zero or result in a decimal
                hands |= {tuple(sorted((int(result),) + to_leave[i]))}

            # now try the same thing but switch the order of the pair
            try:
                result = op(*reversed(to_combine[i]))
            except ZeroDivisionError:
                result = INF
            if floor(result) != result:
                result = INF
            if result != INF:
                hands |= {tuple(sorted((int(result),) + to_leave[i]))}
    return hands    # return all the new hands


file = open('2008/s4/s4.5.in')

N = int(file.readline())
line = (file.readline() for i in repeat(1))

for n in range(N):
    # there are N card hands to test
    # The way I solve this problem is by taking the initial hand and preforming every possible combination of +,-,*,/ on
    #  it.  First I take every combination of two numbers and combine those two numbers every possible way, we now have
    #  hands of three number instead of four.  I repeat this until we have hands of one number and return the one that
    #  is closest to 24.
    # read the hand into a tuple (a tuple is an unmodifiable list or array)
    hand = tuple([int(c) for i, c in zip(range(4), line)])
    sub_hands = {hand}  # this is the set containing all the the hands we will evaluate
    for i in range(3):
        new_hands = set()   # this will be the next sets of hands we will evaluate
        for h in sub_hands:
            # for each hand add all the hands it could create
            new_hands |= next_hands(h)
        sub_hands = new_hands

    # find the hand with the value closest or equal to 24
    val = 0
    for h in sub_hands:
        if val < h[0] <= 24:
            val = h[0]

    print(val)