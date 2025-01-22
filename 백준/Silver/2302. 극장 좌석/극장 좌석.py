n = int(input())
m = int(input())
dp = [1 for _ in range(41)]
prev = 1
ans = 1

dp[1] = 1
for i in range(2,41):
    dp[i] = dp[i-1] + dp[i-2]

for i in range(m):
    vip = int(input())
    ans *= dp[vip-prev]
    prev = vip + 1
ans *= dp[n-prev+1]

print(ans)