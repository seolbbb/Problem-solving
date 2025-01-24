import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def union(a, b):
    pa = find(a)
    pb = find(b)
    p[pa] = pb

def find(a):
    if a != p[a]:
        p[a] = find(p[a])
    return p[a]

n, m = map(int,input().split())

p = [i for i in range(n+1)]

for _ in range(m):
    q, a, b = map(int,input().split())

    if q == 0:
        union(a,b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')