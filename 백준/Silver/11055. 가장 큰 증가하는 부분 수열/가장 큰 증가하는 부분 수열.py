import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
dp = [0 for _ in range(1001)]

dp[1] = lst[0]

for i in range(2,n+1):
    current = lst[i-1]
    maxdp = []
    num = i-2

    while True:
        if current > lst[num]:
            maxdp.append(dp[num+1] + current)
        elif num <= 0:
            maxdp.append(current)
            break   
        num -= 1
    dp[i] = max(maxdp)

print(max(dp))