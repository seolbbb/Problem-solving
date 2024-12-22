from collections import deque
import sys
sys.setrecursionlimit(10000)

def dfs(cur):
    vis[cur] = 1
    print(cur, end = ' ')
    for nxt in adj[cur]:
        if vis[nxt]:
            continue
        dfs(nxt)

def bfs():
    queue.append(l)
    vis[l] = 1
    while queue:
        cur = queue.popleft()
        print(cur, end = ' ')
        for nxt in adj[cur]:
            if vis[nxt]:
                continue
            queue.append(nxt)
            vis[nxt] = 1

n, m, l = map(int,input().split())

adj = [[] for _ in range(1001)]
vis = [0 for _ in range(1001)]
queue = deque()
dfs_lst = []
bfs_lst = []

for i in range(1,m+1):
    u, v = map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)

for i in range(1,n+1):
    adj[i].sort()

# DFS 수행
dfs(l)
vis = [0 for _ in range(1001)]
print('')
# BFS 수행
bfs()