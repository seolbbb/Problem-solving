n = int(input())
dp = [[0, []] for _ in range(1000001)]
dp[1][0] = 0
dp[1][1] = [1]
dp[2][0] = 1
dp[2][1] = [1,2]
dp[3][0] = 1
dp[3][1] = [1,3]

for i in range(4,n+1):
    tmp = []
    num = 0
    a = float('inf')
    b = float('inf')
    c = dp[i-1][0] + 1
    tmp.append((c,i-1))

    if i % 3 == 0:
        a = dp[i//3][0] + 1
        tmp.append((a,i//3))
    if i % 2 == 0:
        b = dp[i//2][0] + 1
        tmp.append((b,i//2))
    mint, num = min(tmp)

    dp[i][0] = mint
    dp[i][1] = dp[num][1] + [i]

print(dp[n][0])
print(*(dp[n][1][::-1]))