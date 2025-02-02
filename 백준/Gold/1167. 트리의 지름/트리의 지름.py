import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(start):
    for nxt, cost in graph[start]:
        if dist[nxt] >= 0:
            continue
        dist[nxt] = dist[start] + cost
        dfs(nxt)

n = int(input())
graph = [[] for _ in range(n+1)]
nodes = [list(map(int, input().split())) for _ in range(n)]
dist = [-1 for _ in range(n+1)]
dist[1] = 0

for i in range(n):
    lst = nodes[i]
    for j in range(1, len(lst)-1, 2):
        graph[lst[0]].append((lst[j], lst[j+1]))

dfs(1)
end = dist.index(max(dist))

dist = [-1 for _ in range(n+1)]
dist[end] = 0
dfs(end)

print(max(dist))