from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    dist = [-1 for _ in range(n+1)]
    queue = deque()
    answer = 0
    
    for s, d in edge:
        graph[s].append(d)
        graph[d].append(s)

    queue.append(1)
    dist[1] = 0
    
    while queue:
        cur = queue.popleft()
        
        for nxt in graph[cur]:
            if dist[nxt] >= 0:
                continue
            queue.append(nxt)
            dist[nxt] = dist[cur] + 1
    
    max_dist = max(dist)
    for d in dist:
        if d == max_dist:
            answer += 1
    
    return answer