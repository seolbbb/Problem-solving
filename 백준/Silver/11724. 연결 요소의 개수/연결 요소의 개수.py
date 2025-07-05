from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    if visit[i]:
        continue

    queue = deque([i])
    visit[i] = 1
    cnt += 1

    while queue:
        cur = queue.popleft()

        for nxt in graph[cur]:
            if visit[nxt]:
                continue
            queue.append(nxt)
            visit[nxt] = 1

print(cnt)