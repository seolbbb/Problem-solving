import sys
from collections import deque

n = int(sys.stdin.readline())
visit = [[0 for _ in range(n)] for _ in range(n)]
color = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
queue = deque()
cnt1 = 0
cnt2 = 0

for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            queue.append((i,j))
            visit[i][j] = 1
            cnt1 += 1
            while queue:
                x,y = queue.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if visit[nx][ny] == 1 or color[nx][ny] != color[x][y]:
                        continue
                    queue.append((nx,ny))
                    visit[nx][ny] = 1

visit = [[0 for _ in range(n)] for _ in range(n)]      
      
for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            queue.append((i,j))
            visit[i][j] = 1
            cnt2 += 1
            while queue:
                x,y = queue.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if visit[nx][ny] == 1:
                        continue
                    if color[x][y] == 'B' and color[nx][ny] != 'B':
                        continue
                    if color[x][y] == 'R' and color[nx][ny] == 'B' or color[x][y] == 'G' and color[nx][ny] == 'B':
                        continue
                    queue.append((nx,ny))
                    visit[nx][ny] = 1

print(cnt1, end = ' ')
print(cnt2)