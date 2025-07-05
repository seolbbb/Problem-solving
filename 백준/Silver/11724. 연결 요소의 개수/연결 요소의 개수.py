import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def union(a, b):
    a = find(a)
    b = find(b)

    if a > b:
        parent[a] = b
    elif a < b:
        parent[b] = a

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

for i in range(1, n+1):
    find(i)

print(len(set(parent))-1)