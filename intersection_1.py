# We have two sorted arrays A and B of sizes m and n, create a new array C
# that contains a list of all the common elements in A and B
# Assumption
# A = [1,2,3,4,5,6,7,8,9,10]
# B = [1,3,5,7,9,11,13,15]
# then C should meet the result: C = [1,3,5,7,9]

A = [1,2,3,4,5,6,7,8,9,10]
B = [1,3,5,7,9,11,13,15]

# first solution, use builtin set module
set_a = set(A)
set_b = set(B)
C = sorted(list(set_a & set_b))
print "Solution one: C = ", C

C = []
# second solution, use heapq
# I think this is better, because it doesn't need to sort the array
from heapq import heapify, heappop, heappush
heapify(A)
heapify(B)
if len(A) > len(B):
    shorter, longer = B, A
else:
    shorter, longer = A, B
try:
    while True:
        i = heappop(shorter)
        while True:
            j = heappop(longer)
            if i == j:
                C.append(i)
                break
            elif i > j:
                continue
            else:
                heappush(longer, j)
                break
except IndexError as ie:
    print "Solution 2: C = ", C


