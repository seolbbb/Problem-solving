import sys
from collections import deque
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(node):
    visit[node] = 1
    dfs_lst.append(node)
    for nxt in graph[node]:
        if visit[nxt]:
            continue
        dfs(nxt)

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]
dfs_lst = []
bfs_lst = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

dfs(v)

# bfs

visit = [0 for _ in range(n+1)]
queue = deque([v])
visit[v] = 1

while queue:
    cur = queue.popleft()
    bfs_lst.append(cur)

    for nxt in graph[cur]:
        if visit[nxt]:
            continue
        visit[nxt] = 1
        queue.append(nxt)


print(*dfs_lst)
print(*bfs_lst)