import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
bacon_number = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    dist = [-1 for _ in range(n+1)]
    queue = deque([i])
    dist[i] = 0

    while queue:
        cur = queue.popleft()

        for nxt in graph[cur]:
            if dist[nxt] != -1:
                continue
            dist[nxt] = dist[cur] + 1
            queue.append(nxt)
    
    bacon_number.append((i, sum(dist)+1))

bacon_number.sort(key=lambda x: (x[1], x[0]))

print(bacon_number[0][0])