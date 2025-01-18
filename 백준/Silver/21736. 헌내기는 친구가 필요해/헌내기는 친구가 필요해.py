import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
board = [list(input().rstrip()) for _ in range(n)]
visit = [[0 for _ in range(m)] for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
queue = deque()
cnt = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 'I':
            queue.append((i,j))
            visit[i][j] = 1

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if visit[nx][ny] == 1 or board[nx][ny] == 'X':
            continue
        if board[nx][ny] == 'P':
            cnt += 1
        queue.append((nx,ny))
        visit[nx][ny] = 1

if cnt == 0:
    print('TT')
else:
    print(cnt)