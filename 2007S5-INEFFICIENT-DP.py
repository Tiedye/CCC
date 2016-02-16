__author__ = 'Daniel'
import functools
import itertools
from operator import getitem


@functools.lru_cache(maxsize=None)
def find_score(pins, bc, bw):
    """
    Return scores for the pins and balls and widths
    :param pins: list of pins
    :param bc: ball count + 1
    :param bw: ball width
    :return: list of scores of balls from 0 to bc
    """
    start_index = (len(pins)-1) // 2
    if start_index < bw:
        start_index = bw
    mms = max(min(bw, len(pins) - 2*bw + 1), 1)
    max_score = [-1 for b in range(bc+1)]
    for ms in range(mms):
        l_group = pins[:start_index+ms]
        r_group = pins[start_index+ms:]
        if len(l_group) <= bw:
            l_score = (0, sum(l_group))
        else:
            l_score = find_score(l_group, bc, bw)
        if len(r_group) <= bw:
            r_score = (0, sum(r_group))
        else:
            r_score = find_score(r_group, bc, bw)
        ll = len(l_score)
        lr = len(r_score)
        for b in range(min(ll+lr-1, bc+1)):
            max_score[b] = max(max(map(lambda x: l_score[x]+r_score[b-x], range(max(0, b-(lr-1)), min(ll, b+1)))), max_score[b])
            #                                                              ^limit tested values so there's no excess
    return tuple(itertools.takewhile(lambda x: x != -1, max_score))


file = open('2007/s5/s5.3.in')
T = int(file.readline())
for t in range(T):
    N, K, W = map(int, file.readline().split())
    original_pins = tuple([int(file.readline()) for n in range(N)])
    print(find_score(original_pins, K, W)[K])
    print(find_score.cache_info())
    find_score.cache_clear()
