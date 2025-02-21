from collections import deque

n = int(input())
a, b = map(int, input().split())
graph = [[] for _ in range(n+1)]
dist = [-1 for _ in range(n+1)]
m = int(input())

for _ in range(m):
    p, c = map(int, input().split())
    graph[p].append(c)
    graph[c].append(p)

queue = deque([a])
dist[a] = 0

while queue:
    cur = queue.popleft()

    for nxt in graph[cur]:
        if dist[nxt] > 0:
            continue
        dist[nxt] = dist[cur] + 1
        queue.append(nxt)

print(dist[b])