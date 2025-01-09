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

        for nxt, cost in graph[cur]:
            newcost = curcost + cost
            if dist[nxt] > newcost:
                dist[nxt] = newcost
                heapq.heappush(hq, (newcost, nxt))
    
    return dist[destination]

n, m, x = map(int,input().split())
graph = [[] for _ in range(n+1)]
time = [0 for _ in range(n+1)]
hq = []

for _ in range(m):
    s, d, cost = map(int,input().split())
    graph[s].append((d,cost))

for i in range(1,n+1):
    cost1 = dijkstra(i,x)
    cost2 = dijkstra(x,i)
    time[i] = cost1 + cost2
    
print(max(time))