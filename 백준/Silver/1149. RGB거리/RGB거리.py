import sys
def minimum(current,before):
    result = []
    
    for i in range(3):
        temp = []
        for j in range(3):
            if i == j:
                continue
            temp.append(current[i] + before[j])
        result.append(min(temp))
    
    return result

input = sys.stdin.readline

n = int(input())
dp = [[0 for _ in range(3)] for _ in range(n+1)]
lst = [list(map(int,input().split())) for _ in range(n)]

dp[1] = minimum(lst[1],lst[0])
dp[2] = minimum(lst[2],dp[1])

for i in range(2,n):
    dp[i] = minimum(lst[i],dp[i-1])

print(min(dp[n-1]))