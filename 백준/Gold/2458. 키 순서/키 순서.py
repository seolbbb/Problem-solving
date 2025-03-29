from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
in_order = [0 for _ in range(n+1)]
out_order = [0 for _ in range(n+1)]
ans = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

for i in range(1, n+1):
    queue = deque(graph[i])
    visit = [0 for _ in range(n+1)]

    while queue:
        cur = queue.popleft()
        if visit[cur] == 1:
            continue
        visit[cur] = 1
        in_order[cur] += 1
        out_order[i] += 1

        for nxt in graph[cur]:
            queue.append(nxt)

for i in range(1, n+1):
    if in_order[i] + out_order[i] == n-1:
        ans += 1

print(ans)