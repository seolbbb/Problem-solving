n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]

dp[0][1][0] = 1

for r in range(n):
    for c in range(n):
        if board[r][c] == 1:
            continue

        if c-1 >= 0:
            dp[r][c][0] += dp[r][c-1][0] + dp[r][c-1][1]
        
        if r-1 >= 0:
            dp[r][c][2] += dp[r-1][c][1] + dp[r-1][c][2]
        
        if r-1 >= 0 and c-1 >= 0:
            if board[r-1][c] == 0 and board[r][c-1] == 0:
                dp[r][c][1] += dp[r-1][c-1][0] + dp[r-1][c-1][1] + dp[r-1][c-1][2]

ans = dp[n-1][n-1][0] + dp[n-1][n-1][1] + dp[n-1][n-1][2]
print(ans)