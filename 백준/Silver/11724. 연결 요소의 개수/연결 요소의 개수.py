import sys
from collections import deque
sys.setrecursionlimit(5000)
input = sys.stdin.readline

def dfs(cur):
    vis[cur] = 1
    for nxt in adj[cur]:
        if vis[nxt]:
            continue
        dfs(nxt)

adj = [[] for _ in range(1005)]
vis = [0 for _ in range(1005)]
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
    dfs(i)

print(num)