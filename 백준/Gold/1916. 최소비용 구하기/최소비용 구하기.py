import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
dist = [float('inf')] * (n+1)

for _ in range(m):
    st,dt,cost = map(int,input().split())
    graph[st].append((dt,cost))

st,dt = map(int,input().split())

def dijkstra(start):
    dist[start] = 0

    pq = [(0,start)]

    while pq:
        curcost,cur = heapq.heappop(pq)

        if dist[cur] < curcost:
            continue
            
        for nxt, c in graph[cur]:
            newcost = curcost + c
            if dist[nxt] > newcost:
                dist[nxt] = newcost
                heapq.heappush(pq, (newcost,nxt))

dijkstra(st)
print(dist[dt])