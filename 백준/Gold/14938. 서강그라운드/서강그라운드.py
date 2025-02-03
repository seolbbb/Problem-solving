n, m, r = map(int, input().split())
items = list(map(int, input().split()))
graph = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
ans = 0

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)
    graph[b][a] = min(graph[b][a], c)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j],
                              graph[i][k]+graph[k][j])

for i in range(1, n+1):
    tmp = 0

    for j in range(1, n+1):
        if graph[i][j] <= m:
            tmp += items[j-1]

    ans = max(ans, tmp)

print(ans)