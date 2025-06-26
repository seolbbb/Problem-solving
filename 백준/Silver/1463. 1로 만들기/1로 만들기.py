dp = [1000000 for _ in range(1000001)]
dp[0] = 0
dp[1] = 0

for i in range(2, 1000001):
    dp[i] = min(dp[i], dp[i-1] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)

n = int(input())

print(dp[n])