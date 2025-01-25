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

v, e = map(int, input().split())
parent = [i for i in range(v+1)]
edges = sorted([list(map(int, input().split())) for _ in range(e)], 
               key = lambda x: x[2])
cost = []

for a, b, c in edges:
    if len(cost) == v - 1:
        break

    if find(a) != find(b):
        cost.append(c)
        union(a, b)
    
print(sum(cost))