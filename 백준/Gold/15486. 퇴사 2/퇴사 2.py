import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n+1)]
tp = [[]for _ in range(n+1)]

for i in range(n):
    tp[i] = list(map(int, input().split()))

for i in range(n):
    t, p = tp[i]
    if i + t <= n:
        dp[i + t] = max(dp[i + t], dp[i] + p)
    dp[i + 1] = max(dp[i + 1], dp[i])

print(max(dp))