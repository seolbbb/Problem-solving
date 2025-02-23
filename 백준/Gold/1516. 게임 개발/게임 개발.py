import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
in_degree = [0 for _ in range(n+1)]
time = [0 for _ in range(n+1)]
queue = deque()

for i in range(1, n+1):
    lst = list(map(int, input().split()))

    for j in range(len(lst)-1):
        if j == 0:
            time[i] = lst[j]
        else:
            graph[lst[j]].append(i)
            in_degree[i] += 1

for i in range(1, n+1):
    if in_degree[i] == 0:
        queue.append(i)

cur_max = time[:]

while queue:
    cur = queue.popleft()

    for nxt in graph[cur]:
        in_degree[nxt] -= 1
        cur_max[nxt] = max(cur_max[nxt], cur_max[cur] + time[nxt])
        if in_degree[nxt] == 0:
            queue.append(nxt)
            
for i in range(1, len(time)):
    print(cur_max[i])