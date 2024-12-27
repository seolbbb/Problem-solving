import sys
input = sys.stdin.readline

n = int(input())
lst = [0] + list(map(int,input().split()))
dp = [[0,1001] for _ in range(n+1)]

dp[1][0] = 1
dp[1][1] = lst[1]

for i in range(2,n+1):
    lst2 = [x for x, y in dp if y < lst[i]]
    dp[i][0] = max(lst2,default=0) + 1
    dp[i][1] = lst[i]

print(max(dp)[0])