import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def union(a, b):
    pa = find(a)
    pb = find(b)
    if pa > pb:
        parent[pa] = pb
    else:
        parent[pb] = pa

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

g = int(input())
p = int(input())
parent = [i for i in range(g+1)]
planes = [int(input()) for _ in range(p)]
ans = 0

for plane in planes:
    if find(plane) == 0:
        break
    union(find(plane), find(plane)-1)
    ans += 1

print(ans)