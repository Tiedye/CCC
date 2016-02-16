from time import clock

__author__ = 'Daniel'


# fails for 12

t_s = clock()

file = open('s5.10.in')
N = int(file.readline())
L = [int(file.readline()) for n in range(N)] + [0]
P = int(file.readline())
A = [int(file.readline()) for m in range(P)]
A.sort()

t_l = clock()

# maximum sugar for a state
#  fist index is including or excluding last pie
#  second index is number of lies in the original list included
#  third index is the number of minimum pies
#  fourth index is the number of maximum pies
#  fifth index indicates the origin of the last pie (original list, maximum, minimum pies)
mS = [[[[[0
          for l in range(3) if l == 0 or (M+m != n+1 and M+m != P)]
         for M in range(min(n+1, P)+1-m)]
        for m in range(min(n+1, P)+1)]
       for n in range(N+1)]
      for i in range(2)]

t_i = clock()

mS[0][0][0][0][0] = L[0]
if P != 0:
    mS[0][0][0][0][1] = A[0]
    mS[0][0][0][0][2] = A[-1]

# the trial cases are for any state that has zero pies from original list, that state is zero, so we skip those
for n in range(1, N+1):
    for m in range(min(n+1, P)+1):
        for M in range(min(n+1, P)+1-m):
            for l in range(3):
                max_i = 0
                max_e = 0
                if l == 0:
                    # add M/n cases
                    if m > 0:
                        max_i = max(mS[1][n][m-1][M][1], max_i)
                        max_e = max(mS[1][n][m-1][M][1], max_e)
                    if M > 0:
                        max_e = max(mS[0][n][m][M-1][2], max_e)
                elif M+m == P or M+m == n+1:
                    continue
                if M+m != n+1 and n > 0:
                    # add n cases
                    max_i = max(mS[1][n-1][m][M][0], max_i)
                    max_e = max(mS[1][n-1][m][M][0], mS[0][n-1][m][M][0], max_e)
                if l == 0:
                    mS[0][n][m][M][l] = max_i + L[n]
                elif l == 2:
                    mS[0][n][m][M][l] = max_i + A[-M-1]
                mS[1][n][m][M][l] = max_e

t_c1 = clock()

final_max = 0
for m in range(min(N+1, P)+1):
    for M in range(min(N+1, P)+1-m):
        for l in range(3):
            if l == 0:
                if M == 0:
                    rA = A[m:]
                else:
                    rA = A[m:-M]
                final_max = max(final_max,
                                mS[1][N-1][m][M][l] + sum(rA[len(rA)//2:]),
                                mS[0][N-1][m][M][l] + sum(rA[-((-len(rA))//2):]))
            elif M+m == P or M+m == N+1:
                continue
            elif l == 1:
                if M == 0:
                    rA = A[m+1:]
                else:
                    rA = A[m+1:-M]
                final_max = max(final_max, mS[1][N][m][M][l] + sum(rA[len(rA)//2:]))
            elif l == 2:
                rA = A[m:-M-1]
                final_max = max(final_max, mS[0][N][m][M][l] + sum(rA[-((-len(rA))//2):]))

t_c2 = clock()

print(final_max)

print(t_l-t_s, t_i-t_l, t_c1-t_i, t_c2-t_c1, '\n', t_c2-t_s, sep='\n')