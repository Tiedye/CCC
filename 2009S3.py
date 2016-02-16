__author__ = 'Daniel'
from collections import deque


# the connections between people will be represented by a 49 by 49 2d array as they tell us the max person count is 49
grid = [[False for i in range(50)] for j in range(50)]


# define functions for creating and removing friendships
def add(x, y):
    grid[x][y] = True
    grid[y][x] = True


def rem(x, y):
    grid[x][y] = False
    grid[y][x] = False


# make functions for counting friends and friends of friends
def friends(x):
    fr = set()
    for i in range(50):
        if grid[x][i]:
            fr.add(i)
    return fr


def friends_of_friends(x):
    fr = friends(x)
    ffr = set()
    for f in fr:
        ffr |= friends(f)
    return ffr - fr - {x}


# find degrees of separation
# this uses a breadth first search
# ds represents the degrees of separation of x to every visited element
# visited is a set containing all visited elements
# nxt is the queue that contains the elements to be examined next
def sep(x, y):
    ds = [0] * 50
    visited = {x}
    # add the initial person to the visited set
    nxt = deque([x])
    # add the initials person to a list to be examined
    while nxt:  # keep looking until their is no one left
        current_person = nxt.popleft()
        # store the next person to be looked at and remove them from the queue
        if current_person == y:
            # if it's the person we're looking for return their degree of separation
            return ds[y]
        to_add = friends(current_person) - visited
        # otherwise add all of that persons friends minus the people we've already visited to the queue
        nxt.extend(to_add)
        for f in to_add:
            ds[f] = ds[current_person] + 1
            # make all those people's degree of separation the degree of separation of the current person plus one
        visited |= to_add
        # add those people he the set of visited people
    else:
        return -1
        # if we don't find any connection return -1


# initialize the initial friend configuration
add(2, 6)
add(1, 6)
add(5, 6)
add(4, 6)
add(3, 6)
add(3, 4)
add(4, 5)
add(3, 5)
add(3, 15)
add(15, 13)
add(13, 14)
add(13, 12)
add(12, 11)
add(11, 10)
add(12, 9)
add(10, 9)
add(9, 8)
add(8, 7)
add(7, 6)
add(16, 17)
add(17, 18)
add(18, 16)

file = open('2009/s3/s3.4.in')
lines = file.readlines()
line = 0
# here we read the command on a line, and depending on the number of arguments we read we increase the index of the
# next line to be read by 3 of the command has two arguments and 2 id the command has one argument
while line < len(lines):
    cl = lines[line].strip()
    if cl == 'i':
        add(int(lines[line + 1]), int(lines[line + 2]))
        line += 3
    elif cl == 'd':
        rem(int(lines[line + 1]), int(lines[line + 2]))
        line += 3
    elif cl == 'n':
        print(len(friends(int(lines[line + 1]))))
        line += 2
    elif cl == 'f':
        print(len(friends_of_friends(int(lines[line + 1]))))
        line += 2
    elif cl == 's':
        ds = sep(int(lines[line + 1]), int(lines[line + 2]))
        line += 3
        if ds == -1:
            print('Not connected')
        else:
            print(ds)
    elif cl == 'q':
        break
