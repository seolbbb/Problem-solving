import sys
input = sys.stdin.readline

def bellman_ford(start, n, edges):
    dist = [float('inf') for _ in range(n+1)]
    dist[start] = 0

    for i in range(n):
        for cur, nxt, cost in edges:
            if dist[cur] != float('inf') and dist[nxt] > dist[cur] + cost:
                dist[nxt] = dist[cur] + cost
    
    for cur, nxt, cost in edges:
        if dist[cur] != float('inf') and dist[nxt] > dist[cur] + cost:
            return True
    
    return False

tc = int(input())
for _ in range(tc):
    n, m, w = map(int, input().split())
    edges = []

    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))

    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    for i in range(1, n+1):
        edges.append((0, i, 0))

    if bellman_ford(0, n, edges):
        print('YES')
    else:
        print('NO')