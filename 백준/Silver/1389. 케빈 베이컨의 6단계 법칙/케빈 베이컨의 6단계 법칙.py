import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    dist = [-1 for _ in range(n+1)]
    queue = deque()
    queue.append(start)
    dist[start] = 0

    while queue:
        cur = queue.popleft()

        for nxt in graph[cur]:
            if dist[nxt] >= 0:
                continue
            queue.append(nxt)
            dist[nxt] = dist[cur] + 1

    return sum(dist)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
k_num = float('inf')
ans = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    tmp = bfs(i)
    if k_num > tmp:
        k_num = tmp
        ans = i

print(ans)