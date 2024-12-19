import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
dp = [0 for _ in range(100001)]

dp[1] = lst[0]

for i in range(2,n+1):
    if dp[i-1] > 0:
        dp[i] = dp[i-1] + lst[i-1]
    else:
        dp[i] = lst[i-1]

print(max(dp[1:n+1]))