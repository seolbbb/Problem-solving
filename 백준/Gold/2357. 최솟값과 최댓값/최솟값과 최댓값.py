import sys
import math
input = sys.stdin.readline

n, m = map(int ,input().split())
arr = [int(input()) for _ in range(n)]
min_dp = [[0 for _ in range(int(math.log2(n))+1)] for _ in range(n)]
max_dp = [[0 for _ in range(int(math.log2(n))+1)] for _ in range(n)]

for i in range(n):
    min_dp[i][0] = arr[i]
    max_dp[i][0] = arr[i]

for j in range(1, int(math.log2(n))+1):
    for i in range(n):
        if i + (1 << j) > n:
            break
        min_dp[i][j] = min(min_dp[i][j-1], min_dp[i + (1 << (j-1))][j-1])
        max_dp[i][j] = max(max_dp[i][j-1], max_dp[i + (1 << (j-1))][j-1])

for _ in range(m):
    l, r = map(int, input().split())
    k = int(math.log2(r - l + 1))
    mi = min(min_dp[l-1][k], min_dp[r - (1 << k)][k])
    mx = max(max_dp[l-1][k], max_dp[r - (1 << k)][k])
    print(mi, mx)