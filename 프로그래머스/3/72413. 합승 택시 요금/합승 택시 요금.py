import heapq
import copy

def solution(n, s, a, b, fares):
    
    def dijkstra(st):
        dist = [float('inf') for _ in range(n+1)]
        hq = [(0, st)]
        dist[st] = 0

        while hq:
            curcost, cur = heapq.heappop(hq)
            if dist[cur] < curcost:
                continue

            for cost, nxt in graph[cur]:
                newcost = curcost + cost
                if dist[nxt] > newcost:
                    dist[nxt] = newcost
                    heapq.heappush(hq, (newcost, nxt))

        return dist

    graph = [[] for _ in range(n+1)]
    answer = float('inf')
    
    for st, dt, cost in fares:
        graph[st].append((cost, dt))
        graph[dt].append((cost, st))
    
    dist1 = dijkstra(s)
    nxt = [(i, v) for i, v in enumerate(dist1) if v != float('inf')]
    
    for i, v in nxt:
        tmp = v
        d = dijkstra(i)
        tmp += d[a]
        tmp += d[b]
        answer = min(answer, tmp)
    
    return answer