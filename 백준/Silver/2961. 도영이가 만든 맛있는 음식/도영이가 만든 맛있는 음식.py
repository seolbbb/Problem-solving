import sys
sys.setrecursionlimit(10**7)

def backtrack(depth, start, s, b, target):
    global ans

    if depth == target:
        ans = min(ans, abs(s-b))
        return
    
    for i in range(start, n):
        ns = s * ing[i][0]
        nb = b + ing[i][1]

        backtrack(depth+1, i+1, ns, nb, target)

n = int(input())
ing = [list(map(int, input().split())) for _ in range(n)]
ans = 10**10

for i in range(1, n+1):
    backtrack(0, 0, 1, 0, i)

print(ans)