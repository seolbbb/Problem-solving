import sys
input = sys.stdin.readline

t, w = map(int,input().split())
pos = [0] + [int(input()) for _ in range(t)]
dp = [[0 for _ in range(w+1)] for _ in range(t+1)]

# dp[i][j] 에서 j는 이동한 횟수, t = 1 일때 위치가 1 이기 때문에 j%2 == 0: 위치 1, j%2 == 1: 위치 2
for i in range(1,t+1):
    for j in range(w+1):
        if pos[i] == 1:
            if j % 2 == 0:
                if j == 0:
                    dp[i][j] = dp[i-1][j] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]) + 1
            else:
                dp[i][j] = dp[i-1][j]
        elif pos[i] == 2:
            if j % 2 == 1:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]) + 1
            else:
                dp[i][j] = dp[i-1][j]
print(max(dp[t]))