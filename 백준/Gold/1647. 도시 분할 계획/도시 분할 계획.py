import sys
sys.setrecursionlimit(10**7)
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

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
edges = [list(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x: x[2])

mst = []

for a, b, cost in edges:
    if find(a) != find(b):
        union(a, b)
        mst.append(cost)
        if len(mst) == n-1:
            break

print(sum(mst)-max(mst))