import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    dist = [float('inf') for _ in range(n+1)]
    dist[start] = 0
    hq = [(0,start)]

    while hq:
        curcost, cur = heapq.heappop(hq)

        if dist[cur] < curcost:
            continue
        for nxt, cost in graph[cur]:
            newcost = curcost + cost
            if dist[nxt] > newcost:
                dist[nxt] = newcost
                heapq.heappush(hq,(newcost, nxt))
    
    return dist

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    s, d, c = map(int,input().split())
    graph[s].append((d,c))
    graph[d].append((s,c))

dist1 = dijkstra(1)
a = 1
for i in range(1, n+1):
    if dist1[i] > dist1[a]:
        a = i

dist2 = dijkstra(a)
b = a
for i in range(1, n+1):
    if dist2[i] > dist2[b]:
        b = i

print(dist2[b])