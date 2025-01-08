import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
parent = [0 for _ in range(n+1)]
queue = deque()
parent[1] = -1

for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

queue.append(1)
while queue:
    node = queue.popleft()
    for nxt in graph[node]:
        if parent[nxt] == 0:
            parent[nxt] = node
            queue.append(nxt)

for i in range(2,n+1):
    print(parent[i])