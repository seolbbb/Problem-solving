import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
graph = [[] for i in range(n+1)]
degree = [0 for _ in range(n+1)]
queue = deque()
ans = []

for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    degree[b] += 1

for i in range(1, n+1):
    if degree[i] == 0:
        queue.append(i)

while queue:
    cur = queue.popleft()
    ans.append(cur)

    for nxt in graph[cur]:
        degree[nxt] -= 1
        if degree[nxt] == 0:
            queue.append(nxt)

print(*ans)