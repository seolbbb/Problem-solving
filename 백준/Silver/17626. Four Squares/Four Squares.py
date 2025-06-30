dp = [4 for _ in range(50001)]
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 3

for i in range(4, 50001):
    for j in range(int(i**0.5), 0, -1):
        dp[i] = min(dp[i], dp[i-j**2]+1)

n = int(input())

print(dp[n])