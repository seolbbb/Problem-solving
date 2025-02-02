import sys
import heapq
input = sys.stdin.readline

def dijkstra(s, d):
    dist = [float('inf') for _ in range(n+1)]
    parent = [i for i in range(n+1)]
    path = []
    hq = [(0, s)]
    dist[s] = 0

    while hq:
        curcost, cur = heapq.heappop(hq)

        if dist[cur] < curcost:
            continue

        for cost, nxt in graph[cur]:
            newcost = curcost + cost
            if dist[nxt] > newcost:
                dist[nxt] = newcost
                parent[nxt] = cur
                heapq.heappush(hq, (newcost, nxt))

    p = d
    while parent[p] != p:
        path.append(p)
        p = parent[p]
    path.append(p)
    path = path[::-1]
    
    return dist[d], path


n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

st, dt = map(int, input().split())
length, pa = dijkstra(st, dt)
print(length)
print(len(pa))
print(*pa, sep=' ')