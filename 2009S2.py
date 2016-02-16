__author__ = 'Daniel'


file = open('2009/s2/s2.4.in')
lines = file.readlines()[2:]
# read all the lines to an array and discard the first two as all the data are in the lines after th first two

cols = [int(l.replace(' ', ''), 2) for l in lines]
# convert each line into a binary integer so we can use the xor operation on it

# the process here is to go through every possible combination of xoring
# to figure out how to do this, first realize that at each step there are two possible steps we can take, we can xor the
# row with the one above it or we can do nothing to the row, this means that the bottom row has two options, it can be
# it's original self or it can be xored with the row above it, and since that row has two possibilities as well, the
# total possibilities for the bottom row is 3 (2 + 1).  If we then consider hat the row above that one then the bottom
# row has four possibilities (2 + 1 + 1).  Thus we can see the maximum number of possibilities is the number of rows
# plus one.  What we've done here is we've stored the current possibilities in a set, the reason we use a set is because
# a set cannot contain duplicates, so if we just find every possible combination and exclude all duplicates and count
# this, we have the total possible combinations.

states = set()
for c in cols:
    new_states = set()
    for s in states:
        new_states.add(s ^ c)
        # xor the current row with all rows in the set
    new_states.add(c)
    # add the current row unmodified to the set
    states = new_states
    # store the new set into the old sets spot

print(len(states))