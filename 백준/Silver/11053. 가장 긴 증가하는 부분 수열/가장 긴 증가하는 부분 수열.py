n = int(input())
arr = [0] + list(map(int, input().split()))
dp = [0 for _ in range(n+1)]

dp[1] = 1

for i in range(2, n+1):
    lst = []

    for j in range(i):
        if arr[i] > arr[j]:
            lst.append(dp[j])

    if lst:
        dp[i] = max(lst) + 1
    else:
        dp[i] = 1

print(max(dp))