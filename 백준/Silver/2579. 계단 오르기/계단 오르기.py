n = int(input())
score = [0 for _ in range(n+1)]
dp = [0 for _ in range(n+1)]

for i in range(1,n+1):
    score[i] = (int(input()))

if n == 1:
    print(score[1])
    exit(0)
elif n == 2:
    print(score[1] + score[2])
    exit(0)

dp[1] = score[1]
dp[2] = score[1] + score[2]

for i in range(3,n+1):
    dp[i] = max(dp[i-3] + score[i-1] + score[i], dp[i-2] + score[i])

print(dp[n])