import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
dp = [0 for _ in range(1001)]

dp[1] = lst[0]

for i in range(2,n+1):
    current = lst[i-1]
    for j in range(i-1):
        if current > lst[j]:
            dp[i] = max(dp[i],dp[j+1]+current)
    if dp[i] == 0:
        dp[i] = current

print(max(dp))