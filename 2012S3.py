__author__ = 'Daniel'
from collections import Counter
from time import clock


ts = clock()
file = open('2012/S3/s3.5.in')
mc = set()
mcc = 0
smc = set()
smcc = 0
ac = Counter()
for i in range(int(file.readline())):
    n = int(file.readline())
    ac[n] += 1
    if ac[n] > mcc:
        if len(smc - {n}) != 0: # error caused by lone numbers being shifted down when itself recuured
            smc = mc - {n}      # this causes the same number to be in both the most and second most set
            smcc = mcc          # first fix attept had empty sets shifting down occasionally
        mc = {n}
        mcc = ac[n]
    elif ac[n] == mcc:
        mc.add(n)
    elif ac[n] > smcc:
        smc = {n}
        smcc = ac[n]
    elif ac[n] == smcc:
        smc.add(n)

srtmc = sorted(mc)
srtsmc = sorted(smc)

if len(srtmc) > 1:
    print(srtmc[-1] - srtmc[0])
else:
    print(max(abs(srtmc[0] - srtsmc[0]), abs(srtmc[0] - srtsmc[-1])))
print(clock()-ts)