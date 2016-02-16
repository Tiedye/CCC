__author__ = 'Daniel'


file = open('2007/s5/s5.5.in')
T = int(file.readline())
# there are T test cases
for t in range(T):
    # read the number of bowling pins, the number of balls, and the width of the balls
    N, K, W = [int(t) for t in file.readline().split()]
    # read the pin numbers in to an array
    pins = [int(file.readline()) for n in range(N)]
    # calculate the number of point you get for knocking down a particular pin and the W - 1 pins to the right of it
    #  this is the points you can get for throwing a ball to various spots
    pin_sum = [sum(pins[n:n+W]) for n in range(N)]
    # maximum points you can get for throwing K balls anywhere up to a particular pin or anywhere to the right of it
    pin_max = [[-1 for n in range(N-k*W)] for k in range(K)]
    # this does the first pass, so any index will be at least equal to all the values after it
    pin_max[0][-1] = pin_sum[-1]
    for i in range(2, N+1):
        pin_max[0][-i] = max(pin_max[0][-i+1], pin_sum[-i])
    for k in range(1, K):
        #this is an optimization that makes it so we can check less stuff
        pin_max[k] += pin_max[k-1][N-k*W:]
        for i in range(N-1-W*k, -1, -1):
            # for each pin, check if you can get more points for knocking that pin down along with the pins that that
            #  ball doesnt tough to its right, or simply use the maximum for a ball that was thrown more to the right
            # hard to explain, i could draw it
            pin_max[k][i] = max(pin_sum[i]+pin_max[k-1][i+W], 0, *pin_max[k][i+1:i+1+W])
    print(pin_max[-1][0])

