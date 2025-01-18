import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    dist = [-1 for _ in range(n+1)]
    dist[start] = 0
    queue = deque([start])

    while queue:
        x = queue.popleft()
        for nxt, cost in graph[x]:
            if dist[nxt] >= 0:
                continue
            dist[nxt] = dist[x] + cost
            queue.append(nxt)
    
    return dist

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    s, d, c = map(int,input().split())
    graph[s].append((d,c))
    graph[d].append((s,c))

dist1 = bfs(1)
a = 1
for i in range(1,n+1):
    if dist1[i] > dist1[a]:
        a = i

dist2 = bfs(a)
b = a
for i in range(1,n+1):
    if dist2[i] > dist2[b]:
        b = i

print(dist2[b])