import heapq

n, k = map(int,input().split())
dx = [(0,n),(1,1),(1,-1)]
dist = [float('inf') for _ in range(200001)]
hq = [(0,n)]
dist[n] = 0

while hq:
    curcost, cur = heapq.heappop(hq)

    if dist[cur] < curcost:
        continue

    dx = [(0,cur),(1,1),(1,-1)]    

    for i in range(3):
        cost, move = dx[i]
        nxt = cur + move
        newcost = curcost + cost
        if 0 <= nxt < 200001 and dist[nxt] > newcost:
            dist[nxt] = newcost
            heapq.heappush(hq, (newcost,nxt))

print(dist[k])