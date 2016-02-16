__author__ = 'Daniel'


file = open('2007/s1/s1.1.in')
# this is when the election is happening
YR = 2007
MT = 2
DY = 27

N = int(file.readline())
for n in range(N):
    # get this persons date of birth
    yr, mt, dy = [int(t) for t in file.readline().split()]
    if YR - yr > 18:
        # check first if they're over 18
        print('Yes')
    elif YR - yr == 18:
        if MT - mt > 0:
            # if they are 18 check if their birth month is before the election
            print('Yes')
        elif MT - mt == 0:
            if DY - dy >= 0:
                # if they're born the month of the election, check if they are born on or before the election day
                print('Yes')
            else:
                print('No')
        else:
            print('No')
    else:
        print('No')