import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())
dx = [0,1,0,-1]
dy = [1,0,-1,0]
board = []
distant = [[-1 for _ in range(m)] for _ in range(n)]
queue = deque()

for i in range(n):
    board.append(list(map(int,sys.stdin.readline().rstrip())))

queue.append((0,0))
distant[0][0] = 0
while queue:
    x, y = queue.popleft()
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if xx < 0 or xx >= n or yy < 0 or yy >= m:
            continue
        if board[xx][yy] == 0 or distant[xx][yy] >= 0:
            continue
        queue.append((xx,yy))
        distant[xx][yy] = distant[x][y] + 1

print(distant[n-1][m-1] + 1)