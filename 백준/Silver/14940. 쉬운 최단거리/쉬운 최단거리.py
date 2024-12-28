import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
board = [[] for _ in range(n)]
dist = [[-1 for _ in range(m)] for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
queue = deque()

for i in range(n):
    board[i] = list(map(int,input().split()))

for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            queue.append((i,j))
            dist[i][j] = 0

while queue:
    x,y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if board[nx][ny] == 0 or dist[nx][ny] >= 0:
            continue
        queue.append((nx,ny))
        dist[nx][ny] = dist[x][y] + 1


for i in range(n):
    for j in range(m):
        if dist[i][j] == -1 and board[i][j] == 0:
            dist[i][j] = 0

for row in dist:
    print(*row)