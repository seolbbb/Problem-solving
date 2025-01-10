from collections import deque

def bfs1(num,s):

    dist = [-1 for _ in range(200001)]
    queue = deque()

    queue.append(num)
    dist[num] = 0
    cnt = 1
    min_time = 0

    while queue:
        cur = queue.popleft()
        dx = [-1,1,cur]

        for i in dx:
            nx = cur + i

            if nx == s and dist[cur] + 1 == min_time:
                cnt += 1

            if nx < 0 or nx > 200000:
                continue
            if dist[nx] >= 0 and dist[nx] != dist[cur] + 1:
                continue
            dist[nx] = dist[cur] + 1
            queue.append(nx)
        
        if dist[s] >= 0:
            min_time = dist[s]

    return dist[k], cnt

n, k = map(int,input().split())

time, cnt = bfs1(n, k)
print(time)
print(cnt)