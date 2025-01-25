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

n = int(input())
parent = [i for i in range(n)]
edges = []
planets = []

for i in range(n):
    x, y, z = map(int, input().split())
    planets.append((x, y, z, i))

for k in range(3):
    planets.sort(key = lambda x: x[k])
    for i in range(n-1):
        x1, y1, z1, idx1 = planets[i]
        x2, y2, z2, idx2 = planets[i+1]
        cost = min(abs(x1-x2), abs(y1-y2), abs(z1-z2))
        edges.append((cost, idx1, idx2))

edges.sort(key = lambda x: x[0])

ans = 0
selected = 0

for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        ans += cost
        selected += 1
        if selected == n-1:
            break

print(ans)