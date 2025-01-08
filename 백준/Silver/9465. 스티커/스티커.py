import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [[0] + list(map(int,input().split())) for _ in range(2)]
    dp = [[0,0] for _ in range(n+1)]
    
    if n == 1:
        print(max(arr[0][1],arr[1][1]))
        continue

    dp[1][0] = arr[0][1]
    dp[1][1] = arr[1][1]
    dp[2][0] = dp[1][1] + arr[0][2]
    dp[2][1] = dp[1][0] + arr[1][2]

    for i in range(3,n+1):
        dp[i][0] = max(dp[i-1][1] + arr[0][i], dp[i-2][1] + arr[0][i])
        dp[i][1] = max(dp[i-1][0] + arr[1][i],dp[i-2][0] + arr[1][i])
    
    print(max(dp[n]))