import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
hq = []

for _ in range(n):
    x = int(input())

    if x:
        heappush(hq, (abs(x), x))
    else:
        if hq:
            print(heappop(hq)[1])
        else:
            print(0)