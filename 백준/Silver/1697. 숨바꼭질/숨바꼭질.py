from collections import deque
n, k = map(int,input().split())
queue = deque()
dist = []
for i in range(100001):
    dist.append(-1)
queue.append(n)
dist[n] = 0

while queue:
    x = queue.popleft()
    dx = [-1,1,x]
    if x == k:
        print(dist[x])
    for i in range(3):
        nx = x + dx[i]
        if nx < 0 or nx > 100000:
            continue
        if dist[nx] >= 0:
            continue
        queue.append(nx)
        dist[nx] = dist[x] + 1