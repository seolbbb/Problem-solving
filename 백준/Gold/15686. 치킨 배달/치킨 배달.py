import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
chicken = []
home = []
ans = float('inf')

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            home.append((i,j))
        elif arr[i][j] == 2:
            chicken.append((i,j))

cases = list(combinations(chicken,m))

for i in range(len(cases)):
    dist = 0

    for r1, c1 in home:
        temp = 251
        for r2, c2 in cases[i]:
            temp = min(temp, abs(r1-r2) + abs(c1-c2))
        dist += temp
        
    ans = min(ans, dist)

print(ans)