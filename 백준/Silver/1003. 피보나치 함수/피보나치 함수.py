t = int(input())

# 0부터 40까지 저장
dp = [(1, 0), (0, 1)]  # (fib(0) 호출 수, fib(1) 호출 수)

for i in range(2, 41):
    a, b = dp[i-1]
    c, d = dp[i-2]
    dp.append((a + c, b + d))

for _ in range(t):
    n = int(input())
    print(dp[n][0], dp[n][1])