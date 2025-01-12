import sys
import heapq
input = sys.stdin.readline

n, k = map(int,input().split())
gems = []
bags = []

for _ in range(n):
    m, v = map(int,input().split())
    gems.append((m, v))

for _ in range(k):
    bags.append(int(input()))

gems.sort()
bags.sort()

max_heap = []
res = 0
i = 0

for bag in bags:
    while i < n and gems[i][0] <= bag:
        heapq.heappush(max_heap, -gems[i][1])
        i += 1

    if max_heap:
        res += -heapq.heappop(max_heap)

print(res)