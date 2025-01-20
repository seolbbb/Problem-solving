import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
dp1 = [0 for _ in range(1001)]
dp2 = [0 for _ in range(1001)]
res = []

dp1[1] = 1
dp2[n] = 1

for i in range(2,n+1):
    tmp = []

    for j in range(i-1):
        if lst[i-1] > lst[j]:
            tmp.append(dp1[j+1])

    if len(tmp) == 0:
        dp1[i] = 1
    else:
        dp1[i] = max(tmp) + 1

for i in range(n-1,0,-1):
    tmp = []

    for j in range(n-1,i-2,-1):
        if lst[i-1] > lst[j]:
            tmp.append(dp2[j+1])

    if len(tmp) == 0:
        dp2[i] = 1
    else:
        dp2[i] = max(tmp) + 1

for i in range(1,n+1):
    res.append(dp1[i] + dp2[i])

print(max(res) - 1)