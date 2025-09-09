# 최단거리 구하기 문제
# 노드 사이의 거리가 모두 1이기 때문에 다익스트라 필요 없이 BFS로 풀 수 있음.

import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
dist = [-1 for _ in range(n+1)]
queue = deque([])
ans = []

for _ in range(m):  # 그래프 연결
    a, b = map(int, input().split())
    graph[a].append(b)

queue.append(x)
dist[x] = 0

while queue:
    cur = queue.popleft()

    for nxt in graph[cur]:
        if dist[nxt] >= 0:  # 이미 방문했으면 continue
            continue
        dist[nxt] = dist[cur] + 1   # 현재 위치에서 거리 + 1 해주기
        if dist[nxt] == k:
            ans.append(nxt)     # 거리가 K 라면 ans에 추가
        queue.append(nxt)

ans.sort()
if ans:
    print(*ans, sep='\n')
else:
    print(-1)