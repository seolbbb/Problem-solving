import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n+1)]
tp = [[0,0]]

for i in range(n):
    tp.append(list(map(int, input().split())))

for i in range(1, n + 1):
    if i + tp[i][0] <= n + 1:
        dp[i + tp[i][0] - 1] = max(dp[i + tp[i][0] - 1], dp[i - 1] + tp[i][1])
    dp[i] = max(dp[i], dp[i - 1])

print(max(dp))