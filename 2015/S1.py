__author__ = 'Daniel'


file = open('S1.in')

K = int(file.readline())
nums= []
for k in range(K):
    i = int(file.readline())
    if i == 0:
        nums.pop()
    else:
        nums.append(i)
print(sum(nums))