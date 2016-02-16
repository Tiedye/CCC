__author__ = 'Daniel'

file = open('2006/s3/s3.2.in')
rx, ry, jx, jy = map(float, file.readline().split())
dx = jx - rx
dy = jy - ry
A = 0.0
B = 0.0
C = 1.0
if dy == 0.0:
    if ry == 0.0:
        C = 0.0
        B = 1.0
    else:
        B = 1.0 / ry
elif dx == 0.0:
    if ry == 0.0:
        C = 0.0
        A = 1.0
    else:
        A = 1.0 / rx
else:
    if rx - ry * (dx / dy) == 0.0:
        C = 0.0
        A = -dy / dx
        B = 1.0
    else:
        A = 1.0 / (rx - ry * (dx / dy))
        B = 1.0 / (ry - rx * (dy / dx))

min_x, max_x = sorted([rx, jx])
min_y, max_y = sorted([ry, jy])

N = int(file.readline())
INF = 10000000
hit_count = 0
for n in range(N):
    raw = [float(t) for t in file.readline().split()][1:]
    vertices = [tuple(raw[i * 2:i * 2 + 2]) for i in range(len(raw) // 2)]
    vertices += [vertices[0]]
    sides = [tuple(vertices[i:i + 2]) for i in range(len(raw) // 2)]
    for side in sides:
        dx = side[1][0] - side[0][0]
        dy = side[1][1] - side[0][1]
        A2 = 0.0
        B2 = 0.0
        C2 = 1.0
        if dy == 0.0:
            if side[0][1] == 0.0:
                C2 = 0.0
                B2 = 1.0
            else:
                B2 = 1.0 / side[0][1]
        elif dx == 0.0:
            if side[0][0] == 0.0:
                C2 = 0.0
                A2 = 1.0
            else:
                A2 = 1.0 / side[0][0]
        else:
            if side[0][0] - side[0][1] * (dx / dy) == 0.0:
                C2 = 0.0
                A2 = -dy / dx
                B2 = 1.0
            else:
                A2 = 1.0 / (side[0][0] - side[0][1] * (dx / dy))
                B2 = 1.0 / (side[0][1] - side[0][0] * (dy / dx))
        if A * B2 - A2 * B == 0.0:
            y = INF
        else:
            y = (A * C2 - A2 * C) / (A * B2 - A2 * B)
        if B * A2 - B2 * A == 0.0:
            x = INF
        else:
            x = (B * C2 - B2 * C) / (B * A2 - B2 * A)
        x = round(x, 10)
        y = round(y, 10)
        l_min_x, l_max_x = sorted([side[1][0], side[0][0]])
        l_min_y, l_max_y = sorted([side[1][1], side[0][1]])
        if min_y <= y <= max_y and l_min_y <= y <= l_max_y and min_x <= x <= max_x and l_min_x <= x <= l_max_x:
            hit_count += 1
            break
        # we ignore the case of sides that are flat against the line fo sight as those are caught by other edge checks
print(hit_count)