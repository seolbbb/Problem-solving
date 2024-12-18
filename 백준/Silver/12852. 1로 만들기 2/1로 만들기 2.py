n = int(input())
dp = [0 for _ in range(n+1)]
pre = [0 for _ in range(n+1)]

dp[1] = 0
pre[1] = 0

for i in range(2,n+1):
    dp[i] = dp[i-1] + 1
    pre[i] = i-1

    if i % 3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1
        pre[i] = i//3
    if i % 2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1
        pre[i] = i//2

print(dp[n])

cur = n
while True:
    print(cur, end = ' ')
    if cur == 1:
        break
    cur = pre[cur]