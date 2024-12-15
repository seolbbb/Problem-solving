import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())
dx = [0,1,0,-1]
dy = [1,0,-1,0]
dz = [1,-1]
board = [[list(map(int,sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
distant = [[[0 for _ in range(m)] for _ in range(n)]for _ in range(h)]
queue = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if board[i][j][k] == 1:
                queue.append((i,j,k))
            elif board[i][j][k] == 0:
                distant[i][j][k] = -1

while queue:
    z, x, y = queue.popleft()
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if xx < 0 or xx >= n or yy < 0 or yy >= m:
            continue
        if board[z][xx][yy] != 0 or distant[z][xx][yy] >= 0:
            continue
        queue.append((z,xx,yy))
        distant[z][xx][yy] = distant[z][x][y] + 1
    for i in range(2):
        zz = z + dz[i]
        if zz < 0 or zz >= h:
            continue
        if board[zz][x][y] != 0 or distant[zz][x][y] >= 0:
            continue
        queue.append((zz,x,y))
        distant[zz][x][y] = distant[z][x][y] + 1

day = 0

for i in distant:
    for j in i:
        for k in j:
            if k == -1:
                print(-1)
                exit(0)
            day = max(k,day)

if day == 0:
    print(0)
else:
    print(day)