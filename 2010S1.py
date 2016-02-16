__author__ = 'Daniel'


file = open('2010/S1/s1.2.in')
lines = file.readlines()
# read all the lines in the file

tokens = [l.split() for l in lines[1:]]
# split each line up into its parts, so the line 'ABC 3 5 2' becomes a list ['ABC', '3', '5', '2']
# the first line is ignored, thus the [1:]

data = [(-(float(t[1])*2 + float(t[2])*3 + float(t[3])), t[0]) for t in tokens]
# now make this into a list of tuples (a tuple is a list that cant be changed) that contains the score of the computer
# and the name of it, so the computer ['ABC', '3', '5', '2'] becomes (23.0, 'ABC')
# the score is made negative because the sort function sorts from lowest to highest, and we want the highest, so this
# makes the highest numbers the lowest

data.sort()
# this will automatically sort the list first by score (the first item in the tuples) and then by name (the second item)

if len(data) != 0:
    print(data[0][1])
    # only print the first item if it exists

if len(data) > 1:
    print(data[1][1])
    # only print the second item if it exists