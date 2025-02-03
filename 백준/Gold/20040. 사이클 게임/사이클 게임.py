import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def union(a, b):
    pa = find(a)
    pb = find(b)
    if rank[pa] == rank[pb]:
        parent[pa] = pb
        rank[pb] += 1
    elif rank[pa] > rank[pb]:
        parent[pb] = pa
    else:
        parent[pa] = pb

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

n, m = map(int, input().split())
parent = [i for i in range(n)]
rank = [1 for _ in range(n)]
ans = 0

for i in range(1, m+1):
    a, b = map(int, input().split())

    if find(a) != find(b):
        union(a, b)
    else:
        ans = i
        break

print(ans)