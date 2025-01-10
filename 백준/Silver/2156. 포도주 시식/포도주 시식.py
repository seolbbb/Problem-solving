import sys
input = sys.stdin.readline

n = int(input())
wine = [0] + [int(input()) for _ in range(n)]
dp = [[0,0,0] for _ in range(n+1)]

if n == 1:
    print(wine[1])
    exit(0)
elif n == 2:
    print(wine[1] + wine[2])
    exit(0)

dp[1][1] = wine[1]
dp[2][0] = wine[1]
dp[2][1] = wine[2]
dp[2][2] = dp[1][1] + wine[2]

for i in range(3,n+1):
    dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
    dp[i][1] = dp[i-1][0] + wine[i]
    dp[i][2] = dp[i-1][1] + wine[i]

print(max(dp[n]))