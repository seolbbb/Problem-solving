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
    return(parent[a])

n, m = map(int, input().split())
enemy = [[] for _ in range(n+1)]
parent = [i for i in range(n+1)]
rank = [0 for _ in range(n+1)]
ans = 1

for _ in range(m):
    a, b = map(int, input().split())
    enemy[a].append(b)
    enemy[b].append(a)

    if find(a) == find(b):
        ans = 0
        break
    elif len(enemy[a]) >= 2:
        union(enemy[a][0], b)
    elif len(enemy[b]) >= 2:
        union(enemy[b][0], a)

print(ans)