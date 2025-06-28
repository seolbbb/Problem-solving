n = int(input())
score = [0] + [int(input()) for _ in range(n)]
dp = [0 for _ in range(n+1)]

if n == 1:
    print(score[1])
elif n == 2:
    print(score[1]+score[2])
else:
    dp[1] = score[1]
    dp[2] = score[1] + score[2]

    for i in range(3, n+1):
        dp[i] = max(dp[i-2]+score[i], dp[i-3]+score[i-1]+score[i])

    print(dp[n])