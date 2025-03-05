import sys
import heapq
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

def union(a, b):
    pa = find(a)
    pb = find(b)

    if pa != pb:
        parent[pa] = pb

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

n = int(input())
parent = [i for i in range(n+1)]
edges = []
vertex = []

for i in range(1, n+1):
    x, y = map(float, input().split())
    
    for edge, ex, ey in edges:
        dist = ((ex-x)**2 + (ey-y)**2) ** 0.5
        vertex.append((dist, edge, i))
    edges.append((i, x, y))

heapq.heapify(vertex)
cnt = 0
ans = 0

while cnt < n-1:
    dist, a, b = heapq.heappop(vertex)

    if find(a) != find(b):
        union(a, b)
        cnt += 1
        ans += dist

print(round(ans, 2))