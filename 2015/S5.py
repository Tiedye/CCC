
file = open('s5.14.in')
N = int(file.readline())
L = [int(file.readline()) for n in range(N)] + [0]  # read the ordered list of pies into a list
P = int(file.readline())
A = [int(file.readline()) for m in range(P)]        # read the pies to be inserted into a list and sort it
A.sort()

# Because of the versatile but slow nature of python's lists, I condensed
# what was a 5D array (first index was 0 or 1 to indicate I or E,
# second was n, third was m, etc.) but it took longer to initialize the
# list than actually calculate the states.  Using one list and multiplying
# the indexes by fixed numbers to simulate a multidimensional array was
# more than 6x faster.

# these are the factors to multiply the indices by
s5 = 1
s4 = 2*s5
s3 = (P+1)*s4
s2 = (P+1)*s3
s1 = 2*s2

# this will hold all of the states
s = [0]*(2*s1)

# these are the bases states
s[0] = L[0]
if P != 0:
    s[1] = A[-1]

# loop through every possible valid state, in the order were all of the prerequisite states are already calculated.
nc, nm = 0, s2
for n in range(1, N+1):
    nc, nm = nm, nc
    for m in range(min(n+1, P)+1):
        for M in range(min(n+1, P)+1-m):
            # we calculate the value of I and E for a state at the same
            #  time, first when the last item is from the original list
            max_i = 0
            max_e = 0
            # include a case only if the case is valid
            # include states where the last pie is from the insertion list
            if m > 0:
                max_i = s[1*s1 + nc + (m-1)*s3 + M*s4 + 1]
                max_e = s[1*s1 + nc + (m-1)*s3 + M*s4 + 1]
            if M > 0:
                max_e = max(s[nc + m*s3 + (M-1)*s4 + 1], max_e)
            # include states where the last pie is from the original list
            if M+m != n+1 and n > 0:
                max_i = max(s[1*s1 + nm + m*s3 + M*s4], max_i)
                max_e = max(s[1*s1 + nm + m*s3 + M*s4], s[nm + m*s3 + M*s4], max_e)
            # calculate the value of the I function
            s[nc + m*s3 + M*s4] = max_i + L[n]
            # calculate the value of the E function
            s[1*s1 + nc + m*s3 + M*s4] = max_e
            # now calculate the value of the functions when the last item is from the insertion list
            if M+m != P and M+m != n+1 and n > 0:
                # if the last item inserted is from the new list (l = 1) and the state has the maximum
                # number of pies from the inserted list, then this state cannot exist and is skipped
                # or if the number of inserted pies equals the total number of inserted pies it is skipped
                # include the cases where the last pie is from the original case if the case is valid
                max_i = s[1*s1 + nm + m*s3 + M*s4]
                max_e = max(s[1*s1 + nm + m*s3 + M*s4], s[nm + m*s3 + M*s4])
                s[nc + m*s3 + M*s4 + 1] = max_i + A[-M-1]
                s[1*s1 + nc + m*s3 + M*s4 + 1] = max_e

# finally add the sums of the leftover pies
final_max = 0
for m in range(min(N+1, P)+1):
    for M in range(min(N+1, P)+1-m):
        # rA is all the pies we didn't add to the list
        if M == 0:
            rA = A[m:]
        else:
            rA = A[m:-M]
        final_max = max(final_max,
                        s[1*s1+nm+m*s3+M*s4] + sum(rA[len(rA)//2:]),
                        s[nm+m*s3+M*s4] + sum(rA[-((-len(rA))//2):]))
                                    # this strange statement causes upward rounding as opposed to downwards
        if M+m != P or M+m != N+1:
            if M == 0:
                rA = A[m+1:]
            else:
                rA = A[m+1:-M]
            final_max = max(final_max, s[1*s1+nc+m*s3+M*s4+1] + sum(rA[len(rA)//2:]))
            rA = A[m:-M-1]
            final_max = max(final_max, s[nc+m*s3+M*s4+1] + sum(rA[-((-len(rA))//2):]))

print(final_max)