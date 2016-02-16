__author__ = 'Daniel'


state = ((0, 2, 2, 2, 0), (0, 1, 2, 1, 0), (0, 0, 1, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0))

file = open('2011/s3/s3.1.in')
test_cases = [tuple([int(t) for t in line.split()]) for line in file.readlines()[1:]]
for test_case in test_cases:
    m, x, y = test_case
    while m:
        value = state[y//5**(m-1)][x//5**(m-1)]
        if value == 0:
            print('empty')
            break
        elif value == 2:
            print('crystal')
            break
        else:
            if m == 1:
                print('empty')
                break
            x %= 5**(m-1)
            y %= 5**(m-1)
            m -= 1