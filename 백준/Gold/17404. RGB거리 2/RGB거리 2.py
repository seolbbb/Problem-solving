n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0 for _ in range(3)] for _ in range(n+1)] for _ in range(3)]

for i in range(3):
    dp[i][1] = [float('inf'), float('inf'), float('inf')]
    dp[i][1][i] = cost[0][i]
    for j in range(2, n+1):
        dp[i][j][0] = min(dp[i][j-1][1], dp[i][j-1][2]) + cost[j-1][0]
        dp[i][j][1] = min(dp[i][j-1][0], dp[i][j-1][2]) + cost[j-1][1]
        dp[i][j][2] = min(dp[i][j-1][0], dp[i][j-1][1]) + cost[j-1][2]
    dp[i][n][i] = float('inf')

print(min(min(dp[0][n]), min(dp[1][n]), min(dp[2][n])))