import heapq

def dijkstra(start):
    dist = [float('inf') for _ in range(n)]
    dist[start] = 0
    hq = [(0, start)]

    while hq:
        curcost, cur = heapq.heappop(hq)
        if curcost > dist[cur]:
            continue
        
        for cost, nxt in graph[cur]:
            newcost = cost + curcost
            if newcost < dist[nxt]:
                dist[nxt] = newcost
                heapq.heappush(hq, (newcost, nxt))

    return dist

def backtrack(num, cur):
    global total, ans

    if num == n:
        ans = min(ans, total)
        return
    
    if total >= ans:
        return

    for i in range(n):
        if visit[i] == 1:
            continue
        time = cost[cur][i]
        visit[i] = 1
        total += time
        backtrack(num + 1, i)
        visit[i] = 0
        total -= time

n, k = map(int, input().split())
adj = [list(map(int, input().split())) for _ in range(n)]
graph = [[] for _ in range(n)]
visit = [0 for _ in range(n)]
cost = []
total = 0
ans = 10**6

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        graph[i].append((adj[i][j], j))

# 미리 i -> j 가는 경로 다 구해놓기.
for i in range(n):
    cost.append(dijkstra(i))

backtrack(0, k)
print(ans)