from collections import deque
from collections import defaultdict

a,b = map(int,input().split())
dist = defaultdict(int)
queue = deque()
queue.append(a)
dist[a] = 1

while queue:
    x = queue.popleft()
    nx = x*2
    if nx > b:
        continue
    if dist[nx]:
        continue
    queue.append(nx)
    dist[nx] = dist[x] + 1

    nx = (x*10)+1
    if nx > b:
        continue
    if dist[nx]:
        continue
    queue.append(nx)
    dist[nx] = dist[x] + 1

if dist[b] == 0:
    print(-1)
else:
    print(dist[b])