import sys
input = sys.stdin.readline

def union(a, b):
    pa = find(a)
    pb = find(b)

    if rank[pa] == rank[pb]:
        rank[pa] += 1
        parent[pb] = pa
    elif rank[pa] > rank[pb]:
        parent[pb] = pa
    else:
        parent[pa] = pb

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

n = int(input())
m = int(input())
parent = [i for i in range(n+1)]
rank = [0 for _ in range(n+1)]
enemy = [[] for _ in range(n+1)]

for _ in range(m):
    cmd, a, b = map(str, input().split())
    a = int(a)
    b = int(b)
    find(a)
    find(b)
    
    if cmd == 'E':
        enemy[a].append(b)
        enemy[b].append(a)
        if len(enemy[a]) >= 2:
            union(enemy[a][0], b)
        elif len(enemy[b]) >= 2:
            union(enemy[b][0], a)
    
    if cmd == 'F':
        union(a, b)

ans = len(list(set(parent)))-1

print(ans)