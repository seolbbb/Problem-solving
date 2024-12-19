import sys
input = sys.stdin.readline

n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
dp = [[] for _ in range(n+1)]

if n == 1:
    print(lst[0][0])
    exit(0)

dp[1] = [lst[0][0] + lst[1][i] for i in range(len(lst[1]))]

for i in range(2,n):
    for j in range(len(dp[i-1])+1):
        if j == 0:
            dp[i].append(dp[i-1][j] + lst[i][j])
        elif j == len(dp[i-1]):
            dp[i].append(dp[i-1][j-1] + lst[i][j])
        else:
            dp[i].append(max(dp[i-1][j] + lst[i][j], dp[i-1][j-1] + lst[i][j]))

print(max(dp[n-1]))