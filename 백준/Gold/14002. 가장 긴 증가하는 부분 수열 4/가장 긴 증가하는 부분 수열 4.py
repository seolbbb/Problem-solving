n = int(input())
seq = list(map(int,input().split()))
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if seq[i] > seq[j]:
            dp[i] = max(dp[i], dp[j] + 1)

length = max(dp)
LIS = ''

for i in range(n-1,-1,-1):
    if dp[i] == length:
        LIS = str(seq[i]) + ' ' + LIS
        length -= 1

print(max(dp))
print(LIS)