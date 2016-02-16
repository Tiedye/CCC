__author__ = 'Daniel'


# read input
file = open('2011/s5/s5.6.in')
lines = file.readlines()
K = int(lines[0])
switches = [int(s) for s in lines[1:1+K]]

# group activated switches
groups = []
group_count = 0
current_group_start = 0
current_group_end = 0
for s in range(len(switches)):
    if switches[s] == 1:
        if current_group_end == 0:
            current_group_start = s
            current_group_end = s
        current_group_end += 1
    elif current_group_end != 0:
            groups.append((current_group_start, current_group_end))
            current_group_end = 0

if current_group_end != 0:
    groups.append((current_group_start, current_group_end))


# initialize an array to store the minimum switch activations to remove group
INF = 1000000
min_switches = [[INF for y in range(len(groups))] for x in range(len(groups))]


# find the minimum switched to deactivate a group of groups of switches
def find_min(bgn, end):
    if bgn > end:
        return 0
    if min_switches[bgn][end] < INF:
        return min_switches[bgn][end]
    sc = 0
    while groups[bgn+sc][1] - groups[bgn][0] <= 7:
        min_switches[bgn][end] = min(min_switches[bgn][end], req_switches(bgn, bgn+sc) + find_min(bgn+sc+1, end))
        sc += 1
        if bgn+sc == len(groups):
            break
    return min_switches[bgn][end]


# find the switches required to deactivate small groups of switches
def req_switches(bgn, end):
    group_len = groups[end][1] - groups[bgn][0]
    if group_len == 6 and switches[groups[bgn][0] + 2] == 1 and switches[groups[bgn][0] + 3] == 1:
        return INF
    elif group_len == 7 and switches[groups[bgn][0] + 3] == 1:
        return INF
    return max(group_len, 4) - sum(map(switch_count, groups[bgn:end+1]))


# find switches in a group
def switch_count(g):
    b, e = g
    return e-b

# find minimum switches for all groups together
print(find_min(0, len(groups)-1))