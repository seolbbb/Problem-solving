import sys
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
m = int(input())
parent = [i for i in range(n+1)]
graph = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union(i+1, j+1)

path = list(map(int,input().split()))

connected = 1
for i in range(len(path) -1):
    if find(path[i]) != find(path[i+1]):
        connected = 0
        break

if connected == 1:
    print('YES')
else:
    print('NO')