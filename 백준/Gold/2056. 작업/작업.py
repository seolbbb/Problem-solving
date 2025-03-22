import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
in_degree = [0 for _ in range(n+1)]
time = [0 for _ in range(n+1)]
start_time = [0 for _ in range(n+1)]
queue = deque()
ans = 0

# 진입 차수, graph 리스트 생성
for i in range(1, n+1):
    lst = list(map(int, input().split()))
    time[i] = lst[0]
    if lst[1] > 0:
        in_degree[i] = lst[1]
        for m in lst[2:]:
            graph[m].append(i)

# 진입 차수 0 인 간선 큐에 추가
for i in range(1, n+1):
    if in_degree[i] == 0:
        queue.append(i)

while queue:
    cur = queue.popleft()

    for nxt in graph[cur]:
        in_degree[nxt] -= 1
        start_time[nxt] = max(start_time[nxt], start_time[cur] + time[cur])
        if in_degree[nxt] == 0:
            queue.append(nxt)
    
for i in range(1, n+1):
    ans = max(ans, start_time[i] + time[i])

print(ans)