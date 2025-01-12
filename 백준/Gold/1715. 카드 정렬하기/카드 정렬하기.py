import sys
import heapq
input = sys.stdin.readline

n = int(input())
hq = []
res = 0

for _ in range(n):
    heapq.heappush(hq,int(input()))

while hq:
    if len(hq) == 1:
        break
    
    a = heapq.heappop(hq)
    b = heapq.heappop(hq)
    res += a + b
    heapq.heappush(hq,a+b)

print(res)