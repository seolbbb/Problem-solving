import sys
import heapq
input = sys.stdin.readline

def dijkstra(start,destination):
    dist = [float('inf') for _ in range(n+1)]
    dist[start] = 0
    hq = [(0,start)]

    while hq:
        curcost, cur = heapq.heappop(hq)

        if dist[cur] < curcost:
            continue

        for nxt,cost in graph[cur]:
            newcost = curcost + cost
            if dist[nxt] > newcost:
                dist[nxt] = newcost
                heapq.heappush(hq,(newcost,nxt))
    
    return dist[destination]

n,e = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(e):
    s,d,c = map(int,input().split())
    graph[s].append((d,c))
    graph[d].append((s,c))

v1,v2 = map(int,input().split())

dist1 = dijkstra(1,v1) + dijkstra(v1,v2) + dijkstra(v2,n)
dist2 = dijkstra(1,v2) + dijkstra(v2,v1) + dijkstra(v1,n)

res = min(dist1,dist2)

if res == float('inf'):
    print(-1)
else:
    print(res)