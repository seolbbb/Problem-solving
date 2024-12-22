import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]
dist = [-1 for _ in range(n+1)]
queue = deque()
num = 0

for _ in range(m):
    u, v = map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)

queue.append(1)
dist[1] = 0
while queue:
    cur = queue.popleft()
    for nxt in adj[cur]:
        if dist[nxt] >= 0:
            continue
        queue.append(nxt)
        dist[nxt] = dist[cur] + 1
        if dist[nxt] <= 2:
            num += 1

print(num)