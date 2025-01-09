import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    dist[start] = 0
    hq = [(0,start)]

    while hq:
        curcost,cur = heapq.heappop(hq)

        if dist[cur] < curcost:
            continue
        
        for nxt, cost in graph[cur]:
            newcost = curcost + cost
            if dist[nxt] > newcost:
                dist[nxt] = newcost
                heapq.heappush(hq, (newcost,nxt))
    

v,e = map(int,input().split())
st = int(input())
graph = [[] for _ in range(v+1)]
dist = [float('inf') for _ in range(v+1)]
lst = []

for _ in range(e):
    s,d,c = map(int,input().split())
    graph[s].append((d,c))

dijkstra(st)

for i in range(1,v+1):
    if dist[i] == float('inf'):
        lst.append('INF')
    else:
        lst.append(dist[i])

print(*lst,sep = '\n')