# BFS
# from collections import deque

# n = int(input())
# m = int(input())

# graph = [[] for _ in range(n+1)]
# visit = [0 for _ in range(n+1)]
# queue = deque()
# cnt = 0

# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# queue.append(1)
# visit[1] = 1

# while queue:
#     cur = queue.popleft()

#     for nxt in graph[cur]:
#         if visit[nxt] == 1:
#             continue
#         queue.append(nxt)
#         visit[nxt] = 1
#         cnt += 1

# print(cnt)

# Union-Find

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

n = int(input())
m = int(input())
parent = [i for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

print(sum(1 for i in range(2, n+1) if find(i) == find(1)))