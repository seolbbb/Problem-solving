arr1 = list(input())
arr2 = list(input())
n = len(arr1)
m = len(arr2)
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
lcs = ''

for i in range(1,n+1):
    for j in range(1,m+1):
        if arr1[i-1] == arr2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

lcs_len = dp[n][m]
temp = lcs_len

for i in range(n,0,-1):
    for j in range(m,0,-1):
        cur = dp[i][j]
        if cur > dp[i-1][j] and cur > dp[i][j-1] and cur > dp[i-1][j-1] and cur == temp:
            temp -= 1
            lcs = arr1[i-1] + lcs
            break


print(lcs_len)
print(lcs)