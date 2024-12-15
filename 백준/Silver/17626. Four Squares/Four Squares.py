import math

memo = {}

n = int(input())

for i in range(1,n+1):
    root = math.isqrt(i)
    minimum = 4
    if i == root**2:
        memo[i] = 1
    else:
        for j in range(1,root+1):
            cnt = 1
            cnt += memo[i-j**2]
            if cnt < minimum:
                minimum = cnt
        memo[i] = minimum

print(memo[n])