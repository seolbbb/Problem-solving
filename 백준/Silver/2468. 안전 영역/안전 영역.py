import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
dx = [0,1,0,-1]
dy = [1,0,-1,0]
height = [list(map(int,input().split())) for _ in range(n)]
max_height = max([max(row) for row in height])
safe_cnt = []

for i in range(0,max_height + 1):
    visit = [[0 for _ in range(n)] for _ in range(n)]
    queue = deque()
    cnt = 0
    for j in range(n):
        for k in range(n):
            if height[j][k] <= i:
                visit[j][k] = 1

    for j in range(n):
        for k in range(n):
            if visit[j][k] == 0:
                cnt += 1
                queue.append((j,k))
                visit[j][k] = 1
                while queue:
                    x, y = queue.popleft()
                    for m in range(4):
                        nx = x + dx[m]
                        ny = y + dy[m]
                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue
                        if visit[nx][ny] == 1:
                            continue
                        queue.append((nx,ny))
                        visit[nx][ny] = 1
    
    safe_cnt.append(cnt)

print(max(safe_cnt))