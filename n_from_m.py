# Get N from M
m = 10
n = 3

pool = range(1, m + 1)
print pool

finalgroup = 2 ** m - 1
print finalgroup

# iteration
i = 0
k = 1
while i <= finalgroup:
    candidate = bin(i)[2:]
    #candidate = (m - len(candidate)) * '0' + candidate
    candidate = candidate.zfill(m)
    if candidate.count('1') == n:
        print "No - %d" % k
        k += 1
        result = []
        for j in range(m):
            if candidate[j] == '1':
                result.append(pool[j])
            else:
                next
        print result
    i += 1
