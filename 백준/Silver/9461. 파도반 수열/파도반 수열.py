dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0 for _ in range(90)]

for i in range(11, 101):
    dp[i] = dp[i-1] + dp[i-5]

t = int(input())

for _ in range(t):
    n = int(input())
    print(dp[n])