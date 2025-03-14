import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def union(a, b):
    pa = find(a)
    pb = find(b)

    if pa < pb:
        parent[pb] = pa
        return pa, pb
    elif pa > pb:
        parent[pa] = pb
        return pb, pa

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

t = int(input())

for _ in range(t):
    n = int(input())
    parent = [i for i in range((2*n) + 1)]
    ans = [1 for _ in range((2*n) + 1)]
    name = dict()
    m = 1

    for _ in range(n):
        p, q = map(str, input().rstrip().split())
        if p not in name:
            name[p] = m
            m += 1
        if q not in name:
            name[q] = m
            m += 1

        np = find(name[p])
        nq = find(name[q])

        if np != nq:
            small, large = union(np, nq)
            ans[small] += ans[large]
            print(ans[small])
        else:
            print(ans[np])