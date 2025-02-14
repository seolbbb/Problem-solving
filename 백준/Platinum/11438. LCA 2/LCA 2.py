import sys
from math import log2
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# depth와 parent 저장하는 리스트 생성
depth = [0 for _ in range(n+1)]
parent = [0 for _ in range(n+1)]
parent[1] = 1
depth[1] = 0

queue = deque([1])
dist = [-1 for _ in range(n+1)]
dist[1] = 0

while queue:
    cur = queue.popleft()
    for nxt in graph[cur]:
        if dist[nxt] >= 0:
            continue
        dist[nxt] = dist[cur] + 1
        queue.append(nxt)
        depth[nxt] = dist[nxt]
        parent[nxt] = cur

# sparse table 생성
k = int(log2(n)) + 1
st = [[0 for _ in range(n+1)] for _ in range(k)]


for i in range(1, n+1):
    st[0][i] = parent[i]

for i in range(1, k):
    for j in range(1, n+1):
        st[i][j] = st[i-1][st[i-1][j]]

# LCA 구하기
q = int(input())

for _ in range(q):
    n1, n2 = map(int, input().split())

    if depth[n1] > depth[n2]:
        n1, n2 = n2, n1
    diff = depth[n2] - depth[n1]

    # n2에서 깊이의 차이만큼 이동한 후의 노드 구함(깊이 맞추기).
    for exp in range(k):
        if diff & (1 << exp):
            n2 = st[exp][n2]

    if n1 == n2:
        print(n1)
        continue
    
    # 각각의 노드에서 2^exp 번 거슬러 올라갔을 때 
    # 두 개의 노드가 같지 않다면 거슬러 올라간 노드로 갱신
    for exp in range(k-1, -1, -1):
        if st[exp][n1] != st[exp][n2]:
            n1 = st[exp][n1]
            n2 = st[exp][n2]
    
    print(parent[n1])