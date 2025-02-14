import sys
import heapq
input = sys.stdin.readline

def union(a, b):
    pa = find(a)
    pb = find(b)

    if pa != pb:
        parent[pa] = pb

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

n = int(input())
m = int(input())
parent = [i for i in range(n+1)]
edges = []
cnt = 0
cost = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    heapq.heappush(edges, (c, a, b))

while cnt < n-1:
    c, a, b = heapq.heappop(edges)

    if find(a) != find(b):
        union(a, b)
        cnt += 1
        cost += c

print(cost)