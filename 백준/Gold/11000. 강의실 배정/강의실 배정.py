import sys
import heapq
input = sys.stdin.readline

n = int(input())
times = []
hq = [0]
res = 0

for _ in range(n):
    s, t = map(int,input().split())
    times.append((s,t))

times.sort(key = lambda x: (x[0],x[1]))

for s, t in times:
    while hq and hq[0] <= s:
        heapq.heappop(hq)
    heapq.heappush(hq,t)
    res = max(res,len(hq))

print(res)