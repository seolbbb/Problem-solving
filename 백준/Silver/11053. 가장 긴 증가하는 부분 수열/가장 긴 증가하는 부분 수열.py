import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
dp = [0 for _ in range(1001)]

dp[1] = 1

for i in range(2,n+1):
    tmp = []

    for j in range(i-1):
        if lst[i-1] > lst[j]:
            tmp.append((dp[j+1]))

    if len(tmp) == 0:
        dp[i] = 1
    else:
        pre = max(tmp)
        dp[i] = pre + 1

print(max(dp))