import heapq

n, k = map(int,input().split())
dist = [float('inf') for _ in range(200001)]
# 시간복잡도 줄이기 위해 dist 배열의 크기를 k * 2 + 1 로 바꿨는데 오류가 뜸.
# n이 k보다 클 경우도 생각해야 하기 때문

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