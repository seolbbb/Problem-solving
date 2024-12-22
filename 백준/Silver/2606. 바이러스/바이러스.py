import sys
from collections import deque

def dfs(cur):
    vis[cur] = 1
    for nxt in adj[cur]:
        if vis[nxt]:
            continue
        dfs(nxt)

def bfs():
    queue.append(1)
    vis[1] = 1
    while queue:
        cur = queue.popleft()
        for nxt in adj[cur]:
            if vis[nxt]:
                continue
            queue.append(nxt)
            vis[nxt] = 1

n = int(input())
m = int(input())
adj = [[] for _ in range(101)]
vis = [0 for _ in range(101)]
queue = deque()
num = 0

for _ in range(m):
    u, v = map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)

bfs()

print(sum(vis) - 1)