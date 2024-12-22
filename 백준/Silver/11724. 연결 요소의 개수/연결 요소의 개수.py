import sys
from collections import deque
input = sys.stdin.readline

adj = [[] for _ in range(1005)]
vis = [0 for _ in range(1005)]
stack = deque()
num = 0

n, m = map(int,input().split())

for _ in range(m):
    u, v = map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)

for i in range(1,n+1):
    if vis[i]:
        continue
    num += 1
    stack.append(i)
    vis[i] = 1
    while stack:
        cur = stack.pop()
        for j in adj[cur]:
            if vis[j]:
                continue
            stack.append(j)
            vis[j] = 1

print(num)
