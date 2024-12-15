import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
dx = [0,1,0,-1]
dy = [1,0,-1,0]
board = []
distant = [[0 for _ in range(m)] for _ in range(n)]
queue = deque()
for i in range(n):
    board.append(list(map(int,sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            queue.append((i,j))
        elif board[i][j] == 0:
            distant[i][j] = -1

while queue:
    x, y = queue.popleft()
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if xx < 0 or xx >= n or yy < 0 or yy >= m:
            continue
        if board[xx][yy] != 0 or distant[xx][yy] >= 0:
            continue
        queue.append((xx,yy))
        distant[xx][yy] = distant[x][y] + 1

day = 0

for i in distant:
    for j in i:
        if j == -1:
            print(-1)
            exit(0)
        day = max(j,day)

if day == 0:
    print(0)
else:
    print(day)