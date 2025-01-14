from collections import deque

n, m = map(int,input().split())

dist = [-1 for _ in range(101)]
skip = [0 for _ in range(101)]
queue = deque()

for _ in range(n+m):
    s, d = map(int,input().split())
    skip[s] = d

queue.append(1)
dist[1] = 0

while queue:
    x = queue.popleft()

    if x == 100:
        break

    for i in range(1,7):
        nx = x + i
        if nx > 100:
            continue
        if skip[nx] > 0:
            nx = skip[nx]
        if dist[nx] >= 0:
            continue
        dist[nx] = dist[x] + 1
        queue.append(nx)

print(dist[100])