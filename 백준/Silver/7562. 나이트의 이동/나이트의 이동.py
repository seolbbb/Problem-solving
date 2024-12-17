import sys
from collections import deque

t = int(sys.stdin.readline())
dx = [1,1,2,2,-1,-1,-2,-2]
dy = [2,-2,1,-1,2,-2,1,-1]

for _ in range(t):
    l = int(sys.stdin.readline())
    board = [[0 for _ in range(l)] for _ in range(l)]
    dist = [[-1 for _ in range(l)] for _ in range(l)]
    queue = deque()

    x,y = map(int,sys.stdin.readline().split())
    a,b = map(int,sys.stdin.readline().split())
    queue.append((x,y))
    board[x][y] = 1
    dist[x][y] = 0

    while queue:
        x,y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue
            if dist[nx][ny] >= 0:
                continue
            if board[nx][ny] == 1:
                print(dist[nx][ny] + 1)
                break
            queue.append((nx,ny))
            dist[nx][ny] = dist[x][y] + 1
    print(dist[a][b])