n = int(input())

dp = [0,1,1]

for i in range(4,n+1):
    m = float('inf')

    if i % 3 == 0:
        if (1 + dp[(i//3)-1]) < m:
            m = (1 + dp[(i//3)-1])
    if i % 2 == 0:
        if (1 + dp[(i//2)-1]) < m:
            m = (1 + dp[(i//2)-1])
    if (1 + dp[i-2]) < m:
        m = (1 + dp[i-2])
    dp.append(m)

print(dp[n-1])