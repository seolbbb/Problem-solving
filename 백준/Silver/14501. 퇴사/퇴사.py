import sys
input = sys.stdin.readline

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n + 1)]

for i in range(n):
    if i + lst[i][0] <= n:
        dp[i + lst[i][0]] = max(dp[i + lst[i][0]], dp[i] + lst[i][1])
    dp[i + 1] = max(dp[i + 1], dp[i])

print(dp[n])