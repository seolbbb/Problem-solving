import sys
import heapq

n = int(input())
arr = list(map(int, input().split()))
sorted_arr = sorted(arr)
m = int(input())
cmd = [list(map(int, input().split())) for _ in range(m)]

costs = {}
costs[tuple(arr)] = 0
hq = [(0, arr)]

while hq:
    curcost, cur = heapq.heappop(hq)
    if costs[tuple(cur)] < curcost:
        continue
    if cur == sorted_arr:
        continue

    for l, r, c in cmd:
        tmp = 0
        nxt = cur[:]
        tmp = nxt[l-1]
        nxt[l-1] = nxt[r-1]
        nxt[r-1] = tmp
        if tuple(nxt) in costs and costs[tuple(nxt)] <= curcost + c:
            continue
        costs[tuple(nxt)] = curcost + c
        heapq.heappush(hq, (curcost + c, nxt))

print(costs.get(tuple(sorted_arr), -1))