import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int,input().split())
    time = [0] + list(map(int,input().split()))
    graph = [[] for _ in range(n+1)]
    prev = [[] for _ in range(n+1)]
    in_degree = [0 for _ in range(n+1)]
    dp = [time[i] for i in range(n+1)]
    queue = deque()

    for _ in range(k):
        a, b = map(int,input().split())
        graph[a].append(b)
        prev[b].append(a)
        in_degree[b] += 1
    w = int(input())

    for i in range(1,n+1):
        if in_degree[i] == 0:
            queue.append(i)

    while queue:
        cur = queue.popleft()
        prev_time = 0

        for p in prev[cur]:
            prev_time = max(prev_time, dp[p])
        dp[cur] += prev_time

        for nxt in graph[cur]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)
        
    print(dp[w])